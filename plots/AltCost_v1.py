### Make all altitude comparison plots by D. Kittell
### Started on July 6, 2019
###
### UPDATES:
### 21-Jul 2019 Added Joker's Wild Ride, Rocksim prediction,
###             and recent launches.
### 28-Sep 2019 Added Gizmo XL DD
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
    ttl = r"Extreme DarkStar (My L3)"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt (Known Flights Only)
    data = [['May',  '1', '2011', 'L1410',  'CTI', 4828.3, 1410, 10608],\
            ['Oct', '29', '2011', 'M2020',  'CTI', 8429.4, 2020, 17834],\
            ['Mar', '31', '2012', 'M3700',  'CTI', 6800.0, 3600, 15000],\
            ['n/a','/na',  'n/a', 'K1200',  'CTI', 2014.0, 1200,  5243],\
            ['Oct', '31', '2015', 'M2250',  'CTI', 5472.2, 2250, 12458],\
            ['Aug', '30', '2019',  'K830', 'LOKI', 2287.0,  830,  4707]]

    # Marker size/type/color
    symb = [[10, "o", "saddlebrown"  ],\
            [10, "o", "darkorange"   ],\
            [10, "o", "lightcyan"    ],\
            [10, "o", "lightcyan"    ],\
            [10, "o", "yellow"       ],\
            [12, "v", "chocolate"    ]]

    return [ttl,data,symb]

###########################################################################
# DarkStar Junior by WildMan, Maiden Flight May 13, 2017.
###########################################################################

def FlightLog_DSJrWM():

    # Title
    ttl = r"DarkStar Junior by WildMan"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt
    data = [['May', '13', '2017',  'I285',  'CTI',  510.1,  285,  4466],\
            ['Aug', '12', '2017',  'J600',  'CTI',  998.6,  600,  8373],\
            ['Sep',  '4', '2017',  'J394',  'CTI',  970.4,  394,  6794],\
            ['Nov', '11', '2017',  'J396', 'LOKI',  650.0,  396,  5347],\
            ['Dec',  '9', '2017', 'J1000', 'LOKI', 1220.0, 1000,  9284],\
            ['Jan', '13', '2018',  'J453',  'CTI', 1012.6,  453,  6708],\
            ['Feb', '10', '2018',  'J650', 'LOKI',  942.0,  650,  7974],\
            ['Mar',  '9', '2019',  'K627', 'LOKI', 1519.0,  627, 10396],\
            ['Jun',  '8', '2019',  'J500',   'AT',  723.0,  500,  6133],\
            ['Jul', '20', '2019',  'J420',   'AT',  658.0,  420,  5577]]

    # Marker size/type/color
    symb = [[10, "o", "silver"       ],\
            [10, "o", "red"          ],\
            [10, "o", "green"        ],\
            [12, "v", "chocolate"    ],\
            [12, "v", "floralwhite"  ],\
            [10, "o", "white"        ],\
            [12, "v", "chocolate"    ],\
            [12, "v", "red"          ],\
            [10, "s", "lime"         ],\
            [10, "s", "orangered"    ]]

    return [ttl,data,symb]

###########################################################################
#  Competitor 3 by WildMan, Maiden Flight November 2, 2013.
###########################################################################

def FlightLog_Comp3WM():

    # Title
    ttl = r"Competitor 3 by WildMan"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt
    data = [['Nov',  '2', '2013',  'K940',  'CTI', 1632.7,  940,  9200],\
            ['Dec', '10', '2016', 'J1026', 'LOKI', 1267.0, 1026,  7170],\
            ['Feb', '11', '2017',  'K185',   'AT', 1417.2,  185,  7817],\
            ['Sep',  '3', '2017',  'K711',  'CTI', 2377.3,  711, 12108],\
            ['Oct', '14', '2017',  'J528', 'LOKI',  741.0,  528,  3556],\
            ['Mar',  '9', '2019',  'K815',  'CTI', 2303.7,  815, 11092],\
            ['Apr', '13', '2019', 'K1127', 'LOKI', 1285.0, 1127,  6515]]

    # Marker size/type/color
    symb = [[10, "o", "lightcyan"    ],\
            [12, "v", "mediumpurple" ],\
            [10, "s", "ivory"        ],\
            [10, "o", "white"        ],\
            [12, "v", "floralwhite"  ],\
            [10, "o", "saddlebrown"  ],\
            [12, "v", "aqua"         ]]

    return [ttl,data,symb]

###########################################################################
#  Intimidator 4 Kit Bash, Maiden Flight November 1, 2014.
###########################################################################
# NOTES
# - No.1 Unpainted, "Eat My Shorts" w/ sharpie on green fiberglass - good
# - No.2 Bright Orange & Auto Clear, "If Found..." sticker - crashed
# - No.3 Joker's Wild Ride, same fins and NC w/ nose weight - crashed
# - No.4 StarChaser full body wrap and cheap clear - good
# - No.5 RedShift, full body sand and repaint - good 

def FlightLog_Intimidator4():

    # Title
    ttl = r"Intimidator 4 (Kit Bash)"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt
    data = [['Nov',  '1', '2014', 'M3400',  'CTI', 9994.5, 3400, 19035],\
            ['Oct', '31', '2015', 'M1419',   'AT', 7755.5, 1419, 17449],\
            #['Nov',  '5', '2016', 'M2400',   'AT', 7716.5, 2400, 13655],\
            ['Mar', '10', '2018', 'M1101',  'CTI', 5197.6, 1101, 14698],\
            ['Sep',  '1', '2019', 'M2020',  'CTI', 8429.4, 2020, 17319],\
            ['Oct', '12', '2019', 'L1400', 'LOKI', 2850.6, 1400, 6727]]

    # Marker size/type/color
    symb = [[10, "o", "lightcyan"    ],\
            [10, "s", "ivory"        ],\
            #[10, "s", "mediumblue"   ],\
            [10, "o", "white"        ],\
            [10, "o", "darkorange"   ],\
            [12, "v", "floralwhite"  ]]

    return [ttl,data,symb]

###########################################################################
# Gizmo XL DD by WildMan, Maiden Flight November 10, 2018.
###########################################################################

def FlightLog_GizmoXLDD():

    # Title
    ttl = r"Gizmo XL DD"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt (Known Flights Only)
    data = [['Nov', '10', '2018', 'M2080',  'CTI', 6827.3, 2080,  7163]]

    # Marker size/type/color
    symb = [[10, "o", "saddlebrown"  ]]

    return [ttl,data,symb]

###########################################################################
# Altitude Plot - ALL
###########################################################################
def AltCost_ALL(fout,title,aa,bb):

    # set titles
    xtxt = r"Reload Price"
    ytxt = r"Max Altitude AGL (ft)"

    # axes limits
    xmin = 0
    xmax = 800
    ymin = 0
    ymax = 24000

    # axes tick settings
    nx = 9
    ny = 13
    dx = (xmax-xmin)/(nx-1.0)
    dy = (ymax-ymin)/(ny-1.0)
    mx = 4
    my = 4
    xticks = [r"$0",r"$100",r"$200",r"$300",r"$400",r"$500",r"$600",\
        r"$700",r"$800"]
    yticks = [r"0",r"2,000",r"4,000",r"6,000",r"8,000",r"10,000",\
        r"12,000",r"14,000",r"16,000",r"18,000",r"20,000",r"22,000",\
        r"24,000"]

    # figure settings
    figsize = (3,2.75)
    dpi = 1000

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
    f.subplots_adjust(left=0.2,right=0.9,bottom=0.2,top=0.85)

    # move axes spines outward
    ax.spines['left'].set_position(('outward',30.0))
    ax.spines['bottom'].set_position(('outward',30.0))

    # border visibiliy
    ax.title.set_position([.5,1.07])
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.grid(b=True,which='major',color='chartreuse',\
        linestyle='-',linewidth=1.0)
    ax.grid(b=True,which='minor',color='lightseagreen',\
        linestyle='-',linewidth=0.25)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)

    # Axis padding
    ax.get_xaxis().tick_bottom()
    ax.xaxis.labelpad = 17
    ax.get_yaxis().tick_left()
    ax.yaxis.labelpad = 17

    # border line width
    ax.spines['top'].set_linewidth(2.0)
    ax.spines['right'].set_linewidth(2.0)
    ax.spines['bottom'].set_linewidth(2.0)
    ax.spines['left'].set_linewidth(2.0)

    # axes tick settings
    ax.get_yaxis().set_tick_params(which='both',direction='in',pad=10,\
        right='off',width=2.0)
    ax.get_xaxis().set_tick_params(which='both',direction='in',pad=10,\
        top='off',width=2.0)
    ax.get_yaxis().set_tick_params(which='major',length=13.0,width=2.0)
    ax.get_xaxis().set_tick_params(which='major',length=13.0,width=2.0)
    ax.get_yaxis().set_tick_params(which='minor',length=7.0,width=2.0)
    ax.get_xaxis().set_tick_params(which='minor',length=7.0,width=2.0)
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
        line.set_linewidth(2.0)
    for label in ticklabels:
        label.set_fontsize(18)

    # set the text
    ax.set_title(title,fontsize=18,weight='bold')
    ax.set_ylabel(ytxt,fontsize=18,weight='bold')
    ax.set_xlabel(xtxt,fontsize=18,weight='bold')
    ax.set_xticklabels(xticks,fontsize=18,weight='bold',\
        rotation=45,ha='right')
    ax.set_yticklabels(yticks,fontsize=18,weight='bold')

    ##########################
    ### ADD YOUR DATA HERE ###
    ##########################

    # Make shaded regions for the different letters.

    # I-Range
    i1 = aa*320.01+bb
    i2 = aa*640.0+bb
    itot=np.linspace(i1,i2)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='slategrey',label='_nolegend_')
    plt.text(0.5*(i1+i2),22000,r'I',fontsize=14,family=family,\
        color='k',fontweight='bold')

    # J-Range
    i1 = aa*640.01+bb
    i2 = aa*1280.0+bb
    itot=np.linspace(i1,i2)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='mediumblue',label='_nolegend_')
    plt.text(0.5*(i1+i2),22000,r'J',fontsize=14,family=family,\
        color='k',fontweight='bold')

    # K-Range
    i1 = aa*1280.01+bb
    i2 = aa*2560.0+bb
    itot=np.linspace(i1,i2)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='turquoise',label='_nolegend_')
    plt.text(0.5*(i1+i2),22000,r'K',fontsize=14,family=family,\
        color='k',fontweight='bold')

    # L-Range
    i1 = aa*2560.01+bb
    i2 = aa*5120.0+bb
    itot=np.linspace(i1,i2)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='chartreuse',label='_nolegend_')
    plt.text(0.5*(i1+i2),22000,r'L',fontsize=14,family=family,\
        color='k',fontweight='bold')

    # M-Range
    i1 = aa*5120.01+bb
    i2 = aa*10240.0+bb
    itot=np.linspace(i1,i2)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='gold',label='_nolegend_')
    plt.text(0.5*(i1+i2),22000,r'M',fontsize=14,family=family,\
        color='k',fontweight='bold')

    # N-Range
    i1 = aa*10240.01+bb
    i2 = aa*18000.0+bb
    itot=np.linspace(i1,i2)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='orangered',label='_nolegend_')
    plt.text(725,22000,r'N',fontsize=14,family=family,\
        color='k',fontweight='bold')

    # Scatter Plots (different symbols)
    k=0
    lb=aa*4000+bb
    ub=aa*11000+bb
    linecolor='ivory'
    rlabel='rocket'

    # Loop twice to render the correct order
    for jj in range(2):

        # Loop over rocket kits (k)
        for k in range(5):

            if k==0:
                [ttl,data,symb] = FlightLog_DSJrWM()
                lb = aa*400+bb
                ub = aa*1600+bb
                linecolor='red'
                rlabel='Darkstar Jr.'
            if k==1:
                [ttl,data,symb] = FlightLog_Comp3WM()
                lb = aa*600+bb
                ub = aa*2600+bb
                linecolor='ivory'
                rlabel='Competitor 3'
            if k==2:
                [ttl,data,symb] = FlightLog_ExtremeDS()
                lb = aa*1600+bb
                ub = aa*9000+bb
                linecolor='black'
                rlabel='Extreme Darkstar'
            if k==3:
                [ttl,data,symb] = FlightLog_Intimidator4()
                lb = aa*2000+bb
                ub = aa*10200+bb
                linecolor='orangered'
                rlabel='Intimidator 4 (Kit Bash)'
            if k==4:
                [ttl,data,symb] = FlightLog_GizmoXLDD()
                rlabel='_nolegend_'

            # Flight Data
            nf=0
            for flight in data:
                nf=nf+1
            print "There are ",nf," flights in the databse."
            xdat=np.zeros(nf)
            ydat=np.zeros(nf)
            ii=0
            for flight in data:
                xdat[ii]=aa*flight[5]+bb
                ydat[ii]=flight[7]
                ii+=1

            # Curve Fit
            # slope, intercept, r_value, p_value, std_err
            if nf>1 and jj==0:
                [m,b,r,p,std]=sp.stats.linregress(xdat,ydat)
                xfit=np.linspace(lb,ub)
                yfit=np.multiply(xfit,m)+b

                outline=mpe.withStroke(linewidth=4.0,foreground='black')
                plt.plot(xfit,yfit,'k-',color=linecolor,linewidth=2.0,\
                    label=rlabel,\
                    path_effects=[outline])

            # Loop over flights in data (i)
            i=0
            for flight in data:

                # Loop over marker parameters (j)
                j=0
                for marker in symb:
                    if (i==j):
                        ms = marker[0]*0.75
                        mt = marker[1]
                        mc = marker[2]
                    j+=1
                mfg = flight[4]
                motor = flight[3]
                str1=r'%s %s'%(mfg,motor)
                print str1
                if (jj==1):
                    plt.plot(xdat[i],ydat[i],'ko',markersize=ms,\
                        markeredgewidth=1.5,markeredgecolor='k',\
                        markerfacecolor=mc,label='_nolegend_',marker=mt)
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
    loc=4

    legend = ax.legend(loc=loc,ncol=2,\
        prop=matplotlib.font_manager.FontProperties(\
            family=family,weight='bold',size=10),\
        numpoints=1,fancybox=False,borderpad=0.5)
    legend.get_frame().set_linewidth(1.5)
    legend.get_frame().set_edgecolor("k")

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
fout = 'Alt_Cost'
ttl = 'Cost to Altitude'
AltCost_ALL(fout,ttl,0.05889,35.28)
