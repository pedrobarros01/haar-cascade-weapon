"""
This is the main entry point of the application.

Import the bare minimum needed and add any initialization code here.
opencv_createsamples -info amostras.lst -num 1200 -w 24 -h 24 -vec positives.vec
opencv_traincascade -data classifier -vec positives.vec -bg bg.txt -numPos 1200 -numNeg 600 -numStages 10 -w 50 -h 50
opencv_traincascade -data classifier -vec positives.vec -bg bg.txt -numPos 400 -numNeg 4488 -numStages 15 -w 24 -h 24 -minHitRate 0.50
"""
import os
from src.app.HarCascade import cascade_video
from src.app.ETLRetangle import extract, transform_negatives_in_txt
def main(mode):
    if mode == 1:
        extract()
    elif mode == 2:
        transform_negatives_in_txt()
    else:
        cascade_video()
    return 0


if __name__ == "__main__":
    SystemExit(main(3))
