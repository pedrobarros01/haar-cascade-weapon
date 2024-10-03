import os
import cv2
caminho_preprocessamento_negativa = 'src/images/preProcessamento/negativa'
lista_preprocessamento_negativa = os.listdir(caminho_preprocessamento_negativa)
caminho_negativa = 'src/images/n'
caminho_teste = 'src/images/testes'
for i, arquivo in enumerate(lista_preprocessamento_negativa):
    if arquivo.endswith('.jpg') and i < 3997:

        caminho = os.path.join(caminho_preprocessamento_negativa, arquivo)
        img = cv2.imread(caminho)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(caminho, gray)
        os.replace(caminho, os.path.join(caminho_negativa, arquivo))
    
    if arquivo.endswith('.jpg') and i >= 3997:
        caminho = os.path.join(caminho_preprocessamento_negativa, arquivo)
        img = cv2.imread(caminho)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(caminho, gray)
        os.replace(caminho, os.path.join(caminho_teste, arquivo))


