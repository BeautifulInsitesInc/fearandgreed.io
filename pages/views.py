from django.shortcuts import render
from django.core.mail import send_mail

def temp(request):
	return render(request, "temp.html",{})

def home(request):
	return render(request, "home.html",{})

def about(request):
	return render(request, "about.html",{})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message_phone = request.POST['message-phone']
		message_service = request.POST['message-service']
		message_subject = request.POST['message-subject']
		message = request.POST['message']

		# Send eamil
		send_mail(
			'Message from fearandgreed.io', # subject
			message, # message
			message_email, # from email
			['fearandgreed.io@gmail.com'], # to email
			fail_silently=False,
			)

		return render(request, "contact.html",{'message_name':message_name})
	else:
		# return the page
		return render(request, "contact.html",{'test':"testgood"})

def blog(request):
	return render(request, "blog.html",{})
