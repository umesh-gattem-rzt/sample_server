# -*- coding: utf-8 -*-
"""
| **@created on:** 13/11/17,
| **@author:** Umesh Kumar,
| **@version:** v0.0.1
|
| **Description:**
|
| **Sphinx Documentation Status:**
|
"""

import os

from server.sample_extension_server.logging_config_manager import setup_logging

setup_logging(default_path=os.path.join("/".join(__file__.split('/')[:-1]), 'config', 'logging.yaml'))
