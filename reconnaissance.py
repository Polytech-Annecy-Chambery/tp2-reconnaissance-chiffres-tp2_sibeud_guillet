from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    sim_max=0
    nbr=0
    a=0
    im_bin=image.binarisation(S)
    im_loc=im_bin.localisation()
    for i in liste_modeles:
       a+=1 
       im=im_loc.resize(i.H,i.W) 
       sim=im.similitude(i)
       if sim>sim_max:
           sim_max=sim
           nbr=a 
    return nbr
