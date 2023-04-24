Capture and display a video stream from an IP camera using OpenCV.

Usage:
1. Set the IP address of the IP camera in the `ip_address` variable.
2. Run the code.

This code uses the OpenCV library to capture a video stream from an IP camera and display it in real-time in a window. The IP address of the IP camera is stored in the `ip_address` variable, and the URL of the video stream from the IP camera is generated based on this address.

The code creates a `VideoCapture` object to capture the video stream from the IP camera. In an infinite loop, frames of video are read from the camera using the `read` method of the `VideoCapture` object. If a frame is successfully read, it is displayed in a window using the `imshow` method of the OpenCV library. The window is named "Webcam".

The loop runs until the user presses the "q" key, at which point the loop is broken, the `VideoCapture` object is released using the `release` method, and the window displaying the video stream is closed using the `destroyAllWindows` method of the OpenCV library.

Dependencies:
- OpenCV (cv2) library

Limitations:
- The IP camera must be configured to provide a video stream accessible via HTTP.
- The code assumes that the video stream is available at the default port (8080) of the IP camera.
