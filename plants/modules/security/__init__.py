#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from flask_cors import CORS

cors = CORS()


def init_module(app):
    """Initialzie the `security` module."""
    cors.init_app(app)


__all__ = ("init_module",)
