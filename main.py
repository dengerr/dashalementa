# codign: utf-8
import logging

from flask import Flask, render_template, request, redirect

from models import Page


app = Flask(__name__)


@app.route('/')
def hello():
    return redirect('/examples/')
    pages = Page.query()
    print 'zxcv'
    for page in pages.iter():
        print page
    return render_template('index.html',
        pages=pages,
    )


@app.route('/interiors/')
def interiors():
    from db import pages
    page = pages.get('interiors')
    text = render_template('interiors.html', items=page['items'])
    return render_template('base.html',
        page=page,
        text=text,
    )


@app.route('/interiors/<folder>/')
def interior(folder):
    from db import pages
    page = pages.get('interiors')
    text = render_template('interior.html', folder=folder, images=page['items'][folder])
    return render_template('base.html',
        page=page,
        text=text,
    )


@app.route('/<slug>/')
def by_slug(slug):
    from db import pages
    page = pages.get(slug)
    if page:
        text = open('html/{}.html'.format(slug)).read().decode('utf-8')
    else:
        text = ''
    return render_template('base.html',
        page=page,
        text=text,
    )


@app.route('/add/')
def add():
    from db import pages
    for idx, pg in enumerate(pages.values()):
        #page = Page(id=pg['slug'], **pg)
        #page.idx = idx + 1
        #page.put()
        Page.get_or_insert(
            pg['slug'],
            idx=idx + 1,
            body=open('html/{}.html'.format(pg['slug'])).read().decode('utf-8')
            **pg
        )
    return redirect('/about/')


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
        comments=comments,
    )


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

