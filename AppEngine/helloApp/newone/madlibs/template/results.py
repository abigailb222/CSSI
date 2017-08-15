import json
import logging
import os
import urllib

import jinja2
import webapp2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class NamesHandler(webapp2.RequestHandler):
    def get(self):
        response = urllib2.urlopen("https://uinames.com/api/")
        content = response.read()
        content_dict = json.loads(content)

        main_template = env.get_template('name.html')
        self.response.out.write(main_template.render(content_dict))

app = webapp2.WSGIApplication([
    ('/', NamesHandler),
], debug=True)
