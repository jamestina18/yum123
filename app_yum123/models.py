from django.db import models
import bcrypt, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class YumManager(models.Manager):
     def basic_val(self, postData):
          errors = {}
          if len(postData['first_name']) < 2:
               errors["first_name"] = "First name should be at least 2 characters"
          if len(postData['last_name']) < 2:
               errors["last_name"] = "Last name should be at least 2 characters"
          if not EMAIL_REGEX.match(postData['email_address']):
               errors["email_address"] = 'Email is not valid'
          emailCheck = self.filter(email_address=postData['email_address'])
          if emailCheck:
               errors['email_address'] = "Email is already in use"
          if len(postData['city']) < 2:
               errors["city"] = "City should be at least 2 characters"
          if len(postData['zip_code']) < 5:    
               errors["zip_code"] = "Zip code should be at least 5 characters"
          if postData['password'] != postData['confirm_password']:
               errors['password'] = 'Your password do not match'
          return errors
          
     def authenticate(self, email_address, password):
          users = self.filter(email_address = email_address)
          if not users:
               return False
          user = users[0]
          return bcrypt.checkpw(password.encode(), user.password.encode())
      

class User(models.Model):
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     email_address = models.EmailField(unique=True)
     profile_pic = models.FileField(null=True, blank=Tru)
     city = models.CharField(max_length=45)
     zip_code = models.CharField(max_length=5)
     password = models.CharField(max_length=45)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     objects = YumManager()
     def __str__(self):
          return f"{self.first_name} {self.last_name}{self.email_address} {self.password}"

class Restau_api_obj(models.Model):
     name = models.CharField(max_length=255)
     location = models.CharField(max_length=255)
     image = models.ImageField()
     ratings = models.CharField(max_length=45)

     def __str__(self):
          return f"{self.name} {self.location}{self.image} {self.ratings}"


class Review(models.Model):
     comment = models.CharField(max_length=255)
     commenter = models.ForeignKey(User, related_name='user_review', on_delete=models.CASCADE)
     yelp_api = models.ForeignKey(Restau_api_obj, related_name='yelp_review', on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True, null=True)
     updated_at = models.DateTimeField(auto_now=True, null=True)


