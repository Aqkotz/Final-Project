# Andy Kotz final project: graphing calculator with regressions

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, TextAsset
from ggame import CircleAsset
from math import sin, cos, radians

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000

def isnumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
purple = Color(0x9B30FF, 1.0)
grey = Color(0xd3d3d3, 0.7)
thinline = LineStyle(0, black)
yaxis = RectangleAsset(1, 1000, thinline, black)
xaxis = RectangleAsset(1900, 1, thinline, black)
ycursor =  RectangleAsset(1, 1000, thinline, grey)
xcursor = RectangleAsset(1900, 1, thinline, grey)
class Xcursorclass(Sprite):
    def __init__(self, position):
        super().__init__(xcursor, position)
class Ycursorclass(Sprite):
    def __init__(self, position):
        super().__init__(ycursor, position)
xcurse = Xcursorclass((0,0))
ycurse = Ycursorclass((0,0))
xaxisrulings = RectangleAsset(1, 7, thinline, black)
yaxisrulings = RectangleAsset(7, 1, thinline, black)
thinline = LineStyle(0, black)
mycircle = CircleAsset(3, thinline, blue)
mycirclebig = CircleAsset(6, thinline, blue)
Sprite (xaxis, (0, 500))
Sprite (yaxis, (950, 0))
yaxisrulingsprites = [Sprite(yaxisrulings, (947.5, y*20)) for y in range(-100, 100, 1)]
xaxisrulingsprites = [Sprite(xaxisrulings, (x*20+10, 497)) for x in range(-150, 150, 1)]

xcoordinates2 = range(-1500, 1500, 1)
xcoordinates = []
for x in xcoordinates2:
    x = x/32
    xcoordinates.append(x)

linetypelist = input("linear, quadratic, cubic, plot, function (l, q, c, p, f). Separate by commas: ")
linetypelist = linetypelist.split(",")
for linetype in linetypelist:
    if linetype == "l":
        m = float(input("linear m: "))
        b = float(input("linear b: "))
    if linetype == "q":
        a = float(input("quadratic a: "))
        b = float(input("quadratic b: "))
        c = float(input("quadratic c: "))
    if linetype == "c":
        a = float(input("cubic a: "))
        b = float(input("cubic b: "))
        c = float(input("cubic c: "))
        d = float(input("cubic d: "))
    if linetype == "f":
        function = list(input("y="))
        goforfunction = 0
        while goforfunction <= len(function)-2:
            number1 = function[goforfunction]
            number2 = function[goforfunction+1]
            if isnumber(number1):
                if isnumber(number2):
                    newnumber1 = int(number1)*10+int(number2)
                    function[goforfunction] = newnumber1
                    function.remove(number2)
            elif not isnumber(number1):
                goforfunction += 1
        print (function)
    if linetype == "p":
        again = True
        ylistpts=[]
        xlistpts=[]
        while again == True:
            point = input("input point x,y. press q to quit, r to regress: ")
            if point == "q" or point == "r":
                again = False
            if again == True:
                point = point.split(",")
                Sprite(mycirclebig, (20*float(point[0])+950, -20*float(point[1])+500))
                xlistpts.append(float(point[0]))
                ylistpts.append(float(point[1]))
    if linetype == "l":
        for x in xcoordinates:
            yval = 20*((-m)*x-b)+500
            if yval >= 0:
                sprites = Sprite(mycircle, (20*x+950, yval))
    if linetype == "q":
        for x in xcoordinates:
            yval = 20*(-a*x**2-b*x-c)+500
            if yval >= 0:
                sprites = Sprite(mycircle, (20*x+950, yval))
    if linetype == "c":
        for x in xcoordinates:
            yval = 20*(-a*x**3-b*x**2-c*x-d)+500
            if yval >= 0:
                sprites = Sprite(mycircle, (20*x+950, yval))
coords = None
def mousePosition(event):
    global text
    global coords
    if coords != None:
        coords.destroy()
    xcurse.y = event.y-7
    ycurse.x = event.x-9
    text = TextAsset("(" + str(round((event.x-959)/20)) + "," + str(round((-(event.y-507))/20)) + ")", style = '10pt Arial')
    coords = Sprite(text, (event.x-7, event.y-22))
    

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
myapp.listenMouseEvent('mousemove', mousePosition)
