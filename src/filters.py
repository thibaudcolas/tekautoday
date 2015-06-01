import jinja2
import flask
import records

blueprint = flask.Blueprint('filters', __name__)


@jinja2.contextfilter
@blueprint.app_template_filter()
def date_record(context, date):
    try:
        record = records.get_record_by_date(date)
    except StopIteration:
        record = {
            'hash': 'nothing',
            'date': '3320-05-04',
            'id': 1337
        }

    return record
