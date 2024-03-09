#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""API Services."""


from uuid import UUID

from werkzeug.exceptions import HTTPException

from plants.modules.db.model import Plant

from .schema import plant_schema, plants_schema


def search(text: str, page: int = 1, size: int = 100):
    """Search plants.

    Args:
        text (str): Query text.

        page (int): Page number.

        size (int): Page size.

    Returns:
        List[PlantSchema]: List of plants metadata.
    """
    query = Plant.query

    if text:
        query.filter(Plant.title_tsv.match(text) | Plant.description_tsv.match(text))

    plants = query.paginate(page=page, per_page=size, error_out=False).items

    return plants_schema.dump(plants)


def read(id_: UUID):
    """Read a plant.

    Args:
        id_ (UUID): Plant UUID.

    Returns:
        PlantSchema: Plant metadata.

    Raises:
        HTTPException: Exception when record is not found.
    """
    plant = Plant.query.filter_by(id=id_).first()

    if not plant:
        raise HTTPException(code=404, description="Plant not found.")

    return plant_schema.dump(plant)
