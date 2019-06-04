#!/usr/bin/env python3
from pip._internal import main as pipmain

packages = ('wget',)
for package in packages:
    pipmain(['install',package])
