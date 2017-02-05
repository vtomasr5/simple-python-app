#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 vjuan <vtomasr5@gmail.com>
#
# Distributed under terms of the GPLv3 license.

"""
Simple python bottlepy app for testing Openshift
"""

from bottle import route, run

@route('/')
def index():
    return 'Hello "put here whatever you want"! ;)'

run(host='0.0.0.0', port=8080)
