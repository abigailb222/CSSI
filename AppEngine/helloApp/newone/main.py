import logging
import os

import jinja2
import webapp2


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def post(self):
        my_day = self.request.get('day')
        picture = self.request.get('picture')
        good_day = my_day == 'good'
        images = {
            'groot.png': '/groot.png',
            'favicon': '/favicon.ico',
        }
        messages = {
            'good': 'Yeah it\'s a good day!',
            'bad': 'Hope you feel better.',
            'meh': 'Let\'s go to lunch',
        }
        default = "try again"
        template_vars = {
            'image_source': images.get(picture, '/groot.png'),
            'message': messages.get(my_day, default),
            'bad_message': 'feel better',
            'good_day': good_day,
        }
        template = jinja_environment.get_template(
            'html_newone/index.html')
        self.response.write(template.render(template_vars))

##def is_prime(n):
#    for possible_factor in range(2,n):
#        if n% possible_factor == 0:
    #        logging.info('Found a factor : %d', possible_factor)
    #        return False
#    return True''''

class AnotherHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template(
            'html_newone/question.html')
        message = "Hello Hello Hello!"
        logging.info(message)
        self.response.write(template.render())

#'''''
#class MainHandler(webapp2.RequestHandler):
#    def get(self):
    #    self.response.write('Hello world!')
#
#class WorldHandler(webapp2.RequestHandler):
#    def get(self):
#        self.response.write('Hello Hello!')'''

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/question', AnotherHandler),

], debug=False)
