# Andy Kotz final project: graphing calculator with regressions

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, TextAsset
from ggame import CircleAsset, ImageAsset
from math import sin, cos, radians

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000

def correlation(xlistpts,ylistpts):
    N = len(xlistpts)
    corgofor = 0
    Exylist = []
    while corgofor <= len(xlistpts)-1:
        jum = xlistpts[corgofor]*ylistpts[corgofor]
        Exylist.append(jum)
        corgofor += 1
    Exy = sum(Exylist)
    Ex = sum(xlistpts)
    Ey = sum(ylistpts)
    Ex2list = []
    Ey2list = []
    for j in xlistpts:
        jummy = j**2
        Ex2list.append(jummy)
    for i in ylistpts:
        jumby = i**2
        Ey2list.append(jumby)
    Ex2 = sum(Ex2list)
    Ey2 = sum(Ey2list)
    numerator = (N*Exy)-(Ex*Ey)
    denominator = (((N*Ex2)-(Ex)**2)*((N*Ey2)-(Ey)**2))**0.5
    r = numerator/denominator
    return (r)
def quadreg(xlistpts,ylistpts):
    N = len(xlistpts)
    Ex = sum(xlistpts)
    Ey = sum(ylistpts)
    Ex2list = []
    Ex3list = []
    Ex4list = []
    for j in xlistpts:
        jummy = j**2
        Ex2list.append(jummy)
    Ex2 = sum(Ex2list)
    for j in xlistpts:
        jummy = j**3
        Ex2list.append(jummy)
    Ex3 = sum(Ex3list)
    for j in xlistpts:
        jummy = j**4
        Ex2list.append(jummy)
    Ex4 = sum(Ex4list)
    corgofor = 0
    Exylist = []
    while corgofor <= len(xlistpts)-1:
        jum = xlistpts[corgofor]*ylistpts[corgofor]
        Exylist.append(jum)
        corgofor += 1
    Exy = sum(Exylist)
    Ex2y = Ex2+Ey
    Exx = (Ex2)-(((Ex)**2)/N)
    Exy = (Exy) - ((Ex*Ey)/N)
    Exx2 = (Ex3) - ((Ex2*Ex)/N)
    Ex2y = (Ex2y) - ((Ex2*Ey)/N)
    Ex2x2 = (Ex4) - (((Ex2)**2)/N)
    a = ((Ex2y*Exx)-(Exy*Exx2))/((Exx*Ex2x2)-(Exx2)**2)
    b = ((Exy*Ex2x2)-(Ex2y*Exx2))/((Exx*Ex2x2)-(Exx2)**2)
    c = (Ey/N)-(b*(Ex/N))-(a*(Ex2/N))
    returnlist = [a,b,c]
    return(returnlist)

coords = None
esetreg = TextAsset("Congratulations! you win 1 million dollars!", style = '40pt Arial')
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
circle = CircleAsset(3, thinline, blue)
circlebig = CircleAsset(6, thinline, red)
Sprite (xaxis, (0, 500))
Sprite (yaxis, (950, 0))
smiley = ImageAsset("smileyface.jpg")
yaxisrulingsprites = [Sprite(yaxisrulings, (947.5, y*20)) for y in range(-100, 100, 1)]
xaxisrulingsprites = [Sprite(xaxisrulings, (x*20+10, 497)) for x in range(-150, 150, 1)]

xcoordinates2 = range(-1500, 1500, 1)
xcoordinates = []
for x in xcoordinates2:
    x = x/32
    xcoordinates.append(x)

pointpos = 1
linetypelist = input("choose function, plot (f,p). Separate by commas: ")
linetypelist = linetypelist.split(",")
for linetype in linetypelist:
    if linetype == "f":
        function = input("y=")
        for x in xcoordinates:
            yval = (-20*(eval(function))+500)
            if yval >= 0 and yval <= 1000:
                Sprite (circle, ((20*x+950), yval))
    if linetype == "p":
        again = True
        ylistpts=[]
        xlistpts=[]
        while again == True:
            point = input("input point x,y. press q to quit, qr or lr to regress: ")
            if point == "q" or point == "qr" or point == "lr":
                again = False
            if again == True:
                point = point.split(",")
                xlistpts.append(float(point[0]))
                ylistpts.append(float(point[1]))
            if point == "lr":
                xlistmean = (sum(xlistpts))/len(xlistpts)
                ylistmean = (sum(ylistpts))/len(ylistpts)
                xmeanlist = []
                ymeanlist = []
                for i in xlistpts:
                    x = i-xlistmean
                    x = x**2
                    xmeanlist.append(x)
                for i in ylistpts:
                    y = i-ylistmean
                    y = y**2
                    ymeanlist.append(y)
                sdx = (sum(xmeanlist)/len(xmeanlist))**0.5
                sdy = (sum(ymeanlist)/len(ymeanlist))**0.5
                rval = correlation(xlistpts, ylistpts)
                regreslope = rval*(sdy/sdx)
                regreintercept = ylistmean - (regreslope*xlistmean)
                regreinterceptprint = str(round(10*regreintercept)/10)
                oper = "+"+regreinterceptprint
                if regreintercept < 0:
                    oper = "-"+regreinterceptprint
                if regreintercept == 0:
                    oper = ""
                print ("Regression: y="+str((round(10*regreslope))/10)+"x"+ oper +". r = " + str(round(10000*rval)/10000))
                for x in xcoordinates:
                    yval = (-20*(regreslope*x+regreintercept)+500)
                    if yval >= 0 and yval <= 1000:
                        Sprite (circle, ((20*x+950), yval))
            if point == "qr":
                abc = quadreg(xlistpts,ylistpts)
                quada = abc[0]
                quadb = abc[1]
                quadc = abc[2]
                for x in xcoordinates:
                    yval = (-20*(quada*(x**2)+quadb*x+quadc)+500)
                    if yval >= 0 and yval <= 1000:
                        Sprite (circle, ((20*x+950), yval))
            goforh = 0
            while goforh <= len(xlistpts)-1:
                Sprite(circlebig, (20*float(xlistpts[goforh])+950, -20*float(ylistpts[goforh])+500))
                goforh += 1
            goforlist = 1
            while goforlist <= len(xlistpts)-1:
                pointz = TextAsset("("+str(xlistpts[goforlist-1])+","+str(ylistpts[goforlist-1])+"), ("+str(xlistpts[goforlist])+","+str(ylistpts[goforlist])+")", style = '8pt Arial')
                goforlist+=2
                Sprite (pointz, (10, pointpos*15))
                pointpos+=1
    if linetype in ['a', 'b', 'c', 'd', 'e', 's', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        Sprite (esetreg, (200, 200))
def mousePosition(event):
    global text
    global coords
    if coords != None:
        coords.destroy()
    xcurse.y = event.y-7
    ycurse.x = event.x-9
    text = TextAsset("(" + str(round((event.x-959)/20)) + "," + str(round((-(event.y-507))/20)) + ")", style = '10pt Arial')
    coords = Sprite(text, (event.x-7, event.y-22))
def mouseclick(event):
    Sprite (smiley, (100, 100))
    

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
myapp.listenMouseEvent('mousemove', mousePosition)
myapp.listenMouseEvent('mouseclick', mouseclick)
