from ome_types import from_tiff
import os

ome2 = from_tiff('tubhiswt.ome.tif')

ome3 = ome2.images[0]
ome4 = ome2.experimenters[0]
ome5 = ome2.experiments[0]
ometype = ome5.type[0]
ome6 = ome2.instruments[0]
omeobjectives = ome6.objectives[0]
ome7 = ome6.detectors[0]
ome8 = ome6.light_source_group[0]
stname = ome4.first_name + '.' + ome4.last_name + '.' + ome3.name + '.' + ome5.description + '.' \
    + str(ome6.microscope.model) + '.' + str(ome6.microscope.type) +'.' + str(ome3.acquisition_date)
print("*****************************INFORMATIONS GENERALES*********************************************")
print(ome2)
print("------------------------------DETAILS IMAGES----------------------------------------------------")
print(ome3)
print("------------------------------TYPE--------------------------------------------------------------")
print(ometype)
print("------------------------------DETAILS EXPERIMENTATEUR-------------------------------------------")
print(ome4)
print("------------------------------DETAILS EXPERIENCE------------------------------------------------")
print(ome5)
print("------------------------------DETAILS APPAREILS-------------------------------------------------")
print(ome6)
print("------------------------------DETAILS OBJECTIFS ------------------------------------------------")
print(omeobjectives)
print("------------------------------DETAILS DETECTEURS------------------------------------------------")
print(ome7)
print("------------------------------DETAILS SOURCES LUMINEUSES----------------------------------------")
print(ome8)
print("------------------------------DETAILS SOUHAITES POUR NOMINATIONS DES FICHIERS-------------------")
print("prenom_experimentateur.nom_experimentateur.nom_experience.description_experience.model_microscope.type_microscope.date_acquisition")
print(stname)

