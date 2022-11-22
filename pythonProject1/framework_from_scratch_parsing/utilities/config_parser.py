import configparser

from framework_from_scratch_parsing.CONSTANTS import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f'{ROOT_DIR}/configurations/configuration.ini')


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_driver_id():
        return config.get('browser', 'browser_id')

    @staticmethod
    def get_password(self):
        pass
