import contextlib
import json
import os
import tempfile
from io import StringIO

import pytest
from django.test import TestCase

from fridge.config_handler import ConfigHandler


class ConfigHandlerTest(TestCase):
    @staticmethod
    def test_config_handler_raises_exception_on_invalid_key():
        invalid_json = json.dumps({
            "invalid_key": "",
            "language-code": "",
            "time-zone": 123,
        })

        try:
            with tempfile.TemporaryDirectory() as td:
                temp_file_path = td + ".json"
                with open(temp_file_path, 'w') as fh:
                    fh.write(invalid_json)

            config_handler = ConfigHandler(temp_file_path)
            temp_stdout = StringIO()

            with contextlib.redirect_stdout(temp_stdout):
                config_handler.load_config()

            output = temp_stdout.getvalue().strip()
            assert "Validation errors" in output
        finally:
            os.remove(temp_file_path)

    @staticmethod
    def test_config_handler_raises_exception_on_non_existent_file():
        with pytest.raises(FileNotFoundError):
            ConfigHandler('non-existent-file-name.json')
