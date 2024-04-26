from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def index(request):
    return render(request, "index.html")


def create_user(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = make_password(request.POST["password"])
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exists.")
        else:
            User.objects.create(name=name, email=email, password=password)
            return HttpResponse("User created successfully!")


def table(request):
    users = User.objects.all()
    return render(request, "table.html", {"users": users})


def delete_user(request, pk):
    User.objects.get(id=pk).delete()
    return redirect("/data/")


def update_user(request, uid):
    user_obj = User.objects.get(id=uid)
    return render(request, "update.html", {"user_obj": user_obj})


def update_data(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        name = request.POST["name"]
        email = request.POST["email"]
        User.objects.filter(id=uid).update(name=name, email=email)
        return HttpResponse("User Update Sucessfuly")


def login(request):
    return render(request, "login.html")


# def login_view(request):
#     if request.method == "POST":
#         user = User.objects.get(email=request.POST["email"])
#         if check_password(request.POST["password"], user.password):
#             request.session["login"] = True
#             request.session["username"] = user.name
#             return redirect("/data/")
#         else:
#             return HttpResponse("Invalid Email And Password")


def product(request):
    return render(request, "product.html")


def add_product(request):
    if request.method == "POST":
        name = request.POST["name"]
        descripiton = request.POST["description"]
        image = request.FILES.get("image")
        Product.objects.create(product_name = name , descripiton=descripiton,
                               image=image)
        return HttpResponse("Product  Added Successfully")




def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            password = user.password
            if check_password(password, user.password):
                return redirect("/data/")
            else:
                return HttpResponse("password Incorrect")
        else:
            return HttpResponse("email ID not Ragister")    
