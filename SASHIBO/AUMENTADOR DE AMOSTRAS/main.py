import cv2
import sys
import os
import argparse

#função responsável por extrair as informações do sashibo
def test(location):

    #abrindo imagem
    src = cv2.imread(location)

    resized = cv2.resize(src, (600, 400))
    
    print('Processando imagem: ')
    print(location)

    blur = cv2.GaussianBlur(resized, (7, 7), 3)

    spl = location.split('/')
    spl = spl[len(spl) - 1]

    formatDoc = spl.split('.') 

    directory = os.path.dirname(location)

    fileName = formatDoc[0] + ' - GaussianBlur.' + formatDoc[1]

    os.chdir(directory)

    #cv2.imshow('Blur', blur)

    cv2.imwrite(fileName, blur)

    return 0

def listDir(arg):
    files = []
    for a, _, arq in os.walk(arg):
        if len(arq) != 0:
            for file in arq:
                files.append(a + "/" + file)
    return files
    

#função responsável por coletar os argumentos (nome dos aquivos de imagem) passados na chamada do programa 
def main(argv):

    counter = 0

    print('Processando imagens...')

    #print(argv[1])

    files = listDir(argv[1])

    directory = os.getcwd()

    print(files)
    
    for n in files:
        test(n)
        os.chdir(directory)
        ++counter

    print('<<< Processadas ' + str(counter) + ' imagens >>>')

    return 0
   


#chamada da função main
if __name__ == '__main__':
    sys.exit(main(sys.argv))
