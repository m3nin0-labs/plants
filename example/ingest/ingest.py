import json
from pathlib import Path

from toolbox import ingest_plants_data

#
# General definition
#
base_data_dir = "management/ingest/data/images"
definition_file = "management/ingest/data/plants.json"

#
# 1. Transforming directories
#
base_data_dir = Path(base_data_dir)
definition_file = Path(definition_file)

#
# 2. Loading definition
#
definition_data = json.load(definition_file.open("r"))

#
# 3. Preparing definition data
#
definition_data = list(
    map(
        lambda x: {**x, "file": (base_data_dir / x["file"]).as_posix()}, definition_data
    )
)

#
# 4. Ingesting
#
ingest_plants_data(definition_data)
