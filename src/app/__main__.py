"""
This is the main entry point of the application.

Import the bare minimum needed and add any initialization code here.
opencv_createsamples -info amostras.lst -num 1200 -w 24 -h 24 -vec positives.vec
opencv_traincascade -data classifier -vec positives.vec -bg bg.txt -numPos 200 -numNeg 400 -numStages 15 -w 50 -h 50
opencv_traincascade -data classifier -vec positives.vec -bg bg.txt -numPos 1200 -numNeg 600 -numStages 10 -w 24 -h 24 -maxFalseAlarmRate 0.2
opencv_traincascade -data classifier -vec positives.vec -bg bg.txt -numPos 1500 -numNeg 1000 -numStages 10 -w 24 -h 24 -maxFalseAlarmRate 0.2
"""
import os
from src.app.HarCascade import cascade_video
from src.app.ETLRetangle import RectangleYOLO
import argparse
def main(mode):
    if mode == 'TREINOT':
        os.remove('amostras.lst')
        os.remove('bg.txt')
        os.remove('positives.vec')
        RectangleYOLO.prepare_train(3100, 1000)
    else:
        cascade_video()
    
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Treinamento e teste do algoritmo de haar cascade para imagens de armas')
    parser.add_argument('--modo', action='store', dest='modo', required=True, help='Modo do projeto\nTREINOT - Preparação do treino do algoritmo com a sua base de imagens\nVIDEO - Upload de video para teste\nTREINOP - Treino parcial do algoritmo com a sua base de imagens')
    
    arg = parser.parse_args()
    SystemExit(main(arg.modo))
