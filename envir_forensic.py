#coding:utf-8

import os
#Création du user case
case = input ("Case name: ")
#Test présence dossier Forensic
here = os.path.exists("/root/Forensic")

if here :
    print ("Le dossier Forensic existe déjà. Souhaitez vous ajouter votre cas dedans ? yes/no")
    answer = input (">")
    answer = str(answer)
    if answer == "yes" :
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
        print ("Le case : {} a bien été créé dans le dossier Forensic.".format (case))

    else :
        print ("Au revoir bobo")

else :
    print ("Le dossier Forensic n'existe pas. Souhaitez vous le créér ? yes/no")
    answer2 = input (">")
    answer2 = str(answer2)
    if answer2 == "yes" :
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
        print ("Tous les dossier ont bien été créé dans le dossier Forensic, case : {}".format (case))
    else :
        print ("Au revoir")
