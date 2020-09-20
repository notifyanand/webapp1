from flask import Flask, render_template, request

app = Flask(__name__)

class Person:
  def __init__(self, name, phone):
    self.name = name
    self.phone = phone

contacts = []

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

@app.route('/addressbook', methods=['POST', 'GET'])
def addressbook():
    person1 = Person("dummy", "dummy")

    returnText = "Method Called Is : " + request.method
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        person1 = Person(name, phone)
        contacts.append(person1)
        print("returnText:"+returnText)
        return render_template('addressbook.html', contacts=contacts)
    else:
        return render_template('addressbook.html', contacts=contacts)

if __name__ == "__main__":
    app.run(debug=True)