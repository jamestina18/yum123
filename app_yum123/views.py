from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import requests


# Define business ID 
business_id = 'gl-DfHpBukXV4pKlxOjnFg'
# Define the API_KEY, ENDPOINT, and the HEADER
API_KEY = '6x3Onh5VL7jL1l8qvo5l2wBp1tQp2K5QixW1faZXgLN0uX40qX0vvjNa2hC7s1iy5zx446hJRY1AIEinPUOY3s6rH-uIrMxmvTMgJMkhSp6Nf0Le5m9QHmp0OabAYHYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

#Define the parameters
PARAMETERS = {'term': 'restaurant',
'limit': '50',
'radius': '10000',
'offset': '50',
'location': ''
}
#Make request to yelp api
response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
# #Convert to string JSON
business_data =  response.json()
# for b in business_data['businesses']:
     
def api(request):
     zip_code = request.POST['zip_code']
     PARAMETERS['location'] = zip_code
     response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
     business_data =  response.json()
     print(business_data)
     context = {
          'restaurant_data': business_data['businesses'],
          }
     return render(request, 'Home.html',context)
# this is from the homepage that only user can comment
def must_be_looged(request):
     if 'user' not in request.session:
          messages.error(request, 'You must be loggen in! ')
     return render(request, 'Home.html')

def success(request):
     if 'user' not in request.session:
          return('/')
     return render(request, 'feed.html')

#rendering api data to the template using zipcode
def logged(request):
     zip_code = request.POST['zip_code']
     PARAMETERS['location'] = zip_code
     response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
     business_data =  response.json()
     print(business_data)
     context = {
          'restaurant_data': business_data['businesses'],
          }
     return render(request, 'feed.html',context)



def index(request):
     return render(request, 'Home.html')
#this route is for the log in navbar     
def login(request):
     return render(request,'login.html')

# this route the user to html page upon succesfull log in 
def feed_welcome(request):
     if 'user_id' not in request.session:
          return HttpResponse("<h1>You must be loggen in</h1>")
     user = User.objects.get(id=request.session['user_id'])
     context = {
          "user": user
     }
     return render(request,'feed.html', context)



#this route is for the sign up nav bar
def signup(request):
     return render(request, 'signup.html')
#signing up of thenew user will route back to log in page after success

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def new_user(request):
     if request.method == "POST":
          errors = User.objects.basic_val(request.POST)
          if len(errors) > 0:
               for k, v in errors.items():
                    messages.error(request, v)
               return redirect('/signup')
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']
          email_address = request.POST['email_address']
          profile_pic = request.POST['profile_pic']
          city = request.POST['city']
          zip_code = request.POST['zip_code']
          password = request.POST['password']
          hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
          User.objects.create(first_name=first_name,last_name=last_name,profile_pic=profile_pic, email_address=email_address,city=city,zip_code=zip_code, password=hash_pw)
     return redirect('/login')

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['profile_image'])
#     else:
#         form = UploadFileForm()
#     return(upload_file)

def login_member(request):
     if request.method == "POST":
          email_address = request.POST['email_address']
          password = request.POST['password']
          if not User.objects.authenticate(email_address, password):
               messages.error(request, 'Email and Password do not match')
               return redirect("/login")
          user = User.objects.get(email_address = email_address)
          request.session['user_id'] = user.id
          return redirect("/feed_welcome")
     return redirect('/login') 

def logout(request):
     del request.session['user_id']
     return redirect('/login')
     
def welcome_home(request):
     return render('/')


