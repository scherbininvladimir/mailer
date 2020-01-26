import threading
import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.shortcuts import redirect

from app.models import Message

class StatusView(ListView):
    queryset = Message.objects.all().order_by('-pk')[:10]
    template_name = 'status.html'

class MessageView(CreateView):
    success_url = '/'
    model = Message
    template_name = 'message.html'
    fields = ['msg', 'delay']

    def form_valid(self, form):
        def send_message():
            message = Mail(
                from_email='scherbinin.vladimir@gmail.com',
                to_emails='scherbinin.vladimir@gmail.com',
                subject='sf-e2-homework',
                html_content=msg.msg
            )
            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                msg.is_sent = True
                msg.save()
            except Exception as e:
                print(e.message)
        msg =  form.save()
        t = threading.Timer(msg.delay, send_message)
        t.start()
        return redirect(self.success_url)