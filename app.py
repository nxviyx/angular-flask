# from flask import Flask, send_from_directory
# from flask_restful import Api, Resource, reqparse
# from flask_cors import CORS #comment this on deployment
# from api.HelloApiHandler import HelloApiHandler
#
# app = Flask(__name__, static_url_path='', static_folder='frontend/build')
# # CORS(app) #comment this on deployment
# api = Api(app)
#
# @app.route("/", defaults={'path':''})
# def serve(path):
#     return send_from_directory(app.static_folder,'index.html')
#
# api.add_resource(HelloApiHandler, '/flask/hello')

# from flask import Flask, send_from_directory
#
# app = Flask(__name__)
#
#
# @app.route('/<path:path>', methods=['GET'])
# def static_proxy(path):
#   return send_from_directory('./', path)
#
#
# @app.route('/')
# def root():
#   return send_from_directory('./', 'index.html')
#
# @app.route('/flask/hello')
# def test():
#   return "Hellow from heroku"
#
# if __name__ == '__main__':
#   # This is used when running locally only. When deploying use a webserver process
#   # such as Gunicorn to serve the app.
#   app.run(host='127.0.0.1', port=8080, debug=True)
#
#
# @app.errorhandler(500)
# def server_error(e):
#   return 'An internal error occurred [main.py] %s' % e, 500


from flask import Flask,render_template, request, jsonify
from flask_compress import Compress

# initialize flask application
app = Flask(__name__,static_url_path='',static_folder='dist',template_folder='dist')
Compress(app)


@app.route('/')
def test():
    return render_template("index.html")

@app.route('/flask/hello')
def testing():
  return "Hellow from heroku"

if __name__ == '__main__':
    # run web server
    app.run()

