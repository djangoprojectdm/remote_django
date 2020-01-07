from datetime import datetime

from django.shortcuts import render,redirect
from.models import registrationdata
from forms import registrationform,loginform
from django.http.response import HttpResponse
def registration_view(request):
    if request.method=="POST":
        rform = registrationform(request.POST)
        if rform.is_valid():
            fname =request.POST.get('firstname')
            lname = request.POST.get('lastname')
            uname = request.POST.get('username')
            pwd = request.POST.get('password')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            gender = rform.cleaned_data.get('gender')
            dob = datetime.now()

            data=registrationdata(
                firstname=fname,
                lastname=lname,
                username=uname,
                password=pwd,
                mobile=mobile,
                email=email,
                gender=gender,
                date_of_birth=dob


            )
            data.save()
            rform=registrationform()
            return render(request,'reg.html',{'rform':rform})
        else:
             return HttpResponse("user missed some data")
    else:
        rform = registrationform()
        return render(request,'reg.html',{'rform':rform})
def login_view(request):
    if request.method=="POST":
        lform = loginform(request.POST)
        if lform.is_valid():
            username1 = request.POST.get('username')
            password1 = request.POST.get('password')

            uname = registrationdata.objects.filter(username=username1)

            pwd = registrationdata.objects.filter(password=password1)

            if uname and pwd:
                return HttpResponse("success")
            else:
                return HttpResponse("faied")
        else:
            return HttpResponse("user missed data")
    else:
        lform = loginform()
        return render(request, 'log.html', {'lform':lform})







# Create your views here.
