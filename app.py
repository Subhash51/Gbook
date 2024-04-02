from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/login')
def index2():
    return render_template('mainPage.html')

@app.route('/thank')
def index3():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)
