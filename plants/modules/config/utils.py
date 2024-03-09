#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Configuration utilities."""

from pathlib import Path

from flask import current_app


def get_storage():
    """Get storage directory path.

    Returns:
        str: Storage directory path.
    """
    return Path(current_app.config["STORAGE_DIR"])
