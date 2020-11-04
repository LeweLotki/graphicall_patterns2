import numpy as np
import cv2
import math
from packages import images2 as im
from packages import drawing as dw

ix = -1
iy = -1
drawing = False
img = cv2.imread(r'images\wood.png')
thickness_tool = 2
jx, jy = [0,0]
right_clicked = False

part_one = True

def rotatePoint(centerPoint,point,angle):
    angle = math.radians(angle)
    temp_point = point[0]-centerPoint[0] , point[1]-centerPoint[1]
    temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
    return temp_point
    
def mandala(event, x, y, flags, param): 
      
    global ix, iy, drawing, img, thickness_tool, jx, jy, right_clicked

    
    cv2.circle(img, (90,im.fill_cord+30), 42, (215,215,215), -1)
    img[im.fill_cord:im.fill_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.fill_shaded    
         
    if event == cv2.EVENT_RBUTTONDOWN: 
        right_clicked = True
        jx = x 
        jy = y                 
    
    elif event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True
        ix = x 
        iy = y             
        if x > 70 and x < 140: 
            cv2.setMouseCallback("image", activate)      
     
    
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing == True:
            if not right_clicked:
                # print(ix,iy)
                if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900 :
                    n = 8
                    i = n
                    while i > 0:               
                        new_point = rotatePoint((575,375),(x,y),(n-i)*(360/n))
                        if int(new_point[1]) > 50 and int(new_point[1]) < 700 and int(new_point[0]) > 250 and int(new_point[0]) < 900 :
                            img[int(new_point[1]):int(new_point[1]) + thickness_tool, int(new_point[0]):int(new_point[0]) + thickness_tool, : ] = (0,0,0)
                        i -= 1
            else:
                if jy > 50 and jy < 700 and jx > 250 and jx < 900 and y > 50 and y < 700 and x > 250 and x < 900 :
                    n = 8
                    i = n
                    while i > 0:               
                        new_point = rotatePoint((jx,jy),(x,y),(n-i)*(360/n))
                        if int(new_point[1]) > 50 and int(new_point[1]) < 700 and int(new_point[0]) > 250 and int(new_point[0]) < 900 :
                            img[int(new_point[1]):int(new_point[1]) + thickness_tool, int(new_point[0]):int(new_point[0]) + thickness_tool, : ] = (0,0,0)
                        i -= 1
                
            # if x > 70 and x < 140: 
                # cv2.setMouseCallback("image", activate)
    
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        if not right_clicked:
            if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900:
                    n = 8
                    i = n
                    while i > 0:               
                        new_point = rotatePoint((575,375),(x,y),(n-i)*(360/n))
                        if int(new_point[1]) > 50 and int(new_point[1]) < 700 and int(new_point[0]) > 250 and int(new_point[0]) < 900 :
                            img[int(new_point[1]):int(new_point[1]) + thickness_tool, int(new_point[0]):int(new_point[0]) + thickness_tool, : ] = (0,0,0)
                        i -= 1
            else:
                if jy > 50 and jy < 700 and jx > 250 and jx < 900 and y > 50 and y < 700 and x > 250 and x < 900 :
                    n = 8
                    i = n
                    while i > 0:               
                        new_point = rotatePoint((jx,jy),(x,y),(n-i)*(360/n))
                        if int(new_point[1]) > 50 and int(new_point[1]) < 700 and int(new_point[0]) > 250 and int(new_point[0]) < 900 :
                            img[int(new_point[1]):int(new_point[1]) + thickness_tool, int(new_point[0]):int(new_point[0]) + thickness_tool, : ] = (0,0,0)
                        i -= 1
        # if x > 70 and x < 140: 
            # cv2.setMouseCallback("image", activate)

def draw_rectangle(event, x, y, flags, param): 
      
    global ix, iy, drawing, img 
      
    cv2.circle(img, (90,im.square_cord+30), 42, (215,215,215), -1)
    img[im.square_cord:im.square_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.square_shaded    
      
    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True
        ix = x 
        iy = y             
        if x > 70 and x < 140: 
            cv2.setMouseCallback("image", activate)      
    
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing == True:
            # print(ix,iy)
            if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900 :
                cv2.rectangle(img, pt1 =(ix, iy), pt2 =(x, y),  color =(0, 0, 0), thickness = -1) 
            # if x > 70 and x < 140: 
                # cv2.setMouseCallback("image", activate)
    
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900:
            cv2.rectangle(img, pt1 =(ix, iy), pt2 =(x, y), color =(0, 0, 0), thickness =-1) 
        # if x > 70 and x < 140: 
            # cv2.setMouseCallback("image", activate)

def rubber(event, x, y, flags, param): 
      
    global ix, iy, drawing, img 
      
    cv2.circle(img, (90,im.rubber_cord+30), 42, (215,215,215), -1)
    img[im.rubber_cord:im.rubber_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.rubber_shaded  
      
    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True
        ix = x 
        iy = y             
        if x > 70 and x < 140: 
            cv2.setMouseCallback("image", activate)    
            
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing == True:
            # print(ix,iy)
            if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900 :
                cv2.rectangle(img, pt1 =(ix, iy), pt2 =(x, y),  color =(255, 255, 255), thickness = -1) 
      
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900:
            cv2.rectangle(img, pt1 =(ix, iy), pt2 =(x, y), color =(255, 255, 255), thickness =-1) 

def pencil(event, x, y, flags, param): 
      
    global ix, iy, drawing, img, thickness_tool
    
    cv2.circle(img, (90,im.pencil_cord+30), 42, (215,215,215), -1)
    img[im.pencil_cord:im.pencil_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.pencil_shaded
      
    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True
        ix = x 
        iy = y             
        if x > 70 and x < 140: 
            cv2.setMouseCallback("image", activate) 
            
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing == True:
            # print(ix,iy)
            if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900 :
                img[y:y+5,x:x+5,:] = (0,0,0)
      
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900:
            img[y:y+thickness_tool,x:x+thickness_tool,:] = (0,0,0)

def circle(event, x, y, flags, param): 
      
    global ix, iy, drawing, img, thickness_tool
    
    cv2.circle(img, (90,im.circle_cord+30), 42, (215,215,215), -1)
    img[im.circle_cord:im.circle_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.circle_shaded
    
    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True
        ix = x 
        iy = y             
        if x > 70 and x < 140: 
            cv2.setMouseCallback("image", activate) 
            
    # elif event == cv2.EVENT_MOUSEMOVE: 
        # if drawing == True:
            # # print(ix,iy)
            # if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900 :
                # cv2.circle(img, (int((ix+x)/2), int((iy+y)/2)),int(math.sqrt( ((ix-x)**2)+((iy-y)**2) )),(0,0,0),-1)
      
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        radius = int(math.sqrt( ((ix-x)**2)+((iy-y)**2) ))
        if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900 and iy + radius > 50 and iy + radius < 700 and ix + radius > 250 and ix + radius < 900 :
            cv2.circle(img, (int((ix+x)/2), int((iy+y)/2)),radius,(0,0,0),thickness_tool)

def line(event, x, y, flags, param): 
      
    global ix, iy, drawing, img, thickness_tool
    
    cv2.circle(img, (90,im.line_cord+30), 42, (215,215,215), -1)
    img[im.line_cord:im.line_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.line_shaded
    
    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True
        ix = x 
        iy = y             
        if x > 70 and x < 140: 
            cv2.setMouseCallback("image", activate) 
            
    # elif event == cv2.EVENT_MOUSEMOVE: 
        # if drawing == True:
            # # print(ix,iy)
            # if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900 :
                # cv2.line(img,(ix,iy),(x,y),(0,0,0),2)
      
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900:
            cv2.line(img,(ix,iy),(x,y),(0,0,0),thickness_tool)

def plume(event, x, y, flags, param): 
      
    global ix, iy, drawing, img 
    
    cv2.circle(img, (90,im.plume_cord+30), 42, (215,215,215), -1)
    img[im.plume_cord:im.plume_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.plume_shaded    
      
    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True
        ix = x 
        iy = y             
        if x > 70 and x < 140: 
            cv2.setMouseCallback("image", activate) 
            
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing == True:
            # print(ix,iy)
            if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900 :
                cv2.line(img,(ix,iy),(x,y),(0,0,0),2)
      
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900:
            cv2.line(img,(ix,iy),(x,y),(0,0,0),2)
            
def activate(event, x, y, flags, param):   
    
    global part_one, thickness_tool
    
    for val in im.list_icon:
        cv2.circle(img, (90,val[1]+30), 42, (255,255,255), -1)
        img[val[1]:val[1]+im.size[0], im.size[0]:2*im.size[0], :] = val[0]
    
    if event == cv2.EVENT_LBUTTONDOWN and y > im.square_cord and y < im.square_cord+70 and x > 70 and x < 140: 
        cv2.setMouseCallback("image", draw_rectangle)
        
    if event == cv2.EVENT_LBUTTONDOWN and y > im.rubber_cord and y < im.rubber_cord+70 and x > 70 and x < 140:
        cv2.setMouseCallback("image", rubber)
    
    if event == cv2.EVENT_LBUTTONDOWN and y > im.pencil_cord and y < im.pencil_cord+70 and x > 70 and x < 140:
        cv2.setMouseCallback("image", pencil)  
    
    if event == cv2.EVENT_LBUTTONDOWN and y > im.circle_cord and y < im.circle_cord+70 and x > 70 and x < 140:
        cv2.setMouseCallback("image", circle)  
        
    if event == cv2.EVENT_LBUTTONDOWN and y > im.line_cord and y < im.line_cord+70 and x > 70 and x < 140:
        cv2.setMouseCallback("image", line)  

    if event == cv2.EVENT_LBUTTONDOWN and y > im.fill_cord and y < im.fill_cord+70 and x > 70 and x < 140:
        cv2.setMouseCallback("image", mandala) 
        
    if event == cv2.EVENT_LBUTTONDOWN and y > im.paint_cord and y < im.paint_cord+70 and x > 70 and x < 140:
        cv2.circle(img, (90,im.paint_cord+30), 42, (215,215,215), -1)
        img[im.paint_cord:im.paint_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.paint_shaded
        part_one = False
        
    if event == cv2.EVENT_LBUTTONDOWN and y > im.ths_cord and y < im.ths_cord+20 and x > 180 and x < 200:
        for val in im.list_brush:
            cv2.circle(img, (190,val[1]+10), 22, (255,255,255), -1)
            img[val[1]:val[1]+im.size_brush[0], 180:200, :] = val[0]
        cv2.circle(img, (190,im.ths_cord + 10), 22, (215,215,215), -1)
        img[im.ths_cord:im.ths_cord+im.size_brush[0], 180:200, :] = im.ths_shaded
        thickness_tool = 2
        
    if event == cv2.EVENT_LBUTTONDOWN and y > im.thn_cord and y < im.thn_cord+20 and x > 180 and x < 200:
        for val in im.list_brush:
            cv2.circle(img, (190,val[1]+10), 22, (255,255,255), -1)
            img[val[1]:val[1]+im.size_brush[0], 180:200, :] = val[0]
        cv2.circle(img, (190,im.thn_cord + 10), 22, (215,215,215), -1)
        img[im.thn_cord:im.thn_cord+im.size_brush[0], 180:200, :] = im.thn_shaded
        thickness_tool = 5    
        
    if event == cv2.EVENT_LBUTTONDOWN and y > im.thb_cord and y < im.thb_cord+20 and x > 180 and x < 200:
        for val in im.list_brush:
            cv2.circle(img, (190,val[1]+10), 22, (255,255,255), -1)
            img[val[1]:val[1]+im.size_brush[0], 180:200, :] = val[0]
        cv2.circle(img, (190,im.thb_cord + 10), 22, (215,215,215), -1)
        img[im.thb_cord:im.thb_cord+im.size_brush[0], 180:200, :] = im.thb_shaded
        thickness_tool = 10  
           
img[50:700,250:900,:] = (255, 255, 255)
# print(np.shape(img), np.shape(im.fill))
for val in im.list_icon:
    cv2.circle(img, (90,val[1]+30), 42, (255,255,255), -1)
    img[val[1]:val[1]+im.size[0], im.size[0]:2*im.size[0], :] = val[0]
for val in im.list_brush:
    cv2.circle(img, (190,val[1]+10), 22, (255,255,255), -1)
    img[val[1]:val[1]+im.size_brush[0], 180:200, :] = val[0]
cv2.circle(img, (190,im.ths_cord + 10), 22, (215,215,215), -1)
img[im.ths_cord:im.ths_cord+im.size_brush[0], 180:200, :] = im.ths_shaded

cv2.namedWindow(winname = "image") 
cv2.setMouseCallback("image", activate)

# if rectangle == True:
    # cv2.setMouseCallback("image", draw_rectangle) 

while part_one: 
    cv2.imshow("image", img) 
    if cv2.waitKey(10) == 27: 
        break
    elif cv2.waitKey(10) == ord('c'):
        img[50:700,250:900,:] = (255, 255, 255)

cv2.destroyAllWindows() 

new_size = (300,300)

dw.basic_set(img, new_size)
dw.turning_set(img, new_size)
dw.fliping_h_set(img, new_size)
dw.fliping_w_set(img, new_size)



