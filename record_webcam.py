# OpenCV (cv2) for video processing, datetime for timestamping, and os for file operations.
import cv2
from datetime import datetime
import os


# Create a path to a directory called 'recordings' within the current working directory.
recordings_dir = os.path.join('recordings')

# Create this recordings directory if it doesn't exist using the path specified.
if not os.path.exists(recordings_dir):
    os.makedirs(recordings_dir)


def record_over_webcam(channel: int) -> None:
    """
    Record video over an internal or external webcam feed and save it for later viewing.

    Args:
        channel (int): The channel number of the camera record from.

    Returns:
        None
    """
    try:
        # create a timestamp using the current date and time to uniquely name each recorded video.
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # initialize a video capture object to start streaming video from the specified camera channel.
        cap = cv2.VideoCapture(channel)

        # check if the video capture object was successfully initialized.
        # If not, an error message is printed, and a ValueError is raised
        if not cap.isOpened():
            print("Error opening camera. Please check if an external camera is connected.")
            raise ValueError(
                f"Error opening camera channel {channel}. Please check if an external camera is connected.")

        # create a VideoWriter object (out) to save the video.
        # We specify the output file path, the codec to use (mp4v),
        # the frames per second, and the frame size (both obtained from the video capture object).
        out = cv2.VideoWriter(
            os.path.join(recordings_dir, f'{timestamp}_{channel}_webcam_recording.mp4'),
            cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

        stream_video(cap, out)
    except Exception as e:
        print(f"Error in record_over_webcam: {e}")

def stream_video(cap: cv2.VideoCapture, out: cv2.VideoWriter):
    """
    Read frames from the capture object, write them to a file using the writer object, and display them for viewing until the 'q' is pressed.

    Args:
        cap: cv2.VideoCapture: The video capture object to read frames from.
        out: cv2.VideoWriter: The video writer object to write frames with.

    Returns:
        None
    """
    try:
        while True:
            ret, frame = cap.read()
            out.write(frame)
            cv2.imshow("Webcam - Press 'q' key to quit.", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"Error in stream_video: {e}")
    # After recording is complete we ensure release our video capture, writer, and destroy our window.
    finally:
        cap.release()
        out.release()
        cv2.destroyAllWindows()


def main():
    # Call the function to record video passing 0 for internal camera streaming.
    record_over_webcam(0)


if __name__ == "__main__":
    main()


