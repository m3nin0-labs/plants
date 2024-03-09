#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Plants validation module."""

from flask_marshmallow import Marshmallow

ma = Marshmallow()


def init_module(app):
    """Initialize the ``Validation`` module."""

    ma.init_app(app)


__all__ = ("init_module",)
