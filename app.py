from flask import Flask, render_template, request
import sys
import re

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    regex = text = result = ''
    if request.method == 'POST':
        regex = request.form.get('regex')
        text = request.form.get('text')
        if regex and text:
            result = re.match(regex, text)
        return render_template('index.html', regex=regex, text=text, result=result)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
