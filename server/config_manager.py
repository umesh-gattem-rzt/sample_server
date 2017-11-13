# -*- coding: utf-8 -*-
"""
| **@created on:** 10/11/17,
| **@author:** Umesh Kumar,
| **@version:** v0.0.1
|
| **Description:**
| 
|
| **Sphinx Documentation Status:** Complete
|
..todo::
    --
"""

import json
import logging
import os
from collections import OrderedDict

from typeguard import typechecked

from server.logging_config_manager import setup_logging
from server.utils.singleton import Singleton

logger = logging.getLogger(__name__)


class CommonConfig(object):
    """
    | **@author:** Umesh Kumar
    | Common Configuration
    """

    @typechecked
    def __init__(self, common_config: dict):
        try:
            self.HOST = common_config['host']
            self.PORT = common_config['port']
            self.DEBUG = common_config['debug']
        except KeyError as ke:
            raise Exception('Key Error. Config Error', ke)


class ConfigManager(metaclass=Singleton):
    """
    | **@author:** Umesh Kumar
    |
    | Configuration Manager
    """

    @typechecked
    def __init__(self, config_file_path: str):
        global SAMPLE_CONFIG_DATA
        try:
            SAMPLE_CONFIG_DATA = json.load(open(config_file_path), object_pairs_hook=OrderedDict)
        except Exception as e:
            logger.critical(
                'Configuration file path error. Please provide configuration file path: {}'.format(config_file_path))
            raise Exception(
                'Configuration file path error. Please provide configuration file path: ' + config_file_path, e)
        try:
            self.CommonConfig = CommonConfig(SAMPLE_CONFIG_DATA['common_config'])
        except KeyError as ke:
            raise Exception('Key not found. ', ke)

    def get_config_manager(self):
        """
        | **@author:** Umesh Kumar
        |
        | Get Configuration Manager
        :return: Configuration Manager
        """
        return self

    @typechecked
    def update_config_manager(self, config_file_path: str):
        """
        | **@author:** Umesh Kumar
        |
        | Update Configuration Manager
        :param config_file_path: Configuration file path
        """
        logger.info("Updating Library Configuration - Config File: {}".format(config_file_path))
        self.__init__(config_file_path=config_file_path)

    def update_logging_config_manager(self, config_file_path: str):
        """
        | **@author:** Umesh Kumar
        |
        | Update Logging Configuration
        :param config_file_path: Configuration file path
        """
        logger.info("Updating Library Logging configuration - Config File:{}".format(config_file_path))
        setup_logging(default_path=config_file_path)
        self.CommonConfig._GLOBAL_LOGGING_CONFIG_FILE_PATH = config_file_path


ConfigPath = os.path.join("/".join(__file__.split('/')[:-1]), 'config', 'config.json')
SAMPLE_CONFIG = ConfigManager(config_file_path=ConfigPath).get_config_manager()
SAMPLE_CONFIG_DATA = OrderedDict()