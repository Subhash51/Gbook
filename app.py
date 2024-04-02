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

# A simplified data structure to represent cylinders (you'll likely use a database)
cylinders = [
    {'name': 'Oxygen Cylinder', 'price': 100, 'capacity': '10L'},
    {'name': 'Nitrogen Cylinder', 'price': 150, 'capacity': '15L'},
    {'name': 'Medical Gas Cylinder', 'price': 80, 'capacity': '5L'}
]

@app.route('/main')
def index4():
    sort_option = request.args.get('sort', 'default')  # Get the sort option from the query string

    # Basic sorting logic (you'll need to adjust for real scenarios)
    if sort_option == 'asc':
        sorted_cylinders = sorted(cylinders, key=lambda x: x['price'])
    elif sort_option == 'desc':
        sorted_cylinders = sorted(cylinders, key=lambda x: x['price'], reverse=True)
    else:
        sorted_cylinders = cylinders

    return render_template('mainPage.html', cylinders=sorted_cylinders)

if __name__ == '__main__':
    app.run(debug=True)
