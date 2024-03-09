#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

import uuid
from datetime import datetime

from flask_alembic import Alembic
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.types import UUIDType
from sqlalchemy_utils.types.ts_vector import TSVectorType

#
# Extension object
#
db = SQLAlchemy()
alembic = Alembic()


#
# Models
#
class TimestampMixin:
    """Timestamp model."""

    created = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    """Creation date."""

    updated = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    """Update date."""


class Plant(db.Model, TimestampMixin):
    """Plant metadata model."""

    id = db.Column(UUIDType, primary_key=True, default=uuid.uuid4)
    """Record UUID."""

    title = db.Column(db.String(120), nullable=False)
    """Record title."""

    description = db.Column(db.String(), nullable=False)
    """Record description."""

    #
    # Full-text search related columns
    #
    title_tsv = db.Column(
        TSVectorType("title", regconfig="english"),
        db.Computed("to_tsvector('english', \"title\")", persisted=True),
    )
    """Record title (as vector)."""

    description_tsv = db.Column(
        TSVectorType("description", regconfig="english"),
        db.Computed("to_tsvector('english', \"description\")", persisted=True),
    )
    """Record description (as vector)."""

    #
    # Files
    #
    files = db.relationship("PlantFile", backref="plan")
    """Plant associated files."""

    #
    # Indices
    #
    __table_args_ = (
        db.Index("idx_plants_title_tsv", title_tsv, postgresql_using="gin"),
        db.Index("idx_plants_description_tsv", description_tsv, postgresql_using="gin"),
    )


class PlantFile(db.Model, TimestampMixin):
    """Plant files model."""

    id = db.Column(UUIDType, primary_key=True, default=uuid.uuid4)
    """Record UUID."""

    file_key = db.Column(db.String(64))
    """File key."""

    file_location = db.Column(db.String())
    """File location."""

    plant_id = db.Column(UUIDType, db.ForeignKey("plant.id"))
    """Plant record."""
