from pylatex import *
from pylatex.base_classes import *
from pylatex.utils import *
from pylatex.package import *
from pylatex._version import *
from pylatex.basic import *
import os

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
    
    # Section divider
    resumesection = UnsafeCommand('newcommand', r'\resumesection', options= 1, extra_arguments=r"\vspace{-0.5cm}\section*{\color{highlight}#1}\vspace{-0.2cm}\hrule\vspace{0.2cm}")
    doc.preamble.append(resumesection)
    
    # Define new command for contactInfo
    location = UnsafeCommand('newcommand', r'\location', options=1, extra_arguments=r"\begin{center}\vspace{-0.1cm}#1\vspace{-0.3cm}\end{center}")
    doc.preamble.append(location)
    
    # Define new command for Name
    name = UnsafeCommand('newcommand', r'\name', options=1, extra_arguments=r"\begin{center}\section*{\LARGE \color{highlight}#1}\vspace{-0.8cm}\end{center}")
    doc.preamble.append(name)
    

#packages needed for tex file
def packages(doc):
    doc.preamble.append(Package("bbding"))
    doc.preamble.append(Package('import'))
    doc.preamble.append(Package("enumitem"))


#header
def header(doc, Username, loc, email, phone, linkedIn, otherContacts):
    doc.append(name(arguments=Arguments(Username)))
    doc.append(location(arguments=loc))
   
    with doc.create(Center()):
        doc.append(Command("href","mailto:email@domain", extra_arguments=email))
        doc.append(VerticalSpace("0.1cm"))
        doc.append(phone)
        doc.append(VerticalSpace("0.1cm"))
        #TODO: revise this line. are they giving id or link
        doc.append(Command("href","https://www.linkedin.com/in/" + linkedIn, extra_arguments="LinkedIn: " + linkedIn))
       
        for i in otherContacts:
            if "github" in i:
                #FIXME: revise this line. are they giving id or link
                doc.append(VerticalSpace("0.1cm"))
                doc.append(Command("href","https://github.com/" + i, extra_arguments="GitHub: " + i))
            doc.append(VerticalSpace("0.1cm"))
            doc.append(i)
   

#summary
def summary(doc, sum):
    doc.append(resumeSection('Summary'))
    doc.append(sum)


#education part
def education(doc, ed):
    doc.append(resumeSection("Education"))
    for college, map1 in ed.items():
        for place, map2 in map1.items():
            doc.append(Command("textbf", college,extra_arguments= Command("textbf",Command("hfill ", place))))
            doc.append(Command("par"))
            for degree, date in map2.items():
                doc.append(Command("textit", degree,extra_arguments= Command("hfill ", date)))
                doc.append(Command("par"))


# profesonoal experence 
def experence(doc, exp):
    doc.append(resumeSection("Professonal Experence"))
    for job, map1 in exp.items():
        for place, map2 in map1.items():
            doc.append(Command("textbf", job, extra_arguments= Command("textbf",Command("hfill", place))))
            doc.append(Command("par"))
            for title, map3 in map2.items():
                for date, dutys in map3.items():
                    doc.append(Command("textit",title, extra_arguments= Command("hfill", date)))
                    with doc.create(Itemize()) as itemize:
                        for i in range(len(dutys)):
                            itemize.add_item(dutys[i])
     
        
#key skills
def keySkills(doc, skills):
    doc.append(resumeSection("Key Skills"))
    doc.append(skills)
        
        
#certtification        
def certification(doc, cert):
    doc.append(resumeSection("Certification"))
    with doc.create(Itemize()) as itemize:
        for i in cert:
            itemize.add_item(Command("textit",i, extra_arguments= Command("hfill",cert[i])))

#other topics        
def other(doc, otherName, oth):
    doc.append(resumeSection(otherName))
    with doc.create(Itemize()) as itemize:
        for i in oth:
            itemize.add_item(Command("textit",i, extra_arguments= Command("hfill", oth[i])))
        