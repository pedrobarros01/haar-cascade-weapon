import os
caminho_positiva = 'src/images/p'
caminho_teste = 'src/images/testes'
caminho_preprocessamento_positivo = 'src/images/preProcessamento/positiva'
lista_dir_pos_preprocessamento = os.listdir('src/images/preProcessamento/positiva')
for arquivo in lista_dir_pos_preprocessamento:
    if arquivo.endswith('.jpg'):
        caminho = os.path.join(caminho_preprocessamento_positivo, arquivo)
        nome = arquivo.replace(' ', '').replace('(', '_').replace(')', '')
        os.rename(caminho, os.path.join(caminho_preprocessamento_positivo, nome))


lista_dir_pos_preprocessamento = os.listdir('src/images/preProcessamento/positiva')
for i, arquivo in enumerate(lista_dir_pos_preprocessamento):
    if i < 2899:
        caminho = os.path.join(caminho_preprocessamento_positivo, arquivo)
        os.replace(caminho, os.path.join(caminho_positiva, arquivo))
    else:
        caminho = os.path.join(caminho_preprocessamento_positivo, arquivo)
        os.replace(caminho, os.path.join(caminho_teste, arquivo))