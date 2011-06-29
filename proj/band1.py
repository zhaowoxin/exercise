#!/usr/bin/python

import os
import time

source = ['/home/yang/python/', '/home/yang/script/']
target_dir = '/home/yang/'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'successfun backup to', target
else:
    print 'Backup Failed'
