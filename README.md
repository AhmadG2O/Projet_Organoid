# Projet_Organoid
Fichier config d'OMERO

Ce repository contient les fichiers avec les variables d'environnements nécessaire au fonctionnement d'OMERO et des fonctions pythons permettant la nomination de fichier.

Dans le dossier Fonction python on retrouve :
- ome_type.py : fonction parsant les données contenues dans l'entête OME-XML d'un fichier OME-TIFF permettant leur traitement via python.
- nomination_fichier.py : fonction permettant la copie puis la nomination d'un fichier OME-Tiff selon les informations conservées dans l'entête OME-XML et un formulaire renseignant le marquage utilisé lors de l'expérience.

Les fichiers settings.env et ice-omero.bash situés dans /opt/ doivent être source lorsqu'on démarre le serveur manuellement.
Le fichier confw.env situé dans /opt/ doit être source lorsqu'on démarre le client web manuellement. 
Les fichiers config.xml situés dans .../etc/grid sont parcouru lorsque l'on démarre le serveur et le client web. 

omero-init.d et omero-web-init.d permet de démarrer le serveur et le client web automatiquement.
Les fichiers virtualbox*.bash permettent de résoudre le problème de démarrage du serveur sous VM.
