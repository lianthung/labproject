import datetime
from flask_ckeditor import CKEditor
from flask import Flask, request, render_template, redirect, send_file
from docxfile import open_file
from database import load_patients_from_db, load_patient_from_db, add_patient_to_db, add_test_report_to_db

app = Flask(__name__)
ckeditor = CKEditor(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/hmingziahna', methods=['GET', 'POST'])
def hmingziahna():
    if request.method == 'GET':
        patients = load_patients_from_db(datetime.date.today())

    if request.method == 'POST':
        data = request.form
        add_patient_to_db(data)
        patients = load_patients_from_db(datetime.date.today())

    return render_template('hmingziahna.html', patients=patients)

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        patients = load_patients_from_db(datetime.date.today())
        spatient = {}

    if request.method == 'POST':
        add_test_report_to_db(request.args['id'], request.args['rate'], request.args['investigation'], request.args['test_result'])

    return render_template('result.html', spatient=spatient, patients=patients)

@app.route('/result/<id>', methods=['GET', 'POST'])
def p_detail(id):
    patients = load_patients_from_db(datetime.date.today())
    spatient = load_patient_from_db(id)
    #print("spatient in app.py: " + str(spatient))
    if request.method == 'POST':
        print(request.form['investigation'])
        result = request.form
        add_test_report_to_db(result)

    return render_template('result.html', spatient=spatient, patients=patients)

@app.route('/open_patient_file')
def open_patient_file():
    open_file()
    return "nothing"

#if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=True)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)