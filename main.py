import pyautogui as PG
from  PIL import Image, ImageGrab
import time
def Hit(key) :
    PG.keyDown(key)

def action(data) :

    for i in range(370,375) :
        for j in range(560,675) :
            if(data[i, j]<100) :
                Hit('up')
                return


    for i in range(370, 375):
        for j in range(520,560) :
            if (data[i, j] < 100):
                Hit('down')
                return


    # for i in range(300, 350):
    #     for j in range(400,575) :


if __name__ == '__main__':
    print("the program will start in 2 sec")
    time.sleep(2)
    Hit('up')
    while(True) :
        image = ImageGrab.grab().convert('L')
        data = image.load()
        action(data)


    # image = ImageGrab.grab().convert('L')
    # data = image.load()
    #
    # for i in range(330, 360):
    #     for j in range(520,560) :
    #         data[i, j]= 0
    # image.show()

