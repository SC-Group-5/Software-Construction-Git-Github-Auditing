#Diffin files..These are changes made to the file hence showing what has been removed or added from the original file.

#This is the changed code
import re

def rearrange_name(name):

    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)

    if result == None:

        return name

