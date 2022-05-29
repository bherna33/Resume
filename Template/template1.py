from pylatex import *
from pylatex.base_classes import *
from pylatex.utils import *
from pylatex.package import *
from pylatex._version import *
from pylatex.basic import *
import os.path

#deletes test file
if os.path.exists("TestFile.tex"):
    os.remove("TestFile.tex")

#Custom command name
class name(CommandBase):
    _latex_name = 'name'
    packages = [Package("xcolor")]


# Custon command location
class location(CommandBase):
    _latex_name = 'location'
    packages = [Package('hyperref')]
 
 
#Custom command contactInfo   
class contactInfo(CommandBase):
    _latex_name = 'contactInfo'
    packages = [Package('xcolor')]
        

#Custom command contactInfo   
class resumeSection(CommandBase):
    _latex_name = 'resumesection'
    packages = [Package('indentfirst')]
 
 
#Custon command linkedIn       
class linkedIn(CommandBase):
    _latex_name = 'linkedIn'
        
        
#Custon command linkedIn       
class github(CommandBase):
    _latex_name = 'github'
        
    
#Custom command list
#all commands are global in the tex file
def commands(doc):
    # define a color set to dark black
    doc.preamble.append(Command('definecolor',"highlight", extra_arguments=("RGB","0,0,0")))
    
    # command that set the index lentgh to 9pts
    doc.preamble.append(Command('setlength\parindent', "9pt"))
    
    doc.preamble.append(Command('setlist', 'nosep'))
    
    #set itimize list to dashes 
    doc.preamble.append(Command('renewcommand\labelitemi', '-'))
    
    #set pagestyle to empty
    doc.preamble.append(Command('pagestyle', 'empty'))
    
    #set set family default
    doc.preamble.append(UnsafeCommand('renewcommand', r"\familydefault", extra_arguments="\sfdefault"))
    
    # github command
    github = UnsafeCommand('newcommand', r'\github', extra_arguments=r"\textcolor{rgb:red,110;green,84;blue,148}{\faGithubSquare}")
    doc.preamble.append(github)
    
    # linkedIn command
    linkedIn = UnsafeCommand('newcommand', r'\linkedIn', extra_arguments= r"\textcolor{rgb:red,6;green,108;blue,170}{\faLinkedinSquare}")
    doc.preamble.append(linkedIn)
    
    # Section divider
    resumesection = UnsafeCommand('newcommand', r'\resumesection', options= 1, extra_arguments=r"\vspace{-0.5cm}\section*{\color{highlight}#1}\vspace{-0.2cm}\hrule\vspace{0.2cm}")
    doc.preamble.append(resumesection)
    
    # Define new command for contactInfo
    location = UnsafeCommand('newcommand', r'\location', options=1, extra_arguments=r"\begin{center}\vspace{-0.1cm}#1\vspace{-0.3cm}\end{center}")
    doc.preamble.append(location)
    
    # Define new command for contactInfo
    contactInfo = UnsafeCommand('newcommand', r'\contactInfo', options=1, extra_arguments=r"\begin{center}\vspace{-0.1cm}#1\vspace{-0.3cm}\end{center}")
    doc.preamble.append(contactInfo)
    
    # Define new command for Name
    name = UnsafeCommand('newcommand', r'\name', options=1, extra_arguments=r"\begin{center}\section*{\LARGE \color{highlight}#1}\vspace{-0.8cm}\end{center}")
    doc.preamble.append(name)
    

#packages needed for tex file
def packages(doc):
    doc.preamble.append(Package("bbding"))
    doc.preamble.append(Package('import'))
    doc.preamble.append(Package("enumitem"))


#header
def header(doc, Username):
   doc.append(name(arguments=Arguments(Username)))
   doc.append(location(arguments="location, Location"))
   doc.append(contactInfo(arguments=Command("href","mailto:email@domain", extra_arguments=("youremail@email.com",
                                                                                           " (123) 456-7890 ", 
                                                                                           Command("href","https://www.linkedin.com/in/branden-hernandez-688365165/", 
                                                                                                   extra_arguments="LinkedIn: branden-hernandez-688365165"), 
                                                                                           Command("href","https://github.com/Bherna33", extra_arguments=" GitHub: Bherna33")))))
   

#summary
def summary(doc):
    doc.append(resumeSection('Summary'))
    doc.append("I am making this resume to make my life easyier to the world. I dont like to do extra work at all and im here to do the bare minumube when it comes to makeing this.jkskmss;lsm kmcdlkm")


#education
def education(doc):
    doc.append(resumeSection("Education"))
    doc.append(Command("textbf", "College",extra_arguments= Command("textbf",Command("hfill ", "city, state"))))
    doc.append(Command("par"))
    doc.append(Command("textit", "Bachilors of whatever",extra_arguments= Command("hfill ", "day/year")))
    doc.append(Command("par"))


# profesonoal experence 
def exp(doc):
    doc.append(resumeSection("Professonal Experence"))
    doc.append(Command("textbf", "Job1", extra_arguments= Command("textbf",Command("hfill", "city,state"))))
    doc.append(Command("par"))
    doc.append(Command("textit","Job1 name", extra_arguments= Command("hfill", "date-date")))
    with doc.create(Itemize()) as itemize:
        itemize.add_item("the first item")
        itemize.add_item("the second item")
        itemize.add_item("the third etc")
     
        
#key skills
def keySkills(doc):
    doc.append(resumeSection("Key Skills"))
    doc.append("key skill one, two, three, fror, five")
        
        
 #certtification        
def cert(doc):
    doc.append(resumeSection("Certification"))
    with doc.create(Itemize()) as itemize:
        itemize.add_item(Command("textit","the first item", extra_arguments= Command("hfill", "date-date")))
        
def other(doc, otherName):
    doc.append(resumeSection(otherName))
    with doc.create(Itemize()) as itemize:
        itemize.add_item(Command("textit","the first item", extra_arguments= Command("hfill", "date-date")))
        
        
def main():
    
    #imported main file so that the file can get the information from there.
    import main
    
    #Vars from main file to be used
    doc = main.doc
    Username = main.user
    
    #parts of the reusme.
    packages(doc)
    commands(doc)
    header(doc, Username)
    summary(doc)
    education(doc)
    exp(doc)
    keySkills(doc)
    cert(doc)
    #other(doc, otherName)
        
    doc.generate_pdf('TestFile', clean_tex=False)