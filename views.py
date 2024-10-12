from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
def profile_f(request):
    if request.method == 'POST':
        usern = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password != password2 :
            messages.error(request, 'Password Did not Match!')
            return HttpResponseRedirect('/profile_f')

        elif User.objects.filter(username=usern).exists():
            messages.error(request, 'This User Already Exist!')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'This Email Already Exist!')

        elif len(usern)<4:
            messages.warning(request, 'Incorrect User, Enter Your Username at least 4 Characters of Number')

        elif len(email)<22:
            messages.warning(request, 'Please Enter Your Email at least 22 Characters')
        
        elif len(password)<6:
            messages.error(request, 'Password at least 6 of characters Number')

        
        else:

            user_obj = User.objects.create_user(usern,email,password)
            user_obj.save()
            messages.success(request, 'Your Sign Up Successfylly')
            return HttpResponseRedirect('/profile_login')
    
    return render(request, 'forms.html')


# Login ---------------------------------------
def login_f(request):
    if request.method == 'POST':
        usern = request.POST.get('username')
        passw = request.POST.get('password')

        user = authenticate(request, username=usern, password=passw)

        if user is not None:
            login(request, user)
            messages.success(request, 'Your Login Was Successfull')
            return HttpResponseRedirect('/profile_login')

        else:
            messages.error(request, 'Invalid Username or Password !')
            return HttpResponseRedirect('/profile_login')

    else:
        return render(request, 'profile_login.html')