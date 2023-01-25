from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # creating a dictionary 
    # bold message atches to string and string replaces bold message
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Morvern'}
    return render(request, 'rango/about.html', context=context_dict)


