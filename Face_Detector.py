import cv2
import random

# Load some pre-trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Choose an image or a video stream or webcam and pass into classifier to be able to find the location of faces
# and put the rectangular
# img = cv2.imread("RDJ.jpg")

webcam = cv2.VideoCapture(0) # 0 - means it is gonna capture our default webcam

# iterate forever over frames
while True:
    # Read the current frame
    successful_frame_read, frame = webcam.read()

    # must change to greyscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates: # on a single video
        # (x, y, w, h) = face_coordinates[0]
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (random.randrange(256), random.randrange(256),
        # random.randrange(256)), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Lazizjon's Face Detector", frame)
    key = cv2.waitKey(1)
    # 1 makes the waitkey wait 1 milisecond and automatically press the key itself, meaning that we are
    # getting a live footage

    if key == 81 or key == 113:
        break

# release the videoCapture object
webcam.release()

print("Code Completed")

# print(face_coordinates)

# Show the image itself
# cv2.imshow("Lazizjon's Face Detector", img)

# Wait here in the code and listen for a key press. This pauses the execution of the code, so it will show the image
# and then it will continue on to the end of the p rogram and exit the running process.
#  # It waits for a key press so that to continue execution of the program

### How the computer looking at the image and how does it know what face looks like and understand it.