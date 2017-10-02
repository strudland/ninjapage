#!/usr/bin/env python
import webapp2
from handlers.main import MainHandler
from handlers.cookie import CookieHandler
from handlers.topics import TopicAdd,TopicHandler





app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieHandler, name="main-page"),
    webapp2.Route('/topic/add', TopicAdd, name="topic-add"),
], debug=True)
