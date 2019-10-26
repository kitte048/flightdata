### Make all altitude comparison plots by D. Kittell
### Started on July 6, 2019
###
### NOTES:
###   This new version of the code is made to compare
###  some of Wildman's 4-inch kits: my Extreme DarkStar
###  and Intimidator 4 "Magmar", versus Extreme Wildman
###  flights that I found on the internet.
###
# Preamble
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as mpe
import matplotlib.font_manager as font_manager
import matplotlib.ticker as ticker
from collections import namedtuple
import gc
import scipy.stats as sp

###########################################################################
# Functions to return the flight data.
###########################################################################

#------------------------------------------
# Color Notes (add as needed)
#------------------------------------------
# CTI Motors are 10-pt circles ("o")
#     - Classic is "silver"
#     - Red Lightning is "red"
#     - Green is "green"
#     - White is "white"
#     - White Thunder is "lightcyan"
#     - Skidmark is "saddlebrown"
#     - Imax is "darkorange"
#     - C-Star is "yellow"
#     - C-Star (FAST) is also "yellow"
#     - Blue Streak is "blue"
#     - Metalstorm is "gray"
#------------------------------------------
# LOKI Motors are 12-pt triangles ("v")
#     - Spitfire is "chocolate"
#     - White is "floralwhite"
#     - Red is "red"
#     - Cocktail is "mediumpurple"
#     - Blue is "aqua"
#------------------------------------------
# AT RMS Motors are 10-pt squares ("s")
#     - Mojave Green is "lime"
#     - White Lightning is "ivory"
#     - Redline is "orangered"
#     - Blue Thunder is "mediumblue"
#     - Fast Blackjack is "black"
#     - Propellant X is "olive"
#------------------------------------------

###########################################################################
# Extreme DarkStar by WildMan, Maiden Flight May 13, 2017.
###########################################################################

def FlightLog_ExtremeDS():

    # Title
    ttl = r"Extreme DarkStar (L3)"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt (Known Flights Only)
    data = [['May',  '1', '2011', 'L1410',  'CTI', 4828.3, 1410, 10608],\
            ['Oct', '29', '2011', 'M2020',  'CTI', 8429.4, 2020, 17834],\
            ['Mar', '31', '2012', 'M3700',  'CTI', 6800.0, 3600, 15000],\
            ['n/a','/na',  'n/a', 'K1200',  'CTI', 2014.0, 1200,  5243],\
            ['Oct', '31', '2015', 'M2250',  'CTI', 5472.2, 2250, 12458]]

    # Marker size/type/color
    symb = [[10, "o", "saddlebrown"  ],\
            [10, "o", "darkorange"   ],\
            [10, "o", "lightcyan"    ],\
            [10, "o", "lightcyan"    ],\
            [10, "o", "yellow"       ]]

    return [ttl,data,symb]

###########################################################################
#  MD Intimidator 4, Maiden Flight November 1, 2014.
###########################################################################
# NOTES
# - minimum diameter, modified kit
# - unpainted (No.1) and bright orange "If Found..." sticker (No.2)

def FlightLog_MDIntim4():

    # Title
    ttl = r"MinD Intimidator 4"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt
    data = [['Nov',  '1', '2014', 'M3400',  'CTI', 9994.5, 3400, 19035],\
            ['Oct', '31', '2015', 'M1419',   'AT', 7755.5, 1419, 17449]]

    # Marker size/type/color
    symb = [[10, "o", "lightcyan"    ],\
            [10, "s", "ivory"        ]]

    return [ttl,data,symb]

###########################################################################
#  Intimidator 4 by WildMan, Maiden Flight March 10, 2018.
###########################################################################
# NOTES
# - "StarChaser" (No.1) with repaint to "Magmar" (No.2)

def FlightLog_Intmd4WM():

    # Title
    ttl = r"Intimidator 4 by WildMan"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt
    data = [['Mar', '10', '2018', 'M1101',  'CTI', 5197.6, 1101, 14698],\
            ['Aug', '31', '2019',  ' ', 'Rocksim', 8429.4, 2020, 19325]]

    # Marker size/type/color
    symb = [[10, "o", "white"        ],\
            [10, "o", "darkorange"   ]]

    return [ttl,data,symb]

###########################################################################
#  Wildman Extreme, composite altitude data from the internet.
###########################################################################
# NOTES
# -  4 flights from www.insanerocketry.com (Jason or Tim Cook)
# - 13 flights from www.rocketreviews.com (Mike Caplinger)
# -  1 flight from www.rocketreviews.com (Nick Larsen)
# -  1 flight from TRF (Larry ?)
#
def FlightLog_WMExtremes():

    # Title
    ttl = r"Extreme Wildman"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt

            # Jason or Tim (?) Cook
    data = [['Oct', '27', '2018',  'L930', 'LOKI', 3587.2,  930, 10337],\
            ['Nov', '25', '2017', 'M1200', 'LOKI', 5122.6, 1200, 12811],\
            ['Feb',  '4', '2017', 'L1170',   'AT', 4232.0, 1170, 10797],\
            ['Dec', '11', '2016', 'L1040', 'LOKI', 3707.0, 1040,  9148],\
            # Mike Caplinger
            ['Mar',  '2', '2018',  'L990',  'CTI', 2771.0,  990,  7983],\
            ['Dec',  '2', '2017',  'K540',   'AT', 1596.3,  540,  3948],\
            ['Jun', '10', '2016', 'M2250',  'CTI', 5472.2, 2250, 14038],\
            ['Jan',  '2', '2016',  'K550',   'AT', 1539.1,  550,  3808],\
            ['Dec',  '6', '2014',  'K550',   'AT', 1539.1,  550,  3300],\
            ['Jun', '14', '2014', 'K1103',   'AT', 1789.0, 1103,  4242],\
            ['Nov',  '2', '2013',  'L851',  'CTI', 3683.2,  851, 10774],\
            ['Apr',  '6', '2013',  'L910',  'CTI', 2856.1,  910,  8100],\
            ['Nov',  '3', '2012',  'K815',  'CTI', 2303.7,  815,  6142],\
            ['Nov',  '6', '2011',  'M650',   'AT', 5964.0,  650, 15158],\
            ['May',  '7', '2011',  'K940',  'CTI', 1632.7,  940,  4102],\
            ['Mar',  '5', '2011', 'M1297',   'AT', 5416.6, 1297, 12751],\
            ['Feb',  '5', '2011', 'K1085',  'CTI', 2412.0, 1085,  7168],\
            # Nick Larsen
            ['Jul', '24', '2012',  'K550',   'AT', 1539.1,  550,  3548],\
            # Larry (hognutz63 on TRF)
            ['n/a','n/a',  'n/a', 'M3000', 'LOKI', 8838.0, 3000, 19532]]

    # Marker size/type/color
    symb = [[12, "v", "floralwhite"  ],\
            [12, "v", "chocolate"    ],\
            [10, "s", "black"        ],\
            [12, "v", "red"          ],\
            [10, "o", "blue"         ],\
            [10, "s", "gray"         ],\
            [10, "o", "yellow"       ],\
            [10, "s", "ivory"        ],\
            [10, "s", "ivory"        ],\
            [10, "s", "olive"        ],\
            [10, "o", "white"        ],\
            [10, "o", "yellow"       ],\
            [10, "o", "saddlebrown"  ],\
            [10, "s", "ivory"        ],\
            [10, "o", "lightcyan"    ],\
            [10, "s", "ivory"        ],\
            [10, "o", "lightcyan"    ],\
            [10, "s", "ivory"        ],\
            [12, "v", "floralwhite"  ]]

    return [ttl,data,symb]

###########################################################################
# Altitude Plot (J-N Range, up to 12000 Ns)
###########################################################################
def AltPlot_JN(fout,title,data,symb,L3His,lb,ub,misc):

    # set titles
    xtxt = r"Total Impulse (N-s)"
    ytxt = r"Max Altitude AGL (ft)"

    # axes limits
    xmin = 0
    xmax = 12000
    ymin = 0
    ymax = 24000

    # axes tick settings
    nx = 7
    ny = 7
    dx = (xmax-xmin)/(nx-1.0)
    dy = (ymax-ymin)/(ny-1.0)
    mx = 4
    my = 4
    xticks = [r"0",r"2000",r" ",r"6000",r" ",r"10000",r" "]
    yticks = [r"0",r"4,000",r"8,000",r"12,000",r"16,000",\
        r"20,000",r"24,000"]

    # figure settings
    figsize = (3,2.75)
    dpi = 3000

    # text settings
    family = 'sans-serif'

    # Open a new figure
    fig = plt.figure(figsize=figsize,dpi=dpi)
    f,ax = plt.subplots(1)
    
    # Font
    for label in (ax.get_xticklabels()+ax.get_yticklabels()):
        label.set_fontname(family)
        label.set_fontsize(26)

    # border position
    f.subplots_adjust(left=0.2,right=0.9,bottom=0.22,top=0.85)

    # border visibiliy
    ax.title.set_position([.5,1.07])
    ax.set_axisbelow(True)
    ax.grid(b=True,which='major',color='chartreuse',\
        linestyle='-',linewidth=1.0)
    ax.grid(b=True,which='minor',color='lightseagreen',\
        linestyle='-',linewidth=0.25)
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    ax.grid(True)

    # Axis padding
    ax.get_xaxis().tick_bottom()
    ax.xaxis.labelpad = 17
    ax.get_yaxis().tick_left()
    ax.yaxis.labelpad = 17

    # border line width
    ax.spines['top'].set_linewidth(4.0)
    ax.spines['right'].set_linewidth(4.0)
    ax.spines['bottom'].set_linewidth(4.0)
    ax.spines['left'].set_linewidth(4.0)

    # axes tick settings
    ax.get_yaxis().set_tick_params(which='both',direction='in',pad=10,\
        right='on',width=4.0)
    ax.get_xaxis().set_tick_params(which='both',direction='in',pad=10,\
        top='on',width=4.0)
    ax.get_yaxis().set_tick_params(which='major',length=13.0,width=4.0)
    ax.get_xaxis().set_tick_params(which='major',length=13.0,width=4.0)
    ax.get_yaxis().set_tick_params(which='minor',length=7.0,width=4.0)
    ax.get_xaxis().set_tick_params(which='minor',length=7.0,width=4.0)
    ax.axis([xmin,xmax,ymin,ymax])
    ax.xaxis.set_ticks(np.linspace(xmin,xmax,nx))
    ax.yaxis.set_ticks(np.linspace(ymin,ymax,ny))
    minorLocatorX = ticker.MultipleLocator(dx/mx)
    minorLocatorY = ticker.MultipleLocator(dy/my)
    ax.xaxis.set_minor_locator(minorLocatorX)
    ax.yaxis.set_minor_locator(minorLocatorY)

    # resize all ticks
    ticklines = ax.get_xticklines()+ax.get_yticklines()
    ticklabels = ax.get_xticklabels()+ax.get_yticklabels()
    for line in ticklines:
        line.set_linewidth(4.0)
    for label in ticklabels:
        label.set_fontsize(26)

    # set the text
    ax.set_title(title,fontsize=26,weight='bold')
    ax.set_ylabel(ytxt,fontsize=26,weight='bold')
    ax.set_xlabel(xtxt,fontsize=26,weight='bold')
    ax.set_xticklabels(xticks,fontsize=22,weight='bold')
    ax.set_yticklabels(yticks,fontsize=22,weight='bold')

    ##########################
    ### ADD YOUR DATA HERE ###
    ##########################

    # Make shaded regions for the different letters.

    # J-Range
    itot=np.linspace(640.01,1280.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='mediumblue',label='_nolegend_')
    plt.text(0.5*(640.01+1100.0),21000,r'J',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # K-Range
    itot=np.linspace(1280.01,2560.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='turquoise',label='_nolegend_')
    plt.text(0.5*(1280.01+2200.0),21000,r'K',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # L-Range
    itot=np.linspace(2560.01,5120.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='chartreuse',label='_nolegend_')
    plt.text(0.5*(2560.01+5000),21000,r'L',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # M-Range
    itot=np.linspace(5120.01,10240.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='gold',label='_nolegend_')
    plt.text(0.5*(5120.01+9440),21000,r'M',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # N-Range
    itot=np.linspace(10240.01,12000.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='orangered',label='_nolegend_')
    plt.text(0.5*(10240.01+11500),21000,r'N',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # Flight Data
    nf=0
    for flight in data:
        nf=nf+1
    print "There are ",nf," flights in the databse."

    xdat=np.zeros(nf)
    ydat=np.zeros(nf)
    i=0
    for flight in data:
        xdat[i]=flight[5]
        ydat[i]=flight[7]
        i+=1

    print 'xdat = ',xdat
    print 'ydat = ',ydat

    # Curve Fit
    # slope, intercept, r_value, p_value, std_err
    [m,b,r,p,std]=sp.stats.linregress(xdat,ydat)
    print 'slope ',m
    print 'intercept ',b
    print 'r squared ',r
    xfit=np.linspace(lb,ub)
    yfit=np.multiply(xfit,m)+b

    str1=r'Y=%1.2f*X+%4.0f'%(m,b)
    str2=r'r$^2$=%1.4f'%(r)
    plt.text(5500,3500,str1,fontsize=18,family=family,\
        color='orangered',fontweight='bold')
    plt.text(5500,5500,str2,fontsize=18,family=family,\
        color='orangered',fontweight='bold')

    outline=mpe.withStroke(linewidth=10.0,foreground='black')
    plt.plot(xfit,yfit,'k-',color='orangered',linewidth=3.4,\
        label=r'_nolegend_',\
        path_effects=[outline])

    #===========================================#
    # Historical L3 Flight Data (Optional)
    if L3His:
        [ttl2,data2,symb2] = FlightLog_ExtremeDS()
        nf2=0
        for flight in data2:
          nf2+=1
        print "There are ",nf2," flights in the databse."
        xdat2=np.zeros(nf2)
        ydat2=np.zeros(nf2)
        i=0
        for flight in data2:
            xdat2[i]=flight[5]
            ydat2[i]=flight[7]
            i+=1

        # Curve Fit
        # slope, intercept, r_value, p_value, std_err
        [m,b,r,p,std]=sp.stats.linregress(xdat2,ydat2)
        print 'slope ',m
        print 'intercept ',b
        print 'r squared ',r
        xfit2=np.linspace(1600,9000)
        yfit2=np.multiply(xfit2,m)+b
        plt.plot(xfit2,yfit2,'k-',color='plum',linewidth=3.4,\
            label=r'_nolegend_',\
            path_effects=[outline])
        plt.plot(xfit,yfit,'k-',color='orangered',linewidth=3.4,\
            label=r'_nolegend_',\
            path_effects=[outline])

        # Scatter Plot (different symbols)
        i=0
        for flight in data2:
            j=0
            for marker in symb2:
                if (i==j):
                    ms = marker[0]
                    mt = marker[1]
                    mc = marker[2]
                j+=1
            mfg = flight[4]
            motor = flight[3]
            str1=r'%s %s'%(mfg,motor)
            print str1
            plt.plot(xdat2[i],ydat2[i],'ko',markersize=ms,\
                markeredgewidth=2.5,markeredgecolor='darkmagenta',\
                markerfacecolor=mc,label=str1,marker=mt)
            i+=1

        # Extra Labels
        plt.text(6500,11500,r"Extreme DarkStar",fontsize=16,family=family,\
            color='darkmagenta',fontweight='bold')
        plt.text(6500,9500,r"(Reference, My L3)",fontsize=16,family=family,\
            color='darkmagenta',fontweight='bold')
        plt.text(1700,17000,r"Extreme",fontsize=18,family=family,\
            color='orangered',fontweight='bold')
        plt.text(1700,15000,r"Wildman(s)",fontsize=18,family=family,\
            color='orangered',fontweight='bold')
        plt.text(1700,13000,r"4x Fliers",fontsize=18,family=family,\
            color='orangered',fontweight='bold')

    #===========================================#
    # Other Minimum Diameter Flight Data (Optional)
    if misc:
        [ttl3,data3,symb3] = FlightLog_MDIntim4()
        nf3=0
        for flight in data3:
          nf3+=1
        print "There are ",nf3," flights in the databse."
        xdat3=np.zeros(nf3)
        ydat3=np.zeros(nf3)
        i=0
        for flight in data3:
            xdat3[i]=flight[5]
            ydat3[i]=flight[7]
            i+=1

        # Scatter Plot (different symbols)
        i=0
        for flight in data3:
            j=0
            for marker in symb3:
                if (i==j):
                    ms = marker[0]
                    mt = marker[1]
                    mc = marker[2]
                j+=1
            mfg = flight[4]
            motor = flight[3]
            str1=r'%s %s'%(mfg,motor)
            print str1
            plt.plot(xdat3[i],ydat3[i],'ko',markersize=ms,\
                markeredgewidth=2.5,markeredgecolor='darkgreen',\
                markerfacecolor=mc,label=str1,marker=mt)
            i+=1

        # Extra Labels
        plt.text(9000,16500,r"Min Dia.",fontsize=16,family=family,\
            color='darkgreen',fontweight='bold')
        plt.text(9000,14500,r"Version",fontsize=16,family=family,\
            color='darkgreen',fontweight='bold')


    #==========================================#

    # Scatter Plot (different symbols)
    i=0
    for flight in data:
        j=0
        for marker in symb:
            if (i==j):
                ms = marker[0]
                mt = marker[1]
                mc = marker[2]
            j+=1
        mfg = flight[4]
        motor = flight[3]
        str1=r'%s %s'%(mfg,motor)
        print str1
        plt.plot(xdat[i],ydat[i],'ko',markersize=ms,\
            markeredgewidth=2.5,markeredgecolor='k',\
            markerfacecolor=mc,label=str1,marker=mt)
        i+=1


    # legend location code.
    # ========================
    # 'best'..............0
    # 'upper right'.......1
    # 'upper left'........2
    # 'lower left'........3
    # 'lower right'.......4
    # 'right'.............5
    # 'center left'.......6
    # 'center right'......7
    # 'lower center'......8
    # 'upper center'......9
    # 'center'............10
    #
    loc=9

#    legend = ax.legend(loc=loc,ncol=4,\
#        prop=matplotlib.font_manager.FontProperties(\
#            family=family,weight='bold',size=9),\
#        numpoints=1,fancybox=False,borderpad=0.5)
#    legend.get_frame().set_linewidth(3.5)
#    legend.get_frame().set_edgecolor("k")

    # save the image
    plt.tight_layout()
    f.savefig(fout+'.png',format='png')
    plt.clf()

    return []

###########################################################################
###########################################################################
###
### Main Program Starts Here
###
###########################################################################
###########################################################################

fout = 'ExtremeWM_Alt'
[ttl,data,symb] = FlightLog_WMExtremes()
L3His = True
lb = 1000
ub = 8500
misc = False
AltPlot_JN(fout,ttl,data,symb,L3His,lb,ub,misc)


