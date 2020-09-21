from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///addressbook.db'
db = SQLAlchemy(app)
Bootstrap(app)

class Person:
  def __init__(self, name, phone):
    self.name = name
    self.phone = phone

class AddressBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(25))

    def __repr__(self):
        return self.id


@app.route('/addressbook', methods=['POST', 'GET'])
def addressbook():

    returnText = "Method Called Is : " + request.method
    action = request.args.get('action')
    id = request.args.get('id')

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        new_contact = AddressBook(name=name, phone=phone)
        try:
            db.session.add(new_contact)
            db.session.commit()
        except:
            return 'There was an issue adding the contact'
    elif action == "delete":
        contact_to_delete = AddressBook.query.get_or_404(id)
        try:
            db.session.delete(contact_to_delete)
            db.session.commit()
        except:
            return 'There was a problem deleting that contact'

    contacts = AddressBook.query.order_by(AddressBook.name).all()
    return render_template('addressbook.html', contacts=contacts)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    returnText = "Method Called Is : " + request.method
    print("returnText:"+returnText)
    return "Welcome to the Home Page!<br>" + returnText

@app.route('/greet')
def greet():
    returnText = "Method Called Is : " + request.method
    username = request.args.get('name')
    if username is None:
        return "Welcome to the Home Page!<br> Pass a parameter in the URL?name=something to see the magic happen <br>" + returnText
    else:
        print("returnText:"+returnText + " name parameter value = "+ username)
        return "<b>"+ username +" </b>"+ "Welcome to the Home Page!<br>" + returnText

@app.route('/age', methods=['POST', 'GET'])
def age():

    returnText = "Method Called Is : " + request.method
    if request.method == 'POST':
        age = request.form['age']
        print("returnText:"+returnText)
        return render_template('age.html', age=age)
    else:
        return render_template('age.html', age=0)

if __name__ == "__main__":
    app.run(debug=True)