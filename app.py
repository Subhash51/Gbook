from flask import *
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Gbook"
mongo = PyMongo(app)

@app.route('/insert_data', methods=['POST'])
def insert_data():
    username = request.form['username']
    print(username,flush=True)
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirmPassword']

    if password != confirm_password:
        return jsonify({"message": "Passwords do not match"})

    collection = mongo.db.users  
    result = collection.insert_one({"username": username, "email": email, "password": password})

    return jsonify({"message": "Data inserted successfully", "id": str(result.inserted_id)})


@app.route('/')
def index():
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
  


@app.route('/thanks')
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
