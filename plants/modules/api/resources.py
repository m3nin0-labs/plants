#
# Copyright (C) 2024 Plants.
#
# Plants is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""API Resources."""

from flask_restful import Api, Resource, reqparse

from .services import read, search

api = Api()


#
# Arg parser
#
parser = reqparse.RequestParser()
parser.add_argument("text", type=str, location="args")
parser.add_argument("page", type=int, location="args")
parser.add_argument("size", type=int, location="args")


#
# Search
#
class PlantSearch(Resource):
    """Search plants endpoint."""

    def get(self):
        """Search plants operation."""
        args = parser.parse_args()

        # query
        text = args.get("text")

        # pagination
        page = args.get("page")
        size = args.get("size")

        return search(text, page, size)


#
# Read
#
class PlantRead(Resource):
    """Read metadata from a given plant."""

    def get(self, plant_id):
        """Read plant metadata operation."""
        return read(plant_id)


#
# Resources registration.
#
api.add_resource(PlantSearch, "/plants")
api.add_resource(PlantRead, "/plants/<uuid:plant_id>")
