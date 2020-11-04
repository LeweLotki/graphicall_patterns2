import numpy as np
import cv2

new_size = (300,300)

def basic_set(img, new_size):

    final_image = img[60:690,260:890,:]
    final_image = cv2.resize(final_image,new_size)
    final = np.zeros((3*new_size[0],6*new_size[0],3))

    for val in range(0,3*new_size[0],new_size[0]):
        for val2 in range(0,6*new_size[0],new_size[0]):
            final[val:val + new_size[0], val2:val2 + new_size[0],:] = final_image
            
    # for val in range(0,450,150):
            # final[0:150, val:val + 150,:] = final_image


    cv2.imshow('final image', final)
    cv2.imwrite('basic_set', final)
    # cv2.imshow('f',final_image)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows() # cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE) 
        
def turning_set(img, new_size):
    final_image = img[60:690,260:890,:]
    final_image = cv2.resize(final_image,new_size)
    final = np.zeros((3*new_size[0],6*new_size[0],3))
    temp_final_image = final_image.copy()      
    for val in range(0,3*new_size[0],new_size[0]):
        for val2 in range(0,6*new_size[0],new_size[0]):
            temp_final_image = cv2.rotate(temp_final_image, cv2.ROTATE_90_COUNTERCLOCKWISE) 
            final[val:val + new_size[0], val2:val2 + new_size[0],:] = temp_final_image

    # for val in range(0,450,150):
            # final[0:150, val:val + 150,:] = final_image


    cv2.imshow('final image', final)
    cv2.imwrite('turning_set', final)
    # cv2.imshow('f',final_image)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        
def fliping_h_set(img, new_size):
    final_image = img[60:690,260:890,:]
    final_image = cv2.resize(final_image,new_size)
    final = np.zeros((3*new_size[0],6*new_size[0],3))
    temp_final_image = final_image.copy()      
    for val in range(0,3*new_size[0],new_size[0]):
        for val2 in range(0,6*new_size[0],new_size[0]):
            temp_final_image = cv2.flip(temp_final_image,0) 
            final[val:val + new_size[0], val2:val2 + new_size[0],:] = temp_final_image

    # for val in range(0,450,150):
            # final[0:150, val:val + 150,:] = final_image


    cv2.imshow('final image', final)
    cv2.imwrite('fliping_h_set', final)
    # cv2.imshow('f',final_image)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        
def fliping_w_set(img, new_size):
    final_image = img[60:690,260:890,:]
    final_image = cv2.resize(final_image,new_size)
    final = np.zeros((3*new_size[0],6*new_size[0],3))
    temp_final_image = final_image.copy()      
    for val in range(0,3*new_size[0],new_size[0]):
        for val2 in range(0,6*new_size[0],new_size[0]):
            temp_final_image = cv2.flip(temp_final_image,1) 
            final[val:val + new_size[0], val2:val2 + new_size[0],:] = temp_final_image

    # for val in range(0,450,150):
            # final[0:150, val:val + 150,:] = final_image


    cv2.imshow('final image', final)
    cv2.imwrite('fliping_w_set', final)
    # cv2.imshow('f',final_image)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
