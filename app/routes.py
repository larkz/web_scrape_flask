from app import app
from app import forms
from flask import render_template, flash, redirect
import sys

from app import db
from app import models

@app.route('/webform')
def webform():
    form = forms.web_form()
    return render_template('sample_form.html', title='Sign In', form=form)

@app.route('/webscrape', methods=['GET', 'POST'])
def webscrape():
    web_scrape_form = forms.webscrape_form()
    if web_scrape_form.validate_on_submit():
        # flash('Web scraping for URL {}'.format(web_scrape_form.website_url.data))
        print('Clicked scrape button!', file=sys.stdout)
        data = models.User(username="234", email="gg", password_hash="66")
        
        db.session.add(data)
        db.session.commit()
        return redirect('/index')

    return render_template('scrape_form.html', title='Web Scraping Portal', form=web_scrape_form )

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Larkin'}
    return render_template('index.html', title='Home', user=user)





