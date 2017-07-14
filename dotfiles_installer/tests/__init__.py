import os
import unittest


class TestCase(unittest.TestCase):
    _fixtures_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures'))

    def load_fixture_file(self, path):
        return open(os.path.join(self._fixtures_path, path))

    def load_fixture_file_s(self, path):
        with self.load_fixture_file(path) as f:
            return f.read()
