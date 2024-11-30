from distutils.command.check import check

import cv2

img = cv2.imread('farol.jpg')
dim = cv2.selectROI('Selecione a area de recorte',img,False)
cv2.destroyWindow('Selecione a area de recorte')
# print(dim)
v1 = int(dim[0])
v2 = int(dim[1])
v3 = int(dim[2])
v4 = int(dim[3])

recorte = img[v2:v2+v4,v1:v1+v3]
caminho = 'recortes/'
nome_arquivo = input('digite o nome do arquivo')


cv2.imwrite(f'{caminho}{nome_arquivo}.jpg',recorte)
print('imagem salva com sucesso')



cv2.waitKey(0)



### cortar uma imagem utilizando o paint do windows

# img = cv2.imread('farol.jpg')
# print(img.shape)
# #eixo y 310-520
# #eixo x 120-420
# recorte = img[310:520,120:420]
# print(recorte.shape)
# cv2.imshow('imagem',img)
# cv2.imshow('Recorte',recorte)
#
# cv2.waitKey(0)




