#!/usr/bin/bash
pelican -s publishconf.py && scp -rp ./output/ pmav99@78.47.1.101:~/logiconomy.gr/repo/
