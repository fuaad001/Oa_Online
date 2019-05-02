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

@main.route('/divorce2')
def divorce2():
   '''
   View root page function that returns the divorce2 page and its data
   '''

   title = 'divorce2'

   return render_template('divorce2.html')

@main.route('/process2')
def process2():
   '''
   View root page function that returns the process2 page and its data
   '''

   title = 'process2'

   return render_template('process2.html')

@main.route('/laws')
def laws():
   '''
   View root page function that returns the laws page and its data
   '''

   title = 'laws'

   return render_template('laws.html')