from google import genai
import os
from flask import Blueprint,render_template,flash,url_for,redirect,current_app,request, jsonify
from . import db
from .models import User

views_bp = Blueprint('views',__name__)
 
import google.generativeai as genai

# Load API key from environment variables (Recommended for security)
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
@views_bp.route("/index", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        data = request.get_json()
        user_input = data.get("question")

        if not user_input:
            return jsonify({"error": "Invalid input"}), 400

        # Generate AI response
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(user_input)
        print(jsonify({"response": response.text}))
        return jsonify({"response": response.text})  # Send JSON response

    return render_template("index.html")  # Load HTML page for GET request

@views_bp.route("/home")
def home():
    return render_template("home.html")

@views_bp.route("/KnowYourStatus")
def KnowYourStatus():
    return render_template("KnowYourStatus.html")


@views_bp.route("/TextBooks")
def TextBooks():
    return render_template("TextBooks.html")

@views_bp.route("/Quiz")
def Quiz():
    return render_template("Quiz.html")

@views_bp.route("/Exam")
def Exam():
    return render_template("Exam.html")

@views_bp.route("/Schedule")
def Schedule():
    return render_template("Schedule.html")


@views_bp.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        f_email = request.form.get("email")
        f_password = request.form.get("password")
        print(f_password,f_email)
        user = User.query.filter_by(email = f_email).first()
        if user and user.password == f_password:
            return redirect("/index")
        else:
            print(user, user.password ,user.password == f_password)
            return redirect("/login")
    return render_template("login.html")


@views_bp.route("/", methods = ["GET","POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        if password1 == password2 :
            try:
                user = User(name = name, phone = phone, email = email, password = password1)
                db.session.add(user)
                db.session.commit()
                return redirect("/login")
            except Exception as e:
                print(e)
                return redirect("/signup")
    return render_template("signup.html")


# @views_bp.route("/home", methods = ["POST","GET"])
# def home():
#     if request.method == "POST":
#         data = request.get_json()  # Get JSON data from request
#         userInput = data.get("question")  # Extract 'question' from JSON

#         client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))
#         response = client.models.generate_content(
#             model="gemini-2.0-flash", contents = userInput
#         )
#         print(response.text)
        
#         return render_template("/home",res = response.text)
    
#     return render_template("home.html")

