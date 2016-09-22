"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect
from Lizard2 import app
from Lizard2 import forms
from .forms import NewScheduleForm


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.jade',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/newschedule', methods=['GET', 'POST'])
def newschedule():
    """Creates a new schedule page."""    
    id = request.form['scheduleid']
    start = request.form['start']
    end = request.form['end']
    duration = request.form['duration']
    return redirect('/schedules') 
    '''return render_template(
        'calendar.jade',
        title='New Schedule',
        year=datetime.now().year,
        message=id   
    )'''
@app.route('/calendar')
def calendar():
    """Renders the calendar page."""
    return render_template(
        'calendar.jade',
        title='Calendar',
        year=datetime.now().year,
        message=id
    )

@app.route('/schedules')
def schedules():
    """Renders the schedules page."""
    return render_template(
        'schedules.jade',
        title='Schedules',
        year=datetime.now().year,
        message='Your schedules page.'
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.jade',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.jade',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
