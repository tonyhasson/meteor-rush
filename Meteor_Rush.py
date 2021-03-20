import random,time,math,shelve
import os.path

import pygame
import pygame.locals as pl

pygame.font.init()

from pygame.math import Vector2
pygame.init()

##colors
black=(0,0,0)
red=(220,0,0)
green = (0, 255, 0)
blue=(0,0,220)
white = (255, 255, 255)
yellow=(255,255,0)
##calling high score:
d = shelve.open('hs_meteor.txt')
high_score = d['score']
hs_name=d['name']
d.close()


##images
walkRight = [pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\R1.png'), pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\R2.png'), pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\R3.png'),
             pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\R4.png'), pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\R5.png'), pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\R6.png'),
             pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\R7.png'), pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\R8.png'), pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\R9.png')]
walkLeft = [pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\L1.png'), pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\L2.png'), pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\L3.png'),
            pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\L4.png'), pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\L5.png'), pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\L6.png'),
            pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\L7.png'), pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\L8.png'), pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\L9.png')]
char = pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\standing.png')
bg_menu=[pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame0.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame1.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame2.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame3.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame4.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame5.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame6.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame7.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame8.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame9.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame10.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame11.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame12.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame13.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame14.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame15.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame16.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame17.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame18.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame19.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame20.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame21.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame22.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame23.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame24.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame25.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame26.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame27.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame28.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame29.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame30.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame31.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame32.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame33.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame34.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame35.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame36.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame37.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame38.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame39.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame40.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame41.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame42.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame43.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame44.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame45.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame46.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame47.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame48.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame49.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame50.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame51.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame52.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame53.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame54.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame55.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame56.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame57.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame58.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame59.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame60.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame61.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame62.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame63.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame64.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame65.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame66.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame67.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame68.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame69.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame70.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame71.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame72.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame73.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame74.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame75.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame76.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame77.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame78.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame79.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame80.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame81.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame82.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame83.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame84.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame85.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame86.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame87.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame88.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame89.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame90.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame91.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame92.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame93.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame94.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame95.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame96.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame97.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame98.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame99.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame100.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame101.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame102.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame103.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame104.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame105.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame106.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame107.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame108.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame109.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame110.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame111.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame112.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame113.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame114.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame115.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame116.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame117.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame118.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame119.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame120.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame121.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame122.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame123.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame124.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame125.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame126.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame127.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame128.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame129.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame130.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame131.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame132.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame133.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame134.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame135.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame136.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame137.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame138.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame139.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame140.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame141.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame142.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame143.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame144.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame145.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame146.jpg'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\menu_bg\frame147.jpg')
]
blackhole_img=[pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame0.jpg'),pygame.image.load(
    r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame1.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame2.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame3.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame4.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame5.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame6.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame7.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame8.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame9.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame10.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame11.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame12.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame13.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame14.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame15.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame16.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame17.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame18.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame19.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame20.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame21.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame22.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame23.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame24.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame25.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame26.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame27.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame28.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame29.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame30.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame31.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame32.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame33.jpg'),
               pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole'
                                 r'\frame34.jpg'),pygame.image.load(
        r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\blackhole\frame35.jpg')
]
bg=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\moon_bg.png')
meteor_left= pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\meteor_l.png')
meteor_right= pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\meteor_r.png')
meteor_purple=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\meteor_p.png')
heart=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\heart.png')
flame=[pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\fire1.png'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\fire2.png'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\fire3.png'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\fire4.png')]
alien_ship=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\alien_ship.png')
reg_ammo=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\ammo_regular.png')
start_img=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\start_img.png')
click_start=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\click_start.png')
game_over=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\game_over.png')
buy_heart_img=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\buy_heart.png')
click_bheart=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\click_bheart.png')
continue_img=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\continue.png')
name_img=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\enter_name.png')
infinity_img=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\infinity.png')
##weapons images
reg_weapon=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\regular_weapon.png')
shotgun_weapon=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\shotgun_weapon.png')
machinegun_weapon=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\machinegun_weapon.png')
lazer_weapon=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\lazer_weapon.png')
blackhole_weapon=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\blackhole_weapon.png')
bigbullet_weapon=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\bigbullet_weapon.png')
##bullet images
big_bullet=[pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\bullets\bigbullet_f1.png'),pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\bullets\bigbullet_f2.png')]
reg_bullet=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\bullets\reg_bullet.png')
alien_bullet=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\bullets\alien_bullet.png')
machinegun_bullet=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\bullets\machinegun_bullet.png')
lazer_bullet=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\bullets\lazer.png')
shotgun_bullet=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\bullets\shotgun_bullet.png')
blackhole_bullet=pygame.image.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\weapons'
                             r'\bullets\blackhole_bullet.png')

##sounds
bullet_sound=pygame.mixer.Sound(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\sounds'
                                r'\shoot.wav')
alien_sound=pygame.mixer.Sound(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\sounds'
                                r'\aliensound.wav')
menu_music=pygame.mixer.Sound(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\sounds'
                                r'\menu_music.wav')
heart_sound=pygame.mixer.Sound(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\sounds'
                                r'\heart_sound.wav')
gameover_sound=pygame.mixer.Sound(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\sounds'
                                r'\gameover_sound.wav')
alien_bullet_sound=pygame.mixer.Sound(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\sounds'
                                r'\alienbullet_sound.wav')
bullethit_sound=pygame.mixer.Sound(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\sounds'
                                r'\bullethit_sound.wav')
dmg_sound=pygame.mixer.Sound(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\sounds\dmg_sound.wav')

space_music=pygame.mixer_music.load(r'C:\Users\tonyh\OneDrive\Desktop\programing\python\pictures\learning_img\sounds\space_music.wav')

bullet_sound.set_volume(0.1)
alien_sound.set_volume(0.2)
gameover_sound.set_volume(0.5)
menu_music.set_volume(0.1)
alien_bullet_sound.set_volume(0.5)
bullethit_sound.set_volume(0.5)
dmg_sound.set_volume(0.1)
pygame.mixer_music.set_volume(1)
pygame.mixer_music.play(-1)

##creating the screen
window=pygame.display.set_mode((840,480))
##creating title
pygame.display.set_caption("Meteor Rush")
clock=pygame.time.Clock()

##creating player
class player(object):

    def __init__(self,x,y,width,height,hitbox_x,hitbox_y,weapon):
        self.x = 400
        self.y = 420
        self.width = 64
        self.height = 64
        self.hitbox_x=hitbox_x
        self.hitbox_y=hitbox_y
        self.weapon=weapon
        self.name=""
        self.vel = 10
        self.is_jump = 0
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.ammo=0
        ##walking animation
    def draw(self,window):
        if man.walkCount + 1 >= 27:
            man.walkCount = 0
        if man.right:
            window.blit(walkRight[man.walkCount // 3], (man.x, man.y))
            man.walkCount += 1
        elif man.left:
            window.blit(walkLeft[man.walkCount // 3], (man.x, man.y))
            man.walkCount += 1
        else:
            window.blit(char, (man.x, man.y))

##meteors,etc..
class projectiles(object):
    def __init__(self, image, vel, x, y, hitbox_x, hitbox_y,direction):
        self.image = image
        self.vel = vel
        self.x = x
        self.y = y
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y
        self.flame_count=0
        self.direction=direction
        self.count_hit=0
        self.direction_x=0
        self.direction_y=0
        self.bh_pos_x=0
        self.bh_pos_y=0
        self.count_bullet=0




##life in game
class life(object):
    def __init__(self,image,x,y):
        self.image=image
        self.x = x
        self.y = y
        self.hitbox_x=32
        self.hitbox_y=30

##bullets
class bullets(object):
    def __init__(self,x,y,image,radios,mouse_x,mouse_y,start_x,start_y,hitbox_x,hitbox_y):
         self.x=x
         self.y=y
         self.image=image
         self.radios = radios
         self.mouse_x = mouse_x
         self.mouse_y = mouse_y
         self.direction_x=pygame.math.Vector2
         self.direction_y = pygame.math.Vector2
         self.vel=10
         self.hitbox_x=hitbox_x
         self.hitbox_y=hitbox_y
         self.start_x=start_x
         self.start_y=start_y
         self.count_image=0
         self.ShotGunList=[]
         self.IsShotGun_main=False
         self.angle=0
         self.distance=0
         self.bh_pos_x = 0
         self.bh_pos_y = 0
         self.my_alien=0
    ##drawing the bullet
    def draw(self,window):
        if self.image!=big_bullet:
            window.blit(self.image, (self.x, self.y))

        elif self.image==big_bullet:
            if self.count_image==2:
                self.count_image=0
            window.blit(self.image[self.count_image],(self.x,self.y))
            self.count_image+=1
    def draw_rotate(self,window,rotate_img,rect):
        window.blit(rotate_img, rect)



##button class
class Button(object):
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        global text_loop
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        ##start button:goes from menu to entering name
        if img_in==start_img:
            if x + width > mouse[0] > x and y + height > mouse[1] > y:
                window.blit(img_act, (x_act, y_act))
                if click[0] and action != None:

                    text_loop=True
                    action()
            else:
                window.blit(img_in, (x, y))
        ##buy heart button:buying a heart for 100 ammo
        elif img_in==buy_heart_img:
            if man.ammo>=100:
                window.blit(img_in, (x, y))
                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    if click[0] and action != None:
                        action()





##text class
class TextInput:
    """
    This class lets the user input a piece of text, e.g. a name or a message.
    This class let's the user input a short, one-lines piece of text at a blinking cursor
    that can be moved using the arrow-keys. Delete, home and end work as well.
    """
    def __init__(
            self,
            initial_string="",
            font_family="",
            font_size=35,
            antialias=True,
            text_color=(0, 0, 0),
            cursor_color=(0, 0, 1),
            repeat_keys_initial_ms=400,
            repeat_keys_interval_ms=35,
            max_string_length=-1):
        """
        :param initial_string: Initial text to be displayed
        :param font_family: name or list of names for font (see pygame.font.match_font for precise format)
        :param font_size:  Size of font in pixels
        :param antialias: Determines if antialias is applied to font (uses more processing power)
        :param text_color: Color of text (duh)
        :param cursor_color: Color of cursor
        :param repeat_keys_initial_ms: Time in ms before keys are repeated when held
        :param repeat_keys_interval_ms: Interval between key press repetition when held
        :param max_string_length: Allowed length of text
        """

        # Text related vars:
        self.antialias = antialias
        self.text_color = text_color
        self.font_size = font_size
        self.max_string_length = max_string_length
        self.input_string = initial_string  # Inputted text

        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)

        self.font_object = pygame.font.Font(font_family, font_size)

        # Text-surface will be created during the first update call:
        self.surface = pygame.Surface((1, 1))
        self.surface.set_alpha(0)

        # Vars to make keydowns repeat after user pressed a key for some time:
        self.keyrepeat_counters = {}  # {event.key: (counter_int, event.unicode)} (look for "***")
        self.keyrepeat_intial_interval_ms = repeat_keys_initial_ms
        self.keyrepeat_interval_ms = repeat_keys_interval_ms

        # Things cursor:
        self.cursor_surface = pygame.Surface((int(self.font_size / 20 + 1), self.font_size))
        self.cursor_surface.fill(cursor_color)
        self.cursor_position = len(initial_string)  # Inside text
        self.cursor_visible = True  # Switches every self.cursor_switch_ms ms
        self.cursor_switch_ms = 500  # /|\
        self.cursor_ms_counter = 0

        self.clock = pygame.time.Clock()

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.cursor_visible = True  # So the user sees where he writes

                # If none exist, create counter for that key:
                if event.key not in self.keyrepeat_counters:
                    self.keyrepeat_counters[event.key] = [0, event.unicode]

                if event.key == pl.K_BACKSPACE:
                    self.input_string = (
                        self.input_string[:max(self.cursor_position - 1, 0)]
                        + self.input_string[self.cursor_position:]
                    )

                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)
                elif event.key == pl.K_DELETE:
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + self.input_string[self.cursor_position + 1:]
                    )

                elif event.key == pl.K_RETURN:
                    return True

                elif event.key == pl.K_RIGHT:
                    # Add one to cursor_pos, but do not exceed len(input_string)
                    self.cursor_position = min(self.cursor_position + 1, len(self.input_string))

                elif event.key == pl.K_LEFT:
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)

                elif event.key == pl.K_END:
                    self.cursor_position = len(self.input_string)

                elif event.key == pl.K_HOME:
                    self.cursor_position = 0

                elif len(self.input_string) < self.max_string_length or self.max_string_length == -1:
                    # If no special key is pressed, add unicode of key to input_string
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + event.unicode
                        + self.input_string[self.cursor_position:]
                    )
                    self.cursor_position += len(event.unicode)  # Some are empty, e.g. K_UP

            elif event.type == pl.KEYUP:
                # *** Because KEYUP doesn't include event.unicode, this dict is stored in such a weird way
                if event.key in self.keyrepeat_counters:
                    del self.keyrepeat_counters[event.key]

        # Update key counters:
        for key in self.keyrepeat_counters:
            self.keyrepeat_counters[key][0] += self.clock.get_time()  # Update clock

            # Generate new key events if enough time has passed:
            if self.keyrepeat_counters[key][0] >= self.keyrepeat_intial_interval_ms:
                self.keyrepeat_counters[key][0] = (
                    self.keyrepeat_intial_interval_ms
                    - self.keyrepeat_interval_ms
                )

                event_key, event_unicode = key, self.keyrepeat_counters[key][1]
                pygame.event.post(pygame.event.Event(pl.KEYDOWN, key=event_key, unicode=event_unicode))

        # Re-render text surface:
        self.surface = self.font_object.render(self.input_string, self.antialias, self.text_color)

        # Update self.cursor_visible
        self.cursor_ms_counter += self.clock.get_time()
        if self.cursor_ms_counter >= self.cursor_switch_ms:
            self.cursor_ms_counter %= self.cursor_switch_ms
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            cursor_y_pos = self.font_object.size(self.input_string[:self.cursor_position])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if self.cursor_position > 0:
                cursor_y_pos -= self.cursor_surface.get_width()
            self.surface.blit(self.cursor_surface, (cursor_y_pos, 0))

        self.clock.tick()
        return False

    def get_surface(self):
        return self.surface

    def get_text(self):
        return self.input_string

    def get_cursor_position(self):
        return self.cursor_position

    def set_text_color(self, color):
        self.text_color = color

    def set_cursor_color(self, color):
        self.cursor_surface.fill(color)

    def clear_text(self):
        self.input_string = ""
        self.cursor_position = 0




##variables and lists
text_loop=True
menu=True
mainloop=True
clicked=False
counter_image=0
man=player(400,420,64,64,28,60,reg_weapon)
meteor_list=[]
heart1=life(heart,0,0)
heart2=life(heart,30,0)
heart3=life(heart,60,0)
heart_count=3
heart_list=[heart1,heart2,heart3]
new_life=[]
bullet_list=[]
change_amount=0
random_end=25
flame_list=[]
alien_list=[]
alien_bullet_list=[]
count_step=0
count_score=0
new_ammo=[]
new_weapon=[]
is_pause=False
counter_done=0
blackhole_counter=0
constant_x=0
constant_y=0

##update function
def refresh_game():
    global count_step,counter_done,constant_x,constant_y,blackhole_counter,count_score
    window.blit(bg,(0,0))
    bullet_move()
    ##showing hearts
    for h in heart_list:
        window.blit(heart,(h.x,h.y))
    ##deleting ammo from screen
    for a in new_ammo:
        if a.y>480:
            new_ammo.pop(new_ammo.index(a))
    ##moving player

    man.draw(window)
    ##flame animation
    for f in flame_list:
        draw_flame(f)

    ##alien ship moving and deleting
    move_alien()
    for a in alien_list:
        if a.x>840 or a.x<0:
            a.y=600
        if blackhole_counter > 0:
            if a.x > constant_x and a.x < constant_x + 300:
                if a.y > constant_y and a.y < constant_y + 300:
                    count_score += 50
                    a.y=600

    ##checking if player is moving or not
    if man.walkCount==0:
         count_step+=1
    elif man.walkCount!=0:
         count_step=0

    ##moving and deleting meteors from list

    for meteor in meteor_list:
              meteor_move(meteor)

              if meteor.y>=480 and meteor.y<600:
                   meteor.y=600
                  ##creating flame from meteor fall
                   if count_score > 150:
                       if meteor.image!=meteor_purple:
                                create_flame(meteor.x)
                   #meteor_list.pop(meteor_list.index(meteor))
              ##sucking meteors into black hole
              if blackhole_counter>0:
                  if meteor.x>constant_x and meteor.x<constant_x+300:
                      if meteor.y>constant_y and meteor.y<constant_y+300:
                          count_score+=10
                          meteor.y=600
              ##deleting meteors:
              if meteor.y==600:
                  meteor_list.pop(meteor_list.index(meteor))


    ##deleting player bullets from list
    for b in bullet_list:
        if b.y<0 or b.x<0 or b.x>840 or b.y>480:
            b.y=600



    ##deleting alien bullets from list
    for a in alien_bullet_list:
        if a.y < 0 or a.x < 0 or a.x > 840 or a.y > 480:
            if a.y<600:
                a.y = 600
                alien_list[a.my_alien].count_bullet-=1
                print(str(alien_list[a.my_alien].count_bullet))

        if blackhole_counter > 0:
            if a.x > constant_x and a.x < constant_x + 300:
                if a.y > constant_y and a.y < constant_y + 300:
                    a.y=600


    ##regular meteors

    if random.randint(0, random_end-change_amount+5) == 0 :
       meteor_go(random.randint(0,840),1)
    ##purple meteors
    if count_score>300:
        if random.randint(0, random_end-change_amount+5) == 0:
           meteor_go(random.randint(0, 840), 2)
    ##alien ship
    if count_score>500 or count_step>100:
        if random.randint(0,random_end*3)==1 or count_step>100:
            create_alien()
            alien_sound.play()
            count_step=0
    ##creating random ammo
    if man.weapon!=reg_weapon:
        if random.randint(0,random_end*7)==2:
            new_ammo.append(projectiles(reg_ammo, 8, random.randint(0,840), -100, 64, 64, "down"))
    ##if no ammo,switch the regular weapon
    if man.ammo<=0:
        man.weapon=reg_weapon
    ##showing blackhole animation:
    if blackhole_counter>0:
        blackhole_animation(constant_x,constant_y)
    collision()
    score()
    ammo()
    prize_down()
    draw_weapon()
    buy_heart = Button(buy_heart_img, 0, 100, 230, 64, click_bheart, 0, 60, give_heart)
    pygame.display.update()

##functions:
def drop_weapon(x,y):
    num=random.randint(0,40)
    if num==0 or num==5:
        new_weapon.append(projectiles(shotgun_weapon,7,x,y,98,22,"down"))
    if num==1 or num==7 or num==8:
        new_weapon.append(projectiles(bigbullet_weapon, 7, x, y, 100, 28, "down"))
    elif num == 2:
        new_weapon.append(projectiles(blackhole_weapon, 7, x, y, 100, 28, "down"))
    elif num == 3 or num==9:
        new_weapon.append(projectiles(lazer_weapon, 7, x, y, 120, 38, "down"))
    elif num == 4 or num==10 or num==11:
        new_weapon.append(projectiles(machinegun_weapon, 7, x, y, 100, 40, "down"))
##draw weapon:
def draw_weapon():
    window.blit(man.weapon,(0,60))

##black hole animation:
def blackhole_animation(x,y):
    global blackhole_counter
    if blackhole_counter < 90:
        window.blit(blackhole_img[blackhole_counter % 36], (x, y))
        blackhole_counter += 1

    if blackhole_counter>=90:
        blackhole_counter=0



##creating the meteor
def meteor_go(x,num):

     if num==1:
         if x>=0 and x<=420:
             y=-100
             meteor_new = projectiles(meteor_left, 5+(change_amount/4), x,y,60,56,"left")
             meteor_new.bh_pos_x = meteor_new.x
             meteor_new.bh_pos_y = meteor_new.y

             meteor_list.append(meteor_new)
             #meteor_move(meteor_new)


         elif x>=421 and x<=840:
             y =-100
             meteor_new = projectiles(meteor_right, 5+(change_amount/4), x,y,60,56,"right")
             meteor_new.bh_pos_x = meteor_new.x
             meteor_new.bh_pos_y = meteor_new.y

             meteor_list.append(meteor_new)
             #meteor_move(meteor_new)
     if num==2:
         y = -100
         meteor_new = projectiles(meteor_purple, 7+(change_amount/4), x, y, 60, 100,"down")
         meteor_new.bh_pos_x = meteor_new.x
         meteor_new.bh_pos_y = meteor_new.y

         meteor_list.append(meteor_new)
         #meteor_move(meteor_new)

##moving the meteor
def meteor_move(meteor):
    global blackhole_counter,constant_x,constant_y
    if meteor.y < 480:
        if blackhole_counter==0:

            meteor.y+=meteor.vel


            if meteor.image==meteor_left:
                 meteor.x+=meteor.vel
                 window.blit(meteor_left,(meteor.x,meteor.y))
                 meteor.bh_pos_x = meteor.x
                 meteor.bh_pos_y = meteor.y

            elif meteor.image==meteor_right:
                 meteor.x -= meteor.vel
                 window.blit(meteor_right, (meteor.x, meteor.y))
                 meteor.bh_pos_x = meteor.x
                 meteor.bh_pos_y = meteor.y

            elif meteor.image==meteor_purple:

                 window.blit(meteor_purple, (meteor.x, meteor.y))
                 meteor.bh_pos_x = meteor.x
                 meteor.bh_pos_y = meteor.y
        else:
            ##if the meteor is in the game,move it toward the black hole

                meteor.direction_x, meteor.direction_y = constant_x+150 - meteor.bh_pos_x, constant_y+150 - meteor.bh_pos_y
                distance = (meteor.direction_x ** 2 + meteor.direction_y ** 2) ** .5
                if distance != 0:
                    NORMALIZED_DISTANCE = 15
                    multiplier = NORMALIZED_DISTANCE / distance

                    meteor.direction_x *= multiplier
                    meteor.direction_y *= multiplier
                    meteor.x += round(meteor.direction_x)
                    meteor.y += round(meteor.direction_y)
                    window.blit(meteor.image, (meteor.x, meteor.y))



##creating the flame
def create_flame(pos_x):
    flame_new = projectiles(flame, 0, pos_x, 420, 60, 60,"none")
    flame_list.append(flame_new)
    draw_flame(flame_new)




##drawing the flame
def draw_flame(f):
        if f.flame_count+1<=56:

            window.blit(flame[f.flame_count % 4], (f.x, 420))

            f.flame_count += 1
        else:

            flame_list.pop(flame_list.index(f))


##creating the alien ship and alien bullet
def create_alien():

    num=random.randint(0,1)
    if num==0:
        alien = projectiles(alien_ship, 8, 0, random.randint(0, 220), 60, 60,"right")
        alien.bh_pos_x = alien.x
        alien.bh_pos_y = alien.y

    elif num==1:
        alien=projectiles(alien_ship,8,840,random.randint(0,220),60,60,"left")
        alien.bh_pos_x = alien.x
        alien.bh_pos_y = alien.y

    alien.count_bullet += 1
    alien_list.append(alien)
    bullet_new = bullets(round(alien.x + alien.hitbox_x // 2), round(alien.y + alien.hitbox_y // 2), alien_bullet, 8, man.x, man.y,  round(alien.x + alien.hitbox_x // 2), round(alien.y + alien.hitbox_y // 2),28,25)
    bullet_new.my_alien=alien_list.index(alien)
    alien_bullet_list.append(bullet_new)

    move_alien()


##moving the alien ship and alien bullets
def move_alien():
    global blackhole_counter

    for a in alien_list:
        if a.y<600:
            if blackhole_counter==0:
                if a.direction=="right":
                    a.x += a.vel
                    a.bh_pos_x = a.x

                elif a.direction=="left":
                    a.x -= a.vel
                    a.bh_pos_x = a.x
            ##move alien ship toward black hole
            else:
                a.direction_x, a.direction_y = constant_x + 150 - a.bh_pos_x, constant_y + 150 - a.bh_pos_y
                distance = (a.direction_x ** 2 + a.direction_y ** 2) ** .5
                if distance != 0:
                    NORMALIZED_DISTANCE = 15
                    multiplier = NORMALIZED_DISTANCE / distance

                    a.direction_x *= multiplier
                    a.direction_y *= multiplier
                    a.x += round(a.direction_x)
                    a.y += round(a.direction_y)
                    window.blit(a.image, (a.x, a.y))


            window.blit(a.image, (a.x, a.y))

    ##creating another bullet if no bullets on screen
        for a in alien_list:
            if a.count_bullet==0:
                if a.y<480:
                    bullet_new = bullets(round(a.x + a.hitbox_x // 2), round(a.y + a.hitbox_y // 2), alien_bullet, 8,
                                         man.x, man.y, round(a.x + a.hitbox_x // 2), round(a.y + a.hitbox_y // 2),28,25)

                    a.count_bullet+=1

                    alien_bullet_list.append(bullet_new)
    ##moving the alien bullet in player direction
    for a in alien_bullet_list:
      if a.y<480:
        if blackhole_counter==0:
            a.direction_x, a.direction_y = a.mouse_x - a.start_x, a.mouse_y - a.start_y
            distance = (a.direction_x ** 2 + a.direction_y ** 2) ** .5
            if distance != 0:
                NORMALIZED_DISTANCE = 15
                multiplier = NORMALIZED_DISTANCE / distance

                a.direction_x *= multiplier
                a.direction_y *= multiplier
                a.x += round(a.direction_x)
                a.y += round(a.direction_y)
                a.bh_pos_x = a.x
                a.bh_pos_y = a.y
                a.draw(window)

                alien_bullet_sound.play()
            ##move bullet toward black hole position
        else:
            a.direction_x, a.direction_y = constant_x + 150 - a.bh_pos_x, constant_y + 150 - a.bh_pos_y
            distance = (a.direction_x ** 2 + a.direction_y ** 2) ** .5
            if distance != 0:
                NORMALIZED_DISTANCE = 15
                multiplier = NORMALIZED_DISTANCE / distance

                a.direction_x *= multiplier
                a.direction_y *= multiplier
                a.x += round(a.direction_x)
                a.y += round(a.direction_y)
                window.blit(a.image, (a.x, a.y))

#man:
##pygame.draw.rect(window,red,(self.x+17,self.y+10,28,60),2)

#regular meteor:
##pygame.draw.rect(window,red,(meteor.x,meteor.y+6,60,56),2)

##purple meteor:
#pygame.draw.rect(window,red,(meteor.x,meteor.y+20,60,100),2)

##bullet:
#pygame.draw.rect(window, red, (self.x , self.y , self.hitbox_x, self.hitbox_y), 2)

#heart:
#pygame.draw.rect(window, red, (life.x-5, life.y-5 , 32, 30), 2)

#ammo:
#pygame.draw.rect(window, red, (ammo.x, ammo.y, 64, 64), 2)

#flame:
#pygame.draw.rect(window, red, (f.x, f.y ,60, 60), 2)

##checking for collisions
def collision():
    global heart_count,count_score,change_amount,constant_x,constant_y,blackhole_counter
    if heart_count>0:
        ##collision between player and regular meteor
        for meteor in meteor_list:
            if meteor.image!=meteor_purple:
                if man.y+10 < meteor.y+6 + meteor.hitbox_y and man.y+10 > meteor.y or man.y+10 + man.hitbox_y > meteor.y+6 and man.y+10 + man.hitbox_y < meteor.y+6 +meteor.hitbox_y:
                    if man.x+17 > meteor.x and man.x+17< meteor.x + meteor.hitbox_x or  man.x+17 + man.hitbox_x > meteor.x and man.x+17 + man.hitbox_x < meteor.x + meteor.hitbox_x:
                           heart_list.pop(heart_count-1)
                           heart_count -= 1
                           meteor_list.pop(meteor_list.index(meteor))
                           dmg_sound.play()

        ##collision between player and purple meteor
            elif meteor.image == meteor_purple:
                if man.y+10 < meteor.y+20 + meteor.hitbox_y and man.y+10 > meteor.y or man.y+10 + man.hitbox_y > meteor.y +20and man.y+10 + man.hitbox_y < meteor.y+20 +meteor.hitbox_y:
                    if man.x+17 > meteor.x and man.x+17< meteor.x + meteor.hitbox_x or  man.x+17 + man.hitbox_x > meteor.x and man.x+17 + man.hitbox_x < meteor.x + meteor.hitbox_x:
                           heart_list.pop(heart_count-1)
                           heart_count -= 1
                           meteor_list.pop(meteor_list.index(meteor))
                           dmg_sound.play()

            ##collision between bullet and regular meteor
        for meteor in meteor_list:
             for b in bullet_list:
                     if meteor.image != meteor_purple:
                        if b.y < meteor.y+6 + meteor.hitbox_y and b.y > meteor.y+6 or b.y + b.hitbox_y > meteor.y+6 and b.y + b.hitbox_y < meteor.y+6 +meteor.hitbox_y:
                            if b.x > meteor.x and b.x< meteor.x + meteor.hitbox_x or  b.x+ b.hitbox_x > meteor.x and b.x + b.hitbox_x < meteor.x + meteor.hitbox_x:
                                if meteor.y<480:
                                    if b.image==blackhole_bullet:
                                        blackhole_counter+=1
                                        constant_x=meteor.x
                                        constant_y=meteor.y
                                    ##create heart prize

                                    if random.randint(0,random_end * 4 - change_amount)==1:
                                        new_life.append(life(heart,meteor.x,meteor.y))
                                    ##create ammo prize

                                    if random.randint(0,random_end+35)==1:
                                        new_ammo.append(projectiles(reg_ammo,8,meteor.x,meteor.y,64,64,"down"))

                                    ##creating weapon prize
                                    if random.randint(0,3)==3:
                                        drop_weapon(meteor.x,meteor.y)
                                    if b.image!=lazer_bullet:
                                        bullet_list.pop(bullet_list.index(b))



                                    #meteor_list.pop(meteor_list.index(meteor))

                                    ##changing the height of the meteor to make him disapper without having a problem with the list.
                                    meteor.y=600

                                    bullethit_sound.play()
                                    count_score+=10
                                    ##increasing the difficulty of the game
                                    if count_score%50==0 and change_amount<16:
                                        change_amount+=2
                                    if count_score%50==0 and change_amount<21 and change_amount>=16:
                                        change_amount+=1
                                    if count_score%100==0 and change_amount<24 and change_amount>=21:
                                        change_amount+=1
                                    if count_score%250==0 and change_amount<29 and change_amount>=24:
                                        change_amount+=1




            ##collision between player bullet and purple meteor
                     elif meteor.image == meteor_purple:
                         if b.y  < meteor.y +20 + meteor.hitbox_y and b.y  > meteor.y +20 or b.y  + b.hitbox_y > meteor.y +20 and b.y  + b.hitbox_y < meteor.y +20 + meteor.hitbox_y:
                             if b.x  > meteor.x and b.x  < meteor.x + meteor.hitbox_x or b.x  + b.hitbox_x > meteor.x and b.x  + b.hitbox_x < meteor.x + meteor.hitbox_x:
                                 if meteor.y < 480:
                                     if b.image == blackhole_bullet:
                                         blackhole_counter += 1
                                         constant_x = meteor.x
                                         constant_y = meteor.y

                                     ##create heart prize
                                     if random.randint(0, random_end * 4 - change_amount) == 1:
                                         new_life.append(life(heart, meteor.x, meteor.y))
                                     ##create ammo prize

                                     if random.randint(0, random_end+35) == 1:
                                         new_ammo.append(projectiles(reg_ammo, 8, meteor.x, meteor.y, 64, 64, "down"))

                                     ##creating weapon prize
                                     if random.randint(0, 3) == 3:
                                         drop_weapon(meteor.x, meteor.y)

                                     if b.image != lazer_bullet:
                                         #bullet_list.pop(bullet_list.index(b))
                                         b.y=600
                                     #meteor_list.pop(meteor_list.index(meteor))
                                     meteor.y = 600
                                     bullethit_sound.play()
                                     count_score += 10

                                     ##increasing the difficulty of the game
                                     if count_score % 50 == 0 and change_amount < 16:
                                         change_amount += 2
                                     if count_score % 50 == 0 and change_amount < 21 and change_amount >= 16:
                                         change_amount += 1
                                     if count_score % 100 == 0 and change_amount < 24 and change_amount >= 21:
                                         change_amount += 1
                                     if count_score % 250 == 0 and change_amount < 29 and change_amount >= 24:
                                         change_amount += 1



        ##collision between player bullet and alien ship
        for b in bullet_list:
            for a in alien_list:
                    if b.y  < a.y + a.hitbox_y and b.y  > a.y  or b.y  + b.hitbox_y > a.y  and b.y  + b.hitbox_y < a.y  + a.hitbox_y:
                        if b.x  > a.x and b.x  < a.x + a.hitbox_x or b.x  + b.hitbox_x > a.x and b.x  + b.hitbox_x < a.x + a.hitbox_x:
                                #bullet_list.pop(bullet_list.index(b))
                                if a.y<480:
                                    b.y=600
                                    if b.image == blackhole_bullet:
                                        blackhole_counter += 1
                                        constant_x = a.x
                                        constant_y = a.y
                                    a.count_hit+=1
                                    if a.count_hit==3:
                                        new_life.append(life(heart, a.x, a.y))
                                        #alien_list.pop(alien_list.index(a))
                                        a.y=600
                                        bullethit_sound.play()
                                        count_score+=50
                                        ##adding ammo for destroying the ship:
                                        if man.weapon != reg_weapon and man.weapon!=blackhole_weapon:
                                            man.ammo += 15


        

        ##collision between life prize and player
        if len(new_life)>0:
            for h in new_life:
                if man.y+10 < h.y-5 + h.hitbox_y and man.y+10 > h.y-5 or man.y+10 + man.hitbox_y > h.y-5 and man.y+10 + man.hitbox_y < h.y-5 +h.hitbox_y:
                    if man.x+17 > h.x-5 and man.x+17< h.x-5 + h.hitbox_x or  man.x+17 + man.hitbox_x > h.x-5 and man.x+17 + man.hitbox_x < h.x-5 + h.hitbox_x:
                          h.x=heart_list[len(heart_list)-1].x+30
                          h.y=0
                          heart_list.append(h)
                          heart_count+=1
                          new_life.pop(new_life.index(h))
                          heart_sound.play()
        ##collision between ammo prize and player
        if len(new_ammo)>0:
            for a in new_ammo:
                if man.y+10 < a.y + a.hitbox_y and man.y+10 > a.y or man.y+10 + man.hitbox_y > a.y and man.y+10 + man.hitbox_y < a.y +a.hitbox_y:
                    if man.x+17 > a.x and man.x+17< a.x + a.hitbox_x or  man.x+17 + man.hitbox_x > a.x and man.x+17 + man.hitbox_x < a.x + a.hitbox_x:
                          if man.weapon!=blackhole_weapon:
                                man.ammo+=10
                          if man.weapon==blackhole_weapon:
                                man.ammo+=1
                          new_ammo.pop(new_ammo.index(a))
                          heart_sound.play()

        ##collision between weapon prize and player
        if len(new_weapon)>0:
            for w in new_weapon:
                if man.y+10 < w.y + w.hitbox_y and man.y+10 > w.y or man.y+10 + man.hitbox_y > w.y and man.y+10 + man.hitbox_y < w.y +w.hitbox_y:
                    if man.x+17 > w.x and man.x+17< w.x + w.hitbox_x or  man.x+17 + man.hitbox_x > w.x and man.x+17 + man.hitbox_x < w.x + w.hitbox_x:
                          if man.weapon==w.image:
                              man.ammo+=5
                          elif man.weapon!=w.image:
                              man.weapon=w.image
                              if man.weapon==bigbullet_weapon:
                                  man.ammo=30
                              elif man.weapon==machinegun_weapon:
                                  man.ammo=30
                              elif man.weapon==lazer_weapon:
                                  man.ammo=25
                              elif man.weapon==shotgun_weapon:
                                  man.ammo=35
                              elif man.weapon==blackhole_weapon:
                                  man.ammo=1
                          new_weapon.pop(new_weapon.index(w))
                          heart_sound.play()

        ##collision between player and flame
        if len(flame_list)>0:
            for f in flame_list:
                if man.y+10 < f.y + f.hitbox_y and man.y+10 > f.y or man.y+10 + man.hitbox_y > f.y and man.y+10 + man.hitbox_y < f.y + f.hitbox_y:
                    if man.x+17 > f.x and man.x+17 < f.x + f.hitbox_x or man.x+17 + man.hitbox_x > f.x and man.x+17 + man.hitbox_x < f.x + f.hitbox_x:
                        heart_list.pop(heart_count - 1)
                        heart_count -= 1
                        flame_list.pop(flame_list.index(f))
                        dmg_sound.play()
        ##collision between player and alien bullet
        for a in alien_bullet_list:
            if man.y+10 < a.y + a.hitbox_y and man.y+10 > a.y or man.y+10 + man.hitbox_y > a.y and man.y+10 + man.hitbox_y < a.y + a.hitbox_y:
                if man.x+17 > a.x and man.x+17 < a.x + a.hitbox_x or man.x+17 + man.hitbox_x > a.x and man.x+17 + man.hitbox_x < a.x + a.hitbox_x:
                    heart_list.pop(heart_count - 1)
                    heart_count -= 1
                    #alien_bullet_list.pop(alien_bullet_list.index(a))
                    a.y=600
                    dmg_sound.play()



##creating a bullet
def bullet_create(pos_x,pos_y):
     global constant_distance
     ##creating regular bullet
     if man.weapon==reg_weapon:
        bullet_new=bullets(round(man.x+man.width//2),round(man.y+man.height//2),reg_bullet,5,pos_x,pos_y,round(man.x+man.width//2),round(man.y+man.height//2),20,20)
        bullet_list.append(bullet_new)
     ##creating big bullet
     elif man.weapon==bigbullet_weapon:
         bullet_new = bullets(round(man.x + man.width // 2), round(man.y + man.height // 2),big_bullet, 12, pos_x, pos_y,round(man.x + man.width // 2), round(man.y + man.height // 2),34,34)
         man.ammo -= 1
         bullet_list.append(bullet_new)
     ##creating machine gun bullet
     elif man.weapon==machinegun_weapon:
         bullet_new = bullets(round(man.x + man.width // 2), round(man.y + man.height // 2),machinegun_bullet, 4, pos_x, pos_y,round(man.x + man.width // 2), round(man.y + man.height // 2),18,16)
         man.ammo -= 1
         bullet_list.append(bullet_new)
     ##creating lazer bullet
     elif man.weapon == lazer_weapon:
         bullet_new = bullets(round(man.x + man.width // 2), round(man.y + man.height // 2), lazer_bullet, 4,
                              pos_x, pos_y, round(man.x + man.width // 2), round(man.y + man.height // 2), 15, 63)
         man.ammo -= 1
         bullet_list.append(bullet_new)
     ##creating shotgun bullets
     elif man.weapon==shotgun_weapon:
         bullet_new1 = bullets(round(man.x + man.width // 2), round(man.y + man.height // 2), shotgun_bullet, 4,
                              pos_x, pos_y, round(man.x + man.width // 2), round(man.y + man.height // 2), 24, 13)
         bullet_new2 = bullets(round(man.x + man.width // 2), round(man.y + man.height // 2), shotgun_bullet, 4,
                              pos_x, pos_y, round(man.x + man.width // 2), round(man.y + man.height // 2), 24, 13)
         bullet_new3 = bullets(round(man.x + man.width // 2), round(man.y + man.height // 2), shotgun_bullet, 4,
                              pos_x, pos_y, round(man.x + man.width // 2), round(man.y + man.height // 2), 24, 13)
         bullet_new4 = bullets(round(man.x + man.width // 2), round(man.y + man.height // 2), shotgun_bullet, 4,
                               pos_x, pos_y, round(man.x + man.width // 2), round(man.y + man.height // 2), 24, 13)
         bullet_new5 = bullets(round(man.x + man.width // 2), round(man.y + man.height // 2), shotgun_bullet, 4,
                               pos_x, pos_y, round(man.x + man.width // 2), round(man.y + man.height // 2), 24, 13)

         bullet_new1.IsShotGun_main=True
         bullet_new1.direction_x, bullet_new1.direction_y = bullet_new1.mouse_x - bullet_new1.start_x, bullet_new1.mouse_y - bullet_new1.start_y
         angle = math.degrees(math.atan2(bullet_new1.direction_y, bullet_new1.direction_x))

         bullet_new1.angle=angle
         bullet_new2.angle=angle + 45
         bullet_new3.angle=angle - 45
         bullet_new4.angle=angle + 22.5
         bullet_new5.angle=angle - 22.5

         bullet_new1.distance = (bullet_new1.direction_x ** 2 + bullet_new1.direction_y ** 2) ** .5

         shotgun_create(bullet_new2,bullet_new1.distance)
         shotgun_create(bullet_new3, bullet_new1.distance)
         shotgun_create(bullet_new4, bullet_new1.distance)
         shotgun_create(bullet_new5, bullet_new1.distance)
         constant_distance=bullet_new1.distance

         bullet_list.append(bullet_new1)
         bullet_list.append(bullet_new2)
         bullet_list.append(bullet_new3)
         bullet_list.append(bullet_new4)
         bullet_list.append(bullet_new5)



         #bullet_new1.ShotGunList.append(bullet_new2)
         #bullet_new1.ShotGunList.append(bullet_new3)
         #bullet_new1.ShotGunList.append(bullet_new4)
         #bullet_new1.ShotGunList.append(bullet_new5)
         #bullet_new1.IsShotGun=True
         #bullet_list.append(bullet_new1)

         man.ammo -= 5

     ##creating black hole bullet
     elif man.weapon == blackhole_weapon:
         bullet_new = bullets(round(man.x + man.width // 2), round(man.y + man.height // 2), blackhole_bullet, 4,
                              pos_x, pos_y, round(man.x + man.width // 2), round(man.y + man.height // 2), 39, 37)
         man.ammo -= 1
         bullet_list.append(bullet_new)





     bullet_move()

##moving a bullet
def bullet_move():
        global constant_distance
        for bullet in bullet_list:
            if bullet.y<600:
                ##moving the player big bullet in mouse direction
                if bullet.image==big_bullet:
                    bullet.direction_x, bullet.direction_y = bullet.mouse_x - bullet.start_x, bullet.mouse_y - bullet.start_y
                    distance = (bullet.direction_x ** 2 + bullet.direction_y ** 2) ** .5
                    if distance!=0:
                        NORMALIZED_DISTANCE = 15
                        multiplier = NORMALIZED_DISTANCE / distance

                        bullet.direction_x *= multiplier
                        bullet.direction_y *= multiplier
                        bullet.x+=round(bullet.direction_x)
                        bullet.y+=round(bullet.direction_y)
                        bullet.draw(window)

                ##moving the player regular bullet in mouse direction
                elif bullet.image==reg_bullet:
                    bullet.direction_x, bullet.direction_y = bullet.mouse_x - bullet.start_x, bullet.mouse_y - bullet.start_y
                    distance = (bullet.direction_x ** 2 + bullet.direction_y ** 2) ** .5
                    if distance != 0:
                        NORMALIZED_DISTANCE = 10
                        multiplier = NORMALIZED_DISTANCE / distance

                        bullet.direction_x *= multiplier
                        bullet.direction_y *= multiplier
                        bullet.x += round(bullet.direction_x)
                        bullet.y += round(bullet.direction_y)
                        bullet.draw(window)

                ##moving the player machine gun bullet in mouse direction
                elif bullet.image==machinegun_bullet:
                    bullet.direction_x, bullet.direction_y = bullet.mouse_x - bullet.start_x, bullet.mouse_y - bullet.start_y
                    distance = (bullet.direction_x ** 2 + bullet.direction_y ** 2) ** .5
                    if distance != 0:
                        NORMALIZED_DISTANCE = 20
                        multiplier = NORMALIZED_DISTANCE / distance

                        bullet.direction_x *= multiplier
                        bullet.direction_y *= multiplier
                        bullet.x += round(bullet.direction_x)
                        bullet.y += round(bullet.direction_y)
                        bullet.draw(window)

                ##moving the player lazer bullet in mouse direction
                elif bullet.image==lazer_bullet:
                    bullet.direction_x, bullet.direction_y = bullet.mouse_x - bullet.start_x, bullet.mouse_y - bullet.start_y
                    angle = math.degrees(math.atan2(bullet.direction_y, bullet.direction_x))
                    rotimage = pygame.transform.rotate(bullet.image, -angle)
                    distance = (bullet.direction_x ** 2 + bullet.direction_y ** 2) ** .5
                    if distance != 0:
                        NORMALIZED_DISTANCE = 15
                        multiplier = NORMALIZED_DISTANCE / distance

                        bullet.direction_x *= multiplier
                        bullet.direction_y *= multiplier
                        bullet.x += round(bullet.direction_x)
                        bullet.y += round(bullet.direction_y)
                        rect = rotimage.get_rect(center=(bullet.x, bullet.y))
                        bullet.draw_rotate(window, rotimage, rect)



                ##moving shotgon bullets towards mouse position:
                elif bullet.image==shotgun_bullet:

                    if bullet.IsShotGun_main:
                        bullet.direction_x, bullet.direction_y = bullet.mouse_x - bullet.start_x, bullet.mouse_y - bullet.start_y
                        #angle = math.degrees(math.atan2(bullet.direction_y, bullet.direction_x))
                        bullet.distance=(bullet.direction_x ** 2 + bullet.direction_y ** 2) ** .5
                        constant_distance=bullet.distance

                    elif not bullet.IsShotGun_main:
                        shotgun_create(bullet,constant_distance)
                    rotimage_main = pygame.transform.rotate(bullet.image, -bullet.angle)
                    if bullet.distance != 0:
                        NORMALIZED_DISTANCE = 15
                        multiplier = NORMALIZED_DISTANCE / bullet.distance

                        bullet.direction_x *= multiplier
                        bullet.direction_y *= multiplier
                        bullet.x += round(bullet.direction_x)
                        bullet.y += round(bullet.direction_y)
                        rect = rotimage_main.get_rect(center=(bullet.x, bullet.y))
                        bullet.draw_rotate(window, rotimage_main, rect)
                ##moving black hole bullet toward mouse position:
                elif bullet.image==blackhole_bullet:
                    bullet.direction_x, bullet.direction_y = bullet.mouse_x - bullet.start_x, bullet.mouse_y - bullet.start_y
                    distance = (bullet.direction_x ** 2 + bullet.direction_y ** 2) ** .5
                    if distance != 0:
                        NORMALIZED_DISTANCE = 8
                        multiplier = NORMALIZED_DISTANCE / distance

                        bullet.direction_x *= multiplier
                        bullet.direction_y *= multiplier
                        bullet.x += round(bullet.direction_x)
                        bullet.y += round(bullet.direction_y)
                        bullet.draw(window)








##shotgun function
def shotgun_create(bullet,distance):
    radian1 = math.radians(bullet.angle)
    bullet.direction_x = distance * math.cos(radian1)
    bullet.direction_y = distance * math.sin(radian1)

    bullet.distance = (bullet.direction_x ** 2 + bullet.direction_y ** 2) ** .5


##showing score
def score():
    global count_score
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score:" + str(count_score)+"  Name: "+str(man.name), True, red)
    window.blit(text, (640, 0))

##showing ammo count
def ammo():
    if man.weapon!=reg_weapon:
        font = pygame.font.SysFont(None, 25)
        text = font.render("Ammo:" + str(man.ammo), True, red)
    elif man.weapon==reg_weapon:
        font = pygame.font.SysFont(None, 25)
        text = font.render("Ammo:", True, red)
        window.blit(infinity_img,(70,25))
    window.blit(text, (0, 30))


##moving prizes down
def prize_down():
    ##dropping life prize
    if len(new_life)>0:
        for life in new_life:
            if life.y<480:
                life.y+=7
                window.blit(life.image,(life.x,life.y))


            else:
                new_life.pop(new_life.index(life))
    ##dropping ammo prize
    if len(new_ammo)>0:
        for ammo in new_ammo:
            if ammo.y < 480:
                ammo.y += 7
                window.blit(ammo.image, (ammo.x, ammo.y))


            else:
                new_ammo.pop(new_ammo.index(ammo))
    ##dropping ammo prize
    if len(new_weapon)>0:
        for weapon in new_weapon:
            if weapon.y < 480:
                weapon.y += 7
                window.blit(weapon.image, (weapon.x, weapon.y))


            else:
                new_weapon.pop(new_weapon.index(weapon))

##creating heart for 100 ammo
def give_heart():
    global heart_count
    heart_list.append(life(heart,heart_list[len(heart_list) - 1].x + 30,0))
    heart_count += 1
    man.ammo-=100




##main menu :
def main_menu():
     pygame.mixer_music.play(-1)
     global menu, mainloop,clicked,text_loop


     while menu:
        clock.tick(37)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop=False
                menu = False
                clicked=True

        global counter_image
        window.blit(bg_menu[counter_image], (0, 0))
        counter_image += 1
        if counter_image == 148:
            counter_image = 0
        start_button = Button(start_img, 840/2-120, 480/2-40, 230, 64, click_start, 840/2-120, 480/2-40, enter_name)
        ##showing high score
        font = pygame.font.SysFont(None, 30)
        text = font.render("High score: " + str(high_score)+
                           " Name: "+str(hs_name), True, red)
        window.blit(text, (840/2-140, 30))
        pygame.display.update()
        #menu_music.play()



##entering a name
def enter_name():
    global menu, mainloop, clicked,text_loop

    name_text = TextInput()
    while text_loop:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                text_loop=False
                mainloop = False
                menu = False
                clicked = True

        global counter_image
        window.blit(bg_menu[counter_image], (0, 0))
        counter_image += 1
        if counter_image == 148:
            counter_image = 0

        # Blit its surface onto the screen
        window.blit(name_img,(840/2-180,480/2-100))
        window.blit(name_text.get_surface(), (840/2-160, 480/2))
        if name_text.update(events):
            man.name=name_text.get_text()
            main_game()
        pygame.display.update()
        clock.tick(30)
        #menu_music.play()

##main game:
def main_game():
    global menu,mainloop,clicked,heart_count,meteor_list,heart1,heart2,heart3,heart_list,new_life,bullet_list,change_amount,\
        flame_list,alien_list,alien_bullet_list,count_step,count_score,new_ammo,text_loop,high_score,hs_name,is_pause,blackhole_counter, \
        constant_x,constant_y
    ##variables are here as well for restarting the game
    start_time=time.time()
    mainloop=True
    heart_count = 3
    meteor_list = []
    heart1 = life(heart, 0, 0)
    heart2 = life(heart, 30, 0)
    heart3 = life(heart, 60, 0)
    heart_list = [heart1, heart2, heart3]
    new_life = []
    bullet_list = []
    change_amount = 0
    flame_list = []
    alien_list = []
    alien_bullet_list = []
    count_step = 0
    count_score = 0
    new_ammo = []
    man.ammo=25
    menu_music.stop()
    while mainloop:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                text_loop=False
                mainloop=False
                menu=False
                clicked=True
                ##mouse clicked for bullet
            if event.type == pygame.MOUSEBUTTONUP:
                is_pause = False
                pos_x,pos_y = pygame.mouse.get_pos()
                bullet_sound.play()
                bullet_create(pos_x,pos_y)
        #if no hearts left
        if heart_count==0:
            window.blit(bg, (0, 0))
            window.blit(game_over,(840/4,480/4))
            pygame.display.update()
            if count_score>high_score:
                high_score=count_score
                hs_name=man.name
            d = shelve.open('hs_meteor.txt')  # here you will save the score variable
            d['score'] = high_score  # thats all, now it is saved on disk.
            d['name'] = hs_name
            d.close()
            pygame.mixer.stop()
            gameover_sound.play()
            time.sleep(3)
            mainloop=False
            text_loop=False

            
        ##key pressing
        keys=pygame.key.get_pressed()

        if keys[pygame.K_a] and man.x>0:
             is_pause = False
             man.x-=man.vel
             man.left=True
             man.right=False
        elif keys[pygame.K_d] and man.x<780:

            is_pause = False
            man.x+=man.vel
            man.right = True
            man.left = False
        else:
            man.right = False
            man.left = False
            man.walkCount=0
        if man.is_jump==0:
            if keys[pygame.K_SPACE]:
                is_pause = False
                man.right = False
                man.left = False
                man.walkCount=0
                man.is_jump=1
        ##jumping
        if man.is_jump==1:
            if man.jumpCount>=-10:
                neg=1


                if man.jumpCount<0:
                    neg=-1
                man.y-=(man.jumpCount**2)*0.4*neg
                man.jumpCount-=1
            else:
                man.is_jump=0
                man.jumpCount=10

        ##pausing game
        if keys[pygame.K_ESCAPE]:
            is_pause=True
            font = pygame.font.SysFont(None, 30)
            text = font.render("Game Paused! Enter Any Game Key To Continue:", True, red)
            window.blit(text, (840 / 2 - 200, 420/2))
            pygame.display.update()





        if not is_pause:
            refresh_game()


        
main_menu()
if not clicked:
    main_game()
pygame.quit()







