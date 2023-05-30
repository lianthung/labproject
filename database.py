from sqlalchemy import create_engine, text
from flask import jsonify, redirect, url_for
import os

url = "mysql+pymysql://labuser:labpassword@127.0.0.1:3306/labdb"

engine = create_engine(url)

def load_patients_from_db(test_date):
    with engine.connect() as conn:
        query = text("SELECT * FROM patient WHERE test_date=:test_date")
        result = conn.execute(query, {"test_date": test_date})
        patients = []
        for row in result.all():
            patients.append(row._asdict())
    return patients

def load_patient_from_db(id):
    with engine.connect() as conn:
        query = text("SELECT * FROM patient WHERE id=:id")
        result = conn.execute(query, {"id":id})
        for row in result.all():
            patient = row._asdict()
    return patient

def add_patient_to_db(data):
    with engine.connect() as conn:
        query = text(
            f"INSERT INTO patient (test_date, sl_no, pname, age, gender, address, mobile, ref_doctor, radiologist, investigation) VALUES (:test_date, :sl_no, :pname, :age, :gender, :address, :mobile, :ref_doctor, :radiologist, :investigation)")

        conn.execute(query,
                     {
                         "test_date": data['test_date'],
                         "sl_no": data['sl_no'],
                         "age": data['age'],
                         "pname": data['pname'],
                         "gender": data['gender'],
                         "address": data['address'],
                         "mobile": data['mobile'],
                         "ref_doctor": data['ref_doctor'],
                         "radiologist": data['radiologist'],
                         "investigation": data['investigation']
                     })
        conn.commit()
    #return redirect('/hmingziahna')
    return redirect(url_for('hmingziahna'))


def add_test_report_to_db(data):
    with engine.connect() as conn:
        query = text(f"UPDATE patient SET investigation=:investigation, rate=:rate, test_result=:test_result WHERE id=:id")
        print(data)
        conn.execute(query, {
            "id": data['id'],
            "investigation": data['investigation'],
            "rate": data['rate'],
            "test_result": data['ckeditor']})

        conn.commit()
    return


def update_patient_to_db(id):
    return

def search_patient(query):
    return
