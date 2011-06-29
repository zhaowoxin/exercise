#!/usr/bin/python

import re

arrays = []
fr = open('current', 'r')
dict = {}
for line in fr:
    p = re.compile(r'.*\s+(\w+@gmail\.com).*')
    m = p.match(line)
    if m:
        s_t = m.group(1)

