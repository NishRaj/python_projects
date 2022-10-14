from crypt import methods
import headfirst.functions as f
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/test')
def hello() -> str:
    return 'Hello World from Flask'

@app.route('/search4',methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    commonLetterSet = f.searchForLetters(phrase,letters)
    return render_template('results.html', the_title=title,the_phrase=phrase,the_letters=letters,the_results=commonLetterSet)
@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title = 'Welcome to search 4 web.')
app.run()