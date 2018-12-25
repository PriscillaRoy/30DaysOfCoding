from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
    # return a rendered template - which looks into the templates folder
    # for the page that has the text data
    return render_template('home.html')

    # Creating layouts allows us to wrap templates
    # so that code need not be re-written

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/articles2')
def articles2():
    return render_template('articles2.html', articles= Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id = id)


if __name__ == '__main__':
    app.run(debug=True)