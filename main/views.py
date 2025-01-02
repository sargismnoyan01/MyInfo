from django.shortcuts import redirect, render
import requests
from django.http import JsonResponse
import geoip2.database
from .models import *
from .forms import *
from MyInfo.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.http import JsonResponse
from user_agents import parse
import requests
from bs4 import BeautifulSoup



def InfoPage(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    referrer = request.META.get('HTTP_REFERER', 'Unknown')
    url = "https://www.mypersonalip.com/hy/աշխարհագրական-ip-հասցե"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    location_element = soup.find('td', text=lambda x: x and ', ' in x)  
    location = location_element.get_text(strip=True) if location_element else "Unknown Location"
    user_agent_string = request.META.get('HTTP_USER_AGENT', '')
    user_agent = parse(user_agent_string)
    
    UserAllInformation.objects.create(
        location=location,
        come_from=referrer,
        device=user_agent.device.family or "Unknown Device",
        browser=user_agent.browser.family or "Unknown Browser",
        browser_version=user_agent.browser.version_string or "Unknown Version",
        device_os=user_agent.os.family or "Unknown OS",
        ip_address=ip,
        os_version=user_agent.os.version_string or "Unknown OS Version",
        is_pc=user_agent.is_pc,
        is_mobile=user_agent.is_mobile,
        is_tablet=user_agent.is_tablet
    )
    return redirect('home')


def HomePage(request):
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
            to = [obj.email,EMAIL_HOST_USER]
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




