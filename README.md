# Détection de Contours avec l'Algorithme de Canny 🖼️

## Description  
Ce projet permet de détecter les contours d'une image à l'aide de l'algorithme de **Canny**.  
Un contour, c'est simplement un tracé qui suit les bords des formes ou des éléments dans une image.  
Il existe plusieurs algorithmes de détection de contours comme **Canny**, **Sobel**, et bien d'autres.

L'image utilisée provient du site [Tanguy](https://www.tanguy.fr/inspirations/les-separations-de-pieces-la-solution-pour-structurer-vos-espaces).

## Fonctionnalités  
- Détection des contours avec l'algorithme de **Canny**
- Interface utilisateur interactive grâce à **Streamlit**
- Upload d'images pour traitement en direct
- Affichage des résultats directement dans l'application web

## Fichier principal  
Le fichier `detection_contours.py` contient l'interface utilisateur développée avec **Streamlit**.  
Vous pourrez uploader vos propres images et visualiser les contours détectés. Lancer avec **streamlit run detection_contours.py**

## Installation des dépendances  
Avant de lancer le projet, assurez-vous d'avoir Python installé sur votre machine.  
Installez ensuite les bibliothèques nécessaires avec les commandes suivantes :  

```bash
pip install opencv-python
pip install streamlit
pip install numpy
