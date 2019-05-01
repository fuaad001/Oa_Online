from flask import render_template, redirect, url_for, flash, request
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user, logout_user, login_required


@auth.route('/login', methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(husband_ID = login_form.husband_ID.data, wife_ID = login_form.wife_ID.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Couple login"

    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/register', methods = ["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(husband_email = form.husband_email.data, husband_name = form.husband_name.data, husband_ID = form.husband_ID.data, wife_email = form.wife_email.data, wife_name = form.wife_name.data, wife_ID = form.wife_ID.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Couple Account creation was Successfull')

        return redirect(url_for('auth.login'))
        title = "New Couple Account"
    return render_template('auth/signup.html', signup_form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been Successfully logged out')
    return redirect(url_for("main.index"))
