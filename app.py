import random
from flask import Flask, render_template

app = Flask(__name__)

card_marks = 'star,sun,moon'
marks = card_marks.split(',')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random_mark')
def random_mark():
    mark = random.choice(marks)
    return mark

if __name__ == '__main__':
    app.run(debug=True)
