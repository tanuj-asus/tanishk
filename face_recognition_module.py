import cv2
import face_recognition

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

# Initialize a list to hold known face encodings and their names
known_face_encodings = []
known_face_names = []

def load_known_faces():
    # Load images and encode them here
    # Example:
    # image = face_recognition.load_image_file("student1.jpg")
    # encoding = face_recognition.face_encodings(image)[0]
    # known_face_encodings.append(encoding)
    # known_face_names.append("Student 1")

load_known_faces()

while True:
    # Capture a single frame
    ret, frame = video_capture.read()

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Use the known face with the shortest distance to the new face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a label with a name below the face
        cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()