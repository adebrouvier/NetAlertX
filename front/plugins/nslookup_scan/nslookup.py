#!/usr/bin/env python
# test script by running:
# tbc

import os
import pathlib
import argparse
import subprocess
import sys
import hashlib
import csv
import sqlite3
import re
from io import StringIO
from datetime import datetime

sys.path.append("/home/pi/pialert/front/plugins")
sys.path.append('/home/pi/pialert/pialert') 

from plugin_helper import Plugin_Object, Plugin_Objects, decodeBase64
from logger import mylog, append_line_to_file
from helper import timeNowTZ, get_setting_value
from const import logPath, pialertPath, fullDbPath
from database import DB
from device import Device_obj


CUR_PATH = str(pathlib.Path(__file__).parent.resolve())
LOG_FILE = os.path.join(CUR_PATH, 'script.log')
RESULT_FILE = os.path.join(CUR_PATH, 'last_result.log')

pluginName = 'NSLOOKUP'

def main():

    mylog('verbose', [f'[{pluginName}] In script'])     


    timeout = get_setting_value('NSLOOKUP_RUN_TIMEOUT')

    # Create a database connection
    db = DB()  # instance of class DB
    db.open()

    # Initialize the Plugin obj output file
    plugin_objects = Plugin_Objects(RESULT_FILE)

    # Create a Device_obj instance
    device_handler = Device_obj(db)

    # Retrieve devices
    unknown_devices = device_handler.getUnknown()

    for device in unknown_devices:
        domain_name, dns_server = execute_nslookup(device['dev_LastIP'], timeout)

        if domain_name != '':
            plugin_objects.add_object(
            # "MAC", "IP", "Server", "Name"
            primaryId   = device['dev_MAC'],
            secondaryId = device['dev_LastIP'],
            watched1    = dns_server,
            watched2    = domain_name,
            watched3    = '',
            watched4    = '',
            extra       = '',
            foreignKey  = device['dev_MAC'])

    plugin_objects.write_result_file()
    
    
    mylog('verbose', [f'[{pluginName}] Script finished'])   
    
    return 0

#===============================================================================
# Execute scan
#===============================================================================
def execute_nslookup (ip, timeout):
    """
    Execute the NSLOOKUP command on IP.
    """
    
    nslookup_args = ['nslookup', ip]

    # Execute command
    output = ""

    try:
        # try runnning a subprocess with a forced (timeout)  in case the subprocess hangs
        output = subprocess.check_output (nslookup_args, universal_newlines=True,  stderr=subprocess.STDOUT, timeout=(timeout), text=True)

        domain_name = ''
        dns_server = ''

        # Parse output using regular expressions
        domain_pattern = re.compile(r'Name:\s+(.+)')        
        server_pattern = re.compile(r'Server:\s+(.+)')

        domain_match = domain_pattern.search(output.stdout)        
        server_match = server_pattern.search(output.stdout)

        if domain_match:
            domain_name = domain_match.group(1)
            mylog('verbose', [f'[{pluginName}] Domain Name: {domain_name}'])

        if server_match:
            dns_server = server_match.group(1)
            mylog('verbose', [f'[{pluginName}] DNS Server: {dns_server}'])

        return domain_name, dns_server

    except subprocess.CalledProcessError as e:
        # An error occured, handle it
        mylog('verbose', [f'[{pluginName}]', e.output])
        mylog('verbose', [f'[{pluginName}] ⚠ ERROR - check logs'])            
    except subprocess.TimeoutExpired as timeErr:
        mylog('verbose', [f'[{pluginName}] TIMEOUT - the process forcefully terminated as timeout reached']) 

    if output == "": # check if the subprocess failed                    
        mylog('verbose', [f'[{pluginName}] Scan: FAIL - check logs']) 
    else: 
        mylog('verbose', [f'[{pluginName}] Scan: SUCCESS'])

    return '', ''   
          
    
    

#===============================================================================
# BEGIN
#===============================================================================
if __name__ == '__main__':
    main()