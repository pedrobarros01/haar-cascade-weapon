import subprocess

def comando_create_samples(quant_positive):

    lista_comando = [
        'opencv_createsamples', 
        '-info', 'amostras.lst', 
        '-num', f'{quant_positive}', 
        '-w', '24', 
        '-h', '24', 
        '-vec', 'positives.vec'
    ]
    
    try:
        # Executa o comando e exibe a saída e erros
        result = subprocess.run(lista_comando, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e.stderr}")



def comando_train_cascade(quant_positive, quant_negative, epocas):
    return f'opencv_traincascade -data classifier -vec positives.vec -bg bg.txt -numPos {quant_positive} -numNeg {quant_negative} -numStages {epocas} -w 24 -h 24 -maxFalseAlarmRate 0.2'