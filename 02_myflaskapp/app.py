from flask import Flask, render_template

app = Flask(__name__)

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
if __name__ == '__main__':
    app.run(debug=True)