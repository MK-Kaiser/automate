#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Mark Kaiser
# Date: 8/9/20
# Description: automates a command when given a list of names, users, processes, services or filenames
from subprocess import Popen, PIPE

command = 'echo'
fileName = 'items.txt'
with open(fileName, 'r', encoding='latin') as lst:
    for i in lst:
        result = Popen(command + " " + i, shell=True, stdout=PIPE, stderr=PIPE)
        print(result.stdout.read().strip())
