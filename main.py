from flask import Flask, request, Response
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "L Bhai Ka Engine Chalu Hai!"

@app.route('/merge')
def merge():
    v = request.args.get('v')
    a = request.args.get('a')
    cmd = ['ffmpeg', '-i', v, '-i', a, '-c:v', 'copy', '-c:a', 'aac', '-map', '0:v:0', '-map', '1:a:0', '-shortest', '-f', 'mp4', '-movflags', 'frag_keyframe+empty_moov', 'pipe:1']
    return Response(subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout, mimetype='video/mp4')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
