#coding:utf-8

import os

case = input ("Case name: ")

#Création de l'arborescence
os.mkdir ("/root/Forensic")
os.mkdir ("/root/Forensic/"+case)
os.mkdir ("/root/Forensic/"+case+"/artefacts")
os.mkdir ("/root/Forensic/"+case+"/source")
os.mkdir ("/root/Forensic/"+case+"/browser")
os.mkdir ("/root/Forensic/"+case+"/browser/chrome")
os.mkdir ("/root/Forensic/"+case+"/browser/firefox")
os.mkdir ("/root/Forensic/"+case+"/download")
os.mkdir ("/root/Forensic/"+case+"/evidence")
os.mkdir ("/root/Forensic/"+case+"/prefetch")
os.mkdir ("/root/Forensic/"+case+"/recycle")

dd = os.lsblk()
print (dd)
