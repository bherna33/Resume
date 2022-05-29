"""
This is a Resume Builder that will display different templates you can choose from then user can input
what they want on the resume. 
"""

import os
from Template import template1
from pylatex import Document

doc = Document(documentclass='article', document_options='11pt',geometry_options={"margin":"0.5in"})
user = "Tester tes Terster"

if __name__ == '__main__':
    
    template1.header(doc,user)
    template1.main()