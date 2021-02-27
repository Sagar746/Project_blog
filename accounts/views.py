from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def contact(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		name=form.cleaned_data['name']
		comment=form.cleaned_data['comment']
		subject='Message from MySite.com'
		message=' %s %s' %(comment,name)
		emailFrom=form.cleaned_data['email']
		emailTo=[settings.EMAIL_HOST_USER]

		send_mail(subject,message,emailFrom,emailTo,fail_silently=True)
		
		return redirect('contact')

	context={
	'form':form
	}
	return render(request,'contact.html',context)