import logging
from flask import Flask, request, url_for, render_template

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/")
def index():
    data = {
        'name': request.args.get('name', 'незнакомец'),
        'message': request.args.get('message', 'Тут было бы твое сообщение')
    }
    return render_template('index.html', **data)


with app.test_request_context():
    logger.info('Url for filled index page: %s',
                 url_for('index', name='Recruto', message='Давай дружить'))
