from django import template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from chat.models import Author, Message
# Create your views here.
def lobby(request):
    if 'Username' in request.session.keys():
        context = { 'username' : request.session['Username']}
        template = loader.get_template('lobby.html')
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/login')  
    # return render(request, 'lobby.html')

def login(request):
    if request.method == "GET":
        if 'Username' in request.session.keys():
            return redirect('/')
        else:
            return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            author = Author.objects.get(Username=username, Password=password)
            request.session['Username'] = author.Username
            template = loader.get_template('lobby.html')
            context = { 'username' : request.session['Username']}
            return HttpResponse(template.render(context, request))
        
        
        except:
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

        if len(Author.objects.filter(Username=username)) > 0:
            template = loader.get_template('register.html')
            error_message = "Username already exists"
            return HttpResponse(template.render({'error_message': error_message},request))

        new_author = Author(Username=username, Password=password,
                       Name=name, Surname=surname)
        new_author.save()
        
        return redirect('/login')
    
def logout(request):
    if 'Username' in request.session.keys():
        del request.session['Username']
        request.session.modified = True
        return redirect('/login')
    else:
        pass