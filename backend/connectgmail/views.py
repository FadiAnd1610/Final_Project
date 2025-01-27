from logging import config
from google.oauth2 import id_token
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google.auth.transport.requests import Request  # ודא שהייבוא נכון
import json
from decouple import config
from django.http import HttpResponse
from .models import gmail_users as gmail

def home(request):
    return HttpResponse("Hello, World!")


@csrf_exempt
def google_auth(request):
    if request.method == 'POST':
        try:
            # קבלת הנתונים מהבקשה
            data = json.loads(request.body)
            token = data.get('token')

            # הדפסת הנתונים שהתקבלו (לטובת בדיקה בטרמינל)
            print("Received data from React:", data)

            # אימות הטוקן
            idinfo = id_token.verify_oauth2_token(
                token, Request(), config('GOOGLE_CLIENT_ID')
            )

            # הפקת נתונים מהטוקן
            email = idinfo.get('email', 'Unknown')
            name = idinfo.get('name', 'Unknown')

            # שמירת הנתונים במודל gmail
            gmail_entry, created = gmail.objects.get_or_create(
                email=email,
                defaults={'name': name}
            )
            if not created:
                # אם הרשומה כבר קיימת, עדכן את השם
                gmail_entry.name = name
                gmail_entry.save()

            # הדפסת מידע שפורק מהטוקן בטרמינל
            print("Token verified. Info:", idinfo)

            # החזרת התגובה ל-React
            return JsonResponse({'message': 'Login successful', 'email': email, 'name': name})
        except ValueError as e:
            print("Invalid token:", e)
            return JsonResponse({'error': 'Invalid token'}, status=400)
        except Exception as e:
            print("An error occurred:", e)
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'GET':
        # החזרת מידע לדוגמה (או מידע מהדאטהבייס אם צריך)
        users = list(gmail.objects.values())
        return JsonResponse({'users': users})

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)











