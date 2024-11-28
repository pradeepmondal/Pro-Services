from celery import shared_task
from application.models import ServiceRequest, ServiceProfessional, User, Customer
from application.database import db
import flask_excel as excel
import time
from datetime import datetime
from application.celery.mail import send_email
from flask import current_app as app
from jinja2 import Environment, FileSystemLoader



@shared_task(ignore_result = False)
def create_sr_csv(sp_id=None):
    with app.app_context():
        if sp_id is None:
            srs = ServiceRequest.query.all()
        else:
            srs = ServiceRequest.query.filter((ServiceRequest.sp_id == sp_id) & ((ServiceRequest.status == 'Completed') | (ServiceRequest.status == 'Closed'))).all()

        if srs:
        
            for sr in srs:
                sr.service_name = sr.service.name
                sr.customer_name = sr.customer.f_name + ' ' + sr.customer.l_name
                sr.service_professional = sr.sp.f_name + ' ' + sr.sp.l_name
            
            column_names = ['sr_id', 's_id', 'service_name', 'c_id', 'customer_name', 'sp_id',  'service_professional', 'description', 'request_date', 'completion_date', 'status', 'remarks', 'rating']

            

            csv = excel.make_response_from_query_sets(query_sets= srs, column_names = column_names, file_type = 'csv')


    
        if sp_id is None:
            file_path = './application/celery/admin_downloads/sr_report.csv'
        else:
            file_path = f'./application/celery/admin_downloads/professionals_reports/{sp_id}_sr_report.csv'

        if srs:
            file = open(file_path, 'wb')
            file.write(csv.data)
            file.close()
        else:
            file = open(file_path, 'w')
            file.write('No Service Requests')
            file.close()


        return file_path


environment = Environment(loader=FileSystemLoader('.'))

@shared_task(ignore_result = True)
def send_daily_reminder():
    with app.app_context():

        sps = ServiceProfessional.query.all()
        

        sps_with_active_srs = []
        sps_without_active_srs = []

        for sp in sps:
            sp.email = User.query.filter(User.uid == sp.sp_id).first().email
            has_active = False
            sp.active_srs = []
            for sr in sp.srs:
                if sr.status in ['Requested', 'In Progress']:
                    
                    sp.active_srs = [request for request in sp.srs if request.status in ['Requested', 'In Progress']]
                    has_active = True
                    sps_with_active_srs.append(sp)
                    break
            if not has_active:
                sps_without_active_srs.append(sp)

        active_sr_template = environment.get_template('application/celery/email_templates/active_sr_template.html')

        for sp in sps_with_active_srs:
            to = sp.email
            subject = 'Daily Reminder from Pro Services'
            content = active_sr_template.render(sp = sp, service_requests = sp.active_srs)

            send_email(to=to, subject=subject, content=content)



@shared_task(ignore_result = True)
def send_monthly_report():
    with app.app_context():

        customers = Customer.query.all()

        monthly_report_template = environment.get_template('application/celery/email_templates/monthly_report_template.html')

        for customer in customers:
            customer.email = User.query.filter(User.uid == customer.c_id).first().email

            customer_total_requests = 0
            customer_completed_requests = 0
            customer_active_requests = 0

            customer.srs = [sr for sr in customer.srs if sr.request_date.month == datetime.now().month - 1  ]

            for sr in customer.srs:
                sr.request_date = sr.request_date.date()

                if sr.completion_date:
                    sr.completion_date = sr.completion_date.date()

                customer_total_requests += 1
                if(sr.status in ['Completed', 'Closed']):
                    customer_completed_requests += 1
                elif(sr.status in ['Requested', 'In Progress']):
                    customer_active_requests += 1


            to = customer.email
            subject = 'Monthly Report - Pro Services'
            content = monthly_report_template.render( customer = customer, service_requests = customer.srs, customer_total_requests = customer_total_requests, customer_completed_requests = customer_completed_requests, customer_active_requests = customer_active_requests)

            send_email(to=to, subject=subject, content=content)



        



        

