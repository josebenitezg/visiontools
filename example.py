# from visiontools.video_editing import concat_videos

# input_videos = ['cam0.mp4', 'cam1.mp4', 'cam2.mp4']
# output_path = 'concatenated_video.mp4'

# # Concatenate horizontally
# concat_videos(input_videos, output_path, direction='horizontal')

from visiontools.camera_loader import CameraApp, CameraConfig
import cv2

# Create a custom configuration with show_window=True
config = CameraConfig(width=1280, height=720, fps=60, show_window=True)

# Initialize the CameraApp with the custom config
# Is useful when you want to run a pipeline on multiple cameras simultaneously
with CameraApp(config) as app:
    # Detect available cameras
    available_cameras = app.detect_cameras()
    
    # Load the first two cameras (if available)
    num_loaded = app.load_cameras(available_cameras[:2])
    
    # Start recording (Optional: provide names for each camera)
    output_folder = app.start_recording(["Front", "Side"])
    
    # Capture frames (in a loop in your main application)
    while True:
        frames = app.capture_frame()
        # Process frames as needed (e.g. manipulate, draw, save, etc.)
        # To exit the loop when 'q' is pressed (only works when show_window is True)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Stop recording
    app.stop_recording()