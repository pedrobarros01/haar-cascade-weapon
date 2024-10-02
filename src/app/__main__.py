"""
This is the main entry point of the application.

Import the bare minimum needed and add any initialization code here.
opencv_createsamples -info amostras.lst -num 201 -w 24 -h 24 -vec positives.vec
opencv_traincascade -data classifier -vec positives.vec -bg bg.txt -numPos 201 -numNeg 491 -numStages 10 -w 24 -h 24
"""
import os
from src.app.HarCascade import cascade
from src.app.ExtractRetangle import extract
def main():
    '''    neg_image_dir = "src/images/n"
        with open("bg.txt", 'w') as f:
            for filename in os.listdir(neg_image_dir):
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    f.write(os.path.join(neg_image_dir, filename) + '\n')'''
    #extract()
    cascade()
    return 0


if __name__ == "__main__":
    SystemExit(main())
