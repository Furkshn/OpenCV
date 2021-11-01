import cv2            # Importing OpenCV Library


img = cv2.imread("fluence.jpg",0)    ## Resmin Okunması --- Reading image

cv2.imshow("First Photo",img)



k = cv2.waitKey(0) &0xFF          ## Klavye Tuşu Ataması Yapıldı. --- Keyboard Key Assigned.

if k == 27:                     ## ESC tuşunun karşılığı 27'dir. --- The equivalent of the ESC key is 27.
    
    cv.destroyAllWindows()
    
elif k == ord("s"):                 ## "s"'ye basıldığı zaman resim kaydedilir ve tüm pencereler kapatılır. --- Pressing "s" saves the picture and closes all windows.
    
    cv2.imwrite("arabamız.png",img)      ## Saving car image as png format --- Araba resmini png formatında kaydetme
    cv2.destroyAllWindows()