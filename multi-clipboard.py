"""
USAGE - This code is a Python script that saves and loads data from a JSON file, and interacts with 
        the system clipboard using the clipboard module. The name of the JSON file is set to 
        copied_clipboard.json.

        The save_data() function saves data to the JSON file, while the load_data() function 
        loads data from the JSON file.

        The code checks if a valid command is passed as an argument when running the script, 
        and performs the corresponding action. If the command is "save", the script prompts the 
        user to enter a key and saves the current clipboard data under that key in the JSON file. 
        If the command is "load", the script prompts the user to enter a key and copies the corresponding 
        data from the JSON file to the clipboard. If the command is "list", the script prints the entire 
        JSON file. If an unknown command is entered, the script prints "Unknown command".

        If an invalid number of arguments is passed, the script prompts the user to pass exactly one command.

AUTHOR - https://github.com/Ahendrix9624/
"""

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
