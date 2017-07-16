import os
import yaml
from . import consts
from ..util import bug


class InvalidSchemaVersion(Exception):
    def __init__(self, version):
        super().__init__("Invalid schema version: {}".format(version))


class _SchemaManager:
    _schemas = {}

    @classmethod
    def register(cls, version):
        def wrapper(schema_klass):
            cls._schemas[version] = schema_klass
            return schema_klass
        return wrapper

    @classmethod
    def get_by_version(cls, version):
        schema = cls._schemas.get(version)
        return schema


register = _SchemaManager.register


class Schema:
    def __init__(self, schema_dict):
        self._schema = schema_dict

    @property
    def version(self):
        return self._schema[consts.SCHEMA_VERSION]

    @property
    def get_const(self, const_name):
        versioned_const_name = "{}_{}".format(self.version, const_name)
        try:
            const = getattr(consts, versioned_const_name)
        except AttributeError:
            try:
                const = getattr(consts, const_name)
            except AttributeError:
                bug("Const {} is not defined".format(const_name))
        return const

    @classmethod
    def load(cls, f):
        return cls.initialize(yaml.load(f.read()))

    @classmethod
    def loads(cls, s):
        return cls.initialize(yaml.load(s))

    @classmethod
    def initialize(cls, schema_dict):
        version = schema_dict[consts.SCHEMA_VERSION]
        schema_klass = cls.get_schema_by_version(version)
        return schema_klass(schema_dict)

    @classmethod
    def get_schema_by_version(cls, version):
        return _SchemaManager.get_by_version(version)


@register(1)
class SchemaV1(Schema):
    @property
    def deps(self):
        return self._schema.get("DEPS", {})

    @property
    def optdeps(self):
        return self._schema.get("OPTDEPS", {})
