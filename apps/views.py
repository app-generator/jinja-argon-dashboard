# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request, redirect
from jinja2  import TemplateNotFound

# App modules
from apps import app

# App main route + generic routing
@app.route('/', defaults={'path': 'dashboard.html'})
@app.route('/')
def index():
  try:
    return render_template( 'pages/dashboard.html', segment='dashboard', parent='pages')
  except TemplateNotFound:
    return render_template('pages/dashboard.html'), 404


# pages
@app.route('/pages/tables/')
def pages_tables():
  return render_template('pages/tables.html', segment='tables', parent='pages')

@app.route('/pages/billing/')
def pages_billing():
  return render_template('pages/billing.html', segment='billing', parent='pages')

@app.route('/pages/virtual-reality/')
def pages_vr():
  return render_template('pages/virtual-reality.html', segment='virtual_reality', parent='pages')

@app.route('/pages/rtl/')
def pages_rtl():
  return render_template('pages/rtl.html', segment='rtl', parent='pages')

@app.route('/pages/profile/')
def pages_profile():
  return render_template('pages/profile.html', segment='profile', parent='pages')

@app.route('/pages/sign-in/')
def pages_sign_in():
  return render_template('accounts/sign-in.html', segment='sign-in', parent='pages')

@app.route('/pages/sign-up/')
def pages_sign_up():
  return render_template('accounts/sign-up.html', segment='sign_up', parent='pages')

@app.template_filter(name = 'replace_value')
def replace_value(value, arg):
  return value.replace(arg, ' ').title()