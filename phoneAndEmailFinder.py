# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# TODO: Create email regex.
emailRegex = re.compile(r"(?i)([a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,})", re.VERBOSE)

# TODO: Find matches in clipboard text.

TEXT = pyperclip.paste()

phoneNumberList = phoneRegex.findall(TEXT)
emailList = emailRegex.findall(TEXT)

# TODO: Copy results to the clipboard.

print("Here's the result that is copied to the clipboard")
resultString = ""
resultString += "Phone Number(s):" + "\n\n"
for tuple in phoneNumberList:
    resultString += tuple[0] + "\n"
resultString += "\nEmail(s)" + "\n\n"
for email in emailList:
    resultString += email + "\n"

print(resultString)
pyperclip.copy(resultString)
