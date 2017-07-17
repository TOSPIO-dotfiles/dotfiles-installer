import os
from .schema import Schema
from .consts import SCHEMA_FILE
from .util import pbug


class PackageInvalidError(Exception):
    pass


class Package:
    def __init__(self, root_dir):
        self._root_dir = root_dir
        schema_file = os.path.join(root_dir, SCHEMA_FILE)
        self._schema = Schema.load(schema_file)

    @property
    def schema(self):
        return self._schema

    @classmethod
    def validate(cls, root_dir):
        pass

    @classmethod
    def load(cls, root_dir):
        try:
            cls.validate(root_dir)
            return Package(root_dir)
        except PackageInvalidError:
            pbug(f"Invalid package at {root_dir}")
