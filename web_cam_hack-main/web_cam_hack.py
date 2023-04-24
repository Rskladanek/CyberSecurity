import cv2  # import the OpenCV library

ip_address = "192.168.0.100"  # IP address of the IP camera
url = "http://" + ip_address + ":8080/video"  # URL of the video stream from the IP camera

cap = cv2.VideoCapture(url)  # create a VideoCapture object for capturing the video stream from the IP camera

while True:  # infinite loop
    ret, frame = cap.read()  # read a frame from the video stream

    if ret:  # if a frame was successfully read
        cv2.imshow("Webcam", frame)  # display the frame in a window

    if cv2.waitKey(1) == ord("q"):  # if the user presses the "q" key
        break  # break out of the infinite loop

cap.release()  # release the VideoCapture object
cv2.destroyAllWindows()  # close the window displaying the video stream
