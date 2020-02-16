### Make all altitude comparison plots by D. Kittell
### Started on July 6, 2019
###
### UPDATES:
### 21-Jul 2019 Added Joker's Wild Ride, Rocksim prediction,
###             and recent launches.
### 28-Sep 2019 Added Gizmo XL DD
### 15-Feb 2020 Added All electronic data, multiple per flight
###
# Preamble
import os
import sys
import numpy as np
import matplotlib
#matplotlib.use('TkAgg')
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
    ttl = r"Extreme DarkStar (My L3) - Altimeter Data"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt/Altimeter
    data = [['May',  '1', '2011', 'L1410',  'CTI', 4828.3, 1410, 10608,'ARTS'],\
            ['May',  '1', '2011', '_nolegend_','', 4828.3, 1410, 10524,'MAWD'],\
            ['Oct', '29', '2011', 'M2020',  'CTI', 8429.4, 2020, 17834,'ARTS'],\
            ['Mar', '31', '2012', 'M3700',  'CTI', 6800.0, 3600, 15000,'???' ],\
            ['n/a','n/a',  'n/a', 'K1200',  'CTI', 2014.0, 1200,  5137,'ARTS'],\
            ['n/a','n/a',  'n/a', '_nolegend_','', 2014.0, 1200,  5243,'MAWD'],\
            ['Oct', '31', '2015', 'M2250',  'CTI', 5472.2, 2250, 12458,'ARTS'],\
            ['Aug', '30', '2019',  'K830', 'LOKI', 2287.0,  830,  4707,'ARTS'],\
            ['Aug', '30', '2019', '_nolegend_','', 2287.0,  830,  4682,'MAWD'],\
            ['Jan', '11', '2020', 'L1030',  'CTI', 2787.9, 1030,  8057,'ARTS'],\
            ['Jan', '11', '2020', '_nolegend_','', 2787.9, 1030,  7976,'MAWD']]

    # Marker size/type/color
    symb = [[10, "o", "saddlebrown"  ],\
            [10, "o", "saddlebrown"  ],\
            [10, "o", "darkorange"   ],\
            [10, "o", "lightcyan"    ],\
            [10, "o", "lightcyan"    ],\
            [10, "o", "lightcyan"    ],\
            [10, "o", "yellow"       ],\
            [12, "v", "chocolate"    ],\
            [12, "v", "chocolate"    ],\
            [10, "o", "red"          ],\
            [10, "o", "red"          ]]

    return [ttl,data,symb]

###########################################################################
# DarkStar Junior by WildMan, Maiden Flight May 13, 2017.
###########################################################################

def FlightLog_DSJrWM():

    # Title
    ttl = r"DarkStar Junior by WildMan - Altimeter Data"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt/Altimeter
    data = [['May', '13', '2017', 'I285' ,  'CTI',  510.1,  285,  4466,'SL1'],\
            ['Aug', '12', '2017', 'J600' ,  'CTI',  998.6,  600,  8373,'SL1'],\
            ['Sep',  '4', '2017', 'J394' ,  'CTI',  970.4,  394,  6794,'SL1'],\
            ['Nov', '11', '2017', 'J396' , 'LOKI',  650.0,  396,  5347,'SL1'],\
            ['Dec',  '9', '2017', 'J1000', 'LOKI', 1220.0, 1000,  9284,'SL1'],\
            ['Jan', '13', '2018', 'J453' ,  'CTI', 1012.6,  453,  6708,'SL1'],\
            ['Feb', '10', '2018', 'J650' , 'LOKI',  942.0,  650,  7974,'SL1'],\
            ['Mar',  '9', '2019', 'K627' , 'LOKI', 1519.0,  627, 10396,'SL1'],\
            ['Jun',  '8', '2019', 'J500' ,   'AT',  723.0,  500,  6133,'SL2'],\
            ['Jun',  '8', '2019', '_nolegend_','',  723.0,  500,  6447,'JLA3'],\
            ['Jul', '20', '2019', 'J420' ,   'AT',  658.0,  420,  5577,'SL2'],\
            ['Jul', '20', '2019', '_nolegend_','',  658.0,  420,  5584,'JLA3']]

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
            [10, "s", "lime"         ],\
            [10, "s", "orangered"    ],\
            [10, "s", "orangered"    ]]

    return [ttl,data,symb]

###########################################################################
#  Competitor 3 by WildMan, Maiden Flight November 2, 2013.
###########################################################################

def FlightLog_Comp3WM():

    # Title
    ttl = r"Competitor 3 by WildMan - Altimeter Data"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt/Altimeter
    data = [['Nov',  '2', '2013', 'K940' ,  'CTI', 1632.7,  940,  9200,'MAWD'],\
            ['Dec', '10', '2016', 'J1026', 'LOKI', 1267.0, 1026,  7170,'SL3'],\
            ['Feb', '11', '2017', 'K185' ,   'AT', 1417.2,  185,  7817,'SL3'],\
            ['Sep',  '3', '2017', 'K711' ,  'CTI', 2377.3,  711, 12108,'SL3'],\
            ['Oct', '14', '2017', 'J528' , 'LOKI',  741.0,  528,  3556,'SL3'],\
            ['Mar',  '9', '2019', 'K815' ,  'CTI', 2303.7,  815, 11037,'SL3'],\
            ['Mar',  '9', '2019', '_nolegend_','', 2303.7,  815, 11092,'JLA3'],\
            ['Apr', '13', '2019', 'K1127', 'LOKI', 1285.0, 1127,  6487,'SL2'],\
            ['Apr', '13', '2019', '_nolegend_','', 1285.0, 1127,  6515,'JLA3']]

    # Marker size/type/color
    symb = [[10, "o", "lightcyan"    ],\
            [12, "v", "mediumpurple" ],\
            [10, "s", "ivory"        ],\
            [10, "o", "white"        ],\
            [12, "v", "floralwhite"  ],\
            [10, "o", "saddlebrown"  ],\
            [10, "o", "saddlebrown"  ],\
            [12, "v", "aqua"         ],\
            [12, "v", "aqua"         ]]

    return [ttl,data,symb]

###########################################################################
#  Intimidator 4 Kit Bash, Maiden Flight November 1, 2014.
###########################################################################
# NOTES
# - No.1 Unpainted, "Eat My Shorts" w/ sharpie on green fiberglass - good
#         (except the motor retainer hack had some base drag on it)
# - No.2 Bright Orange & Auto Clear, "If Found..." sticker - crashed
# - No.3 Joker's Wild Ride, same fins and NC w/ nose weight - crashed
# - No.4 StarChaser full body wrap and cheap clear - good
# - No.5 RedShift, full body sand and repaint - good 

def FlightLog_Intimidator4():

    # Title
    ttl = r"Intimidator 4 (Kit Bash) - Altimeter Data"

    ### The old data does not have consistent weight and aerodynamic
    ### performance, so I can't really use it for linear regression.

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt/Altimeter
    dold = [['Nov',  '1', '2014', 'M3400',  'CTI', 9994.5, 3400, 19035,'SL1'],\
            ['Nov',  '1', '2014', '_nolegend_','', 9994.5, 3400, 19041,'SL3'],\
            ['Oct', '31', '2015', 'M1419',   'AT', 7755.5, 1419, 17449,'SL1'],\
            ['Oct', '31', '2015', '_nolegend_','', 7755.5, 1419, 17454,'SL3'],\
            ['Nov',  '5', '2016', 'M2400',   'AT', 7716.5, 2400, 13661,'SL1'],\
            ['Nov',  '5', '2016', '_nolegend_','', 7716.5, 2400, 13655,'SL3'],\
            ['Sep',  '1', '2019', 'M2020',  'CTI', 8429.4, 2020, 17253,'SL1'],\
            ['Sep',  '1', '2019', '_nolegend_','', 8429.4, 2020, 17254,'SL3'],\
            ['Sep',  '1', '2019', '_nolegend_','', 8429.4, 2020, 17319,'JLA3']]
    data = [['Mar', '10', '2018', 'M1101',  'CTI', 5197.6, 1101, 14698,'SL2'],\
            ['Mar', '10', '2018', '_nolegend_','', 5197.6, 1101, 14620,'MAWD'],\
            ['Oct', '12', '2019', 'L1400', 'LOKI', 2850.6, 1400,  6727,'SL1'],\
            ['Oct', '12', '2019', '_nolegend_','', 2850.6, 1400,  6725,'SL3'],\
            ['Nov',  '9', '2019', 'L1040', 'LOKI', 3707.0, 1040,  9224,'SL1'],\
            ['Nov',  '9', '2019', '_nolegend_','', 3707.0, 1040,  9212,'SL3'],\
            ['Nov',  '9', '2019', '_nolegend_','', 3707.0, 1040,  9268,'JLA3']]

    # Marker size/type/color
    sold = [[10, "o", "lightcyan"    ],\
            [10, "o", "lightcyan"    ],\
            [10, "s", "ivory"        ],\
            [10, "s", "ivory"        ],\
            [10, "s", "mediumblue"   ],\
            [10, "s", "mediumblue"   ],\
            [10, "o", "darkorange"   ],\
            [10, "o", "darkorange"   ],\
            [10, "o", "darkorange"   ]]
    symb = [[10, "o", "white"        ],\
            [10, "o", "white"        ],\
            [12, "v", "floralwhite"  ],\
            [12, "v", "floralwhite"  ],\
            [12, "v", "red"          ],\
            [12, "v", "red"          ],\
            [12, "v", "red"          ]]

    return [ttl,data,symb,dold,sold]

###########################################################################
# Gizmo XL DD by WildMan, Maiden Flight November 10, 2018.
###########################################################################

def FlightLog_GizmoXLDD():

    # Title
    ttl = r"Gizmo XL DD - Altimeter Data"

    # Month/Day/Year/Motor/Mfg/Itot/Fave/Alt/Altimeter
    data = [['Nov', '10', '2018', 'M2080',  'CTI', 6827.3, 2080,  7190,'SL1'],\
            ['Nov', '10', '2018', '_nolegend_','', 6827.3, 2080,  7135,'MAWD']]

    # Marker size/type/color
    symb = [[10, "o", "saddlebrown"  ],\
            [10, "o", "saddlebrown"  ]]

    return [ttl,data,symb]

###########################################################################
###########################################################################
###
### Main Program Starts Here
###
###########################################################################
###########################################################################

print "end of line."
