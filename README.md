# Projet_Organoid
Fichier config d'OMERO

Ce repository contient les fichiers avec les variables d'environnements nécessaire au fonctionnement d'OMERO.

Les fichiers .env situés dans /opt/ doit être source lorsqu'on démarre le serveur manuellement.
Le fichier .bash situé dans /opt/ doit être source lorsqu'on démarre le client web manuellement. 
Les fichiers config.xml situé dans .../etc/grid sont parcouru lorsque l'on démarre le serveur et le client web. 
omero-init.d et omero-web-init.d permet de démarrer le serveur et le client web automatiquement.

Les fichiers virtualbox*.bash permettent de résoudre le problème de démarrage du serveur sous VM.
