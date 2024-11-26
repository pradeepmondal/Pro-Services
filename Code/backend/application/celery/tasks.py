from celery import shared_task
from application.models import ServiceRequest
from application.database import db
import flask_excel as excel
import time
from flask import current_app as app

@shared_task(ignore_result = False)
def subtract(x, y):
    time.sleep(10)
    return x-y

@shared_task(ignore_result = False)
def create_sr_csv():
    with app.app_context():
       
        print(db.session.query(ServiceRequest).all())
        srs = ServiceRequest.query.all()
        
        for sr in srs:
            sr.service_name = sr.service.name
            sr.customer_name = sr.customer.f_name + ' ' + sr.customer.l_name
            sr.service_professional = sr.sp.f_name + ' ' + sr.sp.l_name
        
        column_names = ['sr_id', 's_id', 'service_name', 'c_id', 'customer_name', 'sp_id',  'service_professional', 'description', 'request_date', 'completion_date', 'status', 'remarks', 'rating']

        

        csv = excel.make_response_from_query_sets(query_sets= srs, column_names = column_names, file_type = 'csv')

    

        file_path = './application/celery/admin_downloads/sr_report.csv'

        file = open(file_path, 'wb')
        file.write(csv.data)
        file.close()

        return file_path




