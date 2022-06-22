"""
This is a Resume Builder that will display different templates you can choose from then user can input
what they want on the resume. 
"""

import os
from Template import template1
from pylatex import Document
import json

#read in json file of user data
with open('Userdata.json', 'r') as jsonFile:
        userdata = json.load(jsonFile)
        
doc = Document(documentclass='article', document_options='11pt',geometry_options={"margin":"0.5in"})

# contents for contant info
name = userdata[0]
loc = userdata[1]
email = userdata[2]
phone = userdata[3]
linkedIn = userdata[4]
otherContacts = userdata[5]

# contents for summary
summary = userdata[6]

# contents for education
education = userdata[7]

# contents for job
exp = userdata[8]

# contents for key skills
skills = userdata[9]

#contents for certifications
cert = userdata[10]

#contents for other
otherName = userdata[11]
other = userdata[12]


#template 1 
def temp1():
    template1.header(doc,name, loc, email, phone, linkedIn, otherContacts)
    template1.summary(doc, summary)
    template1.education(doc, education)
    template1.experence(doc, exp)
    template1.keySkills(doc,skills)
    template1.certification(doc, cert)
    template1.other(doc, otherName, other)
    doc.generate_tex('TestFile')


if __name__ == '__main__':
  
    temp1()