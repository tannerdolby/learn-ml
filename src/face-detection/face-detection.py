import cv2
import os

img_src = "images/pexels-gabby-k-6238122.jpg"
curr_directory = os.path.dirname(__file__)
image_path = os.path.join(curr_directory, "..", "..", img_src)

# Classifier to return coordinates of faces
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# read/load the group photo
group_photo = cv2.imread(image_path)

# convert the image to grayscale
gray_photo = cv2.cvtColor(group_photo, cv2.COLOR_BGR2GRAY)

# write the grayscale image to a new file
# cv2.imwrite(os.path.join(curr_directory, "images/group-photo-grayscale.jpg"), gray_photo)

# Iterable containing several tuples
# Detect faces of the grayscale group photo using our classifer
faces = face_classifier.detectMultiScale(gray_photo, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
face_idx = 0

# Loop through faces coordinates and draw boxes onto group photo
for (x,y,w,h) in faces:

    # define the region of interest in the group photo for the current face
    face_section = group_photo[y:y+h, x:x+w]

    # write the current face section to a new image
    face_img_path = os.path.join(curr_directory, f"images/faces/face-{face_idx}.jpg")
    cv2.imwrite(face_img_path, face_section)

    # This `rectangle` function requires the coordinates
    # of the rectangle (the top-left and bottom-right corners),
    # the color of the rectangle, and the thickness of the lines
    # that make up the rectangle.
    # draw rectangles around faces in group photo
    cv2.rectangle(group_photo, (x, y), (x + w, y + h), (255, 0, 0), 10)

    face_idx += 1


# display image
cv2.imshow("group photo", group_photo)

# display grayscale image
# cv2.imshow("grayscale group photo", gray_photo)

# write the group_photo image with rectangles around faces to a new file
cv2.imwrite(os.path.join(curr_directory, "images/group-photo-faces-marked.jpg"), group_photo)

# Ensure when a key is hit e.g. 'Enter' it closes all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
