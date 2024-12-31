from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MainInformations(models.Model):
    icon = models.ImageField('Icon',upload_to='Icon',null=True)
    site_name = models.CharField('Site name',max_length=255)
    site_owner = models.CharField('Site owner',max_length=255)
    img_back = models.ImageField('Image')
    profile = models.CharField('Profile',max_length=255)
    email = models.EmailField('Email')
    phone = PhoneNumberField('Phone number')
    owner_img = models.ImageField('Owner Image',upload_to='Owner_media',null=True)
    current_work = models.CharField('Current workplace',max_length=255,null=True)
    positions = models.TextField('Positions',null=True)
    address_1 = models.CharField('Address',max_length=255,null=True)
    address_2 = models.CharField('Address',max_length=255,null=True,blank=True)


    def __str__(self):
        return f'{self.site_name} {self.site_owner}'
    

    class Meta:
        verbose_name = 'Main Info'
        verbose_name_plural = 'Main Infos'


class ForSkills(models.Model):
    skill_name = models.CharField('Skill name',max_length=255)
    skill_percent = models.IntegerField('Skill percent')


    def __str__(self):
        return self.skill_name
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skill'


class About(models.Model):
    title = models.CharField('Title',max_length=255)
    company = models.CharField('Company name',max_length=255)
    dt_start = models.DateField('Date start',null=True)
    dt_end = models.DateField('Date end',null=True,blank=True)
    present = models.CharField('Present',max_length=255,blank=True) 
    txt = models.TextField('Text')

    def __str__(self):
        return self.title

class AboutTxt(models.Model):
    txt = models.TextField('About Text')


    def __str__(self):
        return f'{self.txt[:38]}...'
    
    
    class Meta:
        verbose_name = 'About text'
        verbose_name_plural = 'About text'

    

class StaffStory(models.Model):
    icon = models.CharField('Icone',max_length=255)
    position = models.CharField('Position',max_length=255)
    info = models.TextField('Information')


    def __str__(self):
        return self.position
    
    class Meta:
        verbose_name = 'Staff story'
        verbose_name_plural = 'Staff story'

class Testimonials(models.Model):
    name = models.CharField('Name',max_length=255)
    text = models.TextField('Text')
    img = models.ImageField('Image',upload_to='Testimonials')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

class Comp_works(models.Model):
    position = models.CharField('Position',max_length=255)
    title = models.CharField('Title',max_length=255)
    subtitle = models.TextField('Subtitle')
    img = models.ImageField('Image',upload_to='comp_works')


    def __str__(self):
        return f'{self.position}-{self.title}'
    
    class Meta:
        verbose_name ='Completed work'
        verbose_name_plural = 'Completed works'

class SubWork(models.Model): 
    main_work = models.ForeignKey(Comp_works,on_delete=models.CASCADE,related_name='main_works')
    video = models.FileField('Video',upload_to='videos')

    def __str__(self):
        return f'{self.main_work}'


class SubAbout(models.Model):
    subworkk = models.ForeignKey(SubWork,on_delete=models.CASCADE,related_name='subaboutt')
    text = models.TextField('Text')

    def __str__(self):
        return f'{self.subworkk}- {self.text[:30]}'
    
class SendMessage(models.Model):
    name = models.CharField('Name',max_length=255)
    email = models.EmailField('Email')
    subject = models.TextField('Subject')
    message = models.TextField('Message')
    data = models.DateTimeField('data',auto_now_add=True,blank=True,null=True)


    def __str__(self):
        return f'{self.name}-{self.email}'
    

    class Meta:
        verbose_name = 'Messages'
        verbose_name_plural = 'Messages'


class SiteURL(models.Model):
    facebook = models.URLField('Facebook')
    instagram = models.URLField('instagram')
    linkedin = models.URLField('linkedin')
    facebook = models.URLField('Facebook')


    def __str__(self):
        return 'Web Sites'
    
    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'



class UserInfo(models.Model):
    date = models.DateTimeField('date',auto_now_add=True)
    city = models.CharField('City',max_length=255)


    def __str__(self):
        return f'{self.date} - {self.city}'
    
    class Meta:
        verbose_name='User Information'
        verbose_name_plural='User Informations'