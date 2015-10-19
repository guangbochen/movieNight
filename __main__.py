"""
    This is the main file to init the movie trailer application
    Note: this file is inspired by werkzeug.pocoo.org
"""
import os
from urllib.parse import urlparse
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader
from models.movie import Movie
from controllers.movies_controller import MoviesController

# define the Movie Night WSGI application
class MovieNight(object):

    def __init__(self):
        template_path  = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape = True)

    def dispath_request(self, request):
        error = None
        url   = ''
        return self.render_tempalte('home.html', error=error, url=url)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispath_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def render_tempalte(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        # init movies controller and call get favorite movies method to get list of movies
        favorite_movie_list = MoviesController().get_favorite_movies()
        return Response(t.render(context, movies=favorite_movie_list), mimetype='text/html')


#init MovieNight instance
def create_app(with_static=True):
    app = MovieNight()
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app

# call this method to boots the application
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('localhost', 5000, app, use_debugger=True, use_reloader=True)


