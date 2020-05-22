from utils.configuration_loader import load_configuration
from cerberus import Validator
import json

default_configuration = {
    "db-name": "db.sqlite3",
    "language-code": "en-us",
    "time-zone": "UTC"
}
schema = {
    "db-name": {'type': 'string', 'empty': False},
    "language-code": {'type': 'string', 'empty': False},
    "time-zone": {'type': 'string', 'empty': False}
}


class ConfigHandler:
    validator = Validator(schema)
    configuration = load_configuration('configuration.json')

    def load_config(self):
        if not self.validator.validate(self.configuration):
            print('Validation errors: ' + json.dumps(self.validator.errors))

    def get_config_value(self, key):
        if not any(key == k for k in schema):
            raise Exception(f'Specified key: {key} is not supported')

        if self.validator.errors.get(key):
            return default_configuration[key]

        return self.configuration[key]
