# -*- coding: utf-8 -*-
"""
| **@created on:** 10/11/17,
| **@author:** Umesh Kumar,
| **@version:** v0.0.1
|
| **Description:**
| Singleton Class
|
| Sphinx Documentation Status:** Complete
|
..todo::
"""


class Singleton(type):
    """
    Singleton Class
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
