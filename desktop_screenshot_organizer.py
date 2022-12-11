#! python3

# Small script to remove screenshots from my Desktop

import os, shutil

prompt = "1. Go to your Desktop's directory, and type 'pwd' at the command line prompt"
prompt += "\nand copy the resulting path e.g. /Users/pjteh/Desktop."
prompt += "\n2. Paste or insert the resulting path here at this prompt: "

desktop = input(prompt)

# desktop = '/Users/pjteh/Desktop'
screenshots_folder = desktop + "/Screenshots"

for filename in os.listdir(desktop):
    if os.path.isdir(os.path.join(desktop, filename)): #If filename is a Directory
        continue
    if os.path.isfile(os.path.join(desktop, filename)): #If filename is a file
        if not (filename.startswith('Screenshot')):
            continue
        if not os.path.exists(screenshots_folder):
            # Create the folder if it doesn't exist.
            os.mkdir(os.path.join(desktop, 'Screenshots'))
        shutil.move(os.path.join(desktop, filename), screenshots_folder) # Move file from desktop to Screenshots folder
        print(f"Moving {filename} to Screenshots folder...")

# Print message if no screenshots were found
print("No Screenshots to move")

