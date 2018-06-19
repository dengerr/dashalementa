from google.appengine.ext import ndb


class Account(ndb.Model):
    username = ndb.StringProperty()
    userid = ndb.IntegerProperty()
    email = ndb.StringProperty()


class Page(ndb.Model):
    slug = ndb.StringProperty()
    title = ndb.StringProperty()
    body = ndb.TextProperty()
    idx = ndb.IntegerProperty()

