# from flask import Flask, render_template
# import cv2
# from gaze_tracking import GazeTracking

# app = Flask(__name__, template_folder='keerthan')

# # Initialize gaze tracking and webcam
# gaze = GazeTracking()
# webcam = cv2.VideoCapture(0)

# @app.route('/')
# def index():
#     # Analyze the frame using gaze tracking
#     _, frame = webcam.read()
#     gaze.refresh(frame)
#     text = ""

#     if gaze.is_blinking():
#         text = "Blinking"
#     elif gaze.is_right():
#         text = "Looking right"
#     elif gaze.is_left():
#         text = "Looking left"
#     elif gaze.is_center():
#         text = "Looking center"

#     # Pass the gaze tracking information to the template
#     return render_template('index.html', gaze_text=text)

# if __name__ == '__main__':
#     app.run(debug=True)

# # Release the webcam resources
# webcam.release()
# cv2.destroyAllWindows()

# from flask import Flask, render_template, Response
# import cv2
# from gaze_tracking import GazeTracking

# app = Flask(__name__, template_folder='keerthan')

# # Initialize gaze tracking and webcam
# gaze = GazeTracking()
# webcam = cv2.VideoCapture(0)

# def generate_frames():
#     while True:
#         success, frame = webcam.read()
#         if not success:
#             break
#         else:
#             gaze.refresh(frame)
#             text = ""

#             if gaze.is_blinking():
#                 text = "Blinking"
#             elif gaze.is_right():
#                 text = "Looking right"
#             elif gaze.is_left():
#                 text = "Looking left"
#             elif gaze.is_center():
#                 text = "Looking center"

#             # Draw the text on the frame
#             cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(debug=True)

# # Release the webcam resources
# webcam.release()
# cv2.destroyAllWindows()
from flask import Flask, render_template, Response
import cv2
from gaze_tracking import GazeTracking

app = Flask(__name__, template_folder='keerthan')

# Initialize gaze tracking and webcam
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = webcam.read()
        if not success:
            break
        else:
            gaze.refresh(frame)
            text = ""

            if gaze.is_blinking():
                text = "Blinking"
            elif gaze.is_right():
                text = "Looking right"
            elif gaze.is_left():
                text = "Looking left"
            elif gaze.is_center():
                text = "Looking center"

            # Draw the text on the frame
            cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Convert the frame to JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Send the frame as part of the video stream
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

           

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

# Release the webcam resources
webcam.release()
cv2.destroyAllWindows()
