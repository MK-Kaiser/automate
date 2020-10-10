#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Mark Kaiser
# Date: 8/9/20
# Description: automates a command when given a list of names, users, processes, services or filenames
import subprocess

command = "echo"
with open('items.txt', 'r', encoding='latin') as lst:
    for i in lst:
        print(subprocess.Popen(command + " " + i, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().strip())
