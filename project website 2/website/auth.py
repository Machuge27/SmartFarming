#auth.py
from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User,db,Messages
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,login_required,logout_user,current_user
from flask_socketio import  join_room, leave_room


auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    
    Email=request.form.get("email")
    password=request.form.get("password")
    user=User.query.filter_by(email=Email).first()
    if user:
     
       if check_password_hash(user.password,password):
          flash("logged in succesfullc",category="success")
          login_user(user,remember=True)

           # After successful login, join the websocket-room with the user's email
          
          print(f"client with email{current_user.email} joined room")

          return redirect(url_for("views.home"))
       else:
          flash("Incorrect password",category="error")
    else:
    
       flash("User doesn't exist",category="error")

    return render_template("login.html",user=current_user)

@auth.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    #leaving the websoket-room associated with ur email
    print(f"client with email{current_user.email} left the room")

    logout_user()
    
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method=="POST":
      first_name=request.form.get("first_name")
      email=request.form.get("email")
      password1=request.form.get("password1")
      password2=request.form.get("password2")
      print(email,"bri")
      user=User.query.filter_by(email=email).first()
      if user:
         flash("Email already exists",category="error")
      elif len(email)<4:
         print(email)
         flash("email must be greater than 4 charachters",category="error")
      elif len(first_name)<2:
         flash("Name be greater than 2 charachters",category="error")
      elif len(password1)<7:
         flash("password must be greater than 7 charachters",category="error")
      elif password1 != password2:
         flash("passwords don't match",category="error")
      else:
         new_user=User(email=email,first_name=first_name,password=generate_password_hash(password1,method='pbkdf2:sha256'))
         db.session.add(new_user)
         db.session.commit()
         login_user(new_user,remember=True)
         flash("Account Succesfully Created",category="success")
         return redirect(url_for('views.home'))
    return render_template("sign_up.html",user=current_user)

