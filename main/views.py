from django.shortcuts import redirect, render
import requests
from django.http import JsonResponse
import geoip2.database
from .models import *
from .forms import *
from MyInfo.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.http import JsonResponse



def get_user_ip(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_user_city(ip):
    api_key = '2fc240411f3c73112c581b281464ea10'
    url = f'http://api.ipstack.com/{ip}?access_key={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        return data.get('city')
    except requests.RequestException as e:
        print(f'Error fetching data from ipstack: {e}')
        return None

def get_user_location(request):
    ip = get_user_ip(request)
    city = get_user_city(ip)
    return city,ip


def HomePage(request):
    city,ip = get_user_location(request)
    if city is not None:
        UserInfo.objects.create(city = city)
    else:
        UserInfo.objects.create(city = ip)
    maininfo = MainInformations.objects.first()
    forskills = ForSkills.objects.all()
    about = About.objects.all()
    abouttxt = AboutTxt.objects.first()
    staffstory = StaffStory.objects.all()
    testimonials = Testimonials.objects.all()
    comp_works = Comp_works.objects.all()
    form = SendMessageForm
    siteurl = SiteURL.objects.get()
    context = {
        'maininfo': maininfo,
        'forskills': forskills,
        'about': about,
        'abouttxt': abouttxt,
        'staffstory': staffstory,
        'testimonials': testimonials,
        'comp_works': comp_works,
        'siteurl': siteurl,
    }
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            subject = f'Hello {obj.name}. Thank you for your opinion.'
            body = 'I will respond to you soon.'
            from_email = EMAIL_HOST_USER
            to = [obj.email]
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=from_email,
                to=to
            )
            obj.save()
            email.send()
            return JsonResponse({'message': 'Message sent successfully!'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    return render(request, 'index2.html', context)


def BlogPage(request,id,title):
    comp_works = Comp_works.objects.get(id = id,title = title)
    subwork = SubWork.objects.filter(pk = comp_works.id)
    maininfo = MainInformations.objects.first()

    context = {
        'comp_works':comp_works,
        'subwork':subwork,
        'maininfo':maininfo

              }
    return render(request,'blog-single.html',context)




def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_location_from_ip(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Unable to fetch location from IP-API"}
    except Exception as e:
        return {"error": str(e)}

def user_location_view(request):
    ip = get_client_ip(request)
    location = get_location_from_ip(ip)
    return JsonResponse(location)
