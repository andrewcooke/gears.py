
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from math import log


IN2MM = 25.4


def mkratios(chainrings, cassette, wheel, crank):
    allratios = []
    for chainring in chainrings:
        ratios = []
        for sprocket in cassette:
            ratio = wheel * chainring / (sprocket * crank)
            ratios.append(ratio)
            allratios.append(ratios)
            print(chainring, sprocket, log(ratio))
    return allratios


class Bike:

    def __init__(self, name, colour, chainrings, cassette, wheel, crank=175):
        print(name)
        self.name = name
        self.colour = colour
        self.chainrings = chainrings
        self.cassette = cassette
        self.wheel = wheel * IN2MM
        self.crank = crank
        self.ratios = mkratios(chainrings, cassette, wheel, crank)


def setyscale(bikes):
    ys = [log(y) for bike in bikes for ratio in bike.ratios for y in ratio]
    yl, yh = min(ys), max(ys)
    dy = yh - yl
    plt.ylim(yl - 0.1 * dy, yh + 0.1 * dy)

def setlabels(bikes):
    plt.legend(handles=[mp.Patch(color=bike.colour, label=bike.name) 
                        for bike in bikes],
               loc=4)

def plot(*bikes):
    setyscale(bikes)
    setlabels(bikes)
    plt.ylabel("log of effective gear")
    plt.xlabel("rear index")
    nx = max([len(bike.cassette) for bike in bikes])
    for bike in bikes:
        n = len(bike.cassette)
        x = [n-i for i in range(n)]
        for ratio in bike.ratios:
            plt.plot(x, [log(y) for y in ratio], color=bike.colour, marker='o')
    plt.show()
#    plt.savefig("example.png")
    


# deore xt m8000

CRINGXT30 = [30]
CRINGXT32 = [32]
CRINGXT34 = [34]

CRINGXT2434 = [24,34]
CRINGXT2636 = [26,36]
CRINGXT2838 = [28,38]

CRINGXT223040 = [22,30,40]

CSTXT1140 = [11,13,15,17,19,21,24,27,31,35,40]
CSTXT1142 = [11,13,15,17,19,21,24,28,32,37,42]
CSTXT1146 = [11,13,15,17,19,21,24,28,32,37,46]  # 1x11 only

# random 3x9 on my bike

CRACERA = [22,32,42]
CSALIVIO1134 = [11,13,15,17,20,23,26,30,34]


# define different possible bikes

MYBIKE = Bike("26\" Current", "black", CRACERA, CSALIVIO1134, 26)
TEST3X11 = Bike("27.5\" 3x11 11-42", "red", CRINGXT223040, CSTXT1142, 27.5, 170)
TEST2X11L = Bike("27.5\" 2x11 24-34 11-42", "green", CRINGXT2434, CSTXT1142, 27.5, 170)
TEST2X11M = Bike("27.5\" 2x11 26-36 11-42", "green", CRINGXT2636, CSTXT1142, 27.5, 170)
TEST2X11H = Bike("27.5\" 2x11 28-38 11-42", "green", CRINGXT2838, CSTXT1142, 27.5, 170)

MOD2X11L =  Bike("27.5\" 2x11 24-36 11-42", "red", [24,36], CSTXT1142, 27.5, 170)

# plot the bikes

plot(MOD2X11L, TEST2X11L)
