#!/bin/python3.10
import fnmatch
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.*'):
        print(file)
