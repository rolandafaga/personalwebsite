import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_env.get_template('pages/index.html')
        self.response.write(home_template.render())

class BucketHandler(webapp2.RequestHandler):
    def get(self):
        bucket_template = jinja_env.get_template('pages/bucket.html')
        self.response.write(bucket_template.render())

class ResumeHandler(webapp2.RequestHandler):
    def get(self):
        resume_template = jinja_env.get_template('pages/resume.html')
        self.response.write(resume_template.render())

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/bucket', BucketHandler),
    ('/resume', ResumeHandler),
], debug=True)
