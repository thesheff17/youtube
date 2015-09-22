#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Dan Sheffner Digital Imaging Software Soltuions, INC
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

"""
This program will install a better configured vim editor
"""

import __main__ as main
import argparse
import logging
import os
import subprocess
import sys
import timeit
import urllib.request

# logging
try:
    fileName1 = main.__file__
    fileName1 = fileName1.replace("./", "")
    fileName1 = fileName1.replace(".py", "")
    fileName1 = fileName1 + ".log"
except:
    fileName1 = 'console.log'
logging.basicConfig(format='%(asctime)s - %(filename)s - %(funcName)s - \
                           %(levelname)s - %(message)s', level=logging.INFO,
                           filename=fileName1)


class Vim(object):

    version = '0.1'

    def __init__(self):
        self.git_repos = ['https://github.com/tpope/vim-sensible.git',
                          'https://github.com/kien/ctrlp.vim.git',
                          'https://github.com/scrooloose/nerdtree',
                          'https://github.com/klen/python-mode.git',
                          'https://github.com/Lokaltog/vim-powerline.git',
                          'https://github.com/jistr/vim-nerdtree-tabs.git']

        self.apt_packages = 'vim git-core'

    @staticmethod
    def run_command(command, useShell=False, cwd_directory=None):
        commandList = command.split()
        try:
            p = subprocess.Popen(commandList, shell=useShell, cwd=cwd_directory)
            p.communicate()
            if p.returncode == 0:
                logging.info("Command ran successfully: " + command)
            else:
                logging.error("Command failed: " + command)
                print("Command failed: " + command)
                sys.exit(-1)
        except (OSError, IOError):
            logging.error("Command failed: " + command)
            print("Command failed: " + command)
            sys.exit(-1)

    def check_root(self):
        """
        Figures out if the user is root or not while running these scripts
        """

        userId = os.getuid()
        if userId is not 0:
            self.run_command("clear")
            print ("Sorry you should be running this script as root...")
            logging.error("You are not root exiting script...")
            sys.exit(1)

    def packages(self):
        print ("Running updates and installing base packages...")
        if os.path.isfile('/root/localMirror.txt'):
            self.run_command("cp /root/localMirror.txt /etc/apt/sources.list")

        self.run_command("apt-get update")
        self.run_command("apt-get upgrade -y")
        self.run_command("apt-get install -y  " + self.apt_packages)

    def pick_user(self, username):
        self.username = username

        if self.username == 'root':
            self.dir_user = '/root/'
        else:
            self.dir_user = '/home/' + self.username + '/'

            # make sure the home directory exists
            if not os.path.isdir("/home/" + self.username + "/"):
                logging.error("the home directory for this user doesn't exist.")
                sys.exit(1)

    def directories(self):
        path_list = [self.dir_user + '.vim/',
                     self.dir_user + '.vim/autoload/',
                     self.dir_user + '/.vim/bundle/',
                     self.dir_user + '/.vim/colors/',
                     self.dir_user + '/.vim/ftplugin/']

        for each in path_list:
            os.makedirs(each, exist_ok=True)
            logging.info("creating directory: " + each)

    def config(self):
        for each in self.git_repos:
            self.run_command('git clone ' + each, cwd_directory=self.dir_user +
                             '.vim/bundle/')

        # vim auto autoload file
        urllib.request.urlretrieve('https://tpo.pe/pathogen.vim',
                                   self.dir_user +
                                   '.vim/autoload/pathogen.vim')

        # .vimrc for your machine
        urllib.request.urlretrieve('https://raw.githubusercontent.com/' +
                                   'thesheff17/youtube/master/vim/vimrc',
                                   self.dir_user + '.vimrc')

        # color file
        urllib.request.urlretrieve('https://raw.githubusercontent.com/' +
                                   'thesheff17/youtube/master/vim/' +
                                   'wombat256mod.vim',
                                   self.dir_user + '.vim/colors/' +
                                   'wombat256mod.vim')

        # ftp plugin
        urllib.request.urlretrieve('https://raw.githubusercontent.com/' +
                                   'thesheff17/youtube/master/vim/' +
                                   'python_editing.vim',
                                   self.dir_user +
                                   '.vim/ftplugin/python_editing.vim')

    def fix_permissions(self):
        if 'root' not in self.dir_user:
            self.run_command('chown -H -R ' + self.username + ':' +
                             self.username + " /home/" + self.username + '/')

if __name__ == "__main__":
    print ("vim.py started...")
    start = timeit.default_timer()

    # argparser
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", help="user name to use")
    args = parser.parse_args()

    vim = Vim()
    vim.check_root()
    vim.pick_user(args.user)
    vim.packages()
    vim.directories()
    vim.config()
    vim.fix_permissions()

    stop = timeit.default_timer()
    print (str(stop - start) + " seconds to complete...")
    print ("vim.py completed...")
