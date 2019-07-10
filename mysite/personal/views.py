from django.shortcuts import render

# Create your views here.
def index(request):
    #render to html file path inside template directory (personal/templates/personal/home.html)
    # Jinja templating
    return render(request, 'personal/home.html')

def contact(request):
    # render to html file path inside template directory (personal/templates/personal/basic.html)
    return render(request, 'personal/basic.html' ,{'content':['If you would like to contact me, please email me.','abti0810@gmail.com']})