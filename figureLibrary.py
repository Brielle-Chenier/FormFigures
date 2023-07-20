import formFigure
class figureLibrary():
    
    youCollect = []
    yours = formFigure()
    allLibrary = []

    #Create all Form Figures Here
    frog = formFigure('Dart','Brielle','\FormFigures\flaskApp\figureImages\dartDaFrog.png')
    frog.nickName('Puddles')
    frog.setAmountPrinted(10)
    allLibrary.append(frog)
   

    def youOwn(UserName):
        for obj in allLibrary:
            if obj.owner == UserName:
                yours = obj


    def youCollect(name):
        for obj in allLibrary:
            if obj.name == name:
                youCollect.append(obj)

