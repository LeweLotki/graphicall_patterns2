import numpy as np
import cv2

fill_cord = 35
circle_cord = fill_cord + 100
line_cord = circle_cord + 100
paint_cord = line_cord + 100
pencil_cord = paint_cord + 100
rubber_cord = pencil_cord + 100
square_cord = rubber_cord + 100
size = (60,60)
size_brush = (20,20)


fill = cv2.resize(cv2.imread(r'images\icons\ronded\cfill.png'),size)
circle = cv2.resize(cv2.imread(r'images\icons\ronded\ccircle.png'),size)
line = cv2.resize(cv2.imread(r'images\icons\ronded\cline.png'),size)
paint = cv2.resize(cv2.imread(r'images\icons\ronded\cpaint.png'),size)
pencil = cv2.resize(cv2.imread(r'images\icons\ronded\cpencil.png'),size)
rubber = cv2.resize(cv2.imread(r'images\icons\ronded\crubber.png'),size)
square = cv2.resize(cv2.imread(r'images\icons\ronded\csquare.png'),size)

fill_shaded = cv2.resize(cv2.imread(r'images\icons\shaded\sfill.png'),size)
circle_shaded = cv2.resize(cv2.imread(r'images\icons\shaded\scircle.png'),size) 
line_shaded = cv2.resize(cv2.imread(r'images\icons\shaded\sline.png'),size) 
paint_shaded = cv2.resize(cv2.imread(r'images\icons\shaded\spaint.png'),size) 
pencil_shaded = cv2.resize(cv2.imread(r'images\icons\shaded\spencil.png'),size)
rubber_shaded = cv2.resize(cv2.imread(r'images\icons\shaded\srubber.png'),size) 
square_shaded = cv2.resize(cv2.imread(r'images\icons\shaded\ssquare.png'),size) 

ths = cv2.resize(cv2.imread(r'images\icons\ths.png'),size_brush)
thn = cv2.resize(cv2.imread(r'images\icons\thn.png'),size_brush)
thb = cv2.resize(cv2.imread(r'images\icons\thb.png'),size_brush)

ths_shaded = cv2.resize(cv2.imread(r'images\icons\ths_shaded.png'),size_brush)
thn_shaded = cv2.resize(cv2.imread(r'images\icons\thn_shaded.png'),size_brush)
thb_shaded = cv2.resize(cv2.imread(r'images\icons\thb_shaded.png'),size_brush)

ths_cord = line_cord + 20
thn_cord = paint_cord + 20
thb_cord = pencil_cord + 20

list_icon = [[fill,fill_cord], [circle, circle_cord] ,[line, line_cord] , [paint, paint_cord], [pencil, pencil_cord], [rubber, rubber_cord], [square, square_cord]]
list_brush = [[ths,ths_cord],[thn, thn_cord],[thb, thb_cord]]