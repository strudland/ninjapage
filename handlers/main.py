from handlers.base import BaseHandler
from google.appengine.api import users


class MainHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        params = {}
        if user:
            params['user'] = user
            params['logout_url'] = users.create_logout_url('/')
        else:
            params['login_url'] = users.create_login_url('/')

        return self.render_template("home.html", params)
