import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Home (webapp2.RequestHandler):
    def get(self):
        home_template = jinja_env.get_template('pages/index.html')
        self.response.write(home_template.render())

class Resume (webapp2.RequestHandler):
    def get(self):
        resume_template = jinja_env.get_template('pages/resume.html')
        self.response.write(resume_template.render())

class AboutMe (webapp2.RequestHandler):
    def get(self):
        aboutme_template = jinja_env.get_template('pages/about-me.html')
        self.response.write(aboutme_template.render())


app = webapp2.WSGIApplication([
    ('/', Home),
    ('/resume', Resume),
    ('/aboutme', AboutMe),
], debug=True)
