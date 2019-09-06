from ldap3 import Server, Connection, ALL
import sys, string, os, subprocess, sched, time,re,datetime,shutil




folder='C:\\Users\\MMusa\\Desktop\\c' # Roaming Profiles

adminpass() # call admin pass, so we can use password variables

server = Server('Microsoft.com', get_info=ALL) # LDAP server
c = Connection(server,'Microsoft\\administrator','password', auto_bind=True) # Connection and calling password from adminpass function


c.bind()# establish connection


c.search(search_base = 'OU=Companies-TerminatedEmployees,DC=Microsoft,DC=com',   # search filter to look in terminated employees
         search_filter = '(objectClass=person)', # Users only
         attributes = ['sAMAccountName'], # User Account name
         )

for entry in c.entries: # to get  all users 
   user=entry.sAMAccountName # store username in user
   #print (user) # print user
   username=str(user)# store it as string
   V6=username+".V6" # Add V6 to username because each username has folder ends with .V6 
   folder='C:\\Users\\MMusa\\Desktop\\c\\'+V6 # Folder now will have username +.V6
   print (folder)
   input("Press Enter to continue...")
   fix_permission=['icacls',folder,'/T','/Q','/C','/RESET'] # This command to reset permission for each user in case if they were corrupted
   take_owner=['TAKEOWN','/F',folder,'/r', '/d','y'] # this code to take ownership of folder+ subfolders+ all files as well to Administrator
   subprocess.Popen(fix_permission).wait() # Run fix permission
   subprocess.Popen(take_owner).wait()# Run  Take owner
   try: # we call try so it won't stop if folder is not exist for a username
      shutil.rmtree(folder)  # Remove folder and all contents
      print(folder,"Folder has been deleted.") # print on screen it has been deleted
   except:
      print(folder,"Folder not found.") # print folder not found in case if it's not exist

print ("================================================")


print ("Job is done")

print ("================================================")