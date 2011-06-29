#!/usr/bin/python

import os
import time


source = ['/home/yang/python/', '/home/yang/script/']
target_dir = '/home/yang/'
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today

target = today + os.sep + now + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
if os.system(zip_command) == 0:
    print 'successfun backup to', target
else:
    print 'Backup Failed'
print os.sep
