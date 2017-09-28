from handlers.base import BaseHandler

class MainHandler(BaseHandler):
    def get(self):

        params={}
        piskotek = self.request.cookies.get('piskotek')
        if piskotek:
            params['piskotek'] = True
        return self.render_template("home.html", params)
