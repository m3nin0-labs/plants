#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Utilitary tools to ingest data offline."""

import os
import shutil
import uuid

from plants.main import app
from plants.modules.api.schema import plant_schema
from plants.modules.config.utils import get_storage
from plants.modules.db import db, model


#
# Auxiliary operations
#
def _create_plant(plant_metadata, plant_image_file, storage, session):
    """Ingest plant data into the database.

    Args:
        plant_metadata (dict): Plant metadata.

        plant_image_file (str): Path to the plant image.

        storage (Path): Base directory to store data.

        session (Session): Database session.

    Returns:
        Plant: Plant model.
    """
    # validating and creating plant
    plant_schema.validate(plant_metadata, session=session)
    plant = model.Plant(**plant_metadata, id=uuid.uuid4())

    # preparing file
    file_name = os.path.basename(plant_image_file)
    file_dir = storage / str(plant.id)
    file_loc = (file_dir / "data").as_posix()

    file_dir.mkdir(parents=True, exist_ok=True)

    plant.files = [
        model.PlantFile(file_key=file_name, file_location=file_loc),
    ]

    # copying file
    shutil.copy2(plant_image_file, file_loc)

    return plant


#
# High-level functions.
#
def ingest_plants_data(plant_records):
    """Ingest plants into the database.

    Args:
        plant_records (List[Dict]): List of dict containing `metadata`
                                    and `file` properties.

    Returns:
        None
    """
    with app.app_context():
        storage = get_storage()

        for plant_record in plant_records:
            plant = _create_plant(
                plant_metadata=plant_record["metadata"],
                plant_image_file=plant_record["file"],
                storage=storage,
                session=db.session,
            )

            db.session.add(plant)
        db.session.commit()
