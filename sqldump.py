# This script is for taking dumps and if any errors it will log
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
import socket

def run_cmd(cmd,logfile):
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
host=socket.gethostname()
path = "/home/storage/mysql/vimo/{}/{}".format(host,today)
file_name = "{}/vimo.sql.{}.{}.sql.gz".format(path,host,today)
if os.path.isdir(path):
    print("Directory Exist")
else:
    os.mkdir(path)
cmd = "mysqldump --single-transaction --routines --user=root --password=system123 vimo | gzip > {}".format(file_name)
out = run_cmd(cmd,'/home/jenish/sqldumps.log')
print(out)