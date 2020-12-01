from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Food','Food'),('Entertainment','Entertainment'),('Sport','Sport')],validators=[Required()])
    post = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('You can leave a comment',validators=[Required()])
    submit = SubmitField('Comment')