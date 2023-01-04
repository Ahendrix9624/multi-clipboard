multi-clipboard program

You can assign a key value pair to items saved in your clipboard

This saves your clipboard to a file called copied_clipboard.json in the same directory 

###########################################
Saving multiple values under different keys
###########################################

For Example: If we have "This is sample text" saved in the clipboard

Run Command:
python3 multi-clipboard.py save

when prompted "Enter a Key:" press 1 (or any key of your choice)

Copy another text to your clipboard "Sample text 2"

Run Command:
python3 multi-clipboard.py save

when prompted "Enter a Key:" press 2 (or any key of your choice)

You now have saved both of these texts under '1' or '2' key. 

###########################################
Calling back the saved Values
###########################################

Run Command:
python3 multi-clipboard.py load

enter the keys you saved such as '1' or '2'

###########################################
Calling back the saved Values
###########################################
If you forget your key for a saved clipboard run cmd below 

Run Command:
python3 multi-clipboard.py list


###########################################
All Commands 
###########################################
python3 multi-clipboard.py save
python3 multi-clipboard.py load
python3 multi-clipboard.py list

*for windows you might just call 'python' 'python3' is more for unix/linux