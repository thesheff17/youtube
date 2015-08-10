#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright (c) Dan Sheffner Digital Imaging Software Solutions, INC
# Email: Dan@Sheffner.com
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

# fabfile.py

from fabric.api import run

command1 = 'apt-get update'
command2 = 'apt-get -y upgrade'


def uptime():
    run('uptime')


def hostname():
    run('hostname')


def run_updates():
    run(command1)
    run(command2)


def dpkg_list():
    run('dpkg -l')


def check_permissions():
    run('ls -la /root/.ssh/id_rsa')
