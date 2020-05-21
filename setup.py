######################################################################

# This file setsup the  automation config file. It currently contains:
#   various usernames and passwords 
# Author: Ricardo Ruiz
# Date of Creation: 5/17/20

######################################################################

import sys
import json

#create hidden automation_config.json file first (DON'T TRACK THIS FILE)
config_file = '/home/ricky/Code/automation_scripts/.automation_config.json'
with open(config_file) as file:
  config = json.load(file)

website = input("Enter Website:")

if website in config:
  print( "There is already an entry for "  + website)
  decision = input( "Would you like to delete this entry? (y/n)")

  if decision == "y": 
    config.pop(website)
  else:
    sys.exit()
username = input("Enter username:")

password = input("Enter password:")


new_entry = {"username": username, "password": password}

config[website] = new_entry

with open(config_file, 'w') as json_file:
  json.dump(config, json_file)
