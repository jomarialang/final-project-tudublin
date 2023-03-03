import functools
from django.shortcuts import redirect



def is_authenticated(view_func): 

    @functools.wraps(view_func)

    def wrapper(request, *args, **kwargs): 

        if request.user.is_authenticated: 

            return redirect('dashboard')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper