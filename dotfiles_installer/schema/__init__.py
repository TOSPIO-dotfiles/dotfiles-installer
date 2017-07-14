import toml
from . import consts


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

    @classmethod
    def load(cls, f):
        return cls.initialize(toml.load(f))

    @classmethod
    def loads(cls, s):
        return cls.initialize(toml.loads(s))

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
    pass
