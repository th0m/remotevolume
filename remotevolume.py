from flask import Flask, render_template
from subprocess import call
app = Flask(__name__)

@app.route('/')
def home():
    render_template('templates/home.html.tmpl')

@app.route('/up')
def up():
    call(['pactl', 'set-sink-volume', 1, '+10%'])
    
@app.route('/down')
def down():
    call(['pactl', 'set-sink-volume', 1, '-10%'])

if __name__ == "__main__":
    app.run()
