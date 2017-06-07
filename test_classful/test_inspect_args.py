from flask import Flask
from .view_classes import InspectArgsView, NoInspectArgsView
from nose.tools import eq_

app = Flask('inspect_args')

InspectArgsView.register(app)
NoInspectArgsView.register(app)


def test_inspect_args():
    client = app.test_client()
    resp = client.get('/inspect-args/foo/123/456')
    eq_(b"foo unicode(123) unicode(456) int(678)", resp.data)


def test_no_inspect_args():
    client = app.test_client()
    resp = client.get('/no-inspect-args/foo/', query_string={'arg1': 123, 'arg2': 456})
    eq_(b"foo int(123) int(456) int(678)", resp.data)
