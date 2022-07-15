# from cProfile import label
# from distutils.log import debug
# from unicodedata import name
# from cProfile import label
# from crypt import methods
# from flask import Flask
# from flask import (Flask, request, render_template, redirect, url_for, session, send_file)
# from flask_wtf import FlaskForm, RecaptchaField

# from wtforms import (StringField, SubmitField, RadioField, DateTimeField, SelectField, TextAreaField, DateField)
# from wtforms.validators import DataRequired

# # from wttforms.validators import DataRequired
# # except Exception as e:
# # print("Some Modules are missing")
# # except Exception as e:
# #     print("Some Modules are missing")

# app = Flask(__name__)
# app.config["SECRET_KEY"]= 'mysecretkey'

# # class Widgets(FlaskForm):
# #     FirstName=StringField(label="First Name")
# #     LastName= StringField(label = "Last Name")
# @app.route("/", methods=["Get", "POST"])
# def home():
#     return render_template('index.html', form=form)

# if (__name__)== "__main__":
#     app.run(debug=True)

# from crypt import methods
# from tokenize import Number
import MySQLdb
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


app = Flask(__name__)
app.config['SECRET_KEY']= 'LetMeTellYOuASecret'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '4jt2cF@1'
app.config['MYSQL_DB'] = 'license_plate_number'

mysql = MySQL(app)

# class RegistrationForm(FlaskForm):
#     Name = StringField('Name', validators=[InputRequired()])
#     Number = StringField ('License Plate Number')



@app.route('/')
@app.route('/form', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'Name' in request.form and 'Number' in request.form :
        Name = request.form['Name']
        Number = request.form['License Plate Number']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE Name = % s', (Name, ))
        account = cursor.fetchone()
        if account:
            msg = 'Vehicle already parked!'
        # elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        #     msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', Name):
            msg = 'Username must contain only characters and numbers !'
        elif not Name or not Number:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s)', (Name, Number ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('index.html', form =msg)
    # print(request.form)
    # form = RegistrationForm()

    # if form.validate_on_submit():
    #     return f''' <h1> Welcome {form.Name.data} <h1>'''
    # return render_template('index.html', form=form)

if __name__=='__main__':
    app.run(debug=True)
