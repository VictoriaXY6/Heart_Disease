from flask import Blueprint, render_template, Markup
from flask_login import login_required, current_user
from werkzeug.wrappers import request
from ..models import Blog, Writer
from .. import db, data, data_list
from ..description import about_page, risk_page, prevention_page, resources_page
from ..chart_generator import generate_line_chart, generate_pie_chart

# create a Blueprint object called main.
main = Blueprint('main', __name__, 
                template_folder='templates', 
                static_folder='static',
                static_url_path='/main')

# landing page
@main.route('/')
def index():
    pages = [about_page, risk_page, prevention_page, resources_page]
    posts = db.session.query(Blog, Writer).order_by(Blog.updated_date.desc()).join(Writer, Writer.id == Blog.writer_id)
    return render_template('main/index.html', posts=posts, pages=pages, show_author=True, edit_option=False, page_title='Welcome to Home Page')

# about page
@main.route('/about')
def about():
    return render_template('main/about.html', page=about_page, page_title=about_page['title'])

# risk factor page
@main.route('/risk')
def risk():
    return render_template('main/risk.html', page=risk_page, page_title=risk_page['title'])

# How to prevent page
@main.route('/prevention')
def prevention():
    return render_template('main/prevention.html', page=prevention_page, page_title=prevention_page['title'])

# resources page
@main.route('/resources')
def resources():
    return render_template('main/resources.html', page=resources_page, page_title=resources_page['title'])

# charts page
@main.route('/charts')
def charts():
    charts_html = []
    charts_html.append(Markup(generate_line_chart(data)))
    charts_html.append(Markup(generate_pie_chart(data)))
    return render_template('main/charts.html', charts_html=charts_html, column_name=data.columns, data=data_list, page_title='Charts and Data')

# user profile page
@main.route('/profile')
@login_required
def profile():
    posts = db.session.query(Blog).filter(Blog.writer_id == current_user.id).order_by(Blog.updated_date.desc())
    return render_template('main/profile.html', page_title='Welcome back ' + current_user.name, posts=posts, show_author=False, edit_option=True)