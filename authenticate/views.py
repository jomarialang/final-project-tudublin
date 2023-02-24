from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from services.mailgun import send_token
from django.utils.encoding import force_str
from django.contrib.auth import authenticate, login

def login_view(request): 
    errors = {}
    username = request.POST.get('username') or ''
    password = request.POST.get('password') 
    
    if request.method == 'POST': 
        

        print(username, password)

        if username == '': 

            errors['username'] = "Username is required!"
        
        
        if password == '': 

            errors['password'] = "Password is required!"
        elif len(password) < 17: 

            errors['password'] = 'Password must be at least 16 characters!'

        
    if not bool(errors):
        
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)

            return redirect('/dashboard')
        else: 

            pass

    context = {
        'errors': errors
    }        

    return render(request, 'login.html', context)




def register_view(request): 
    errors = {}
    username = request.POST.get('username') or ''
    email = request.POST.get('email') or ''
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm-password') 

    if request.method == "POST":

        if username == '': 

            errors['username'] = 'Username is required!'
        else: 

            find_username = User.objects.filter(username=username).exists()

            if find_username: 
                errors['username'] = 'Username provided already exist!'

        if email == '': 

            errors['email'] = 'Email is required!'
        else: 
            find_email = User.objects.filter(email=email).exists()
            if find_email: 

                errors['email'] = 'Email provided already exist!'

        if password is None:

            errors['password'] = 'Password is required!'

        elif len(password) < 17: 

            errors['password'] = 'Password must be at least 16 characters!'

        if confirm_password is None: 

            errors['confirm_password']  = 'Password must be confirmed!'

        if password and confirm_password: 

            if password != confirm_password:

                errors['password'] = 'Passwords does not match!'



        if not bool(errors): 

            
            # No errors occured. Run the code below.
            

            new_user = User(email=email, username=username)
            new_user.is_staff = True
            new_user.set_password(password)
            new_user.save()
            
            context = { 
                'username': username, 
                'email': email
            }

            return render(request, 'register_success.html', context)


    context = { 
        'errors': errors, 
        'username': username,
        'email': email
    } 
    return render(request, 'register.html', context)






def register_success(request): 


    return render(request, 'register_success.html')


def activate(request, uid64, token): 
    print("activated")
    """
    The code below was roughly taken from the website pylessons. 
    Website: https://pylessons.com/
    Lesson link: https://pylessons.com/django-email-confirm
    """
    user = User()

    try: 
        pass
        uid = force_str()
    except: 
        pass
    return redirect('dashboard')