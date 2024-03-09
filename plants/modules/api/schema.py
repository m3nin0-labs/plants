#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Database model schema."""

from plants.modules.db.model import Plant
from plants.modules.validation import ma


#
# Schemas
#
class PlantSchema(ma.SQLAlchemyAutoSchema):
    """Plant schema model."""

    class Meta:
        model = Plant
        fields = ("title", "description", "links")

    links = ma.Hyperlinks(
        {
            "self": ma.URLFor("plantread", values=dict(plant_id="<id>")),
            "iiif": {
                "base": ma.URLFor(
                    "iiifimagebase",
                    values=dict(
                        version="v2",
                        uuid="<id>",
                    ),
                ),
                "info": ma.URLFor(
                    "iiifimageinfo",
                    values=dict(
                        version="v2",
                        uuid="<id>",
                    ),
                ),
                "image": ma.URLFor(
                    "iiifimageapi",
                    values=dict(
                        version="v2",
                        uuid="<id>",
                        region="full",
                        size="full",
                        rotation=0,
                        quality="default",
                        image_format="png",
                    ),
                ),
            },
        }
    )


#
# Schema object
#
plant_schema = PlantSchema()
plants_schema = PlantSchema(many=True)
