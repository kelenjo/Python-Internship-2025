import os
from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from forms import SubmissionForm
from models import db, Submission

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def submit():
    form = SubmissionForm()
    if form.validate_on_submit():
        try:
            new_submission = Submission(
                name=form.name.data,
                email=form.email.data,
                message=form.message.data
            )
            db.session.add(new_submission)
            db.session.commit()
            flash(f"Thank you for your submission, {new_submission.name}.", "success")
            return redirect(url_for('result', submission_id=new_submission.id))
        except Exception as e:
            db.session.rollback()
            flash("An error occurred while processing your submission.", "danger")
    return render_template('form.html', form=form)

@app.route('/result/<int:submission_id>')
def result(submission_id):
    entry = Submission.query.get_or_404(submission_id)
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)