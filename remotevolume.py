from flask import Flask, render_template, redirect, url_for
from subprocess import call
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html.tmpl')

@app.route('/up')
def up():
    call(['pactl', 'set-sink-volume', '1', '+10%'])
    return render_template('home.html.tmpl')
    
@app.route('/down')
def down():
    call(['pactl', 'set-sink-volume', '1', '-10%'])
    return render_template('home.html.tmpl')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
