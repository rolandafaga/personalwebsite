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

class Projects (webapp2.RequestHandler):
    def get(self):
        projects_template = jinja_env.get_template('pages/projects/index.html')
        self.response.write(projects_template.render())

class TailorEd (webapp2.RequestHandler):
    def get(self):
        tailored_template = jinja_env.get_template('pages/projects/tailored.html')
        self.response.write(tailored_template.render())

class GoogleCSSI (webapp2.RequestHandler):
    def get(self):
        googlecssi_template = jinja_env.get_template('pages/projects/google-cssi.html')
        self.response.write(googlecssi_template.render())
        
class Gallery (webapp2.RequestHandler):
    def get(self):
        gallery_template = jinja_env.get_template('pages/projects/design-portfolio.html')
        self.response.write(gallery_template.render())
        
class WebDesign (webapp2.RequestHandler):
    def get(self):
        webdesign_template = jinja_env.get_template('pages/projects/web-design.html')
        self.response.write(webdesign_template.render())
        
class Contact (webapp2.RequestHandler):
    def get(self):
        contact_template = jinja_env.get_template('pages/contact.php')
        self.response.write(contact_template.render())
        
app = webapp2.WSGIApplication([
    ('/', Home),
    ('/resume', Resume),
    ('/projects/', Projects),
        ('/projects/tailored', TailorEd),
        ('/projects/google-cssi', GoogleCSSI),
        ('/projects/design-portfolio', Gallery),
        ('/projects/web-design', WebDesign),
    ('/contact', Contact),
], debug=True)
