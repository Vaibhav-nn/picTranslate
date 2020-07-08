import cv2

def writer(image,text,coord):
    i=0
    for crd in coord:
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            org = crd 
            fontScale = 1
            color = (255,255,255)   #White
            thickness = 1
            img = cv2.putText(image, text[i], org, font,  
                            fontScale, color, thickness, cv2.LINE_AA)
            i+=1

    print('New image generated')
    return img
