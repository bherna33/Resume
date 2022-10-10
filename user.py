import json

class User():
    def __init__(self):
        # contents for contant info
        self.name = input("what is your name?")
        self.loc = "Miami, Fl"
        self.email = "Testemail@email.com"
        self.phone = "1234567890"
        self.linkedIn = "bhernan637389"
        self.otherContacts = []

        # contents for summary
        self.summary = "this is a test to see if everything i great and dandy. once it is i can \
            continue with tis and make more progresss to ths document\
            i really dont know how to move forward with this, i might  ake a window to add the info to make\
            things erier. we will see."

        # contents for education
        #hashmap{String: hashmap{String: hashmap{String: String}}}
        self.school = {}

        # contents for job
        #hashmap{String : hashmap{String: hashmap{String: hashmap{String:Array[Strings]}}}}
        #hashmap{"job" : hashmap{"city, state": hashmap{"job name": hashmap{"date":Array[responsibilities]}}}}
        self.exp = {}

        # contents for key skills
        self.skills = "key skill1, keyskill2, keyskills3, 4,5,6,7,8,9"

        #contents for certifications
        #hashmap{String: String}
        #certifiction : date
        self.cert = {}

        #contents for other
        #hashmap{String: String}
        #hasmap{other: date}
        self.misName = "Other Stuff"
        self.other = {}

        #TODO: Add way for user to put file name
        #self.filename = ""
        
        
    def education(self, college, state, degree, date):
        self.school = {college:{state:{degree:date}}}
        return self.school
            
    def experence(self, job,location, title, date, responsiblities):
        self.exp = {job: {location: {title: {date:responsiblities}}}}
        return self.exp
    
    def certifications(self, name, date):
        self.cert = {name:date}
        return self.cert
    
    def misc(self, name, date):
        self.other = {name:date}
        return self.other
            
        
user = User()
education = user.education("college", "state", "degree", "month/year")
experence = user.experence("Job1", "city/state", "title1", "month/year", ["duty1", "duty2", "duty3"])
certification = user.certifications("certification 1", "month/year")
misc = user.misc("name", "month/year")


with open("Userdata.json", "w") as jsonfile:

    json.dump((user.name, user.loc,user.email,user.phone, user.linkedIn, user.otherContacts, user.summary, education, experence,user.skills, certification,user.misName,misc), jsonfile, indent=4)
