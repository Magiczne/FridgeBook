import unittest
import pytest


from utils.configuration_loader import load_configuration


class TestConfigurationLoader(unittest.TestCase):

    def test_loading_fails(self):
        with pytest.raises(FileNotFoundError, match="No such file or directory"):
            load_configuration('non-existing.json')

    def test_successful_loading(self):
        expected = {"db-name": "db.sqlite3", "language-code": "en-us", "time-zone": "UTC"}
        actual = load_configuration('test-configuration.json')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
