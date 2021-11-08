import cv2


cap = cv2.VideoCapture(0)   # 0 is the default (webcam) camera. (Laptop or PC)

width = int(cv2.CAP_PROP_FRAME_WIDTH)
height = int(cv2.CAP_PROP_FRAME_HEIGHT)

print(width,height)


# Video Recording

writer = cv2.VideoWriter("Video_Kaydı",cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))  # "DIVX" indicates windows operating system.

                                                                                        #20 indicates the video speed.
                                                                                        
                                                                                                                                                                        
                                                                                        
while True:
    
    ret, frame = cap.read()
    cv2.imshow("Video",frame)
    

    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): break



cap.release()
writer.release()      # The code that performs the save operation is also released.

cv2.destroyAllWindows()
                                                                 
                                                                
                                                                
                                                                


