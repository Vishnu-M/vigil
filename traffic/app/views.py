from django.shortcuts import render
from pyrebase import pyrebase

config = {
  #secret key
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def sign_in(request):
        return render(request, "signin.html")


def welcome(request):
        return render(request, "welcome.html")


def post_signin(request):
        email=request.POST.get('email')
        password = request.POST.get("pass")
        try:
                user = auth.sign_in_with_email_and_password(email,password)
                print(user)
                return render(request, "welcome.html",{"e":email})
        except:
                message = "invalid cerediantials"
                return render(request,"signin.html",{"msg":message})

def sign_up(request):
        return render(request,"signup.html")

def post_signup(request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        auth.create_user_with_email_and_password(email, password)
        return render(request, "signin.html")
