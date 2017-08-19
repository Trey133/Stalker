#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import subprocess
import os
import time
import requests
import webbrowser
import gnupg
from bs4 import BeautifulSoup as bs
from termcolor import colored
sys.path.insert(0, '/usr/share/stalker')
import variables as vars
import basic
spyder = basic.spyder
save_site = basic.save_site
######################################################################
# COLORED GOOGLE LOGO                                                #
######################################################################
google_logo =colored("G",'red',attrs=['bold'])+colored("O",'blue',attrs=['bold'])+colored("O",'yellow',attrs=['bold'])+colored("G",'magenta',attrs=['bold'])+colored("L",'green',attrs=['bold'])+colored("E",'cyan',attrs=['bold'])
######################################################################
# ABBREVIATIONS FOR STALKER WEB SEARCH                               #
######################################################################
abv = {"Alabama":"AL","Alaska":"AK","Arizona":"AZ","Arkansas":"AR","California":"CA","Colorado":"CO","Connecticut":"CT","Delaware":"DE","Florida":"FL","Georgia":"GA","Hawaii":"HI","Idaho":"ID","Illinois":"IL","Indiana":"IN","Iowa":"IA","Kansas":"KS","Kentucky":"KY","Louisiana":"LA","Maine":"ME","Maryland":"MD","Massachusetts":"MA","Michigan":"MI","Minnesota":"MN","Mississippi":"MS","Missouri":"MO","Montana":"MT","Nebraska":"NE","Nevada":"NV","New·Hampshire":"NH","New·Jersey":"NJ","New·Mexico":"NM","New·York":"NY","North·Carolina":"NC","North Dakota":"ND","Ohio":"OH","Oklahoma":"OK","Oregon":"OR","Pennsylvania":"PA","Rhode·Island":"RI","South·Carolina":"SC","South·Dakota":"SD","Tennessee":"TN","Texas":"TX","Utah":"UT","Vermont":"VT","Virginia":"VA","Washington":"WA","West Virginia":"WV","Wisconsin":"WI","Wyoming":"WY","Washington·DC":"DC"}
######################################################################
# GNUPG SETUP                                                        #
######################################################################
gpg = gnupg.GPG(homedir='/root/.gnupg',verbose=True, keyring='/root/.gnupg/pubring.kbx')
gpg.encoding = 'utf-8'
######################################################################
# SEPERATOR                                                          #
######################################################################
sep = "\n\n==================================================\n\n"
######################################################################
# CLEAR                                                              #
######################################################################
def clear():
    basic.clear()
#######################################################################
# RESTART                                                             #
#######################################################################
def restart():
    basic.restart()
#######################################################################
# TIMER                                                               #
#######################################################################
pause_for = basic.Timer()
wait = pause_for.wait
#######################################################################
show_msg = basic.Msg_Print()
msg = show_msg.std_msg
dmsg = show_msg.alt_msg
clr = show_msg.clr
fst = show_msg.fast_msg
tmd = show_msg.timed_msg
# tmd('Hello there Fred!','magenta',3)
# print clr('Hello Friend!','yellow')
# msg('You Can Add Attributes To Me!','blue',attrs=['bold'])
# dmsg("I have No Attributes!",'blue')
#######################################################################
# Error Handling                                                      #
#######################################################################
class Error(object):
    def log(self, error, command):
# WRITE ERROR DATA TO '/USR/SHARE/STALKER/ERROR.LOG'
        with open("/usr/share/stalker/error.log",'a') as log:
            log.write("\n#############################################################################################################\n")
            log.write(time.strftime("%d/%m/%Y")+" | "+time.strftime("%H:%M:%S"))
            log.write("\n")
            log.write(command)
            log.write("\n")
            log.write(error)
            log.write("\n#############################################################################################################")
            log.close()
    class Warn(object):
# STANDARD WARNING
        def warning(self,message):
            print colored(message,'yellow',attrs=['bold'])
            time.sleep(1)
# STANDARD ERROR
        def error(self,message):
            print colored(message,'red',attrs=['bold'])
            time.sleep(1)
# IMPORTANT NOTICE
        def important(self, message, color, on_color, atts):
            print colored(message,color,on_color,attrs=[atts])
######################################################################
error = Error()
######################################################################
# Profile Management                                                 #
######################################################################
class Profile(object):
# CREATES A NEW PROFILE
    def new(self):
        subprocess.call(["mkdir",'/usr/share/stalker/profiles/%s'% vars.full_name])
        profile_address = "/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name)
        personal_address = "/usr/share/stalker/profiles/%s/%s.bio"% (vars.full_name, vars.full_name)
        pro_address = "/usr/share/stalker/profiles/%s/%s.job"% (vars.full_name, vars.full_name)
        stalker_file = "/usr/share/stalker/profiles/%s/%s.stalker"% (vars.full_name, vars.full_name)
# CHECK TO SEE IF PROFILE PAGES HAVE BEEN CREATED ALREADY
        if vars.start_file == False:
## CREATES THE MAIN PROFILE PAGE
            with open(str(profile_address),'w') as add_profile:
                add_profile.write("#######################################################################################\n%s\n#######################################################################################"% vars.full_name)
                add_profile.close()
## CREATES THE PERSONAL PROFILE PAGE
            with open(str(personal_address),'w') as add_personal:
                add_personal.write("#######################################################################################\n%s\n#######################################################################################"% vars.full_name)
                add_personal.close()
## CREATES THE PROFESSIONAL PROFILE PAGE
            with open(str(pro_address),'w') as add_pro:
                add_pro.write("#######################################################################################\n%s\n#######################################################################################"% vars.full_name)
                add_pro.close()
## CREATES THE STALKER WEBSEARCH PAGE
            with open(str(stalker_file),'w') as stalker_file:
                stalker_file.write("#######################################################################################\n%s\n#######################################################################################"% vars.full_name)
                stalker_file.write("\nStalker Web Search")
                stalker_file.write("\n#######################################################################################\n")
# SKIP PROFILE PAGE CREATING IF THEY ALREADY EXSIST
        else:
            return "Profile Has Been Started Already...\nInfo Not Added!"
        vars.start_file = True
######################################################################
# MAIN PROFILE PAGE WRITER                                         #
######################################################################
    def add(self, data):
        profile_address = "/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name)
        with open(str(profile_address),'a') as add_profile:
            add_profile.write("\n---------------------------------------------------------------------------------------\n%s\n---------------------------------------------------------------------------------------\n"% data)
            add_profile.close()
######################################################################
# PERSONAL PROFILE PAGE WRITER                                     #
######################################################################
    def personal(self, data):
        personal_address = "/usr/share/stalker/profiles/%s/%s.bio"% (vars.full_name, vars.full_name)
        with open(str(personal_address),'a') as add_profile:
            add_profile.write("\n---------------------------------------------------------------------------------------\n%s\n---------------------------------------------------------------------------------------\n"% data)
            add_profile.close()
######################################################################
# PROFESSIONAL PROFILE PAGE WRITER                                   #
######################################################################
    def pro(self, data):
        pro_address = "/usr/share/stalker/profiles/%s/%s.job"% (vars.full_name, vars.full_name)
        with open(str(pro_address),'a') as add_profile:
            add_profile.write("\n---------------------------------------------------------------------------------------\n%s\n---------------------------------------------------------------------------------------\n"% data)
            add_profile.close()
######################################################################
# STALKER FILE WRITER                                                #
######################################################################
    def stalked(self, data):
        pro_address = "/usr/share/stalker/profiles/%s/%s.stalker"% (vars.full_name, vars.full_name)
        with open(str(pro_address),'a') as add_profile:
            add_profile.write("\n=======================================================================================\n%s\n======================================================================================\n"% data)
            add_profile.close()
# THIS FUNCTION 'DOES NOT' RETURN A STRING *OTHER THAN ERRORS.
# THE __STR__(SELF): FUNCTION HERE IS NOT NEEDED BUT IT MAY BE USED IN FUTURE RELEASES
    def __str__(self):
        return clr("This Class Will Not Return A String!\n***except for this one...***",'red')
# INITIALIZE THE PROFILE() CLASS
#######################
tpro = Profile()
######################################################################
# TARGET
######################################################################
# (HOLDS ALL DEFINITIONS FOR TARGET OBJECT CREATION.
# EVERY OBJECT THAT A TARGET CAN HAVE IS DEFINED HERE.)
######################################################################
class Target(object):
### __str__
    def __str__(self):
        return str(vars.first_name)+" "+str(vars.last_name)+"\n "+str( vars.city)+" "+str(vars.state)
######################################################################
### basic_info
######################################################################
    def basic_info(self, first_name, middle_name, last_name, city, state):
        vars.first_name = first_name
        vars.middle_name = middle_name
        vars.last_name = last_name
        vars.city = city
        vars.state = state
### CHECK TO SEE IF USER INPUT A MIDDLE NAME
        if len(middle_name) >= 1:
            vars.full_name = str(vars.first_name)+"_"+str(vars.middle_name)+"_"+str(vars.last_name)
### IF THE USER DID NOT INPUT A MIDDLE NAME...
        else:
### VARIABLES.FULL_NAME = %FIRST_NAME +'_'+ %LAST_NAME
            vars.full_name = str(vars.first_name)+"_"+str(vars.last_name)
### CHECK TO SEE IF PROFILE PAGES HAVE BEEN STARTED
        if vars.start_file == False:
            tpro.new()
            vars.start_file = True
            data = "\nName: "+str(vars.full_name)+"\nCity: "+str(vars.city)+"\nState: "+str(vars.state)
            tpro.personal(data)
### IF THEY HAVE ALREADY BEEN CREATED
        else:
            data = "\nName: "+str(vars.full_name)+"\nCity: "+str(vars.city)+"\nState: "+str(vars.state)
### WRITE %DATA TO .../STALKER/PROFILES/%NAME/%NAME,BIO
            tpro.personal(data)
            msg("Profile Information Has Been Added!",'yellow','bold')
        return first_name, last_name
######################################################################
### phone
######################################################################
    def phone(self, phone):
        vars.phone = phone
        data = "Phone: "+str(vars.phone)
        tpro.personal(data)
######################################################################
### address
######################################################################
    def address(self, address, city, state):
        vars.address = address
        vars.city = city
        vars.state = state
######################################################################
### email
######################################################################
    def email(self, email):
        vars.email = email
######################################################################
# Bio                                                                #
######################################################################
    class Bio(object):
### __str__
        def __str__(self):
            return "Name: "+str(vars.first_name)+" "+str(vars.middle_name)+" "+str(vars.last_name)+"\nAge: "+str(vars.age)+"\nDOB: "+str(vars.dob)+"\nOccupation: "+str(vars.occupation)+"\nCity: "+str(vars.city)+"\nState: "+str(vars.state)
######################################################################
### full_info
######################################################################
        def full_info(self, first_name, middle_name, last_name, address, city, state, dob, age, phone, sec_phone, occupation, employer, employer_phone, employer_address, job_title, hobbies):
            vars.first_name = first_name
            vars.middle_name = middle_name
            vars.last_name = last_name
            vars.address = address
            vars.city = city
            vars.state = state
            vars.dob = dob
            vars.age = age
            vars.phone = phone
            vars.sec_phone = sec_phone
            vars.occupation = occupation
            vars.employer = employer
            vars.employer_phone = employer_phone
            vars.employer_address = employer_address
            vars.job_title = job_title
            vars.hobbies = hobbies
            if len(middle_name) >= 1:
                vars.full_name = str(vars.first_name)+"_"+str(vars.middle_name)+"_"+str(vars.last_name)
            else:
                vars.full_name = str(vars.first_name)+"_"+str(vars.last_name)
            tpro.new()
            data = "\nName: "+str(vars.full_name)+"\nAge: "+str(vars.age)+"\nDOB: "+str(vars.dob)+"\nOccupation: "+str(vars.occupation)+"\nCity: "+str(vars.city)+"\nState: "+str(vars.state)
            tpro.add(data)
            tpro.personal(data)
            tpro.pro(data)
######################################################################
# Psych                                                              #
######################################################################
        class Psych(object):
######################################################################
### PSYCH_PROFILE
######################################################################
            def psych_profile(self, facility, status, notes):
                vars.psych_facility = facility
                vars.psych_status = status
                vars.psych_notes = notes
                data = "Facility: "+str(vars.psych_facility)+"\nPsychiatric Status: "+str(vars.psych_status)+"\n "+("-")*50+"\nNotes: \n"+str(vars.psych_notes)
                tpro.add(data)
######################################################################
# PERSONALITY
######################################################################
            def personality(self, aggressive, passive, loyalty, honesty, pride, gulability, paranoia):
                aggressive = vars.aggressive
                passive = vars.passive
                loyalty = vars.loyalty
                honesty = vars.honesty
                pride = vars.pride
                gulability = vars.gulability
                paranoia = vars.paranoia
### __str__
            def __str__(self):
                return "Facility: "+str(vars.psych_facility)+"\nPsychiatric Status: "+str(vars.psych_status)+"\n "+("-")*50+"\nNotes: \n"+str(vars.psych_notes)
######################################################################
# Children
######################################################################
        class Children(object):
######################################################################
# KID
######################################################################
            def kid(self, name, dob, age, school):
                vars.kid_name = name
                vars.kid_dob = dob
                vars.kid_age = age
                vars.kid_school = school
### __str__
            def __str__(self):
                return "\nName: "+str(vars.kid_name)+"\nDOB: "+str(vars.kid_dob)+"\nAge: "+str(vars.kid_age)+"\nSchool: "+str(vars.kid_school)
######################################################################
##### Marriage
######################################################################
        class Marriage(object):
######################################################################
### marriage
######################################################################
            def marriage(self, spouse, children, joint_assets):
                vars.spouse = spouse
                vars.children = children
                vars.joint_assets = joint_assets
### __str__
            def __str__():
                return "Spouse: "+str(vars.spouse)+"\nChildren: "+str(vars.children)+"\nJoint Assets:"+str(vars.joint_assets)
######################################################################
##### Arrest
######################################################################
        class Arrest(object):
######################################################################
### offense
######################################################################
            def offense(self, date, charge, city, state, officer, ruling, sentence):
                vars.odate = date
                vars.ocharge = charge
                vars.ocity = city
                vars.ostate = state
                vars.officer = officer
                vars.oruling = ruling
                vars.osentence = sentence
### __str__
            def __str__(self):
                return "\nDate: "+str(vars.odate)+"\nCharges: "+str(vars.ocharge)+"\nCity: "+str(vars.ocity)+"\nState: "+str(vars.ostate)+"\nArresting Officer: "+str(vars.officer)+"\nJudges Ruling: "+str(vars.oruling)+"\nSentence: "+str(vars.osentence)
######################################################################
##### Associate
######################################################################
        class Associate(object):
######################################################################
### friend
######################################################################
            def friend(self, name, age, occupation, city, state):
                vars.asc_name = name
                vars.asc_age = age
                vars.asc_occ = occupation
                vars.asc_city = city
                vars.asc_state = state
### __str__
            def __str__():
                return "\nAssociates Name: "+str(vars.name)+"\nAge: "+str(vars.age)+"\nOccupation: "+str(vars.occupation)+"\nCity: "+str(vars.city)+"\nState: "+str(vars.state)
######################################################################
##### Employment
######################################################################
    class Employment(object):
######################################################################
### workplace
######################################################################
        def workplace(self, co_name, title, phone, address):
            vars.employer = co_name
            vars.job_title = title
            vars.employer_phone = phone
            vars.employer_address = address
### __str__
        def __str__(self):
            return str(vars.employer)+" "+str(vars.job_title)+" "+str(vars.employer_phone)+" "+str(vars.employer_address)
######################################################################
##### Vehicle
######################################################################
    class Vehicle(object):
######################################################################
### vehicle
######################################################################
        def vehicle(self, make, model, year, color, plate_number, vin_number):
            vars.vmake = make
            vars.vmodel = model
            vars.vyear = year
            vars.vcolor = color
            vars.plate_number = plate_number
            vars.vin_number = vin_number
### __str__
        def __str__(self):
            return ("-"*50)+"\nMake: "+vars.vmake+"  |  Model: "+vars.vmodel+"  |  Year: "+vars.vyear+"  |  Color: "+vars.vcolor+"\nPlate #: "+vars.plate_number+"  |  VIN #: "+vars.vin_number+"\n"+("-"*50)
######################################################################
##### Device
######################################################################
    class Device(object):
######################################################################
### access_point
######################################################################
        def access_point(self, device_type, manufacturer, mac_address, ip_address):
            vars.device_type = device_type
            vars.manufacturer = manufacturer
            vars.mac_address = mac_address
            vars.ip_address = ip_address
######################################################################
### smartphone
######################################################################
        def smartphone(self, device_type, manufacturer, phone,  mac_address, ip_address):
            vars.device_type = device_type
            vars.manufacturer = manufacturer
            vars.phone_number = phone
            vars.mac_address = mac_address
            vars.ip_address = ip_address
######################################################################
### firewall
######################################################################
        def firewall(self, device_type, manufacturer, mac_address, ip_address):
            vars.device_type = device_type
            vars.manufacturer = manufacturer
            vars.mac_address = mac_address
            vars.ip_address = ip_address
######################################################################
### tablet
######################################################################
        def tablet(self, device_type, manufacturer, mac_address, ip_address):
            vars.device_type = device_type
            vars.manufacturer = manufacturer
            vars.mac_address = mac_address
            vars.ip_address = ip_address
######################################################################
### other
######################################################################
        def other(self, device_type, manufacturer, mac_address, ip_address):
            vars.device_type = device_type
            vars.manufacturer = manufacturer
            vars.mac_address = mac_address
            vars.ip_address = ip_address
### __str__
        def __str__(self):
            return "Device Type: "+str(vars.device_type)+"\nManufacturer: "+str(vars.manufacturer)+"\nMAC: "+str(vars.mac_address)+"\nIP: "+str(vars.ip_address)
######################################################################
##### Reference
######################################################################
    class Reference(object):
######################################################################
### site
######################################################################
        def site(self, url, profile):
            vars.ref_url = url
            page = requests.get(url)
            html = page.text
            text_only = bs(html, 'html.parser')
            text = text_only.get_text()
            vars.data = text.encode('ascii', 'ignore').decode('ascii')
            return vars.data
            with open(profile,'a') as addto_profile:
                addto_profile.write((sep)+vars.data)
                addto_profile.close()
######################################################################
### soc_media
######################################################################
        def soc_media(self, site, user_name, url):
            vars.soc_site = site
            vars.soc_user_name = user_name
            vars.url = url
### __str__
        def __str__(self):
            msg(vars.ref_url+"\n"+("-")*50+"\n"+vars.data,'yellow','bold')
##############################################
##############################################
##############################################
#error = Error()
warning = error.Warn()
warn = warning.warning
#warn('LOOKOUT BATMAN!!!')
imp = warning.important
#imp("FATAL",'yellow','on_red','underline')
target = Target()
##############################################
##############################################
##############################################
######################################################################
# STALKER_LOGO
######################################################################
def stalker_logo():
    clear()
    print colored("""
   _  _     _  _     _  _     _  _     _  _   
 _| || |_ _| || |_ _| || |_ _| || |_ _| || |_ 
|_  ..  _|_  ..  _|_  ..  _|_  ..  _|_  ..  _|
|_      _|_      _|_      _|_      _|_      _|
  |_||_|   |_||_|   |_||_|   |_||_|   |_||_|  

""",'blue',attrs=['bold'])
    print colored("""
    ____ _____  _    _     _  _______ ____  
   / ___|_   _|/ \  | |   | |/ / ____|  _ \ 
   \___ \ | | / _ \ | |   | ' /|  _| | |_) |
    ___) || |/ ___ \| |___| . \| |___|  _ < 
   |____/ |_/_/   \_\_____|_|\_\_____|_| \_\

""",'red',attrs=['bold'])
    print colored("             "+time.strftime("%d/%m/%Y")+" | "+time.strftime("%H:%M:%S"),'red')
    print colored("""
   _  _     _  _     _  _     _  _     _  _   
 _| || |_ _| || |_ _| || |_ _| || |_ _| || |_ 
|_  ..  _|_  ..  _|_  ..  _|_  ..  _|_  ..  _|
|_      _|_      _|_      _|_      _|_      _|
  |_||_|   |_||_|   |_||_|   |_||_|   |_||_|  

""",'blue',attrs=['bold'])
######################################################################
# INTRO_STALKER_LOGO
######################################################################
def intro_stalker_logo():
    print colored("""
   _  _     _  _     _  _     _  _     _  _   
 _| || |_ _| || |_ _| || |_ _| || |_ _| || |_ 
|_  ..  _|_  ..  _|_  ..  _|_  ..  _|_  ..  _|
|_      _|_      _|_      _|_      _|_      _|
  |_||_|   |_||_|   |_||_|   |_||_|   |_||_|  
   
""",'blue',attrs=['bold'])
    print colored("""
    ____ _____  _    _     _  _______ ____  
   / ___|_   _|/ \  | |   | |/ / ____|  _ \ 
   \___ \ | | / _ \ | |   | ' /|  _| | |_) |
    ___) || |/ ___ \| |___| . \| |___|  _ < 
   |____/ |_/_/   \_\_____|_|\_\_____|_| \_\
   
""",'red',attrs=['bold'])
    print colored("             "+time.strftime("%d/%m/%Y")+" | "+time.strftime("%H:%M:%S"),'red')
    print colored("""
   _  _     _  _     _  _     _  _     _  _   
 _| || |_ _| || |_ _| || |_ _| || |_ _| || |_ 
|_  ..  _|_  ..  _|_  ..  _|_  ..  _|_  ..  _|
|_      _|_      _|_      _|_      _|_      _|
  |_||_|   |_||_|   |_||_|   |_||_|   |_||_|  

""",'blue',attrs=['bold'])
    print colored("""

              CASEFILE CREATOR
""",'red',attrs=['bold'])
    print colored("\n     'add\' // \'read\' // \'edit\' // \'quit\' \n",'yellow',attrs=['bold'])
    print colored("      //   \'stalker\'   //   \'phone\' //",'red',attrs=['bold'])
######################################################################
# FULL_INFO
######################################################################
def full_info():
    while True:
        try:
            msg("I\'ll Need Some Information About The Target",'yellow','bold')
            print colored("optional",'green',attrs=['bold'])+" | "+colored("recommended",'blue',attrs=['bold'])+" | "+colored("required",'red',attrs=['bold'])
            first_name = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("First Name: ",'red',attrs=['bold']))
            middle_name = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("Middle Name: ",'blue',attrs=['bold']))
            last_name = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("Last Name: ",'red',attrs=['bold']))
            if len(middle_name) >= 1:
                vars.full_name = str(first_name) +"_"+ str(middle_name) +"_"+ str(last_name)
            else:
                stalker_logo()
                msg("No Middle Name Provided...\n Using First And Last Names Only",'red','bold')
                vars.full_name = str(first_name) +"_"+ str(last_name)
            try:
                msg("Preparing Directory For %s"% vars.full_name,'red','bold')
                subprocess.call(["mkdir","/usr/share/stalker/profiles/%s"% vars.full_name])
                with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'w') as profile:
                    profile.write("#######################################################################################\n%s\n#######################################################################################"% vars.full_name)
                    profile.close()
            except Exception, e:
                print (e)
                time.sleep(2)
            try:
                age = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("Age: ",'green',attrs=['bold']))
                dob = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("Date Of Birth: ",'green',attrs=['bold']))
                address = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("Address: ",'green',attrs=['bold']))
                city = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("City: ",'blue',attrs=['bold']))
                state = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("State: ",'blue',attrs=['bold']))
                phone = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("Primary Phone Number: ",'green',attrs=['bold']))
                sec_phone = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("Secondary Phone Number: ",'green',attrs=['bold']))
                occupation = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("Occupation: ",'green',attrs=['bold']))
                employer = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("Employer: ",'green',attrs=['bold']))
                employer_phone = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("Employer Phone Number: ",'green',attrs=['bold']))
                employer_address = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("Employer Address: ",'green',attrs=['bold']))
                job_title = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("Job Title: ",'green',attrs=['bold']))
                hobbies = raw_input(colored("Enter Targets Known ",'yellow',attrs=['bold'])+colored("Hobbies: ",'green',attrs=['bold']))
            except Exception, e:
                print (e)
                time.sleep(2)
            try:
                with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                    profile.write("\nAge: %s\n"% age )
                    profile.write("DOB: %s\n"% dob )
                    profile.write(("-")*50+"\n")
                    profile.write("Address: %s\n"% address)
                    profile.write("City: %s\n"% city)
                    profile.write("State: %s\n"% state)
                    profile.write(("-")*50+"\n")
                    profile.write("Phone: %s\n"% phone)
                    profile.write("Secondary Phone: %s\n"% sec_phone)
                    profile.write(("-")*50+"\n")
                    profile.write("Occupation: %s\n"% occupation)
                    profile.write("Employer: %s\n"% employer)
                    profile.write("Employer Phone: %s\n"% employer_phone)
                    profile.write("Employer Address: %s\n"% employer_address)
                    profile.write("Job Title: %s\n"% job_title)
                    profile.write(("-")*50+"\n")
                    profile.write("Hobbies: %s"% hobbies)
                    profile.close()
            except Exception, e:
                print (e)
            vars.full_info = True
            bio = target.Bio()
            bio.full_info(first_name, middle_name, last_name, address, city, state, dob, age, phone, sec_phone, occupation, employer, employer_phone, employer_address, job_title, hobbies)
            job = target.Employment()
            job.workplace(employer, job_title, employer_phone, employer_address)
            msg("\nTarget Directory And Profile Successfully Created!!!",'blue','bold')
            time.sleep(2)
            break
        except KeyboardInterrupt:
            msg("\nPROFILE CREATION ABORTED BY USER!!!",'red','bold')
            time.sleep(2)
            break
######################################################################
# BASIC_INFO
######################################################################
def basic_info():
    msg("I\'ll Need Some Information About The Target...\n",'blue','bold')
    first_name = raw_input(colored("Enter Targets ",'red',attrs=['bold'])+colored("First Name: ",'blue',attrs=['bold']))
    middle_name = raw_input(colored("Enter Targets ",'red',attrs=['bold'])+colored("Middle Name: ",'blue',attrs=['bold']))
    last_name = raw_input(colored("Enter Targets ",'red',attrs=['bold'])+colored("Last Name: ",'blue',attrs=['bold']))
    if len(middle_name) >= 1:
        vars.full_name = str(first_name) +"_"+ str(middle_name) +"_"+ str(last_name)
    else:
        stalker_logo()
        msg("No Middle Name Provided...\n Using First And Last Names Only",'red','bold')
        vars.full_name = str(first_name) +"_"+ str(last_name)
    try:
        msg("Preparing Directory For %s"% vars.full_name,'yellow','bold')
        tpro.new()
    except Exception, e:
        print (e)
        time.sleep(2)
    city = raw_input(colored("Enter Targets ",'red',attrs=['bold'])+colored("City: ",'blue',attrs=['bold']))
    state = raw_input(colored("Enter Targets ",'red',attrs=['bold'])+colored("State: ",'blue',attrs=['bold']))
    vars.basic_info = True
    target.basic_info(first_name, middle_name, last_name, city, state)
    data = "\nCity: "+str(city)+"\nState: "+str(state)
    tpro.add(data)
######################################################################
# P_TEST (PERSONALITY_TEST)
######################################################################
def p_test():
    while True:
        print "[1-10]"
        happiness =int(raw_input(colored("Happiness: ",'red',attrs=['bold'])))
        if int(happiness) >= 0 and happiness <= 10:
            aggressive = int(raw_input(colored("Aggressiveness: ",'red',attrs=['bold'])))
            if int(aggressive) >= 0 and int(aggressive) <= 10:
                passive = int(raw_input(colored("Passiveness: ",'red',attrs=['bold'])))
                if int(passive) >= 0 and int(passive) <= 10:
                    loyalty = int(raw_input(colored("Loyalty: ",'red',attrs=['bold'])))
                    if int(loyalty) >= 0 and int(loyalty) <= 10:
                        honesty = int(raw_input(colored("Honesty: ",'red',attrs=['bold'])))
                        if int(honesty) >= 0 and int(honesty) <= 10:
                            pride = int(raw_input(colored("[self] Pride: ",'red',attrs=['bold'])))
                            if int(pride) >= 0 and int(pride) <= 10:
                                gulability = int(raw_input(colored("Gulability: ",'red',attrs=['bold'])))
                                if int(gulability) >= 0 and int(gulability) <= 10:
                                    paranoia = int(raw_input(colored("Paranoia: ",'red',attrs=['bold'])))
                                elif int(gulability) < 0 or int(gulability) > 10:
                                    msg("INPUT MUST BE BETWEEN 1 AND 10",'red','bold')
                                    time.sleep(2)
                                    pass
                                else:
                                    msg("INPUT MUST BE AN INTEGER BETWEEN 1 AND 10",'red','bold')
                                    time.sleep(2)
                                    pass
                            elif int(pride) < 0 or int(pride) > 10:
                                msg("INPUT MUST BE BETWEEN 1 AND 10",'red','bold')
                                time.sleep(2)
                                pass
                            else:
                                msg("INPUT MUST BE AN INTEGER BETWEEN 1 AND 10",'red','bold')
                                pass
                        elif int(honesty) < 0 or int(honesty) > 10:
                            msg("INPUT MUST BE BETWEEN 1 AND 10",'red','bold')
                            pass
                        else:
                            msg("INPUT MUST BE AN INTEGER BETWEEN 1 AND 10",'red','bold')
                            pass
                    elif int(loyalty) < 0 or int(loyalty) > 10:
                        msg("INPUT MUST BE BETWEEN 1 AND 10",'red','bold')
                        pass
                    else:
                        msg("INPUT MUST BE AN INTEGER BETWEEN 1 AND 10",'red','bold')
                        pass
                else:
                    msg("INPUT MUST BE AN INTEGER BETWEEN 1 AND 10",'red','bold')
                    pass
            else:
                msg("INPUT MUST BE AN INTEGER BETWEEN 1 AND 10",'red','bold')
                pass
        else:
            msg("INPUT MUST BE AN INTEGER BETWEEN 1 AND 10",'red','bold')
            pass
    score = ((int(aggressive)-int(passive))+(int(loyalty)-int(pride))+(int(gulability)+int(honesty)))-int(paranoia)
    alt_score = int(aggressive)+int(passive)+int(loyalty)+int(pride)+int(gulability)+int(honesty)+int(paranoia)
    good_score = int(happiness)+int(passive)+int(loyalty)+int(honesty)
    bad_score = int(aggressive)+int(pride)+int(gulability)+int(paranoia)
    msg(str(score),'blue','bold')
    msg(str(alt_score)+"/80",'magenta','bold')
    msg(str(good_score)+"/40",'green','bold')
    msg(str(bad_score)+"/40",'red','bold')
    time.sleep(3)
    personality_test = target.Bio.Psych()
    personality_test.personality(aggressive, passive, loyalty, honesty, happiness, pride, gulability, paranoia)
######################################################################
# ADD_VEHICLE
######################################################################
def add_vehicle():
    while True:
        try:
            msg("Press Return To Add Vehicle\n",'yellow','bold')
            msg("Press Return On Empty Line When You Are Finished\n",'red','bold')
            make = raw_input(colored("Enter Vehicles Make: ",'red',attrs=['bold']))
            if len(make) > 1:
                model = raw_input(colored("Enter Vehicles Model: ",'red',attrs=['bold']))
                year = raw_input(colored("Enter Vehicles Year: ",'red',attrs=['bold']))
                color = raw_input(colored("Enter Vehicles Color: ",'red',attrs=['bold']))
                plate_num = raw_input(colored("Enter Vehicles Plate Number: ",'red',attrs=['bold']))
                vin = raw_input(colored("Enter Vehicles VIN Number: ",'red',attrs=['bold']))
                vec = ("-"*50)+"\nMake: "+make+"  |  Model: "+model+"  |  Year: "+year+"  |  Color: "+color+"\nPlate #: "+plate_num+"  |  VIN #: "+vin+"\n"+("-"*50)
                msg(vec,'yellow','bold')
                new_car = target.Vehicle()
                new_car.vehicle(make, model, year, color, plate_num, vin)
            else:
                msg("Vehicles Have Been Added!")
                break
        except KeyboardInterrupt:
            msg("\nVehicles Have Been Added! ",'yellow','bold')
            break
        data = str(vec)
        tpro.add(data)
        tpro.personal(data)
######################################################################
# SOC_MEDIA
######################################################################
def social_media():
    with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
        profile.write("\nSocial_Media_References: \n")
        profile.close()
    while True:
        try:
            msg("Press Return To Add Social Media Accounts\n",'yellow','bold')
            msg("Press Return On Empty Line When You Are Finished\n",'red','bold')
            sma = raw_input(colored("Enter URL: ",'red',attrs=['bold']))
#            reference = target.Reference()
#            reference.site(sma, "/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name))
            if len(sma) > 5:
                with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                    profile.write(sma+"\n")
                    profile.close()
            else:
                msg("\nAccounts Have Been Added! ",'yellow','bold')
                with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                    profile.write(sep)
                    profile.close()
                    break
        except KeyboardInterrupt:
            msg("\nAccounts Have Been Added! ",'yellow','bold')
            with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                profile.write(sep)
                profile.close()
            break
        data = str(sma)
        tpro.add(data)
        tpro.personal(data)
######################################################################
######################################################################
######################################################################
path = "/usr/share/stalker/profiles/.%s"% str(vars.full_name)
gpg_path = str(path)+".gpg"
######################################################################
######################################################################
######################################################################
def remove_gpg():
    try:
        subprocess.call([":",">",gpg_path])
        subprocess.call(["rm ",gpg_path])
    except Exception, e:
        problem = e
        uc = """subprocess.call([":",">",gpg_path])"+"\n"+"subprocess.call(["rm ",gpg_path])"""
        error.log(str(problem), uc)
        os.system(":>"+gpg_path)
        os.system("rm "+gpg_path)
######################################################################
######################################################################
######################################################################
def encrypt_file():
    try:
        subprocess.call(["gpg","-r","--default-recipient","terminal","--yes","-e",path])
    except Exception, e:
        uc = """subprocess.call(["gpg","-r","--default-recipient","terminal","--yes","-e",path])"""
        problem = e
        error.log(str(problem), uc)
        os.system("gpg -r --default-recipient termianl --yes -e "+path)
######################################################################
######################################################################
######################################################################
def remove_unencrypted():
    try:
        subprocess.call([":",">",path])
        subprocess.call(["rm",path])
    except Exception, e:
        uc = """subprocess.call([":",">",path])\nsubprocess.call(["rm",path])"""
        problem = e
        error.log(str(problem), uc)
        os.system(":>"+path)
        os.system("rm "+path)
######################################################################
######################################################################
######################################################################
def decrypt_file():
#    try:
#       subprocess.call(["gpg","-d","/usr/share/stalker/profiles/.%s.gpg"% vars.full_name,">","/usr/share/stalker/profiles.%s"% vars.full_name])
#    except Exception, e:
    try:
#            e = error_one
        os.system("gpg -d /usr/share/stalker/profiles/.%s.gpg > /usr/share/stalker/profiles/.%s"% vars.full_name)
    except Exception, e:
        uc = """os.system("gpg -d /usr/share/stalker/profiles/.%s.gpg > /usr/share/stalker/profiles/.%s"% vars.full_name)"""
        problem = e
        error.log(str(problem), uc)
#            e = error_two
#            msg("Subprocess.Call Said: \n"+error_one,'red','bold')
        msg("OS.System Said: \n"+str(e),'blue','bold')
######################################################################
######################################################################
######################################################################
def gnupg_encrypt():
    try:
        open("/usr/share/stalker/profiles/.%s"% vars.full_name, 'w')#.write('This is an example.')
        with open('/usr/share/stalker/profiles/.%s'% vars.full_name, 'rb') as f:
            status = gpg.encrypt_file(
                f, recipients=['terminal'],
                output="/usr/share/stalker/profiles/.%s.gpg"% vars.full_name)

        print 'ok: ', status.ok
        print 'status: ', status.status
        print 'stderr: ', status.stderr
    except Exception, e:
        uc = """
        open("/usr/share/stalker/profiles/.%s"% vars.full_name, 'w')#.write('This is an example.')
        with open('/usr/share/stalker/profiles/.%s'% vars.full_name, 'rb') as f:
            status = gpg.encrypt_file(
                f, recipients=['terminal'],
                output="/usr/share/stalker/profiles/.%s.gpg"% vars.full_name)
"""
        problem = e
        error.log(str(problem), uc)
######################################################################
######################################################################
######################################################################
def gnupg_decrypt():
    try:
        subprocess.call(["stty", "-echo"])
        password = raw_input("What\'s The Magic Word\n|?|: ")
        print "\n"
        subprocess.call(["stty", "echo"])
        gpg.decrypt_file('/usr/share/stalker/profiles/.%s.gpg'% vars.full_name, always_trust=False, passphrase=password, output='/usr/share/stalker/profiles/.%s'% vars.full_name)
        time.sleep(2)
    except Exception, e:
        uc = """
        subprocess.call(["stty", "-echo"])
        password = raw_input("What\'s The Magic Word\\n|?|: ")
        subprocess.call(["stty", "echo"])
        gpg.decrypt_file('/usr/share/stalker/profiles/.%s.gpg'% vars.full_name, always_trust=False, passphrase=password, output='/usr$
        time.sleep(2)
"""
        problem = e
        error.log(str(problem), uc)
        print "\n"
        print (e)
        with open('/usr/share/stalker/profiles/.%s.gpg'% vars.full_name, 'rb') as f:
            status = gpg.decrypt_file(f, passphrase=password, output='/usr/share/stalker/profiles/.%s'% vars.full_name)

        print 'ok: ', status.ok
        print 'status: ', status.status
        print 'stderr: ', status.stderr
        with open("/usr/share/stalker/profiles/.%s"% vars.full_name,'r') as profile:
            data = profile.readlines()
            print (data)
            time.sleep(2)
            profile.close()
#    stream = open("/usr/share/stalker/profiles/.%s.gpg"% vars.full_name, "rb")
#    decrypted_data = gpg.decrypt_file(stream)
#    msg(str(decrypted_data),'blue','bold')
######################################################################
######################################################################
######################################################################
def stalker():
#    with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
#        profile.write(vars.first_name+" "+vars.middle_name+" "+vars.last_name)
#        profile.write("\n##################################################################################################\n")
#        profile.close()
    try:
        print(colored("Searching Pipl.com For %s %s %s"% ( vars.first_name, vars.middle_name, vars.last_name),'blue',attrs=['bold']))
        url = "https://www.pipl.com/search/?q="+vars.first_name+"+"+vars.middle_name+"+"+vars.last_name+"&l="+vars.city+"%2C+"+vars.state+"&sloc=US|"+abv[vars.state]+"|"+vars.city+"&in=5"
        time.sleep(2)
        try:
            spyder(url)
        except Exception, e:
            print colored(e,'magenta',attrs=['bold'])
            try:
                out = subprocess.check_output(["wget","-qO-",url,"|","html2text"])
                print colored(str(out),'red',attrs=['bold'])
            except Exception, e:
                print colored(e,'red',attrs=['bold'])
                print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow',attrs=['bold']))
        print(colored("Searching FindMugShots.com For Target...",'blue',attrs=['bold']))
        url = "https://www.findmugshots.com/arrests/"+vars.first_name+"_"+vars.last_name+"_"+abv[vars.state]
        time.sleep(2)
        try:
            spyder(url)
        except Exception, e:
            print colored(e,'magenta',attrs=['bold'])
            try:
                out = subprocess.check_output(["wget","-qO-",url,"|","html2text"])
                print(colored(str(out),'red',attrs=['bold']))
            except Exception, e:
                print colored(e,'red',attrs=['bold'])
                print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow',attrs=['bold']))
        print(colored("Searching MugShots.com For Target...",'blue',attrs=['bold']))
        url = "http://mugshots.com/search.html?q="+vars.first_name+"+"+vars.last_name
        time.sleep(2)
        try:
            spyder(url)
        except Exception, e:
            print colored(e,'magenta',attrs=['bold'])
            try:
                out = subprocess.check_output(["wget","-qO-",url,"|","html2text"])
                print(colored(str(out),'red',attrs=['bold']))
            except Exception, e:
                print colored(e,'red',attrs=['bold'])
                print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow',attrs=['bold']))
        print(colored("Searching WhitePages.plus For Target",'blue',attrs=['bold']))
        url = "https://whitepages.plus/n/"+vars.first_name+"_"+vars.last_name+"/location/"+vars.city+"%252C_"+abv[vars.state]
        time.sleep(2)
        try:
            spyder(url)
        except Exception, e:
            print colored(e,'magenta',attrs=['bold'])
            try:
                out = subprocess.check_output(["wget","-qO-",url,"|","html2text"])
                print(colored(str(out),'red',attrs=['bold']))
            except Exception, e:
                print colored(e,'red',attrs=['bold'])
                print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow',attrs=['bold']))
        print(colored("Searching Zabasearch.com For Target...",'blue',attrs=['bold']))
        url = "http://www.zabasearch.com/people/"+vars.first_name+"+"+vars.last_name+"/"+abv[vars.state]+"/"
        time.sleep(2)
        try:
            spyder(url)
        except Exception, e:
            print colored(e,'magenta',attrs=['bold'])
            try:
                out = subprocess.check_output(["wget","-qO-",url,"|","html2text"])
                print(colored(str(out),'red',attrs=['bold']))
            except Exception, e:
                print colored(e,'red',attrs=['bold'])
                print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow',attrs=['bold']))
        print(colored("Searching PeekYou.com For Target...",'blue',attrs=['bold']))
        url = "http://www.peekyou.com/usa/"+vars.state+"/"+vars.first_name+"_"+vars.last_name
        time.sleep(2)
        try:
            spyder(url)
        except Exception, e:
            print colored(e,'magenta',attrs=['bold'])
            try:
                out = subprocess.check_output(["wget","-qO-",url,"|","html2text"])
                print(colored(str(out),'red',attrs=['bold']))
            except Exception, e:
                print colored(e,'red',attrs=['bold'])
                print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow',attrs=['bold']))
        print(colored("Searching Spokeo.com For Target...",'blue',attrs=['bold']))
        url = "https://www.spokeo.com/"+vars.first_name+"-"+vars.last_name
        time.sleep(2)
        try:
            spyder(url)
        except Exception, e:
            print colored(e,'magenta',attrs=['bold'])
            try:
                out = subprocess.check_output(["wget","-qO-",url,"|","html2text"])
                print(colored(str(out),'red',attrs=['bold']))
            except Exception, e:
                print colored(e,'red',attrs=['bold'])
                print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow',attrs=['bold']))
        print(colored("Searching LinkedIn.com For Target...",'blue',attrs=['bold']))
        url = "https://www.linkedin.com/pub/dir/"+vars.first_name+"/"+vars.last_name+"?trk=uno-reg-guest-home-name-search"
        time.sleep(2)
        try:
            spyder(url)
        except Exception, e:
            print colored(e,'magenta',attrs=['bold'])
            try:
                out = subprocess.check_output(["wget","-qO-",url,"|","html2text"])
                print(colored(str(out),'red',attrs=['bold']))
            except Exception, e:
                print colored(e,'red',attrs=['bold'])
                print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow',attrs=['bold']))
        print(colored("No Search Would Be Complete Without ",'blue',attrs=['bold'])+google_logo)
        url = "https://www.google.com/#q="+vars.first_name+"+"+vars.middle_name+"+"+vars.last_name+"+"+vars.city+"+"+vars.state
        time.sleep(2)
        try:
            spyder(url)
        except Exception, e:
            print colored(e,'magenta',attrs=['bold'])
            try:
                out = subprocess.check_output(["wget","-qO-",url,"|","html2text"])
                print(colored(str(out),'red',attrs=['bold']))
            except Exception, e:
                print colored(e,'red',attrs=['bold'])
                print(colored("I wasn\'t able to reach ",'yellow',attrs=['bold'])+google_logo+colored("...\nI guess this search is complete afterall.",'cyan',attrs=['bold']))
                time.sleep(2)
    except Exception, e:
        print(colored(e,'red',attrs=['bold']))
######################################################################
######################################################################
######################################################################
def stalker_gui():
    try:
        print(colored("Your default web browser will open in a moment...\n Do not close it until all ",'yellow','bold')+colored("10",'red','bold')+colored(" sites are loaded!!!",'yellow','bold'))
        time.sleep(3)
### PIPL.COM
        print(colored("Searching Pipl.com For Target...",'blue','bold'))
        url = "https://www.pipl.com/search/?q="+vars.first_name+"+"+vars.middle_name+"+"+vars.last_name+"&l="+vars.city+"%2C+"+vars.state+"&sloc=US|"+abv[vars.state]+"|"+vars.city+"&in=5"
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
        except Exception, e:
            uc = """
        url = "https://www.pipl.com/search/?q="+vars.first_name+"+"+vars.middle_name+"+"+vars.last_name+"&l="+vars.city+"%2C+"+vars.state+"&sloc=US|"+abv[vars.state]+"|"+vars.city+"&in=5"
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
"""
            problem = e
            error.log(str(problem), uc)
            print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow','bold'))
            time.sleep(2)
### FINDMUGSHOTS.COM
        print(colored("Searching FindMugShots.com For Target...",'blue','bold'))
        url = "https://www.findmugshots.com/arrests/"+vars.first_name+"_"+vars.last_name+"_"+abv[vars.state]
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
        except Exception, e:
            uc = """
        url = "https://www.findmugshots.com/arrests/"+vars.first_name+"_"+vars.last_name+"_"+abv[vars.state]
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
"""
            problem = e
            error.log(str(problem), uc)
            print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow','bold'))
### MUGSHOTS.COM
        print(colored("Searching MugShots.com For Target...",'blue','bold'))
        url = "http://mugshots.com/search.html?q="+vars.first_name+"+"+vars.last_name
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
        except Exception, e:
            uc = """
        url = "http://mugshots.com/search.html?q="+vars.first_name+"+"+vars.last_name
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
"""
            problem = e
            error.log(str(problem), uc)
            print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow','bold'))
### WHITEPAGES.PLUS
        print(colored("Searching WhitePages.plus For Target",'blue','bold'))
        url = "https://whitepages.plus/n/"+vars.first_name+"_"+vars.last_name+"/location/"+vars.city+"%252C_"+abv[vars.state]
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
        except Exception, e:
            uc = """
        url = "https://whitepages.plus/n/"+vars.first_name+"_"+vars.last_name+"/location/"+vars.city+"%252C_"+abv[vars.state]
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
"""
            problem = e
            error.log(str(problem), uc)
            print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow','bold'))
### ZABASEARCH.COM
        print(colored("Searching Zabasearch.com For Target...",'blue','bold'))
        url = "http://www.zabasearch.com/people/"+vars.first_name+"+"+vars.last_name+"/"+abv[vars.state]+"/"
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
        except Exception, e:
            uc = """
        url = "http://www.zabasearch.com/people/"+vars.first_name+"+"+vars.last_name+"/"+abv[vars.state]+"/"
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
"""
            problem = e
            error.log(str(problem), uc)
            print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow','bold'))
### PEEKYOU.COM
        print(colored("Searching PeekYou.com For Target...",'blue','bold'))
        url = "http://www.peekyou.com/usa/"+vars.state+"/"+vars.first_name+"_"+vars.last_name
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
        except Exception, e:
            uc = """
        url = "http://www.peekyou.com/usa/"+vars.state+"/"+vars.first_name+"_"+vars.last_name
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
"""
            problem = e
            error.log(str(problem), uc)
            print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow','bold'))
### SPOKEO.COM
        print(colored("Searching Spokeo.com For Target...",'blue','bold'))
        url = "https://www.spokeo.com/"+vars.first_name+"-"+vars.last_name
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
        except Exception, e:
            uc = """
        url = "https://www.spokeo.com/"+vars.first_name+"-"+vars.last_name
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
"""
            problem = e
            error.log(str(problem), uc)
            print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow','bold'))
### LINKEDIN.COM
        print(colored("Searching LinkedIn.com For Target...",'blue','bold'))
        url = "https://www.linkedin.com/pub/dir/"+vars.first_name+"/"+vars.last_name+"?trk=uno-reg-guest-home-name-search"
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
        except Exception, e:
            uc = """
        url = "https://www.linkedin.com/pub/dir/"+vars.first_name+"/"+vars.last_name+"?trk=uno-reg-guest-home-name-search"
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
"""
            problem = e
            error.log(str(problem), uc)
            print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow','bold'))
### PEOPLELOOKER.COM
        print(colored("Searching PeopleLooker.com For Target...",'blue','bold'))
        url = "https://www.peoplelooker.com/lp/400200/2/loading?fn="+vars.first_name+"&ln="+vars.last_name+"&state="+abv[vars.state]
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
        except Exception, e:
            uc = """
        url = "https://www.peoplelooker.com/lp/400200/2/loading?fn="+vars.first_name+"&ln="+vars.last_name+"&state="+abv[vars.state]
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
"""
            problem = e
            error.log(str(problem), uc)
            print(colored("I wasn\'t able to get that site...\nLet\'s try this one.",'yellow','bold'))
### GOOGLE.COM
        print(colored("No Search Would Be Complete Without ",'blue','bold')+google_logo)
        url = "https://www.google.com/#q="+vars.first_name+"+"+vars.middle_name+"+"+vars.last_name+"+"+vars.city+"+"+vars.state
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
        except Exception, e:
            uc = """
        url = "https://www.google.com/#q="+vars.first_name+"+"+vars.middle_name+"+"+vars.last_name+"+"+vars.city+"+"+vars.state
        time.sleep(2)
        try:
            webbrowser.open(url)
            time.sleep(2)
"""
            problem = e
            error.log(str(problem), uc)
            print(colored("I wasn\'t able to get that site...\n",'red','bold'))
    except Exception, e:
        uc = "gears.stalker_gui()"
        problem = e
        error.log(str(problem), uc)
        print(colored(e,'red','bold'))
######################################################################
######################################################################
######################################################################
def profile_manager():
    name = vars.full_name
    clear()
    sep = "\n\n==================================================\n\n"
###   GET VARIABLES FOR NEW PROFILE
    if vars.full_info == False and vars.basic_info == False:
        try:
            full_info()
            vars.full_info = True
            time.sleep(2)
        except KeyboardInterrupt:
            try:
                basic_info()
                vars.basic_info = True
                msg(target,'blue','bold')
                time.sleep(2)
            except Exception, e:
                uc = "gears.profile_manager()"
                problem = e
                print (e)
                error.log(str(problem), uc)
    else:
        print "Using Information From %s\'s Profile."% vars.full_name
        with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'r') as profile:
            data = profile.read()
            msg(data,'yellow','bold')
            profile.close()
        time.sleep(2)

    try:
        name = vars.full_name
#        address = str(vars.address)
#        age = str(vars.age)
#        dob = str(vars.dob)
#        phone = str(vars.phone)
#        sec_phone = str(vars.sec_phone)
#        employer = str(vars.employer)
#        employer_phone = str(vars.employer_phone)
#        employer_address = str(vars.employer_address)
#        job_title = str(vars.job_title)
        hobbies = str(vars.hobbies)
###   IF USER HITS CTRL^C
    except KeyboardInterrupt:
        clear()
        time.sleep(2)
###   RESTART STALKER
        print "Restarting Stalker..."
        os.execv(sys.executable, ['python'] + sys.argv)
##  OPEN Stalker PROFILE AND ADD USER INPUT INFORMATION
##  ADD VEHICLES TO PROFILE
    add_vehicle()
## OPEN Stalker PROFILE
    with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
        profile.write(sep+"\nKnown Emails: \n")
        profile.close()
    with open("/usr/share/stalker/profiles/%s/%s.bio"% (vars.full_name, vars.full_name),'a') as profile:
        profile.write(sep+"\nKnown Emails: \n")
        profile.close()
##  ASK USER TO ADD EMAIL ADDRESSES TO PROFILE
    while True:
        try:
            print(colored("Press Return To Add An Email Address\n",'yellow','bold'))
            print(colored("Press Return On Empty Line When You Are Finished\n",'red','bold'))
            new_email = raw_input(colored("Enter Targets Known Email Addresses: ",'red',attrs=['bold']))
##  IF USER ENTERED AN EMAIL
            if len(new_email) > 1:
##  OPEN Stalker PROFILE AND ADD EMAIL
                with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                    profile.write("\n "+new_email)
                    profile.close()
                data = "\n   "+str(new_email)
                tpro.personal(data)
##  IF USER DID NOT ENTER AN EMAIL
            else:
                print(colored("\nEmail Addresses Have Been Added! ",'yellow','bold'))
##  OPEN Stalker PROFILE AND ADD SEPERATOR
                with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                    profile.write(sep)
                    profile.close()
                break
##  IF USER HITS CTRL^C
        except KeyboardInterrupt:
##  ADD EMAILS TO Stalker PROFILE
            print(colored("\nEmail Addresses Have Been Added! ",'yellow','bold'))
            with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
##  ADD SEPERATOR
                profile.write(sep)
                profile.close()
            break
    with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
        profile.write("\nImmediate Family: \n")
        profile.close()
    with open("/usr/share/stalker/profiles/%s/%s.bio"% (vars.full_name, vars.full_name),'a') as profile:
        profile.write("\nImmediate Family: \n")
        profile.close()
    while True:
        try:
            print(colored("Press Return To Add Family Member\n",'yellow','bold'))
            print(colored("Press Return On Empty Line When You Are Finished\n",'red','bold'))
            fams = raw_input(colored("Enter Immediate Family Members: ",'red',attrs=['bold']))
            if len(fams) > 1:
                with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                    relation = raw_input(colored("Relationship To "+name+"?: ",'blue',attrs=['bold']))
                    profile.write(fams+"  :  "+relation+"\n")
                    profile.close()
                data = "\n   "+str(fams)+"  :  "+str(relation)
                tpro.personal(data)
            else:
                print(colored("\nFamily Members Have Been Added! ",'yellow','bold'))
                with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                    profile.write(sep)
                    profile.close()
                break
        except KeyboardInterrupt:
            print(colored("\nFamily Members Have Been Added! ",'yellow','bold'))
            with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                profile.write(sep)
                profile.close()
            break
    with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
        profile.write("\nAssociates: \n")
        profile.close()
    with open("/usr/share/stalker/profiles/%s/%s.bio"% (vars.full_name, vars.full_name),'a') as profile:
        profile.write("\nAssociates: \n")
        profile.close()
    while True:
        try:
            print(colored("Press Return To Add Associate\n",'yellow','bold'))
            print(colored("Press Return On Empty Line When You Are Finished\n",'red','bold'))
            asc = raw_input(colored("Enter Associate\'s Name: ",'red',attrs=['bold']))
            if len(asc) > 1:
                with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                    profile.write(asc+"\n")
                    profile.close()
                data = "\n   "+str(asc)
                tpro.personal(data)
            else:
                print(colored("\nAssociates Have Been Added! ",'yellow','bold'))
                with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                    profile.write(sep)
                    profile.close()
                break
        except KeyboardInterrupt:
            print(colored("\nAssociates Have Been Added! ",'yellow','bold'))
            with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                profile.write(sep)
                profile.close()
            break
    social_media()
    with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
        profile.write("Hobbies: \n"+hobbies+sep+"Reference URLs: \n")
        profile.close()
    with open("/usr/share/stalker/profiles/%s/%s.bio"% (vars.full_name, vars.full_name),'a') as profile:
        profile.write("\nHobbies: \n"+hobbies)
        profile.close()
    with open("/usr/share/stalker/profiles/%s/%s.bio"% (vars.full_name, vars.full_name),'a') as profile:
        profile.write("Reference URLS: \n")
        profile.close()
    while True:
        try:
            print(colored("Press Return To Add URL\n",'yellow','bold'))
            print(colored("Press Return On Empty Line When You Are Finished\n",'red','bold'))
            ref_url = raw_input(colored("Enter Reference URLs: ",'red',attrs=['bold']))
            if len(ref_url) > 3:
                with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                    profile.write(ref_url+"\n")
                    profile.close()
                data = "\n   "+str(ref_url)
                tpro.personal(data)
            else:
                print(colored("\nReference URLs Have Been Added! ",'yellow','bold'))
                with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                    profile.write(sep)
                    profile.close()
                break
        except KeyboardInterrupt:
            print(colored("\nReference URLs Have Been Added! ",'yellow','bold'))
            with open("/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name),'a') as profile:
                profile.write(sep)
                profile.close()
                break
    try:
        try:
            remove_gpg()
        except Exception, e:
            uc = """gears.profile_manager()"""
            print(e)
            subprocess.call(":>"+name+".gpg")
            subprocess.call("rm "+name+".gpg")
    except Exception, e:
        uc = """gears.profile_manager()"""
        problem = e
        error.log(str(problem), uc)
        clear()
        print(e)
        time.sleep(2)
        pass
    try:
        try:
            encrypt_file()
        except Exception, e:
            uc = """gears.encrypt_file()"""
            problem = e
            error.log(str(problem), uc)
            print(e)
            subprocess.call(["gpg","-r","--default-recipient","terminal","--yes","-e","/usr/share/stalker/profiles/.",vars.full_name])
    except Exception, e:
        uc = """subprocess.call(["gpg","-r","--default-recipient","terminal","--yes","-e","/usr/share/stalker/profiles/.",vars.full_name])"""
        problem = e
        error.log(str(problem), uc)
        print(e)
        try:
            os.system("gpg -r --default-recipient terminal --yes -u /usr/share/stalker/profiles/."+vars.full_name)
        except Exception, e:
            uc = """os.system("gpg -r --default-recipient terminal --yes -u /usr/share/stalker/profiles/."+vars.full_name)"""
            problem = e
            error.log(str(problem), uc)
            print(colored(e,'red','bold'))
    try:
        try:
            remove_unencrypted()
        except Exception, e:
            uc = """gears.remove_unencrypted()"""
            problem = e
            error.log(str(problem), uc)
            print(e)
            subprocess.call([":",">","/usr/share/stalker/profiles/.",vars.full_name])
    except Exception, e:
        problem = e
        error.log(str(problem), uc)
        print(e)
    try:
        os.system(": > /usr/share/stalker/profiles/."+vars.full_name)
    except Exception, e:
        uc = """os.system(": > /usr/share/stalker/profiles/."+vars.full_name)"""
        problem = e
        error.log(str(problem), uc)
        print(colored(e,'red','bold'))
    try:
        subprocess.call(["rm","/usr/share/stalker/profiles/.",vars.full_name])
    except Exception, e:
        uc = """subprocess.call(["rm","/usr/share/stalker/profiles/.",vars.full_name])"""
        problem = e
        error.log(str(problem), uc)
        print(e)
    try:
        os.system("rm /usr/share/stalker/profiles/."+vars.full_name)
    except Exception, e:
        uc = """os.system("rm /usr/share/stalker/profiles/."+vars.full_name)"""
        problem = e
        error.log(str(problem), uc)
        print(colored(e,'red','bold'))
#===============================================================================================================
##  END PROFILE_MANAGER
#===============================================================================================================
################################################################################################################
################################################################################################################
def goodbye():
    print(colored("""
  ____  ___   ___  ____  ______   _______ _ 
 / ___|/ _ \ / _ \|  _ \| __ ) \ / / ____| |
| |  _| | | | | | | | | |  _  \\ V /|  _| | |
| |_| | |_| | |_| | |_| | |_) || | | |___|_|
 \____|\___/ \___/|____/|____/ |_| |_____(_)

""",'yellow',attrs=['bold']))
######################################################################
######################################################################
######################################################################

def intro():
    try:
        print(colored("\n\nIf you do not plan to create a new casefile, hit Ctrl^C now.\n\n",'cyan',attrs=['bold']))
        full_info()
        vars.intro = True
        if vars.full_info == True:
            vars.basic_info = True
        else:
            basic_info()
    except KeyboardInterrupt:
        stalker_logo()
        print(colored("\nIf You Do Not Plan To Create A CaseFile, I Just Need Some Basic Info...\n",'red','bold'))
        try:
            basic = raw_input(colored("\nAre You Going To Create A CaseFile: ",'yellow',attrs=['bold']))
        except KeyboardInterrupt:
            stalker_logo()
            print(colored("\nUser Hit Ctrl^C!!!\nTerminating Stalker...\n"))
            sys.exit(0)
        if len(basic)>= 1:
            if basic == "n" or basic == "no" or basic == "N" or basic == "NO" or basic == "No":
                try:
                    basic_info()
                except KeyboardInterrupt:
                    print(colored("\nUser Hit Ctrl^C...\nExiting Stalker."))
                    time.sleep(2)
                    sys.exit(0)
                stalker_logo()
                version = raw_input(colored("\nWould you like to run stalker from a [",'yellow',attrs=['bold'])+colored("b",'red',attrs=['bold'])+colored("]rowser or the [",'yellow',attrs=['bold'])+colored("t",'red',attrs=['bold'])+colored("]erminal?\n   >> ",'yellow',attrs=['bold']))
                if version == "T" or version == "t" or version == "terminal" or version == "Terminal" or version == "TERMINAL":
                    try:
                        stalker_logo()
                        try:
                            stalker()
                        except KeyboardInterrupt:
                            print(colored("Stalker Has Been Terminated By User...",'red','bold'))
                            time.sleep(2)
                            sys.exit(0)
                    except KeyboardInterrupt:
                        clear()
                        print(colored("\n\n\n\n\nUSER HIT CTRL^C\nSTOPPING STALKER...",'red','bold'))
                        time.sleep(2)
                        pass
                elif version == "B" or version == "b" or version == "browser" or version == "Browser" or version == "BROWSER":
                    try:
                        stalker_logo()
                        stalker_gui()
                    except KeyboardInterrupt:
                        clear()
                        print(colored("\n\n\n\n\nUSER HIT CTRL^C\nSTOPPING STALKER...",'red',attrsa=['bold']))
                        time.sleep(2)
                        sys.exit(0)
                else:
                    stalker_logo()
                    print(colored("\nINVALID OPTION!!!\n"))
                    pass
            elif basic == "y" or basic == "yes" or basic == "Yes" or basic == "Y" or basic == "YES":
                try:
                    full_info()
                except KeyboardInterrupt:
                    print(colored("I Need Some Information About Your Target Before We Begin...\nLet\'s Try Again.",'red','bold'))
                    time.sleep(2)
                    try:
                        full_info()
                    except KeyboardInterrupt:
                        print(colored("\nYour Failure To Follow Basic Instructions Is Infuriating...\n",'red','bold'))
                        print(colored("\nBye..."))
                        sys.exit(0)
            else:
                print(colored("\nINVALID OPTION!!!",'red','bold'))
                print(colored("\nYOU ARE NOT SMART ENOUGH TO USE THIS PROGRAM...\n      ***TERMINATING STALKER***"))
                sys.exit(0)
        else:
            stalker_logo()
            print(colored("\n\nYou Must Enter An Option!!!",'yellow','bold'))
######################################################################
######################################################################
######################################################################
def read_profile():
    clear()
    msg("Available Profiles: ",'red','bold')
    profile_lst = subprocess.check_output(["ls", "-a", "/usr/share/stalker/profiles/"],stderr=subprocess.PIPE, shell=False)
    msg(str(profile_lst),'blue','bold')
    print "\n\n"
    try:
        vars.first_name = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("First ",'red',attrs=['bold'])+colored("Name: ",'yellow',attrs=['bold']))
        vars.middle_name = raw_input(colored("Enter Targets ",'yellow',attrs=['bold'])+colored("Middle ",'red',attrs=['bold'])+colored("Name: ",'yellow',attrs=['bold']))
        vars.last_name =raw_input(colored("Enter Target ",'yellow',attrs=['bold'])+colored("Last ",'red',attrs=['bold'])+colored("Name: ",'yellow',attrs=['bold']))
        if len(vars.middle_name) >= 1:
            vars.full_name = vars.first_name+"_"+vars.middle_name+"_"+vars.last_name
        else:
            vars.full_name = vars.first_name+"_"+vars.last_name
#        gpg_path = "/usr/share/stalker/profiles/."+str(vars.full_name)+".gpg"
#        dec_path = "/usr/share/stalker/profiles/."+str(vars.full_name)
        clear()
        if len(vars.full_name) >= 3:
            try:
#                subprocess.call(["gpg","-decrypt ","/usr/share/stalker/profiles/.%s.gpg"% vars.full_name,">","/usr/share/stalker/.%s"% vars.full_name])
                gnupg_decrypt()
                try:
                    with open("/usr/share/stalker/profiles/.%s"% vars.full_name,'r') as profile:
                        data = profile.read()
                        msg("\n"+data,'blue','bold')
                        profile.close()
                        msg("CTRL^C To Continue\n\n\n",'red','bold')
                        while True:
                            try:
                                time.sleep(1)
                            except KeyboardInterrupt:
                                print "ok"
                                break
#                                try:
#                                    subprocess.call([":>",name,".gpg"])
#                                    subprocess.call(["rm",name,".gpg"])
#                                    remove_gpg()
#                                except Exception, e:
#                                    clear()
#                                    print (e)
#                                    time.sleep(2)
#                                    pass
#FIXME
#                            subprocess.call("gpg -r terminal --yes -e /usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name))
#                            subprocess.call(":>/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name))
#                            subprocess.call("rm /usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name))
#                            encrypt_file()
###
                except Exception, e:
                    uc = "gears.read_profile()"
                    problem = e
                    error.log(str(problem), uc)
                    print (e)
                    time.sleep(2)
                    pass
            except Exception, e:
#                msg("That Profile Does Not Exsist!!!\nPerhaps You Should Create It!",'red','bold')
                uc = "gears.read_profile()"
                problem = e
                error.log(str(problem), uc)
                print (e)
                time.sleep(2)
                pass
        else:
            msg("Profile Does Not Exsist!!!",'red','bold')
            time.sleep(2)
            pass
    except KeyboardInterrupt:
        pass

######################################################################
######################################################################
######################################################################
def phone_search():
    try:
        phone_num = vars.phone #raw_input(colored("Enter Phone Number: ",'red',attrs=['bold']))
        msg("Searching Zabasearch.com For Phone Number %s..."% vars.phone,'yellow','bold')
        url = "http://www.zabasearch.com/phone/"+phone_num
        time.sleep(2)
        try:
            try:
                subprocess.call(["w3m "+url])
            except Exception, e:
                uc = """subprocess.call([\"w3m \"+url])"""
                problem = e
                error.log(str(problem), uc)
                try:
                    subprocess.call(["wget -qO- "+url+" | html2text"])
                except Exception, e:
                    uc = """subprocess.call([\"wget -qO- \"+url+\" | html2text"])"""
                    problem = e
                    error.log(str(problem), uc)
                    msg("I wasn\'t able to contact ZabaSearch...\n Let\'s try ",'red','bold')+gears.google_logo
                    url = "https://www.google.com/q="+phone_num
                    time.sleep(2)
                    try:
                        subprocess.call(["w3m "+url])
                    except Exception, e:
                        uc = """subprocess.call([\"w3m \"+url])"""
                        problem = e
                        error.log(str(problem), uc)
                        try:
                            webbrowser.open(url)
                        except Exception, e:
                            uc = """webbrowser.open(url)"""
                            problem = e
                            error.log(str(problem), uc)
                            msg("I wasn't able to contact ")+google_logo
                            time.sleep(2)
                            pass
        except Exception, e:
            uc = """gears.phone_search()"""
            problem = e
            error.log(str(problem), uc)
            msg("Here\'s what went wrong...\n"+e,'red','bold')
            time.sleep(3)
    except KeyboardInterrupt:
        msg("USER HIT CTRL^C!!!\n Phone Number Search Terminated...")
        time.sleep(1)
        pass
######################################################################
######################################################################
######################################################################
def edit_profile():
    clear()
    print "\n\n"
    msg("Available Profiles: ",'red','bold')
    profile_lst = subprocess.check_output(["ls", "-a", "/usr/share/stalker/profiles/"],stderr=subprocess.PIPE, shell=False)
    msg(profile_lst,'blue','bold')
    print "\n\n"
    try:
        name = raw_input(colored("Enter Target Name: ",'red',attrs=['bold']))
        vars.full_name = name
        try:
            path = "/usr/share/stalker/profiles/."+str(name)
            gpg_path = str(path)+".gpg"
            msg("Using subprocess.call",'yellow','bold')
            time.sleep(2)
            subprocess.call(["gpg", "--decrypt ",gpg_path," > ",path],stderr=subprocess.PIPE,shell=False)
        except Exception, e:
            uc = """
            path = "/usr/share/stalker/profiles/."+str(name)
            gpg_path = str(path)+".gpg"
            msg("Using subprocess.call",'yellow','bold')
            time.sleep(2)
            subprocess.call(["gpg", "--decrypt ",gpg_path," > ",path],stderr=subprocess.PIPE,shell=False)
"""
            problem = e
            error.log(str(problem), uc)
            try:
#FIXME
                path = "/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name)
                gpg_path = path+".gpg"
                msg("Using subprocess.Popen",'yellow','bold')
                time.sleep(2)
###
#REMOVE
                subprocess.Popen("gpg --decrypt "+gpg_path+" > "+path)
#\\\
            except Exception, e:
                uc = """subprocess.Popen("gpg --decrypt "+gpg_path+" > "+path)"""
                problem = e
                error.log(str(problem), uc)
                try:
#REMOVE
                    msg("FALLING BACK TO OS.SYSTEM!!!",'red','bold')
                    time.sleep(2)
#\\\ FIXME
                    subprocess.call(["gpg", "--decrypt", gpg_path," > ",path])
###
                except Exception, e:
                    uc = """subprocess.call(["gpg", "--decrypt", gpg_path," > ",path])"""
                    problem = e
                    error.log(str(problem), uc)
                    msg("Here\'s What Went Wrong: \n "+e,'red','bold')
                    time.sleep(2)
                    pass
        try:
            subprocess.call(["nano ",path])
        except Exception, e:
            uc = """
subprocess.call(["nano ",path])
"""
            problem = e
            error.log(str(problem), uc)
            msg(e,'red','bold')
            os.system("nano "+path)
        try:
            subprocess.call(":>"+name+".gpg")
            subprocess.call("rm "+name+".gpg")
        except Exception, e:
            uc = """
            subprocess.call(":>"+name+".gpg")
            subprocess.call("rm "+name+".gpg")
"""
            problem = e
            error.log(str(problem), uc)
            clear()
            print (e)
            msg("FALLING BACK ON OS.SYSTEM!!!",'red','bold')
            time.sleep(2)
#REMOVE
            os.system(":>"+name+".gpg")
            os.system("rm "+name+".gpg")
#\\\
            msg("Old Files Have Been Overwritten And Removed!",'green','bold')
            time.sleep(2)
            pass
        try:
#REMOVE
            subprocess.call("gpg -r terminal --yes -e /usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name))
            subprocess.call(":>/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name))
            subprocess.call("rm /usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name))
#\\\
        except Exception, e:
            uc = """
            subprocess.call("gpg -r terminal --yes -e /usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name))
            subprocess.call(":>/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name))
            subprocess.call("rm /usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name))
"""
            problem = e
            error.log(str(problem), uc)
            print (e)
            msg("I wasn\'t able to use subprocess.call...\n FALLING BACK TO OS.SYSTEM!!!",'red','bold')
            time.sleep(2)
#REMOVE
            os.system("gpg -r terminal --yes -e /usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name))
            os.system(":>/usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name))
            os.system("rm /usr/share/stalker/profiles/%s/%s.txt"% (vars.full_name, vars.full_name))
#\\\
            msg("File Removal And Encryption Success!",'green','bold')
            time.sleep(2)
    except KeyboardInterrupt:
        pass

