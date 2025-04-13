import cv2
import matplotlib.pyplot as plt

#Lecture de l'image grace a la fonction imread de cv2 
images=cv2.imread("picsou.jpg")

"""Transformation de l'image en niveaux de gris
avant d'appliquer l'Algo Canny on a cv2 qui manipule les images 
en BGR Blue Green Red d'ou la fonction BGR2GRAY pour permettre d'avoir l'image en niveaux de gris  
"""
gris=cv2.cvtColor(images,cv2.COLOR_BGR2GRAY)

"""Grace a Canny est un algorithme de détection de bords, qui est implémenté sous forme de méthode dans OpenCV 
nous obtenons des contours faibles au plus forts grace a l'assignation des threshold la valeur maximale des threshold étant 255
ce qui est conseillé threshold 1 est plus petit que threshold2 
"""
contours=cv2.Canny(gris,threshold1=80,threshold2=175) 

#Création d'une figure de largeur 10 pouces et de hauteur 4 pouces 
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.axis('off') # les axes seront pas visibles 
plt.title('Image')
"""cv2 manipule les images BGR pour l'affichage nous aurons besoin de la tranformation en RGB , 
car Matplotlib manipule les images en RGB"""
plt.imshow(cv2.cvtColor(images,cv2.COLOR_BGR2RGB))


plt.subplot(1, 2, 2)
plt.title("Contours détectés")
plt.imshow(contours, cmap="Blues") #La methode cmap a de nombeuses valeurs par  Purples gray j'ai juste pris comme ca
plt.axis('off')

plt.tight_layout()
#Affichage du graphe 
plt.show()

