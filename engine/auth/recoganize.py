import os
import cv2

def AuthenticateFace():
    # Absolute paths for model and cascade
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    trainer_path = os.path.join(BASE_DIR, 'trainer', 'trainer.yml')
    cascade_path = os.path.join(BASE_DIR, 'haarcascade_frontalface_default.xml')

    if not os.path.isfile(trainer_path):
        print(f"Error: Trainer file not found at {trainer_path}")
        return 0
    if not os.path.isfile(cascade_path):
        print(f"Error: Cascade file not found at {cascade_path}")
        return 0

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(trainer_path)
    faceCascade = cv2.CascadeClassifier(cascade_path)
    font = cv2.FONT_HERSHEY_SIMPLEX

    names = ['', 'susant']  # index 1 is 'susant'

    # Try camera index 0, fallback to 1
    cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    if not cam.isOpened():
        cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        if not cam.isOpened():
            print("Error: Could not open webcam.")
            return 0

    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    flag = 0

    while True:
        ret, img = cam.read()
        if not ret:
            print("Failed to grab frame from camera.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=4,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id_, accuracy = recognizer.predict(gray[y:y + h, x:x + w])

            confidence = 100 - accuracy
            if confidence >= 45:
                name = names[id_] if id_ < len(names) else "unknown"
                acc_text = f"  {round(confidence)}%"
                flag = 1
            else:
                name = "unknown"
                acc_text = f"  {round(confidence)}%"
                flag = 0

            cv2.putText(img, str(name), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(acc_text), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)
        k = cv2.waitKey(10) & 0xff
        if k == 27 or flag == 1:
            break

    cam.release()
    cv2.destroyAllWindows()
    return flag

# Example usage:
if __name__ == "__main__":
    result = AuthenticateFace()
    print("Authentication result:", "Success" if result else "Failed")