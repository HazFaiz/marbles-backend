from marbles_api.blueprints.users.views import users_api_blueprint
from marbles_api.blueprints.emergencies.views import emergencies_api_blueprint
from marbles_api.blueprints.threads.views import threads_api_blueprint

from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##


app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')

app.register_blueprint(emergencies_api_blueprint,
                       url_prefix='api/v1/emergencies')

app.register_blueprint(threads_api_blueprint,
                       url_prefix='api/v1/threads')

app.register_blueprint(comments_api_blueprint, url_prefix='api/v1/comments')


app.register_blueprint(sessions_api_blueprint, url_prefix='api/v1/sessions')
