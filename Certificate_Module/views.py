from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render,redirect
import csv


from students.models import student

from .utils import render_to_pdf,render_to_file #created in step 4




from django.core.mail import send_mail,EmailMultiAlternatives,EmailMessage
from .settings import EMAIL_HOST_USER

# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#             'today': 'Today', 
#             'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = render_to_pdf('certificate.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')




class GeneratePdf1(View):
    def get(self, request, *args, **kwargs):
        objs=student.objects.all()
        for obj in objs:

            data = {
                'name':obj.name,
                'branch':obj.branch
            }
            if not(obj.sent):
                pdf = render_to_file('certificate.html', data)
                subject= "Zealicon Participation Certificate"
                body = "Hope Zealicon 2k19 touched the emotional chords in you and the event continues to live in your memories forever. Here’s a memento of the fun-loaded extravaganza.\n \n\nRegards,\nSATWIK SINGH\n(Creative Head)"
                from_email=EMAIL_HOST_USER
                to_list=[obj.email]
                message = EmailMessage(subject, body, from_email, to_list)
                file_path = "C:/Users/Archit/Projects/Certificate_Module/temp.pdf"
                pdf1 = open(file_path, 'rb')
                message.attach('certificate.pdf', pdf1.read(), 'application/pdf')
                message.send()
                obj.sent=True
                obj.delete()
                pdf=render_to_pdf('certificate.html', data)
            else:
                return render(request,"not_sent.html",{})
        # return HttpResponse(pdf, content_type='application/pdf')
        return render(request,"sent_all.html",{})


def new(request):
	return render(request,"certificate.html",{})


def load_csv(request):
    csv_filepathname="C:/Users/Archit/Projects/Certificate_Module/student_data.csv"
    dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
    for row in dataReader:
        stu = student()
        stu.name = row[0]
        stu.email= row[1]
        stu.branch = row[2]
        stu.save()
    return render(request,"loader.html",{})
