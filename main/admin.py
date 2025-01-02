from django.contrib import admin
from .models import *



admin.site.register(AboutTxt)
admin.site.register(Testimonials)
admin.site.register(Comp_works)
admin.site.register(SubWork)
admin.site.register(SubAbout)
admin.site.register(SiteURL)
admin.site.register(UserInfo)
admin.site.register(DivaceType)



@admin.register(UserAllInformation)
class UserInformationModelAdmin(admin.ModelAdmin):
    list_display = ['location','user_date','device','come_from']
    list_display_links = ['location','user_date','device','come_from']
    search_fields = ['location','user_date','device','come_from']

@admin.register(MainInformations)
class MainImformationMidelAdmin(admin.ModelAdmin):
    list_display = ['site_name','site_owner','phone']
    list_display_links = ['site_name','site_owner','phone']
    search_fields = ['site_name','site_owner','phone']


@admin.register(ForSkills)
class ForSkillModelAdmin(admin.ModelAdmin):
    list_display=['skill_name','skill_percent']
    list_display_links=['skill_name','skill_percent']
    search_fields=['skill_name','skill_percent']


@admin.register(About)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['title','company']
    list_display_links = ['title','company']
    search_fields = ['title','company']


@admin.register(StaffStory)
class AdminStoryModelAdmin(admin.ModelAdmin):
    list_display = ['position']
    list_display_links = ['position']
    search_fields = ['position']


@admin.register(SendMessage)
class SedMessageModelAdmin(admin.ModelAdmin):
    list_display = ['name','subject','message','data']
    list_display_links = ['name','subject','message','data']
    search_fields = ['name','subject','message','data']    

