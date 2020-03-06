#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This file serve the Web App """
# ---------------------------------------------
# System modules
# ---------------------------------------------
import os

# ---------------------------------------------
# External dependencies
# ---------------------------------------------

# ---------------------------------------------
# Local dependencies
# ---------------------------------------------
from server.app import app

# ---------------------------------------------


if __name__ == "__main__":
    print("Starting Server")
    app.run(use_reloader=True, port=5000, threaded=True)
    print("App started")
