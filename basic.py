#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import subprocess
import os
import requests
import gnupg as gpg
from bs4 import BeautifulSoup as bs
from termcolor import colored
#######################################################################
#######################################################################
#######################################################################
###   BASIC FUNCTIONS   ###############################################
#######################################################################
#######################################################################
#######################################################################
######################################################################
# CLEAR                                                              #
######################################################################
def clear():
    subprocess.call("clear")
#    print colored("\n######################################################################\n",'blue',attrs=['bold'])
#######################################################################
# RESTART                                                             #
#######################################################################
def restart():
    os.execv(sys.executable, ['python'] + sys.argv)
#######################################################################
# WAIT TIMER                                                          #
#######################################################################
class Timer(object):
    def wait(self, timer):
        time.sleep(timer)
#######################################################################
#######################################################################
pause_for = Timer()
wait = pause_for.wait
#   wait(20)
#######################################################################
#######################################################################
#######################################################################
###   MESSAGE HANDLING   ##############################################
#######################################################################
#######################################################################
#######################################################################
class Msg_Print(object):
# STANDARD MESSAGE WITH ATTRIBUTE SPECIFICATION
    def std_msg(self, message, color, atts):
        print colored(message, color, attrs=[atts])
        time.sleep(2)
# STANDATD MESSAGE WITH ADJUSTABLE TIMER
    def timed_msg(self, message, color, timer):
        print colored(message, color, attrs=['bold'])
        time.sleep(int(timer))
# STANDARD MESSAGE WITHOUT ATTRIBUTE SPECIFICATION
    def alt_msg(self, message, color):
        print colored(message, color)
        time.sleep(2)
# STANDARD MESSAGE WITH 'BOLD' ATTRIBUTE
    def clr(self, message, color):
        return colored(message, color, attrs=['bold'])
# STANDARD MESSAGE WITHOUT TIME.SLEEP(X) AND WITH 'BOLD' ATTRIBUTE
    def fast_msg(self, message, color):
        print colored(message, color, attrs=['bold'])
# STANDARD MESSAGE WITHOUT TIME.SLEEP(X) OR ATTRIBUTE SPECIFICATION
    def fast_alt(self, message, color):
        print colored(message, color)
#######################################################################
show_msg = Msg_Print()
msg = show_msg.std_msg
dmsg = show_msg.alt_msg
clr = show_msg.clr
fst = show_msg.fast_msg
tmd = show_msg.timed_msg
#######################################################################
# tmd('Hello there, Fred!','magenta',3)
#   >>> print colored('Hello there, Fred!','magenta',attrs=[bold])
#   >>> time.sleep(3)
# print clr('Hello Friend!','yellow')
# msg('You Can Add Attributes To Me!','blue','bold')
# dmsg("I have No Attributes!",'blue')
#######################################################################
#######################################################################
#######################################################################
###   File/Directory Editing   ########################################
#######################################################################
#######################################################################
#######################################################################
class File(object):
# APPEND TO FILE
    def scribe(self, file, message):
        with open(file, 'a') as edit:
            edit.write(message)
            edit.close()
# APPEND/WRITE TO FILE
    def alt_scribe(self, file, message, option):
        with open(file, option) as edit:
            edit.write(message)
            edit.close()
# READ FILE
    def gander(self, file):
        with open(file, 'r') as read_it:
            data = read_it.read()
            print colored(data, 'blue', attrs=['bold'])
            read_it.close()
#######################################################################
class Delete(object):
# DELETE SPECIFIED FILE
    def del_file(self, file):
        try:
            subprocess.call(["rm ", file])
        except Exception, e:
            print (e)
            subprocess.call(["sudo", " rm ", file])
# DELETE SPECIFIED DIRECTORY
    def del_dir(self, dir_path):
        try:
            subprocess.call(["rm", "-r", dir_path])
        except Exception, e:
            print (e)
            subprocess.call(["sudo", "rm", "-r", dir_path])
# DELETE ALL FILES IN DIRECTORY
    def clear_dir(self, dir_path):
        subprocess.call(["rm", "-r", dir_path, "/*"])
        return "Files Cleared From %s"% dir_path
#######################################################################
class Make_Dir(object):
    def create(self, path):
        subprocess.call(["mkdir", path])
#######################################################################
#scribble = File()
#scribe = scribble.scribe
#alt_scribe = scribble.alt_scribe
#######################################################################
#scribe('/root/testing/test_file.txt','Testing This Class With A Random File')
#look = scribble.gander
#######################################################################
#alt_scribe('/root/testing/test_file.txt','Testing This Class With A Random File','w')
#look('/root/testing/test_file.txt')
#######################################################################
#######################################################################
#######################################################################
###   Error Handling   ################################################
#######################################################################
#######################################################################
#######################################################################
class Error(object):
    def log(self, error, command):
# WRITE ERROR DATA TO '/USR/SHARE/STALKER/ERROR.LOG'
        with open("/usr/share/stalker/error.log", 'a') as log:
            log.write("\n#############################################################################################################\n")
            log.write(time.strftime("%d/%m/%Y")+" | "+time.strftime("%H:%M:%S"))
            log.write("\n")
            log.write(command)
            log.write("\n")
            log.write(error)
            log.write("\n#############################################################################################################")
            log.close()
    def alt_log(self, error):
        with open("/usr/share/stalker/error.log", 'a') as log:
            log.write("\n#############################################################################################################\n")
            log.write(time.strftime("%d/%m/%Y")+" | "+time.strftime("%H:%M:%S"))
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
            print colored(message,color,on_color,attrs=['bold',atts])
#######################################################################
#######################################################################
#######################################################################
###   GPG ENCRYPT/DECRYPT CONTROL   ###################################
#######################################################################
#######################################################################
#######################################################################
# Crypto                                                              #
#######################################################################
#path = "/usr/share/stalker/profiles/.%s"% str(vars.full_name)
#path = "/usr/share/stalker/gpg_test_file"
#gpg = str(path)+".gpg"
#error = Error()
#######################################################################
class Scrambler(object):
######################################################################
# REMOVE GPG                                                         #
######################################################################
    def remove_gpg(self, path):
        try:
            subprocess.call([":",">",path])
            subprocess.call(["rm ",path])
        except Exception, e:
#            problem = e
#            uc = """subprocess.call([":",">",path])"+"\n"+"subprocess.call(["rm ",path])"""
#            error.log(str(problem), uc)
            print (e)
            os.system(":>"+path)
            os.system("rm "+path)
######################################################################
######################################################################
######################################################################
    def encrypt_file(self, path):
        try:
            subprocess.call(["gpg","-r","--default-recipient","terminal","--yes","-e",path])
        except Exception, e:
            print (e)
#            uc = """subprocess.call(["gpg","-r","--default-recipient","terminal","--yes","-e",path])"""
#            problem = e
#            error.log(str(problem), uc)
            os.system("gpg -r --default-recipient termianl --yes -e "+path)
######################################################################
######################################################################
######################################################################
    def remove_unencrypted(self, path):
        try:
            subprocess.call([":",">",path])
            subprocess.call(["rm",path])
        except Exception, e:
            print (e)
#            uc = """subprocess.call([":",">",path])\nsubprocess.call(["rm",path])"""
#            problem = e
#            error.log(str(problem), uc)
            os.system(":>"+path)
            os.system("rm "+path)
######################################################################
######################################################################
######################################################################
    def decrypt_file(self, path, out):
        try:
           subprocess.call(["gpg","-d",path,">",out])
        except Exception, e:
            print (e)
        try:
##                e = error_one
            os.system("gpg -d "+path+" > "+ out)
        except Exception, e:
#            uc = """os.system("gpg -d "+path+" > "+out)"""
#            problem = e
#            error.log(str(problem), uc)
##                e = error_two
##               msg("Subprocess.Call Said: \n"+error_one,'red','bold')
            msg("OS.System Said: \n"+str(e),'blue','bold')
######################################################################
######################################################################
######################################################################
    def gnupg_encrypt(self, path, out):
        try:
            open(path, 'w')#.write('This is an example.')
            with open(path, 'rb') as f:
                status = gpg.encrypt_file(
                    f, recipients=['terminal'],
                    output = out)
            print 'ok: ', status.ok
            print 'status: ', status.status
            print 'stderr: ', status.stderr
        except Exception, e:
#            uc = """
#            open(path, 'w')#.write('This is an example.')
#            with open(path, 'rb') as f:
#                status = gpg.encrypt_file(
#                    f, recipients=['terminal'],
#                    output=out
#"""
#            problem = e
#            error.log(str(problem), uc)
            print (e)
######################################################################
######################################################################
######################################################################
    def gnupg_decrypt(self, path, out):
        try:
            subprocess.call(["stty", "-echo"])
            password = raw_input("What\'s The Magic Word\n|?|: ")
            print "\n"
            subprocess.call(["stty", "echo"])
            gpg.decrypt_file(path, always_trust=False, passphrase=password, output=out)
            time.sleep(2)
        except Exception, e:
#            uc = """
#            subprocess.call(["stty", "-echo"])
#            password = raw_input("What\'s The Magic Word\\n|?|: ")
#            subprocess.call(["stty", "echo"])
#            gpg.decrypt_file(path, always_trust=False, passphrase=password, output=out
#            time.sleep(2)
#"""
#            problem = e
#            error.log(str(problem), uc)
            print "\n"
            print (e)
            with open(path, 'rb') as f:
                status = gpg.decrypt_file(f, passphrase=password, output=out)
            print 'ok: ', status.ok
            print 'status: ', status.status
            print 'stderr: ', status.stderr
            with open(path,'r') as profile:
                data = profile.readlines()
                print (data)
                time.sleep(2)
                profile.close()
                stream = open(path, "rb")
                decrypted_data = gpg.decrypt_file(stream)
                msg(str(decrypted_data),'blue','bold')
######################################################################
crypt = Scrambler()
encrypt = crypt.encrypt_file
decrypt = crypt.decrypt_file
######################################################################
# Web Page Handling                                                  #
######################################################################
class Spyder(object):
    def get_site(self, url):
        page = requests.get(url)
        html = page.text
        text_only = bs(html, 'html.parser')
        text = text_only.get_text()
        data = text.encode('ascii', 'ignore').decode('ascii')
        print (data)
    def save_site(self, url, file):
        page = requests.get(url)
        html = page.text
        text_only = bs(html, 'html.parser')
        text = text_only.get_text()
        data = text.encode('ascii', 'ignore').decode('ascii')
        with open(file,'w') as file:
            file.write(data)
            file.close()
    def multi_save(self, url, file):
        page = requests.get(url)
        html = page.text
        text_only = bs(html, 'html.parser')
        text = text_only.get_text()
        data = text.encode('ascii', 'ignore').decode('ascii')
        with open(file,'a') as file:
            file.write(data)
            file.close()
retrieve = Spyder()
spyder = retrieve.get_site
save_site = retrieve.save_site
multi_save = retrieve.multi_save
# spyder(url)
# save_site(url, '/path/to/file')
# multi_save(url, '/path/to/file') ### Saved Sites Are Appended To 'file'
######################################################################
# Password                                                           #
######################################################################
def del_pass():
    vars.password = ""
def password():
    subprocess.call(["stty", "-echo"])
    vars.password = raw_input("Please Enter Password: ")
    subprocess.call(["stty", "echo"])
### {somecode}
### del_pass() ### <<< REMOVE THE PASSWORD FROM THE VARIABLE FILE >>> FIXME