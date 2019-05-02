from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db, photos
from flask_login import login_required, current_user

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Oa Online'

    return render_template('index.html', title = title)

@main.route('/types')
def types():
   '''
   View root page function that returns the types page and its data
   '''

   title = 'Types'

   return render_template('types.html')

@main.route('/importance')
def importance():
   '''
   View root page function that returns the importance page and its data
   '''

   title = 'importance'

   return render_template('importance.html')

@main.route('/requirements')
def requirements():
   '''
   View root page function that returns the requirements page and its data
   '''

   title = 'requirements'

   return render_template('requirements.html')

@main.route('/process')
def process():
   '''
   View root page function that returns the process page and its data
   '''

   title = 'process'

   return render_template('process.html')

@main.route('/divorce')
def divorce():
   '''
   View root page function that returns the divorce page and its data
   '''

   title = 'divorce'

   return render_template('divorce.html')
