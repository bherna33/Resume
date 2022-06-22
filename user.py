import json

# contents for contant info
name = ""
loc = ""
email = ""
phone = ""
linkedIn = ""
otherContacts = []

# contents for summary
summary = ""

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
skills = ""

#contents for certifications
#hashmap{String: String}
#certifiction : date
cert = {}

#contents for other
#hashmap{String: String}
#hasmap{other: date}
otherName = ""
other = {}

#TODO: Add way for user to put file name
#filename = ""


with open("Userdata.json", "w") as jsonfile:

    json.dump((name, loc,email,phone, linkedIn, otherContacts, summary, education, exp,skills, cert,otherName,other), jsonfile, indent=4)
