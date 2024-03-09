#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Plants API module."""

from flask_iiif import IIIF

from plants.modules.api.file import read_file
from plants.modules.api.resources import api

#
# Initializing IIIF
#
iiif = IIIF()


#
# Module initializer
#
def init_module(app):
    """Initialize IIIF module."""

    # registering IIIF
    iiif.init_app(app)

    # registering IIIF rest api
    iiif.init_restful(api=api, prefix=app.config["IIIF_API_PREFIX"])

    # registering file handler
    iiif.uuid_to_image_opener_handler(read_file)

    # registering app
    api.init_app(app=app)
