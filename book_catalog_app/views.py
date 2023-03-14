from django.shortcuts import render,redirect
from .models import User,Books
from passlib.hash import sha512_crypt as sha512
import string
import random
from django.contrib import messages
import requests
from django.http import  JsonResponse
import json 

# Create your views here.
def index(request):
    if "BookCatalogUserId" in request.session:
        if User.objects.filter(private_token=request.session['BookCatalogUserId']):
            user = User.objects.get(private_token=request.session['BookCatalogUserId'])
            books = Books.objects.filter(user = user)
            for book in books:
                authors = book.author
                authors = authors.replace("[","")
                authors = authors.replace("]","")
                authors = authors.split(",")
                author_id = ""
                for x in authors:
                    author_id = author_id + str(x) + ","
            author_id = author_id[:-1]
            print(author_id)
            return render(request,'index.html',{'user':user,'books':books,'author_id':author_id})
        return redirect('login')
    return redirect('login')

def login(request):
    return render(request,'login.html')

def login_user(request):
    email = request.POST['email']
    password = request.POST['pwd']
    password=sha512.hash(password, rounds=5000,salt="bookcatalogsalt")
    print(password)
    if User.objects.filter(email=email,password=password):
        user = User.objects.get(email=email,password=password)
        user.private_token = ''.join(random.choices(string.ascii_uppercase +string.digits, k=15))
        request.session['BookCatalogUserId']=user.private_token
        user.save()
        return redirect('index')
    messages.info(request,'error')
    return redirect('login')

def logout(request):
    del request.session['BookCatalogUserId']
    return redirect('login')

def get_books(request):
    isbn = request.POST['isbn']
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn
    data = requests.get(url).json()
    useful_data = []
    for x in data["items"]:
        temp_useful_data = {}
        lst = []
        for y in x["volumeInfo"]["authors"]:
            lst.append(y)
        temp_useful_data["authors"] = lst
        temp_useful_data["title"] = x["volumeInfo"]["title"]
        temp_useful_data["pageCount"] = x["volumeInfo"]["pageCount"]
        temp_useful_data["image_url"] = x["volumeInfo"]["imageLinks"]["thumbnail"]
        if "averageRating" in x["volumeInfo"]:
            temp_useful_data["averageRating"] = x["volumeInfo"]["averageRating"]
        else:
            temp_useful_data["averageRating"] = 4
    useful_data.append(temp_useful_data)
    return JsonResponse(useful_data, safe=False)

def add_book_to_collection(request):
    if "BookCatalogUserId" not in request.session or not User.objects.filter(private_token=request.session['BookCatalogUserId']).exists():
        return redirect('login')
    
    isbn = request.GET['isbn']
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn
    data = requests.get(url).json()
    useful_data = []
    for x in data["items"]:
        temp_useful_data = {}
        lst = []
        for y in x["volumeInfo"]["authors"]:
            lst.append(y)
        temp_useful_data["authors"] = lst
        temp_useful_data["title"] = x["volumeInfo"]["title"]
        temp_useful_data["pageCount"] = x["volumeInfo"]["pageCount"]
        temp_useful_data["image_url"] = x["volumeInfo"]["imageLinks"]["thumbnail"]
        if "averageRating" in x["volumeInfo"]:
            temp_useful_data["averageRating"] = x["volumeInfo"]["averageRating"]
        else:
            temp_useful_data["averageRating"] = 4
    useful_data.append(temp_useful_data)

    user = User.objects.get(private_token=request.session['BookCatalogUserId'])
    for x in useful_data:
        book = Books.objects.create(user=user,title=x['title'],author=x['authors'],page_count=x['pageCount'],image_url=x['image_url'],average_rating=x['averageRating'])
        book.save()
    return redirect('index')

def delete(request):
    bookid = request.GET['id']
    book = Books.objects.get(id=bookid)
    book.delete()
    return redirect('index')