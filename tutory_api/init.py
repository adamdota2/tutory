from app import app,csrf
from flask_cors import CORS


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
## API Routes ##
from tutory_api.blueprints.dashboard.views import dashboard_api_blueprint


app.register_blueprint(dashboard_api_blueprint, url_prefix='/api/v1/dashboard')
csrf.exempt(login_api_blueprint)