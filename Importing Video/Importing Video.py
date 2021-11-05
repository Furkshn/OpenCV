import cv2
import time



video_name = "pedestrian.mp4"



cap = cv2.VideoCapture(video_name)   # Video Import: Capture, cap

print("Genişlik: ",cap.get(3))
print("Yükseklik: ",cap.get(4))


if cap.isOpened() == False:    # It is checked whether the video is opened or not.
    
    print("Hata !")
    
    
# The video does not play directly, it is played by combining the pictures with the loop.

while True: 
    
    ret, frame = cap.read()         # Frame is each picture in the video.
                                    # Return indicates whether the operation was successful or not.
    if ret == True:
        
        time.sleep(0.01)      # If not used, the video flows very fast.

        cv2.imshow("Video",frame)
        
    else: 
        break
    
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        
        break


cap.release()        # Stop Capture
cv2.destroyAllWindows()
