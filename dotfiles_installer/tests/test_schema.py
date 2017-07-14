from . import TestCase
from dotfiles_installer.schema import Schema, SchemaV1


class SchemaV1TestCase(TestCase):
    def test_nothing(self):
        self.assertEqual(1, 1)

    def test_schema_version(self):
        schema_s = self.load_fixture_file_s('sample_schema_v1.toml')
        schema = Schema.loads(schema_s)
        self.assertIsInstance(schema, SchemaV1)
