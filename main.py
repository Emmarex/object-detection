import os
import cv2
from imageai.Detection import ObjectDetection

BASE_DIR = os.getcwd()

object_detector = ObjectDetection()


model_path = os.path.join(BASE_DIR, "model/yolo.h5")

object_detector.setModelTypeAsYOLOv3()

if os.path.isfile(model_path) == False:
    #
    model_path = os.path.join(BASE_DIR, "model/yolo-tiny.h5")

    object_detector.setModelTypeAsTinyYOLOv3()

object_detector.setModelPath(model_path)

object_detector.loadModel(
    detection_speed="fast"
)

video_capture = cv2.VideoCapture(0)

# video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1500)
# video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 2500)

cv2.namedWindow('Object Detection System',
                cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

process_this_frame = True

while video_capture.isOpened():

    # Grab a single frame of video
    frame_exists, frame = video_capture.read()

    if not frame_exists:
        break

    # Only process every other frame of video to save time
    if process_this_frame:

        detected_image_array, detections = object_detector.detectObjectsFromImage(  # type: ignore
            input_image=frame,
            custom_objects=None,
            input_type="array",
            output_type="array",
            minimum_percentage_probability=70,
            display_percentage_probability=True,
            display_object_name=True,
            thread_safe=True,
        )

        if detections:
            for eachObject in detections:
                """
                {
                    'name': 'person',
                    'percentage_probability': '99.9723732471466',
                    'box_points': [102, 77, 1176, 760] # [x1, y1, x2, y2]
                }
                """
                left, top, right, bottom = eachObject["box_points"]

                # Draw a box around the object
                cv2.rectangle(
                    frame,
                    (left, top),
                    (right, bottom),
                    (0, 0, 255),
                    2
                )

                # Draw a label with a name below the face
                cv2.rectangle(
                    frame,
                    (left, bottom - 35),
                    (right, bottom),
                    (0, 0, 255),
                    cv2.FILLED
                )
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(
                    frame,
                    eachObject["name"],
                    (left + 6, bottom - 6),
                    font,
                    1.0,
                    (255, 255, 255),
                    1
                )

    process_this_frame = not process_this_frame

    # show video frame
    cv2.imshow('Object Detection System', frame)

    # ESC key to quit application
    if cv2.waitKey(30) & 0xff == 27:  # ESC Key
        print("[INFO] : Terminating application ...")
        break

video_capture.release()
cv2.destroyAllWindows()
