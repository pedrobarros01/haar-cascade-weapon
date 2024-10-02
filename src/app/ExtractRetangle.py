
import cv2
from ultralytics import YOLO
import os


def detect_objects_and_create_txt(image_path, txt_output_path):
    image_orig = cv2.imread(image_path)

    # Carregar o modelo YOLO (verifique o caminho do arquivo best.pt)
    yolo_model = YOLO('best.pt')

    # Realizar a detecção
    results = yolo_model(image_orig)

    # Preparar conteúdo para o arquivo .txt
    annotations = []

    for i, result in enumerate(results):
        classes = result.names
        cls = result.boxes.cls
        conf = result.boxes.conf
        detections = result.boxes.xyxy

        num_objects = sum(conf >= 0.5)  # Contar apenas as detecções com confiança >= 0.5
        if num_objects > 0:
            annotation_line = f"{image_path} {num_objects}"

            for pos, detection in enumerate(detections):
                if conf[pos] >= 0.5:
                    xmin, ymin, xmax, ymax = detection
                    width = int(xmax - xmin)
                    height = int(ymax - ymin)
                    # Adicionar as coordenadas do bounding box (x, y, largura, altura)
                    annotation_line += f" {int(xmin)} {int(ymin)} {width} {height}"
                    label = f"{classes[int(cls[pos])]} {conf[pos]:.2f}"
                    color = (0, int(cls[pos])*20, 255)  # Cor baseada na classe detectada
                    cv2.rectangle(image_orig, (int(xmin), int(ymin)), (int(xmax), int(ymax)), color, 2)
                    cv2.putText(image_orig, label, (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)

            # Adicionar linha de anotação à lista
            annotations.append(annotation_line)
            cv2.imwrite(f'src/images/debug/{i}.jpg', image_orig)

    # Salvar as anotações em um arquivo .txt
    with open(txt_output_path, 'a') as file:
        for annotation in annotations:
            file.write(f"{annotation}\n")


def extract():
    positivo_dir = 'src/images/p'


    arquivos = os.listdir(positivo_dir)
    path_txt = 'amostras.lst'
    for arquivo in arquivos:
        path_image = os.path.join(positivo_dir, arquivo)
        detect_objects_and_create_txt(path_image, path_txt)