import cv2
import matplotlib.pyplot as plt 


image =cv2.imread('picsou.jpg')

gris=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.axis('off') # les axes seront pas visibles 
plt.title('Image')
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))


plt.subplot(1,2,2)
plt.axis('off') # les axes seront pas visibles 
plt.title('Image en niveaux de gris ')
plt.imshow(gris, cmap="gray")


plt.tight_layout()
plt.show()
