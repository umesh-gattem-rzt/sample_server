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
import logging.config
import os
import yaml
import sys


class ErrorFilter(logging.Filter):
    """
    | **@author:** Umesh Kumar
    | Error Filter
    """

    def filter(self, record):
        """
        | Filter Method
        :param record: Record Object
        :return: Boolean
        """
        return record.levelno in [logging.ERROR, logging.CRITICAL]


class InfoFilter(logging.Filter):
    """
    | **@author:** Umesh Kumar
    | Info Filter
    """

    def filter(self, record):
        """
        | Filter Method
        :param record: Record Object
        :return: Boolean
        """
        return record.levelno in [logging.INFO, logging.DEBUG, logging.WARN]


def setup_logging(default_path='logging.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
    """
    | **@author:** Umesh Kumar
    | Logging Setup
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
            except Exception as e:
                print('Error in Logging Configuration. Using default configs', e)
                logging.basicConfig(level=default_level, stream=sys.stdout)
    else:
        logging.basicConfig(level=default_level, stream=sys.stdout)
        print('Failed to load configuration file. Using default configs')
