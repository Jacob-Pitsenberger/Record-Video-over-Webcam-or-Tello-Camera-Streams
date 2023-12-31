# Webcam and Tello Drone Video Recorder Modules

## Description

This repository contains two Python modules that facilitate video recording from different sources: internal/external webcams and Tello drones.

### Webcam Video Recorder Module

This module provides a convenient way to record video from an internal or external webcam using OpenCV in Python.

#### Prerequisites
- Python
- OpenCV (cv2)
- datetime
- os

#### Usage

####  Recording Video
```python
from video_recorder import record_over_webcam

# Record video from the default internal camera (channel 0)
record_over_webcam(0)
```

#### Function Parameters
channel (int): The channel number of the camera to record from.

#### How it Works

1. The module uses OpenCV for video processing, datetime for timestamping, and os for file operations.

2. It creates a directory named 'recordings' within the current working directory to save the recorded videos.

3. The `record_over_webcam` function records video over the specified webcam feed and saves it for later viewing. It takes the camera channel number as an argument.

4. The recorded video is saved in the 'recordings' directory with a unique timestamped filename.

5. The `stream_video` function reads frames from the capture object, writes them to a file using the writer object, and displays them for viewing until the 'q' key is pressed.

6. After recording is complete, it releases the video capture, writer, and destroys the display window.

#### Running the Example
To run the example, simply call the `record_over_webcam` function with the desired camera channel as an argument.

```python
record_over_webcam(0)
```

### Tello Drone Video Recorder Module
This module allows you to record video from a Tello drone using the DJITelloPy library and OpenCV in Python.

#### Prerequisites
- Python
- OpenCV (cv2)
- djitellopy
- datetime

#### Usage

#### Recording Video

```python
from record_tello import record_tello_video

# Connect to Tello drone, record video, and reboot
record_tello_video()
```

#### Function Parameters
No parameters are required.

#### How it Works
1. The module uses OpenCV for video processing, datetime for timestamping, and djitellopy for Tello drone communication.

2. The record_tello_video function connects to a Tello drone, starts video streaming, and records the video to a file.

3. The recorded video is saved with a unique timestamped filename.

4. The recording continues until the 'q' key is pressed.

5. After recording is complete, it closes the video window, releases resources, and reboots the Tello drone.

#### Running the Example
To run the example, simply call the record_tello_video function.

```python
record_tello_video()
```

## License
This module is licensed under the [MIT License](LICENSE.txt).