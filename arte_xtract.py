#coding:utf-8

import shutil
import os

case = input ("Case name: ")

#Liste des utilisateurs disponibles sur la partition montée
users_sdb = os.listdir ("/root/Forensic/"+case+"/source/Users/")
print ("Utilisateurs disponibles :", users_sdb)

#Récupération du nom d'utilisateur
user = input ("Name user : ")

#Extract SAM
shutil.copy('/root/Forensic/'+ case +'/source/Windows/System32/config/SAM','/root/Forensic/'+ case +'/artefacts/SAM')

#Extract SYSTEM
shutil.copy('/root/Forensic/'+ case +'/source/Windows/System32/config/SYSTEM','/root/Forensic/'+ case +'/artefacts/SYSTEM')

#Extract SECURITY
shutil.copy('/root/Forensic/'+ case +'/source/Windows/System32/config/SECURITY','/root/Forensic/'+ case +'/artefacts/SECURITY')

#Extract SOFTWARE
shutil.copy('/root/Forensic/'+ case +'/source/Windows/System32/config/SOFTWARE','/root/Forensic/'+ case +'/artefacts/SOFTWARE')

#Extract DEFAULT
shutil.copy('/root/Forensic/'+ case +'/source/Windows/System32/config/DEFAULT','/root/Forensic/'+ case +'/artefacts/DEFAULT')

#Extract NTUSER.DAT
shutil.copy('/root/Forensic/'+ case +'/source/Users/'+user+'/NTUSER.DAT','/root/Forensic/'+ case +'/artefacts/NTUSER.DAT')

#Extract UsrClass.dat
shutil.copy('/root/Forensic/'+ case +'/source/Users/'+user+'/AppData/Local/Microsoft/Windows/UsrClass.dat','/root/Forensic/'+ case +'/artefacts/UsrClass.dat')
