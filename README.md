# AR-Python
An attempt to create the first easy augmented reality projects with python. This code uses the Ursina and Mediapipe libraries to capture video from a camera and detect hand landmarks in the video. The detected hand landmarks are then used to control the position and animation of a 3D model of a hand, simulating a virtual hand following the movement of a real hand.

The code also detects the number of fingers that are being held up and uses this information to control the animation of the 3D hand model.

- [ ] Animation in progress
- [ ] Motion tracking in the future

## Prerequisites
* Ursina library
* Mediapipe library
* OpenCV library
* PIL library

## Running the code
1. Clone the repository
2. Run the code using Python
3. The code will open a window with a quad displaying the camera input and a 3D hand model that follows the movement of your hand
4. The code also detects the number of fingers that are being held up and uses this information to control the animation of the 3D hand model.

## Note
* The code is using the default camera on the device, if you want to use a different camera you need to change the camera index in the following line of code:
```cap = cv2.VideoCapture(0)```
* The code is also using a 3D model of a hand that is located in the same directory with the code, if you want to use a different model you need to change the path in the following line of code:
```actor = Actor('minonew.glb')```

## Please give out your suggestions and also give a star :smiling_face_with_three_hearts:
### Created by @DawoodLaiq

## Additional Information
This code is using the Mediapipe Hands solution for hand tracking, for more information on how to use Mediapipe Hands solution please check the following link: https://mediapipe.readthedocs.io/en/latest/solutions/hands.html

for more information on the Ursina library please check the following link: https://ursina.readthedocs.io/en/latest/

for more information on the OpenCV library please check the following link: https://opencv.org/

for more information on the PIL library please check the following link: https://pillow.readthedocs.io/en/stable/

This is a basic example of how to use Mediapipe and Ursina library to track hand movement and use it to control the animation of a 3D hand model. Feel free to use the code and adapt it to fit your project.
