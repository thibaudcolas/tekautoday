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
    feed = AtomFeed('Tekau Today',
                    feed_url=request.url,
                    url=request.url_root
                    )

    cache = utils.update_record_cache()
    context = utils.format_response(cache['record'], cache['metadata'])

    title = '{date} – {title}'.format(
        date=context['date'].strftime('%d %B %Y'),
        title=context['record']['title']
    )
    content = flask.render_template('feed.html', **context)

    feed.add(title, content,
             content_type='html',
             author=context['record']['author'],
             url=make_external(context['record']['permalink']),
             updated=datetime.today(),
             published=datetime.today())

    return feed.get_response()
