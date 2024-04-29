from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone




class CustomUserManager(BaseUserManager):
    
    def creat_user(self,email,name='',family='',active_code=None,gender=None,password=None):   #for create user
        if not email:
            raise ValueError(' ایمیل باید وارد شود')
        user=self.model(
            email=self.normalize_email(email),
            name=name,
            family=family,
            active_code=active_code,
            gender=gender
        )
        user.set_password(password)  # hashing password in DB
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,family,password=None,active_code=None,gender=None):   #for create superuser
        user=self.creat_user(
            email=email,
            name=name,
            family=family,
            active_code=active_code,
            gender=gender,
            password=password
            
        )
        user.is_active=True
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
    
    
    
#--------------------------------------------------------------------
    

class CustomUser(AbstractBaseUser,PermissionsMixin):
    
    email=models.EmailField(verbose_name='email', max_length=254,unique=True)
    name=models.CharField(verbose_name='name', max_length=50,blank=True)
    family=models.CharField(verbose_name='family', max_length=50,blank=True)
    GENDER_CHOICES=(('True','male'),('False','Female'))
    gender=models.CharField(verbose_name='gender', max_length=50,choices=GENDER_CHOICES,default='True',null=True,blank=True)
    register_date=models.DateTimeField(verbose_name='date added',default=timezone.now)
    is_active=models.BooleanField(verbose_name='active/inactive',default=False)
    active_code=models.CharField(verbose_name='activation code',max_length=100,null=True,blank=True)
    is_admin=models.BooleanField(verbose_name='admin',default=False)
    
    USERNAME_FIELD='email'   # Specify username
    REQUIRED_FIELDS=['name','family'] #In order to create a superuser, the system asks us for some fields, which we gave the name and surname, but the system will provide us with our email (username) and password.
    
        
    objects=CustomUserManager()  #An instance of the CustomUserManager class must be created in the field called objects
    
    #Note: AUTH_USER_MODEL must be introduced in the program settings and then migrate
    #AUTH_USER_MODEL='account.CustomUser'

    
    
    def __str__(self):
        return self.name+' '+self.family
    
    @property   #With this, normal users cannot access the admin panel
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'