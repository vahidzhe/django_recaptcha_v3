from django.shortcuts import render,HttpResponse
from django.conf import settings

from .forms import UserRegister
import requests
# Create your views here.
def index(request):
    return HttpResponse("hfre")

def register(request):
   
    form = UserRegister(request.POST or None)
    

    secret_key = settings.RECAPTCHA_SECRET_KEY
    response = request.POST.get('g-recaptcha-response')
    # captcha verification
    data = {
        'response': response,
        'secret': secret_key
    }
    resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result_json = resp.json()

    print(result_json)

    if not result_json.get('success'):
        return render(request, 'user/register.html',context= {'form':form,'is_robot': True})
    else:
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()

    return render(request,'user/register.html',context={'form':form,'site_key': settings.RECAPTCHA_SITE_KEY})