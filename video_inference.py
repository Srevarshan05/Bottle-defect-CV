import cv2
from ultralytics import YOLO

def main():
    """
    This function performs live inference by manually managing the webcam stream
    to ensure it runs continuously.
    """
    # Load your custom trained model.
    # Make sure this path is correct for your system.
    model_path = r'C:\Users\Srevarshan\OneDrive\Desktop\bottle_inference\runs\detect\train2\weights\best.pt'
    try:
        model = YOLO(model_path)
    except FileNotFoundError:
        print(f"❌ Error: Model file not found at '{model_path}'. Please check the path.")
        return

    # Use '0' to specify the default webcam.
    source = 0
    
    # Open the video capture object.
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("❌ Error: Could not open webcam. Check connection and permissions.")
        return

    # Attempt to set the webcam's resolution and FPS for consistent performance.
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)

    print("✅ Webcam stream initialized. Press 'q' on the output window to quit.")
    
    while True:
        # Read a frame from the webcam.
        success, frame = cap.read()
        
        if not success:
            print("Failed to read a frame from the webcam.")
            break

        # Perform inference on the current frame.
        # This returns a list of results for the single frame.
        results = model.predict(
            source=frame,
            conf=0.25,
            verbose=False,
            device=0  # Explicitly use GPU
        )

        # Draw the bounding boxes and labels on the frame.
        # Ultralytics results object has a built-in method to display the image.
        annotated_frame = results[0].plot()

        # Display the annotated frame in a window named 'YOLOv8 Live Inference'.
        cv2.imshow('YOLOv8 Live Inference', annotated_frame)
        
        # Break the loop if the 'q' key is pressed.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows.
    cap.release()
    cv2.destroyAllWindows()
    print("Live inference has finished.")

if __name__ == '__main__':
    main()