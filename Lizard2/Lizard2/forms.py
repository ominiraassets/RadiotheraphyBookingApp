from flask_wtf import Form
from wtforms import StringField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired

class NewScheduleForm(Form): 
    scheduleid = DateField('Schedule Date', validators=[DataRequired()])
    start = DateField('Start Time', validators=[DataRequired()])
    end = DateField('End Time', validators=[DataRequired()])
    duration = IntegerField('Appointment Duration', validators=[DataRequired()])