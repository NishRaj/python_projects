import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from headfirst import functions as f
from flask import Flask, render_template, request,escape
import sys
print(sys.path)
print(__name__)
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
    log_request(request,commonLetterSet)
    return render_template('results.html', the_title=title,the_phrase=phrase,the_letters=letters,the_results=commonLetterSet)
@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title = 'Welcome to search 4 web.')
@app.route('/viewLog')
def view_log() -> 'html':
    with open("vsearch.log","r") as logfile:
        contents = []
        for line in logfile:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
       # return str(contents)
    row_title = ('Form Data','Remote Addr','User Agent','Results',)
    return render_template('viewlog.html',the_title='View Log',the_row_titles=row_title,the_data=contents)

def log_request(req:'flask_request',res: str) -> None:
    with open("vsearch.log","a") as logfile:
       #print(str(dir(req)),res,file=logfile)
       print(req.form,file=logfile,end='|')
       print(req.user_agent,file=logfile,end='|')
       print(req.remote_addr,file=logfile,end='|')
       print(res,file=logfile)
app.run()