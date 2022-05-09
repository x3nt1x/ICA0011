"""Script to convert a directory structure to JSON format."""
import os
import json
from pwd import getpwuid


def path_to_dict(path):
    d = {"name": os.path.basename(path), "path": os.path.abspath(path)}

    status = os.stat(path)
    d["mask"] = oct(status.st_mode)[-3:]
    d["owner"] = getpwuid(status.st_uid).pw_name

    if os.path.isdir(path):
        d["type"] = "directory"
        d["children"] = [path_to_dict(os.path.join(path, file)) for file in os.listdir(path)]
    else:
        d["type"] = "file"

    return d


data = json.dumps(path_to_dict("."), indent=4)
print(data)
