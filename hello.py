from flask import Flask, render_template, url_for, request, redirect

import csv

app = Flask(__name__)
print(__name__)

# @app.route('/<string:page_name>')
# def my_home(page_name):
#     return render_template('index.html') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', mode='a') as database:
       subject = data["subject"] 
       email = data["email"]
       message = data["message"]
       csv_writer = csv.writer(database, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
       csv_writer.writerow([subject,email,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():    
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)           
        return 'YOU ARE NOW ONE OF THE BEST ANIME LOVERS!!'
    else:
        return 'something_went_wrong. Try again!'