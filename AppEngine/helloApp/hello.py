import webapp2
import jinja2

ENV = jinja2.Environment( loader= jinja2.FileSystemLoader("templates"))

html_page2="""<html>
<body>
        <form action="/" method="post">
        name: <input type="text" name="field1"/>
        <input type="submit" value="submit"/>
        </form>
    </body>
    </html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(html_page2)

    def post(self):
        self.response.headers['content-type'] = 'text/plain'
        #self.response.write(self.request.POST)
        if "field1" not in self.request.POST:
            self.response.write('field1 not found')
        else:
            field1 = self.request.POST['field1']
            self.response.write("hello " + field1 + "!")

class GreetingHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("greeting to my people")

routes = [
        ('/', MainHandler),
        ('/greeting', GreetingHandler),
]


app = webapp2.WSGIApplication(routes, debug=True)
