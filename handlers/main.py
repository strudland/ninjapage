from handlers.base import BaseHandler
from google.appengine.api import users
from models.topic import Topic

class MainHandler(BaseHandler):
    def get(self):

        topics = Topic.query(Topic.deleted == False).fetch()
        params = {"topics": topics}
        return self.render_template("home1.html", params=params)
