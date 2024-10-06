
import cv2
from ultralytics import YOLO
from src.utils.utils import comando_create_samples, comando_train_cascade
import os


class RectangleYOLO:

    def __init__(self) -> None:
        pass
    @classmethod
    def __detect_objects_and_create_txt(cls ,image_path, txt_output_path):
        image_orig = cv2.imread(image_path)

        # Carregar o modelo YOLO (verifique o caminho do arquivo best.pt)
        yolo_model = YOLO('best.pt')

        # Realizar a detecção
        results = yolo_model(image_orig)
        contar = False
        # Preparar conteúdo para o arquivo .txt
        annotations = []

        for i, result in enumerate(results):
            classes = result.names
            cls = result.boxes.cls
            conf = result.boxes.conf
            detections = result.boxes.xyxy

            num_objects = sum(conf >= 0.7)  # Contar apenas as detecções com confiança >= 0.5
            if num_objects > 0:
                contar = True
                annotation_line = f"{image_path} {num_objects}"

                for pos, detection in enumerate(detections):
                    if conf[pos] >= 0.7:
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
        return contar

    @classmethod
    def __transform_negatives_in_txt(cls, quant):
        neg_image_dir = "src/images/negativa"
        with open("bg.txt", 'w') as f:
            total = len(os.listdir(neg_image_dir))
            for i, filename in enumerate(os.listdir(neg_image_dir)):
                if (filename.endswith(".jpg") or filename.endswith(".png")) and (i <= quant - 1 or quant == -1):
                    f.write(os.path.join(neg_image_dir, filename) + '\n')
                    print(f'Carregando: {((i + 1) / total) * 100}%')


    @classmethod
    def __extract(cls, quant):
        positivo_dir = 'src/images/positiva'
        arquivos = os.listdir(positivo_dir)
        total = len(arquivos)
        path_txt = 'amostras.lst'
        total_amostras = 0
        for i, arquivo in enumerate(arquivos):
            if i <= quant - 1 or quant == -1:
                path_image = os.path.join(positivo_dir, arquivo)
                contar = cls.__detect_objects_and_create_txt(path_image, path_txt)
                if contar:
                    total_amostras += 1
                print(f'Carregando: {((i + 1) / total) * 100}%')
        return total_amostras
    
    @classmethod
    def prepare_train(cls, quant_positives, quant_negatives):
        cls.__transform_negatives_in_txt(quant_negatives)
        total_amostras = cls.__extract(quant_positives)
        comando_create_samples(total_amostras)
        
        
    