from django import template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def lobby(request):

    return render(request, 'chat/lobby.html')

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
        # return redirect('/login')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if username == "admin" and password == "admin":
            request.session['Username'] = username
            return redirect('/lobby')
        else:
            template = loader.get_template('login.html')
            context={'error_message': 'Unmatch user data'}
            return HttpResponse(template.render(context, request))

@csrf_exempt
def register(request):
    if request.method == "GET":
        template = loader.get_template('register.html')
        return HttpResponse(template.render())
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        surname = request.POST['surname']

        # if len(Author.objects.filter(Username=username)) > 0:
        #     template = loader.get_template('register.html')
        #     error_message = "Username already exists"
        #     return HttpResponse(template.render({'error_message': error_message},request))

        # new_author = Author(Username=username, Password=password,
        #                Name=name, Surname=surname)
        # new_author.save()
        
        return redirect('/login')