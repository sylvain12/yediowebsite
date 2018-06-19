from flask import render_template, Blueprint, url_for

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('main/home.html')

@main.route('/services')
def services():
    return render_template('main/services.html')


@main.route('/about')
def about():
    return render_template('main/about.html')


@main.route('/contact')
def contact():
    return render_template('main/contact.html')