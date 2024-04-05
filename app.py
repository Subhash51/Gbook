from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/login')
def index2():
    return render_template('login.html')

@app.route('/thank')
def index3():
    return render_template('thanks.html')

cylinders = [
    {'name': 'Oxygen Cylinder', 'price': 100, 'capacity': '10L'},
    {'name': 'Nitrogen Cylinder', 'price': 150, 'capacity': '15L'},
    {'name': 'Medical Gas Cylinder', 'price': 80, 'capacity': '5L'},
    {'name': 'Helium Cylinder', 'price': 160, 'capacity': '15L'},
    {'name': 'Oygen Cylinder', 'price': 190, 'capacity': '18L'},
    {'name': 'Medical Gas Cylinder', 'price': 60, 'capacity': '3L'},
    {'name': 'Propane Cylinder', 'price': 90, 'capacity': '8L'},
    {'name': 'Nitrogen Cylinder', 'price': 230, 'capacity': '20L'},
    {'name': 'Acetylene Gas Cylinder', 'price': 180, 'capacity': '15L'}
]

@app.route('/main')
def index4():
    sort_option = request.args.get('sort', 'default') 

    if sort_option == 'asc':
        sorted_cylinders = sorted(cylinders, key=lambda x: x['price'])
    elif sort_option == 'desc':
        sorted_cylinders = sorted(cylinders, key=lambda x: x['price'], reverse=True)
    else:
        sorted_cylinders = cylinders

    return render_template('mainPage.html', cylinders=sorted_cylinders)

if __name__ == '__main__':
    app.run(debug=True)
