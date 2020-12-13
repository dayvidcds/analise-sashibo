import cv2
import numpy as np
import sys
import argparse
from matplotlib import pyplot as plt

def test(location):
    src = cv2.imread(location)
    src = cv2.resize(src, (600, 400))

    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    lower_range = np.array([150, 40, 40])
    upper_range = np.array([189, 255, 255])

    mask = cv2.inRange(hsv, lower_range, upper_range)

    gray = cv2.GaussianBlur(mask, (7, 7), 3)

    t, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)

    contours, a = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(src, contours, -1, (0, 0, 255), 1, cv2.LINE_AA)

    x = 0
    y = 0
    w = 0
    h = 0

    for c in contours:
        area = cv2.contourArea(c)
        if area > 10 and area < 1000000:
            (x, y, w, h) = cv2.boundingRect(c)
            #cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2, cv2.LINE_AA)
            #print(x,y,w,h)
            break

    crop = src[y:y+h, x:x+w]

    color = ('b','g','r')

    plt.figure(figsize=(6, 4))

    plt.suptitle('Extração de informações do ' + location)

    grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)

    plt.subplot(grid[0, 0])
    plt.title('Sashibo')
    plt.imshow(crop)

    plt.subplot(grid[0, 1:])
    plt.title('Histograma referente')

    for i,col in enumerate(color):
        histr = cv2.calcHist([crop], [i], None, [256], [0, 256])
        plt.plot(histr, color = col)
        plt.xlim([0, 256])

    plt.subplot(grid[1, :2])
    plt.title('HSV')

    x = np.arange(3)

    hue = crop[:, :, 0].mean()
    saturation = crop[:, :, 1].mean()
    value = crop[:, :, 2].mean()

    values = [saturation, hue, value]

    plot = plt.bar(x, values)

    for value in plot:
        height = value.get_height()
        plt.text(value.get_x() + value.get_width()/2., 1.002*height,'%d' % int(height), ha='center', va='bottom')

    plt.xticks(x, ('Saturação', 'Matiz', 'Valor'))
    plt.xlabel("hsv separado")
    plt.ylabel("Valor") 

    #cv2.imshow('contornos', src)

    #cv2.imshow('crop', crop)

    #print(hue)
    #print(saturation)

    plt.show(block=False)

    return 0

def main():
    parser = argparse.ArgumentParser(description='Imagens a serem processadas')
    parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)

    for _, value in parser.parse_args()._get_kwargs():
        if value is not None:
            break

    print('Processando imagens...')

    for n in value:
        test(n)

    print('<<< Processado >>>')

    while True:
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()

    return 0

if __name__ == '__main__':
    sys.exit(main())
