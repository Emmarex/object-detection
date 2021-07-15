# Object Detection from Video

### How to use the application

\*\*\* Ensure you are connected to the internet

1. Install Python 3.7. You can download from the [official Python website](https://www.python.org/)
2. Clone this repository
3. Open a terminal and change directory to this repo's directory on your system
4. Run `bash pip install virtualenv` or `bash pip3 install virtualenv`
5. Run `bash virtualenv env`
6. Run `bash source env/bin/activate` on a Mac/Linux or `bash env/Scripts/activate` on Windows
7. Run `bash pip install -r requirements.txt` or `bash pip3 install -r requirements.txt`
8. Download the file [here](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5) or [here](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5) if you prefer light weight model and speed and put inside the `models` folder
9. Run `bash python main.py`

### Video Capture

```python
video_path = object_detector.detectObjectsFromVideo(
    camera_input=video_capture,
    # output_file_path=os.path.join(BASE_DIR, "camera_detected_video"),
    frames_per_second=1,
    log_progress=True,
    minimum_percentage_probability=40,
    save_detected_video=False,
    display_box=True,
    display_object_name=True,
    display_percentage_probability=True,
    thread_safe=True
)
```
