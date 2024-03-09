#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""File operations."""

from uuid import UUID

from plants.modules.config.utils import get_storage
from plants.modules.db.model import Plant


def read_file(id_: UUID):
    """Read file from a plant record.

    Args:
        id_ (UUID): Plant Record UUID
    """
    plant = Plant.query.filter_by(id=id_).first()

    # Note: In the current version, one file is used
    #       In a future version, more files can be associated
    #       with one plant (e.g., thumbnail).
    file_location = plant.files[0].file_location

    return get_storage() / file_location
