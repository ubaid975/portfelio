from django.shortcuts import render
from portfelio.models import contact
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        message=request.POST['message']
        contacts=contact(first_name=fname,last_name=lname,phone=phone,email=email,message=message)
        contacts.save()
        messages.success(request,'Form Submited Successfully')
        return render(request,'portfelio/index.html')

    return render(request,'portfelio/index.html')
