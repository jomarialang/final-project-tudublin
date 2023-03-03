from django.shortcuts import render
from decorators import auth
# Create your views here.

@auth.is_authenticated
def homepage(request):

    return render(request, 'homepage.html')

