# Classificador de Detecção de Armas usando YOLO e Haar Cascade

Este projeto visa criar um classificador personalizado para detectar armas utilizando uma combinação de YOLO e Haar Cascade. O processo envolveu vários desafios e melhorias que levaram à construção de um modelo mais adaptado e funcional para a tarefa de detecção de objetos. Além disso, esse projeto apresenta um frontend para facilitar o uso do classifcador treinado e preparar os treinos que foram executados. Essa preparação permite ser utilizada para qualquer datasset não somente sobre armas.

## Abordagem Inicial

O projeto começou seguindo um tutorial do professor Ariel para criar um classificador personalizado, mas surgiram erros durante a identificação dos objetos, o que impediu o progresso inicial.

Após pesquisas adicionais, encontramos um modelo que gerava o classificador com base em um dataset disponível na internet. Com esse modelo, conseguimos criar a primeira versão do classificador usando o dataset fornecido. Embora o código rodasse sem erros, as imagens resultantes não exibiam corretamente as caixas delimitadoras ao redor das armas.

### Ajustes

- Mudamos o dataset original, pois as imagens não estavam sendo processadas como esperado.
- Decidimos usar o **YOLO** para automatizar a geração das caixas delimitadoras ao redor das amostras de treino, uma vez que adicionar essas caixas manualmente seria inviável.
- Criamos um frontend para facilitar os testes dos classificadores treinados, através de upload de vídeo, e também facilitar os primeiros passos do treino do algoritmo, criação das amostras positivas e negativas.

## Transição para YOLO

Optamos por utilizar o modelo de **YOLO** do JoaoAssalim para gerar automaticamente as caixas delimitadoras no dataset de treino, eliminando a necessidade de adicionar as caixas manualmente.

Com o dataset pronto, instalamos o **OpenCV 3.4** localmente para acessar o executável necessário para treinar o classificador **Haar Cascade**.

## Frontend
`Tela Inicial`

![TelaInicial](https://github.com/user-attachments/assets/9c623b8b-85bb-43c4-83c4-96eb74a47c60)

`Tela Descrição`

![TelaDescrição](https://github.com/user-attachments/assets/c754b42d-dc6f-4e27-9758-42dfd7cbabaa)

`Tela Preparação`

![TelaPreparação](https://github.com/user-attachments/assets/ab0f529c-62fe-4914-bf97-b1fb103fd1e3)

`Tela Upload`

![TelaUpload](https://github.com/user-attachments/assets/04972d7f-7f72-4477-88f6-16df4e3e2f8d)



## Resultados Finais

Com o novo dataset, os resultados esperados foram alcançados, com as caixas delimitadoras aparecendo corretamente ao redor dos objetos. No entanto, as caixas inicialmente eram imprecisas. Após testes com diferentes parâmetros do classificador, conseguimos otimizar a precisão das detecções. Entretanto, a depender das imagens é observado algumas imprecisões na detecção de objetos, pelo fato de que as imagens  negativas e positivas dos datassets não exploraram ao máximo caracteristícas fundamentais das imagens de armas.

### Parâmetro de treino
1. Treino
   - 200 imagens positivas e 100 imagens negativas
   - Padrão dos hiperparâmetros
   - 15 épocas
2. Treino
   - 1200 imagens positivas e 600 imagens negativas
   - maxFalseAlarmRate setado para 0.2
   - 10 épocas
3. Treino
   - 2000 imagens positivas e 1000 imagens negativas
   - mesmos parâmetros do 2° treino

Segue os vídeos mostrando os resultados das detecções.

### Vídeo 1

- 200 imagens

[video_200.webm](https://github.com/user-attachments/assets/400bd8ea-8b50-4833-887a-51f41c925d20)

- 1200 imagens

[video_1200.webm](https://github.com/user-attachments/assets/634f1d61-2d05-4297-bd70-f5e51dbd1bba)

- 2000 imagens

[video_2000.webm](https://github.com/user-attachments/assets/ac07d1ca-1f77-4b2c-8671-ae830c14ff03)

### Vídeo 2


- 200 imagens

[video2_200.webm](https://github.com/user-attachments/assets/b3d24bb6-c2c7-4bcb-b480-e034baf1b341)

- 1200 imagens

[video2_1200.webm](https://github.com/user-attachments/assets/91673f72-0bab-4c6b-b64a-44d1b6e69d00)

- 2000 imagens

[video2_2000.webm](https://github.com/user-attachments/assets/322b0824-6d4d-4ead-9bde-713507454a1a)

Video 1 retirado do usuário 

## Estrutura do Código

### Scripts

- **ETLRectangle.py**: Automatiza a extração de caixas delimitadoras utilizando YOLO e prepara os dados para o treinamento do Haar Cascade.
  
- **HarCascade.py**: Aplica o classificador Haar Cascade treinado para detectar objetos em vídeos.

- **transform_image_negative.py** e **transform_image_positive.py**: Processam e movem imagens (consideradas negativas ou positivas, respectivamente) de um diretório de pré-processamento para um diretório final, convertendo-as para a escala de cinza.

- **utils.py**: Contém funções que utilizam comandos do OpenCV via biblioteca `subprocess`, facilitando a execução no script ETLRectangle.

- **FrontEnd.py**: Contém toda a lógica do tkinter para montar o frontend utilizado


## Execução
### Requisito
1. Instale e compile o opencv-3.4, acesse a documentação deles para mais detalhes

### Preparação
1. Caso voce tenha algum datasset de imagens positivas e negativas, coloque nas pastas images/positiva e images/negativa, respectivamente. Se não, deszipe o .zip
2. Coloque no terminal `poetry shell`
3. Coloque no terminal `make install` ou `poetry install`
4. Execute no terminal o `make run` ou `poetry run python -m src.app`
5. Acesse o frontend e aperte o botão de preparação
6. Digite os parâmetros de quantidade de positivas, negativas e épocas que você deseja treinar
7. Aperte o botão de iniciar e espere o terminal retornar o comando de `opencv_traincascade`
8. Execute esse comando no terminal e espere o classificador está treinado

### Upload
1. Caso voce tenha algum datasset de imagens positivas e negativas, coloque nas pastas images/positiva e images/negativa, respectivamente. Se não, deszipe o .zip
2. Coloque no terminal `poetry shell`
3. Coloque no terminal `make install` ou `poetry install`
4. Execute no terminal o `make run` ou `poetry run python -m src.app`
5. Acesse o frontend e aperte o botão de upload
6. Escolha o classificador que você deseja testar
7. Aperte o botão de upload para carregar um vídeo da sua escolha(mp4)
8. Aperte em iniciar e verifique o teste das detecções dos objetos

## Observações
Esse projeto foi desenvolvido em no sistema operacional Ubuntu 22.04.5 LTS, caso esteja utilizando em Windows pode ser necessário alterar manualmente os caminhos das pastas.


## Referências
- https://github.com/JoaoAssalim/Weapons-and-Knives-Detector-with-YOLOv8/blob/main/detecting-images.py (modelo do YOLO)
- https://github.com/Saksham00799/opencv-gun-detection (base de imagens positivas e negativas)
- https://www.kaggle.com/datasets/abhishek4273/gun-detection-dataset (base de imagens positivas)
- https://www.kaggle.com/datasets/ankan1998/weapon-detection-dataset (base de imagens positivas)
- https://github.com/Saksham00799/opencv-gun-detection/blob/master/Gun-Haar-Cascade.py (video 1)
- https://www.kaggle.com/datasets/tongpython/cat-and-dog (base de imagens negativas)
