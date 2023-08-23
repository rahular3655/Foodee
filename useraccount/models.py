from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


#for manage user accounts

class MyAccountManager(BaseUserManager):
    # To create a superuser
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        if not email:
            raise ValueError('The email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

#for admin previlage creation

class accounts(AbstractBaseUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100,unique=True)
    username = models.CharField(max_length=150, unique=True)
    phonenumber = models.CharField(max_length=50,null=True)
    
    
    #required field
    start_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_restaurant=models.BooleanField(default=False)
    
    #To validate emailid as username
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS= ['user_name','first_name','last_name']
    REQUIRED_FIELDS= ['username']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,add_label):
        return True