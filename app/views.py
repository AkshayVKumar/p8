from django.shortcuts import render
from app import forms
from app.models import *
# Create your views here.

# def sam(request):
#     form=forms.from_demo()
#     if request.method=='POST':
#         form=forms.from_demo(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#     return render(request,'img.html',context={'form':form,'data':"hello world"})

def disp(request):
    data=Model_img.objects.all()
    return render(request,'disp.html',context={'objects':data})


def sam(request):
    register=False
    if request.method=="POST":
        user_form=forms.User_Form(request.POST)
        user_data_form=forms.User_data_form(request.POST,request.FILES)
        if user_form.is_valid() and user_data_form.is_valid():
            user=user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            user_data=user_data_form.save(commit=False)
            user_data.user=user

            if 'profile_pic' in request.FILES:
                user_data.profile_pic=request.FILES['profile_pic']
            user_data.save()
            register=True
    else:
        user_form=forms.User_Form()
        user_data_form=forms.User_data_form()
    
    d={'form':user_data_form,'form_user':user_form,'register':register}
    return render(request,'img.html',context=d)