# OpenCV (cv2) for video processing, datetime for timestamping, tello for our drone object.
import cv2
from djitellopy import tello
from datetime import datetime


def record_tello_video_stream(frame_read: tello.BackgroundFrameRead, out: cv2.VideoWriter):
    """
    Run video recording from Tello drone.

    Parameters:
    - frame_read: Tello frame reader object
    - out: Video writer object for recording

    This function continuously captures frames from the Tello drone's video stream,
    writes the frames to the output video file, and displays the frames in a window.
    Press 'q' to stop recording and close the window.

    Note: Adjust the waitKey argument to match the desired frame rate.
    """
    try:
        while True:
            # Capture a frame from the Tello video stream
            frame = frame_read.frame

            # Write the captured frame to the output video file
            out.write(frame)

            # Display the captured frame in a window
            cv2.imshow("Frame", frame)

            # Check for the 'q' key press to exit the loop and stop recording
            if cv2.waitKey(33) & 0xFF == ord('q'):  # Change 33 to 1 for 30fps
                break
    except Exception as e:
        print('An exception occurred in recording tellos video stream')
    finally:
        # Close the window and release the video writer
        cv2.destroyAllWindows()
        out.release()


def main():
    """
    Main function to connect to Tello drone, record video, and reboot.

    This function performs the following steps:
    1. Initializes a connection with the Tello drone.
    2. Enables video streaming from the Tello.
    3. Retrieves the frame reader object for capturing video frames.
    4. Sets up a video writer for recording the video to a file.
    5. Calls the 'run_tello_video' function to start capturing and recording video.
    6. Displays an end-of-main message.
    7. Reboots the Tello drone.
    """
    # create a timestamp using the current date and time to uniquely name each recorded video.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Initialize Tello drone and establish connection
    drone = tello.Tello()
    drone.connect()
    drone.streamon()

    # Obtain frame reader from Tello and get frame dimensions
    frame_read = drone.get_frame_read()
    H, W, _ = frame_read.frame.shape

    # Set up video writer for recording
    out = cv2.VideoWriter(f'{timestamp}_tello_recording.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (W, H))

    # Run video recording function
    record_tello_video_stream(frame_read, out)

    # Display end-of-main message and reboot the drone
    print('end of main, calling drone.reboot')
    drone.reboot()


if __name__ == "__main__":
    main()
