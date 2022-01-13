from distutils.log import debug
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "sneaky"

debug = DebugToolbarExtension(app)


@app.route('/')
def madlib_questions():
    prompts = story.prompts
    return render_template('prompts.html', prompts=prompts)


@app.route('/story')
def write_story():
    template = story.generate(request.args)
