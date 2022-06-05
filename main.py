"""
This is a Resume Builder that will display different templates you can choose from then user can input
what they want on the resume. 
"""

import os
from Template import template1
from pylatex import Document


doc = Document(documentclass='article', document_options='11pt',geometry_options={"margin":"0.5in"})

# contents for contant info
name = "Johnnn Doe"
loc = "city, state"
email = ""
phone = ""
linkedIn = ""
otherContacts = []

# contents for summary
summary = "I am a computer sciencetist that loves to code"

# contents for education
#hashmap{String: hashmap{String: hashmap{String: String}}}
education = {
    "University Near You":
    {"city, state":
        {"Bachlor of Science in Computer science":
            "1/2022"}
        },
    "University Near you":
        {"city, state":
            {"Bachlors of buisness":
                "2/2020"}
            }
        }

# contents for job
#hashmap{String : hashmap{String: hashmap{String: hashmap{String:Array[Strings]}}}}
#hashmap{"job" : hashmap{"city, state": hashmap{"job name": hashmap{"date":Array[responsibilities]}}}}
exp = {
    "College of engerning" : 
    {"city, state": 
        {"Technical Assistant": 
            {"july 2016- current":
                ["Assistant director", "technical supprot", "mannanged and directed"]
                }
            }
        },
    "College of buisnness":
        {"city, state":
            {"inter assistant":
                {"jan 2016- july 2016":
                    ["built computers", "managed money", "file stuff"]
                    }
                }
            }
    }

# contents for key skills
skills = "C++, Java, VSCode, Windows 10, Windows 7, Microsoft Office, CSS, HTML, JavaScript"

#contents for certifications
#hashmap{String: String}
cert = {"latex": "2016", "Java": "2017"}

#contents for other
#hashmap{String: String}
otherName = "Personal projects"
other = {"Chat bot": "2016", "to do list": "2017"}


def temp1():

    
    template1.header(doc,name, loc, email, phone, linkedIn, otherContacts)
    template1.summary(doc, summary)
    template1.education(doc, education)
    template1.experence(doc, exp)
    template1.keySkills(doc,skills)
    template1.certification(doc, cert)
    template1.other(doc, otherName, other)
    template1.main()


if __name__ == '__main__':
  
    temp1()