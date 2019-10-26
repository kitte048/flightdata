### Make all altitude comparison plots by D. Kittell
### Started on July 6, 2019
### 
# Preamble
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
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
#------------------------------------------

###########################################################################
# Extreme DarkStar by WildMan, Maiden Flight May 13, 2017.
###########################################################################

def FlightLog_ExtremeDS():

    # Title
    ttl = r"Extreme DarkStar, L3"

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
#  Intimidator 4 by WildMan, Maiden Flight November 1, 2014.
###########################################################################

def FlightLog_Intmd4WM():

    # Title
    ttl = r"Intimidator 4 by WildMan"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt
    data = [['Nov',  '1', '2014', 'M3400',  'CTI', 9994.5, 3400, 19035],\
            ['Oct', '31', '2015', 'M1419',   'AT', 7755.5, 1419, 17449],\
            ['Mar', '10', '2018', 'M1101',  'CTI', 5197.6, 1101, 14698]]

    # Marker size/type/color
    symb = [[10, "o", "lightcyan"    ],\
            [10, "s", "ivory"        ],\
            [10, "o", "white"        ]]

    return [ttl,data,symb]

###########################################################################
# Altitude Plot (H-K Range, up to 2000 Ns)
###########################################################################
def AltPlot_GK(fout,title,data,symb):

    # set titles
    xtxt = r"Total Impulse (N-s)"
    ytxt = r"Max Altitude AGL (ft)"

    # axes limits
    xmin = 0
    xmax = 2000
    ymin = 0
    ymax = 16000

    # axes tick settings
    nx = 6
    ny = 9
    dx = (xmax-xmin)/(nx-1.0)
    dy = (ymax-ymin)/(ny-1.0)
    mx = 4
    my = 4
    xticks = [r"0",r"400",r"800",r"1200",\
        r"1600"," "]
    yticks = [r"0",r"2,000",r"4,000",r"6,000",r"8,000",\
        r"10,000",r"12,000",r"14,000",r"16,000"]

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

    # G-Range
    itot=np.linspace(80.01,160.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='mediumblue',label='_nolegend_')
    plt.text(85.,1000,r'G',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # H-Range
    itot=np.linspace(160.01,320.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='turquoise',label='_nolegend_')
    plt.text(200.,1000,r'H',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # I-Range
    itot=np.linspace(320.01,640.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='chartreuse',label='_nolegend_')
    plt.text(0.5*(320.01+640.0),1000,r'I',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # J-Range
    itot=np.linspace(640.01,1280.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='gold',label='_nolegend_')
    plt.text(0.5*(640.01+1280.0),1000,r'J',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # K-Range
    itot=np.linspace(1280.01,2560.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='orangered',label='_nolegend_')
    plt.text(0.5*(1280.01+2000),1000,r'K',fontsize=22,family=family,\
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
    xfit=np.linspace(200,1800)
    yfit=np.multiply(xfit,m)+b

    str1=r'Y=%1.2f*X+%4.0f'%(m,b)
    str2=r'r$^2$=%1.4f'%(r)
    plt.text(1000,3500,str1,fontsize=18,family=family,\
        color='k',fontweight='bold')
    plt.text(1000,4800,str2,fontsize=18,family=family,\
        color='k',fontweight='bold')

    outline=mpe.withStroke(linewidth=10.0,foreground='black')
    plt.plot(xfit,yfit,'k-',color='orangered',linewidth=3.4,\
        label=r'_nolegend_',\
        path_effects=[outline])

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

    legend = ax.legend(loc=loc,ncol=4,\
        prop=matplotlib.font_manager.FontProperties(\
            family=family,weight='bold',size=10),\
        numpoints=1,fancybox=False,borderpad=0.5)
    legend.get_frame().set_linewidth(3.5)
    legend.get_frame().set_edgecolor("k")

    # save the image
    plt.tight_layout()
    f.savefig(fout+'.png',format='png')
    plt.clf()

    return []

###########################################################################
# Altitude Plot (I-L Range, up to 4000 Ns)
###########################################################################
def AltPlot_HL(fout,title,data,symb):

    # set titles
    xtxt = r"Total Impulse (N-s)"
    ytxt = r"Max Altitude AGL (ft)"

    # axes limits
    xmin = 0
    xmax = 3500
    ymin = 0
    ymax = 18000

    # axes tick settings
    nx = 8
    ny = 10
    dx = (xmax-xmin)/(nx-1.0)
    dy = (ymax-ymin)/(ny-1.0)
    mx = 4
    my = 4
    xticks = [r"0"," ",r"1000"," ",r"2000"," ",\
        r"3000"," "]
    yticks = [r"0",r"2,000",r"4,000",r"6,000",r"8,000",\
        r"10,000",r"12,000",r"14,000",r"16,000",r"18,000"]

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

    # H-Range
    itot=np.linspace(160.01,320.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='mediumblue',label='_nolegend_')
    plt.text(175.,1400,r'H',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # I-Range
    itot=np.linspace(320.01,640.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='turquoise',label='_nolegend_')
    plt.text(0.5*(320.01+640.0),1400,r'I',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # J-Range
    itot=np.linspace(640.01,1280.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='chartreuse',label='_nolegend_')
    plt.text(0.5*(640.01+1280.0),1400,r'J',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # K-Range
    itot=np.linspace(1280.01,2560.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='gold',label='_nolegend_')
    plt.text(0.5*(1280.01+2560.0),1400,r'K',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # L-Range
    itot=np.linspace(2560.01,4000.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='orangered',label='_nolegend_')
    plt.text(0.5*(2560.01+3500),1400,r'L',fontsize=22,family=family,\
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
    xfit=np.linspace(600,2600)
    yfit=np.multiply(xfit,m)+b

    str1=r'Y=%1.2f*X+%4.0f'%(m,b)
    str2=r'r$^2$=%1.4f'%(r)
    plt.text(2000,3900,str1,fontsize=18,family=family,\
        color='k',fontweight='bold')
    plt.text(2000,5200,str2,fontsize=18,family=family,\
        color='k',fontweight='bold')

    outline=mpe.withStroke(linewidth=10.0,foreground='black')
    plt.plot(xfit,yfit,'k-',color='orangered',linewidth=3.4,\
        label=r'_nolegend_',\
        path_effects=[outline])

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

    legend = ax.legend(loc=loc,ncol=4,\
        prop=matplotlib.font_manager.FontProperties(\
            family=family,weight='bold',size=10),\
        numpoints=1,fancybox=False,borderpad=0.5)
    legend.get_frame().set_linewidth(3.5)
    legend.get_frame().set_edgecolor("k")

    # save the image
    plt.tight_layout()
    f.savefig(fout+'.png',format='png')
    plt.clf()

    return []

###########################################################################
# Altitude Plot (J-N Range, up to 12000 Ns)
###########################################################################
def AltPlot_JN(fout,title,data,symb,L3His,lb,ub):

    # set titles
    xtxt = r"Total Impulse (N-s)"
    ytxt = r"Max Altitude AGL (ft)"

    # axes limits
    xmin = 0
    xmax = 12000
    ymin = 0
    ymax = 28000

    # axes tick settings
    nx = 7
    ny = 8
    dx = (xmax-xmin)/(nx-1.0)
    dy = (ymax-ymin)/(ny-1.0)
    mx = 4
    my = 4
    xticks = [r"0",r"2000",r" ",r"6000",r" ",r"10000",r" "]
    yticks = [r"0",r"4,000",r"8,000",r"12,000",r"16,000",\
        r"20,000",r"24,000",r"28,000"]

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
    plt.text(0.5*(640.01+1100.0),1400,r'J',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # K-Range
    itot=np.linspace(1280.01,2560.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='turquoise',label='_nolegend_')
    plt.text(0.5*(1280.01+2200.0),1400,r'K',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # L-Range
    itot=np.linspace(2560.01,5120.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='chartreuse',label='_nolegend_')
    plt.text(0.5*(2560.01+5000),1400,r'L',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # M-Range
    itot=np.linspace(5120.01,10240.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='gold',label='_nolegend_')
    plt.text(0.5*(5120.01+9440),1400,r'M',fontsize=22,family=family,\
        color='k',fontweight='bold')

    # N-Range
    itot=np.linspace(10240.01,12000.0)
    ylow=itot-1.e6
    yhig=itot+1.e6
    plt.fill_between(itot,yhig,ylow,interpolate=True,alpha=0.5,\
        color='orangered',label='_nolegend_')
    plt.text(0.5*(10240.01+11500),1400,r'N',fontsize=22,family=family,\
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
    plt.text(5500,4500,str1,fontsize=18,family=family,\
        color='k',fontweight='bold')
    plt.text(5500,6500,str2,fontsize=18,family=family,\
        color='k',fontweight='bold')

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
        xfit2=np.linspace(1600,10000)
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
        plt.text(6800,12000,r"Extreme DarkStar",fontsize=16,family=family,\
            color='darkmagenta',fontweight='bold')
        plt.text(6800,10000,r"(Reference, L3 kit)",fontsize=16,family=family,\
            color='darkmagenta',fontweight='bold')
        plt.text(2000,17000,r"Intimidator",fontsize=18,family=family,\
            color='orangered',fontweight='bold')
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

    legend = ax.legend(loc=loc,ncol=4,\
        prop=matplotlib.font_manager.FontProperties(\
            family=family,weight='bold',size=10),\
        numpoints=1,fancybox=False,borderpad=0.5)
    legend.get_frame().set_linewidth(3.5)
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
    
fout = 'DarkStarJr_Alt'
[ttl,data,symb] = FlightLog_DSJrWM()
AltPlot_GK(fout,ttl,data,symb)

fout = 'Comp3WM_Alt'
[ttl,data,symb] = FlightLog_Comp3WM()
AltPlot_HL(fout,ttl,data,symb)

fout = 'ExtremeDS_Alt'
[ttl,data,symb] = FlightLog_ExtremeDS()
L3His = False
lb = 1600
ub = 10000
AltPlot_JN(fout,ttl,data,symb,L3His,lb,ub)

fout = 'Intmd4WM_CompL3_Alt'
[ttl,data,symb] = FlightLog_Intmd4WM()
L3His = True
lb = 2000
ub = 11000
AltPlot_JN(fout,ttl,data,symb,L3His,lb,ub)


