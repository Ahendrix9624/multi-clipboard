#!/usr/bin/env python3
#
#  [Program]
#
#  Multi Clipboard Program
#
#  [Author]
#
#  Drew, https://github.com/Ahendrix9624/
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#  See 'LICENSE' for more information.

import sys
import clipboard 
import json

#name of json file being created
SAVED_DATA = "copied_clipboard.json"

#Writes data to json file 
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

#Reads data from json file      
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return{}

#ensures 2 strings are loaded after the .py file such as save/load/list cmds
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(data)
    else:
        print("Unkown command")
else:
    print("Please pass exactly one command")