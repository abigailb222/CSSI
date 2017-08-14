import jinja2
import webapp2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('main.html')
        self.response.out.write(main_template.render())
    def post(self): ## here's the new POST method in the MainHandler
        self.response.out.write("You have submitted your madlib")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    
], debug=True)
