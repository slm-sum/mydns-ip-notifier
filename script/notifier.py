#!/usr/bin/python3

# notify ip address to mydns.jp

import requests as r
import logging
from logging.handlers import SysLogHandler 
import platform

MASTER_ID = 'your_id'
MASTER_PASSWORD = 'your_password'
# Use HTTP-BASIC method to notify the public address.
API_URL = 'https://www.mydns.jp/login.html'

def main():
	# logging setting
	## choose address. TODO: address on Windows 
	address = '/dev/log'
	if platform.system() == 'Darwin':
		address = '/var/run/syslog'

	logger = logging.getLogger('notifier')
	logger.setLevel(logging.ERROR)
	logger.addHandler(SysLogHandler(address=address, facility='local1'))
	
	# notification
	res = r.get(API_URL, auth=(MASTER_ID, MASTER_PASSWORD))
	
	# logging when the requests failed.
	if res.status_code != 200:
		logger.error('failed to notify my ip address to mydns.jp')
		
if __name__ == "__main__":
	main()

	
