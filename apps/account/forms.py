from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

#---------------------------------------------------------------------------------
class UserCreationForm(forms.ModelForm):   #This form is for creating users by the admin in the admin panel
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='repassword',widget=forms.PasswordInput)
    
    class Meta:
        model=CustomUser
        fields=['email','name','family','gender']
    def clean_password2(self):
        pass1 = self.cleaned_data["password1"]
        pass2 = self.cleaned_data["password2"]
        if pass1 and pass2 and pass1!=pass2:
            raise ValidationError('Password and repassword are not the same')
        
        return pass2
        
    def save(self,commit=True):    #To hash the passwords, we stop the storage system, then we hash the password, and after hashing the password, we add the desired user to the database.
        user=super().save(commit=False)
        
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
        
#-------------------------------------------------------------------------------

class UserChangeForm(forms.ModelForm): #This form is for changing user information
    password=ReadOnlyPasswordHashField(help_text='Click on this <a href="../password">link</a> to change the password') #In this line of code, the admin user is allowed to change the desired user's password
    class Meta:
        model:CustomUser
        fields=['email','password','name','family','gender','is_active','is_admin']
        
#-------------------------------------------------------------------------------