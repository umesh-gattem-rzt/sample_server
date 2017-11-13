# -*- coding: utf-8 -*-
"""
| **@created on:** 16/12/16,
| **@author:** Umesh Kumar,
| **@version:** v0.0.1
|
| **Description:**
|
| **Sphinx Documentation Status:**
|
"""

import os
from server.logging_config_manager import setup_logging

setup_logging(default_path=os.path.join("/".join(__file__.split('/')[:-1]), 'config', 'logging.yaml'))
