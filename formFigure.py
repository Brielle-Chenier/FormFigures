from typing import Self
from PIL import Image
class formFigure():
                     
    def __init__(self, name, owner, path):
        self.name = name
        self.owner = owner
        self.path = path
        self.nickname = name

    name = ''
    owner = ''
    nickname = ''
    amountPrinted = 0
    path = ''
    #img = Image.open(path)
    

    def objectPrinted():
        amountPrinted+=1

    def setAmountPrinter(num):
        amountPrinted = num

    def nickName(newNickName):
        nickname = newNickName
    
    

        