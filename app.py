from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<center><img loading="lazy" src="chipmusic/chipmusic-discovery/SonicGame.png" alt="Sonic" width="56" height="85" border="0" align="top" title="Sonic"></center>'
