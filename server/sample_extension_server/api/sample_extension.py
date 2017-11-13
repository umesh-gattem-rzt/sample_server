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
import logging

from server.sample_extension_server.app import app

logger = logging.getLogger(__name__)


# default app route
@app.route('/')
def home():
    return "success"


# run stage app route
@app.route('/run_template')
def run_template():
    return "success"
