import flask
from urllib import parse
from flask import request
from werkzeug.contrib.atom import AtomFeed
from datetime import datetime
import utils

blueprint = flask.Blueprint('feed', __name__)


def make_external(url):
    return parse.urljoin(request.url_root, url)


@blueprint.route('/atom')
def atom_feed():
    feed = AtomFeed('Recent content',
                    feed_url=request.url,
                    url=request.url_root
                    )

    cache = utils.update_record_cache()
    context = utils.format_response(cache['record'], cache['metadata'])

    feed.add(context['record']['title'], '<p>Test</p>',
             content_type='html',
             author=context['record']['author'],
             url=make_external(context['record']['permalink']),
             updated=datetime.today(),
             published=datetime.today())

    return feed.get_response()
