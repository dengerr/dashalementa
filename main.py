# codign: utf-8
import logging

from flask import Flask, render_template, request, redirect

from models import Page


app = Flask(__name__)


@app.route('/')
def hello():
    return redirect('/about/')
    pages = Page.query()
    print 'zxcv'
    for page in pages.iter():
        print page
    return render_template('index.html',
            pages=pages,
            )


@app.route('/<slug>/')
def by_slug(slug):
    page = Page.get_by_id(slug)
    print page
    return render_template('base.html',
            page=page,
            )


@app.route('/add/')
def add():
    if 1:
        from db import pages
        for idx, pg in enumerate(pages):
            #page = Page(id=pg['slug'], **pg)
            #page.idx = idx + 1
            #page.put()
            Page.get_or_insert(
                pg['slug'],
                idx=idx + 1,
                **pg
            )
        pages = Page.query()
        #for idx, page in enumerate(pages.iter()):
            #page.idx = idx + 1
            #page.id = page.slug
            #page.put()
    return render_template('index.html',
            )


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

