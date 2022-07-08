# This module will return 0 if the service was not running and it will be started
# if the service was already running it will return any non zero value
# this will also create / or log in the existing log files with the returned output of the cmd
# RUN THIS AS A ROOT NO OTHER USER CAN RUN AND WRITE LOGS FOR THIS SCRIPT


import os
import logging
import subprocess
from logging.handlers import RotatingFileHandler
import traceback
import smtplib
from logging.handlers import TimedRotatingFileHandler
from datetime import date

def chk_service(cmd,logfile):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = TimedRotatingFileHandler(logfile,  when='midnight', backupCount=8)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s:%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    output = str(os.popen(cmd).read())
    
    logger.debug('{}'.format(output))

    return output


today = date.today()
path = "/home/storage/mongo/mongodb/erpmongodb/{}".format(today)
if os.path.isdir(path):
    print("Directory Exist")
else:
    os.mkdir(path)
cmd = "mongodump -u admin -p  afNP22sjuWWo7ubX  --authenticationDatabase admin  --db haaki --archive={}/haaki.gz --gzip".format(path)
out = chk_service(cmd,'/home/jenish/mongodump_haaki.log')
print(out)