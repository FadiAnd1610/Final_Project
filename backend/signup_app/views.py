from django.http import JsonResponse
from django.views import View
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import User
from connectgmail.models import gmail_users  # המודל של משתמשי Google
#from django.contrib.auth import login
#from django.contrib.auth import logout
from connectgmail.models import gmail_users
from gallery.models import Image_user
from django.contrib.sessions.backends.db import SessionStore

class AdminDataView(View):
    def get(self, request, *args, **kwargs):
        # משיכת כל המשתמשים
        users = User.objects.all().values("id", "username", "email", "Is_superviser", "Is_active")
        return JsonResponse({"users": list(users)}, status=200)

    

@method_decorator(csrf_exempt, name='dispatch')
class SignUpView(View):
    
    # מתודה זמנית לבדיקת שה-API פעיל
    def get(self, request, *args, **kwargs):
        return JsonResponse({"message": "Signup API is working! Please send a POST request."}, status=200)
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            # בדיקות תקינות קלט
            if not username or not email or not password:
                return JsonResponse({"error": "All fields are required."}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already exists."}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists."}, status=400)
            
            gmail_users.Is_active = True
            # יצירת משתמש חדש
            user = User(
                username=username,
                email=email,
                password=make_password(password),
            )
            user.save()

            # יצירת session_id ידני
            session = SessionStore()
            session['user_id'] = user.id
            session['username'] = user.username
            session['email'] = user.email
            session.create()  # שמירת ה-session במאגר הנתונים
             
            
            if not session.session_key:  # בדיקה שה-Session נוצר בהצלחה
                return JsonResponse({"error": "Failed to create session."}, status=500)

            # יצירת התגובה
            response = JsonResponse({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "session_id": session.session_key,  # session_id שנוצר ידנית
                 "is_superviser": user.Is_superviser  

            }, status=201)

            # הוספת העוגייה של ה-Session (רק **פעם אחת!**)
            response.set_cookie(
                key='sessionid',
                value=session.session_key,
                max_age=3 * 24 * 60 * 60,  # חיי עוגייה - 3 ימים
                httponly=False,  # הפוך ל-False אם אתה רוצה לבדוק ב-JS
                secure=False,  # אין HTTPS, אז False
                samesite="Lax"  # ביטול SameSite לחלוטין
)

            print(f"User created: {user.username}, {user.email}, session_id: {session.session_key}")
            return response

        except Exception as e:
            print(f"An error occurred: {e}")
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)


        
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            print(f"Username received: {username}")
            print(f"Password received: {password}")

            if not username or not password:
                print("Missing username or password")
                return JsonResponse({"error": "Both fields are required."}, status=400)

            user = User.objects.filter(username=username).first()
            if not user:
                print(f"User not found for username: {username}")
                return JsonResponse({"error": "Invalid credentials."}, status=401)

            if not user.check_password(password):
                print("Password check failed")
                return JsonResponse({"error": "Invalid credentials."}, status=401)
            
            
            # יצירת session_id ידני
            session = SessionStore()
            session['user_id'] = user.id
            session['username'] = user.username
            session.create()  # שמירת ה-session במאגר הנתונים
            
            print(f"User {username} ,session_id: {session.session_key},  logged in successfully")
            
            user.Is_active = True
            user.save() # חשוב!!!!!!!!!!!!!!!!!!!!!!!!

            response = JsonResponse({
                "message": "Login successful!",
                "username": user.username,
                "user_id": user.id,
                "Is_active":user.Is_active,
                "session_id": session.session_key,  # session_id שנוצר ידנית
                "is_superviser": user.Is_superviser  

            }, status=200)
            
             # הוספת העוגייה של ה-Session (רק **פעם אחת!**)
            response.set_cookie(
                key='sessionid',
                value=session.session_key,
                max_age=3 * 24 * 60 * 60,  # חיי עוגייה - 3 ימים
                httponly=False,  # הפוך ל-False אם אתה רוצה לבדוק ב-JS
                secure=False,  # אין HTTPS, אז False
                samesite="Lax"  # ביטול SameSite לחלוטין
                )
            return response
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return JsonResponse({"error": "An unexpected error occurred. Please try again."}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class LogOut(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get("username")
            email = data.get("email")  # תמיכה בהתנתקות לפי אימייל

            if not username and not email:  # אם לא התקבל לא username ולא email
                return JsonResponse({"message": "Username or email required"}, status=400)

            # בדיקת משתמש רגיל (אם username קיים)
            user = User.objects.filter(username=username).first() if username else None
            # בדיקת משתמש Google (אם email קיים)
            google_user = gmail_users.objects.filter(email=email).first() if email else None

            if not (user or google_user):  # כאן שיניתי ל-`or` כדי להספיק שמשתמש אחד יימצא
                return JsonResponse({"message": "User not found in the database, you need to create it first"}, status=404)

            # סימון המשתמש כלא פעיל
            if user:
                user.Is_active = False
                user.save()

            if google_user:
                google_user.Is_active = False
                google_user.save()

            # מחיקת כל נתוני ה-Session
            request.session.flush()

            # יצירת תגובה עם מחיקת העוגיה
            response = JsonResponse({"message": "Logout successful. Session deleted and user deactivated."}, status=200)
            response.delete_cookie('sessionid')  # מחיקת העוגיה מהלקוח

            return response

        except Exception as e:
            print(f"An error occurred: {e}")
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)
