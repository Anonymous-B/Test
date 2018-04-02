import cv2
from imutils.video.pivideostream import PiVideoStream
import time
from flask import Flask, render_template, Response
app = Flask(__name__)


def get_frame():
    frame = vs.read()
    ret, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()


@app.route('/')
def index():
    return render_template('index.html')


def gen():
    while True:
        frame = get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(vs),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    vs = PiVideoStream(framerate=32).start()
    time.sleep(2.0)
    app.run(host='192.168.0.102', debug=False)
