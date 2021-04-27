import cv2
import numpy as np

def getLAB(src):

    lab = cv2.cvtColor(src, cv2.COLOR_RGB2LAB)

    lLab = lab[:, :, 0].mean()
    aLab = lab[:, :, 1].mean()
    bLab = lab[:, :, 2].mean()

    return lLab, aLab, bLab

def getHSV(src):

    #alterando espaço de cores para HSV e jogando a nova imagem na variável hsv
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    return hsv

def cropImage(src):

    #detectando a cor do sashibo por range de cor HSV (vermelho mais escuro até o vermelho mais claro)
    #Obs: Foram realizados vários testes com ranges diferentes de vermelho para se chegar nesses valores abaixo

    #definindo os valores HSV mínimo para detecção de cor
    lower_range = np.array([160, 0, 0])
    #definindo os valores HSV máximos para detecção de cor
    upper_range = np.array([180, 255, 255])

    #criando uma máscara na ára onde não for encontrada a cor que estiver no range definido acima
    mask = cv2.inRange(hsv, lower_range, upper_range)

    #imprimindo a máscara
    #cv2.imshow('mask', mask)

    #foi passado um filtro gausiano para suavizar as bordas da área do sashibo para minimizar as perdas
    gray = cv2.GaussianBlur(mask, (7, 7), 3)

    #aqui convertemos a imagem para bits, onde de o valor do pixel for menos que o limite
    # ele se torna 0 e se for maior se torna 1. Isso ajuda no algoritmo de contornos.
    t, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)

    #contornando a área do sashibo
    contours, a = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #pintando contornos na imagem para visualização
    #cv2.drawContours(src, contours, -1, (0, 0, 255), 1, cv2.LINE_AA)

    #variáveis responsáveis por armazenar os valores da posição do sashibo na imagem original
    x = 0
    y = 0
    w = 0
    h = 0

    #Percorrendo todo contorno para extrair as informações da posição do sashibo
    for c in contours:
        area = cv2.contourArea(c)
        if area > 1000 and area < 1000000:
            #criando um retângulo na área encontrada e passando as informações de ponto e área para as variáveis
            (x, y, w, h) = cv2.boundingRect(c)
            #cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2, cv2.LINE_AA)
            #print(x,y,w,h)
            break
        else:
            spl = location.split('/')
            spl = spl[len(spl) - 1]
            print('<<< ERRO AO PROCESSAR IMAGEM >>> ' + spl)

            return -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    #extraindo sashibo
    crop = src[y:y+h, x:x+w]

    #abaixo só trabalhamos com a imagem que foi extraída (que é o sahsibo):

    hsv_crop = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)

    return crop
