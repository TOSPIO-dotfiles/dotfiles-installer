from . import TestCase
from dotfiles_installer.schema import Schema, SchemaV1


class SchemaTestCase(TestCase):
    _schema_file = None

    def setUp(self):
        self._schema = Schema.loads(
            self.load_fixture_file_s(self._schema_file)
        )

    @property
    def schema(self):
        return self._schema


class SchemaV1TestCase(SchemaTestCase):
    _schema_file = 'sample_schema_v1.yaml'

    def test_schema_version(self):
        self.assertIsInstance(self._schema, SchemaV1)

    def test_deps(self):
        self.assertListEqual([
            "github:tospio-dotfiles/y-usuzumi-zsh",
            "github:tospio-dotfiles/y-usuzumi-spacemacs"
        ], self._schema.deps)

    def test_optdeps(self):
        self.assertListEqual([
            "github:tospio-dotfiles/y-usuzumi-proxy"
        ], self._schema.optdeps)
