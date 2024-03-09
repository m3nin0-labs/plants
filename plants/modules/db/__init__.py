#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from .model import alembic, db


def init_module(app):
    """Initialize the ``database`` model."""
    db.init_app(app)
    alembic.init_app(app)


__all__ = ("db", "init_module")
