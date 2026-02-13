from flask import Flask
import datetime

app = Flask(__name__)

a = 0

@app.route('/')
def hello_world():
    global a
    a += 1
    return f'''
    <h1>{str(datetime.datetime.now())}</h1>
    <h2>Visits : {a}<h2>
    <center>
    <img loading="lazy" src="chipmusic/chipmusic-discovery/SonicGame.png" alt="Sonic" width="56" height="85" border="0" align="top" title="Sonic">
    </center>
    '''

@app.route('/jelloshello')
def java_script():
    return f''' 
<body>
    <div id="output"></div>
    <script src="static/javascript_hello.js"></script>
</body>
    '''