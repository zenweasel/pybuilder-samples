#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pybuilder.core import init, use_plugin


use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.unittest")
use_plugin("python.flake8")

default_task = ["install_dependencies", "publish"]

@init
def initialize(project):
    project.build_depends_on('flask')