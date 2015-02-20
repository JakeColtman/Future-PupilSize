import cv2


def process_frame(frame):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    return gray

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    frame = process_frame(frame)
    
    cv2.imshow("frame", frame)
        
    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
