# Use tkinter to select a file
import re
from tkinter import filedialog

filename = filedialog.askopenfilename(initialdir="/home/andy/OneDrive/Obsidian", title="Select file")
print(filename)

# open filename
with open(filename, 'r+') as file_object:
    contents = file_object.read()
    print(contents)

    if re.search(r"---\s*share:\s*true\s*---", contents):
        print(f"{filename} - No need to add Found '\n---\nshare:true\n---\n")
    else:
        old_text = contents  # read the current contents of the file
        file_object.seek(0)  # move the file pointer to the beginning of the file
        file_object.write("---\nshare:true\n---\n")  # write the new text at the beginning of the file
        file_object.write(old_text)  # write the old text after the new text
        print(f"{filename} - added share tag")
