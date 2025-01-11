from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    # מתודה לבדיקת סיסמה
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    # מתודה ליצירת סיסמה מוצפנת
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()
        
    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"    

