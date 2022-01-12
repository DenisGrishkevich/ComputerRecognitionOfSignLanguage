import cv2
import mediapipe as mp
import numpy as np
from matplotlib import pyplot as plt
from solutions.functions import *
from datasets.data_sign import *
from solutions.functions_if import *

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Webcam initialization. 0 - First webcam.
cap = cv2.VideoCapture(0)

# Get the width and the height of the frames
frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# A list containing the index of all points. Updated at each iteration of the loop.
points_list = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], 
                [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]
answer_list_1 = []
answer_list_2 = []
answer_list_3 = []

saving_data = False
number = 0
testing = False

with mp_hands.Hands(
        static_image_mode=False,
        # max_num_hands - Maximum number of hands to be detected.
        max_num_hands=1,
        # min_detection_confidence - Minimum confidence value (between 0 and 1) for the hand detection to be considered successful
        min_detection_confidence=0.7,
        # min_tracking_confidence - Minimum confidence value (between 0 and 1) for the hand landmarks to be considered tracked successfully.
        min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        success, image = cap.read()
        # If the camera fails to connect, it interrupts the cycle and terminates the program.
        if not success:
            print("Ignoring empty camera frame.")
            break
        
        # Flip image
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = True
        results = hands.process(image)
        # Change BGR to RGB
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # The main part is processing the video stream and capturing points.
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Point - The name of the point in the library.            
                for point in mp_hands.HandLandmark:
                    # NormalizedLandmark - Normalized coordinates of the landmark.
                    normalizedLandmark = hand_landmarks.landmark[point]
                    # PixelCoordinatesLandmark - Tuple with the x and y coordinates of the landmark, in pixels.
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, 
                                                                                           normalizedLandmark.y, 
                                                                                           frameWidth,
                                                                                           frameHeight)
                    # Transformation of the variable name into a string for processing by the dictionary.
                    # Writing point values to a list.
                    points_list[point.value] = np.array([normalizedLandmark.x, normalizedLandmark.y, normalizedLandmark.z])
                    # Point visualization
                    # Image - The image where to draw the circle
                    # PixelCoordinatesLandmark - Tuple with the x and y coordinates of the landmark, in pixels.
                    # 5 - The radius of the circle, in pixels
                    # (0, 255, 0) - A tuple with the color of the circle, in BGR (Blue, Green and Red) format.
                    # - 1 - The thickness of the circle outline. If value -1 - circle is filled.
                    cv2.circle(image, pixelCoordinatesLandmark, 5, (255, 0, 0), -1)
                    
                # Calculation of coordinates relative to the "0" point.
                for i in range(1, 21):
                    points_list[i] = points_list[i] - points_list[0]
                # Change the coordinates of the "0" point to 0.0.
                points_list[0] = np.array([0, 0, 0])
                # Three functions. The first is the distance, the second is the distance + edits, the third is if.
                answer_1 = distance_calc(points_list)
                answer_2 = distance_calc_with(points_list)
                answer_3 = sign_if(points_list)
                
                # Displaying a recognizable gesture on the screen
                cv2.putText(image, f'Algorithm 1: {answer_1}', (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                cv2.putText(image, f'Algorithm 2: {answer_2}', (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                cv2.putText(image, f'Algorithm 3: {answer_3}', (10, 80), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                
                # Testing module
                if testing == True:
                    letter = "a"
                    if len(answer_list_1) < 200:
                        check_correct(answer_1, answer_list_1, letter)
                        check_correct(answer_2, answer_list_2, letter)
                        check_correct(answer_3, answer_list_3, letter)
                    if len(answer_list_1) == 200:
                        print(f"1: {np.mean(answer_list_1)}")
                        print(f"2: {np.mean(answer_list_2)}")
                        print(f"3: {np.mean(answer_list_3)}")
                        print("-----------------------")
                
                if saving_data == True:        
                    number = saving_data_sign(points_list, number)
                    
                # Button for outputting all coordinates to the console. 
                # To display the coordinates in the console, press the "S" button.
                if cv2.waitKey(5) & 0xFF == ord("p"):
                    print("___________________________")
                    print(points_list)
                    print("===========================")
                    
                if cv2.waitKey(5) & 0xFF == ord("m"):
                    x = []
                    y = []
                    for i in range(0, 21):
                        x.append(points_list[i][0])
                        y.append(points_list[i][1])
                    plt.title("Matplotlib") 
                    plt.xlabel("x axis") 
                    plt.ylabel("y axis") 
                    plt.plot(x,y,"ob") 
                    plt.show()
                if cv2.waitKey(5) & 0xFF == ord("t"):
                    testing = True
                if cv2.waitKey(5) & 0xFF == ord("s"):
                    saving_data = True    
                        
        # Show webcam with points.   
        cv2.imshow('HandTracking', image)
        
        # To exit the program, press Esc.
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
