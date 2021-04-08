import os
import shutil
import string
from tkinter import *
from tkinter.messagebox import showinfo
from ome_types import from_tiff
       
window = Tk()
def chnge():

    fichier = str(loc_e.get())
    print(fichier)
    ome2 = from_tiff(fichier)
    ome3 = ome2.images[0]
    ome4 = ome2.experimenters[0]
    ome5 = ome2.experiments[0]
    ometype = ome5.type[0]
    ome6 = ome2.instruments[0]
    omeobjectives = ome6.objectives[0]
    ome7 = ome6.detectors[0]
    ome8 = ome6.light_source_group[0]
    
    stname = ome4.first_name + '.' + ome4.last_name + '.' + ome3.name + '.' + ome5.description + '.' + str(ome6.microscope.model) + '.' + str(ome6.microscope.type) +'.' + str(ome3.acquisition_date)
    punct = string.punctuation
    for c in punct :
        stname = stname.replace(c,".")
    print(stname)
    marquage = str(nam_e.get())
    #print(marquage)
    oldext = os.path.splitext(fichier)[1]
    #print(oldext)
    dst = marquage + '.' + stname
    #print(dst)
    newpath = shutil.copy(fichier,'C:/Users/Marek Oomu/Documents/hello/redipository')
    #print(newpath)
    #os.rename('C:/Users/Marek Oomu/Documents/hello/tubhiswt.ome.tif','C:/Users/Marek Oomu/Documents/hello/'+dst + '.ome' + oldext)
    os.rename(newpath,'C:/Users/Marek Oomu/Documents/hello/redipository/'+dst + '.ome' + oldext)


window.title("Change filename")
location = Label(window, text="Entrez la localisation du fichier").grid(row=1, column=0, sticky=E)
loc_e = Entry(window)
loc_e.grid(row=1, column=1, sticky=W)
nam_e = Entry(window)
nam_e.grid(row=2, column=1, sticky=W)
com_name = Label(window, text="Entrez le nom du marquage").grid(row=2, column=0, sticky=E)

submit = Button(window, command=chnge, text="Appliquer", bg="#637985").grid(columnspan = 2)
quit = Button(window, command = window.quit, text = "Quitter", bg="red").grid(columnspan = 2)

window.mainloop()

