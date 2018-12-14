from flask import render_template
import connexion
from flask_cors import CORS

# create the application instance
app = connexion.FlaskApp(__name__,specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# add CORS support
# CORS(app.app)
cors = CORS(app.app, resources=r"/api/*")

# Create a URL route in our application
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


def runServer():
    app.run(host='localhost', port=3001, debug=True)


# if we are running in the standalone mode, run the application
if __name__ == '__main__':
    runServer()