#!/usr/bin/env python
import webapp2
from handlers.main import MainHandler
from handlers.cookie import CookieHandler
from handlers.topics import TopicAdd,TopicDetailsHandler
from workers.send_mail_worker import SendMailWorker





app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieHandler, name="main-page"),
    webapp2.Route('/topic/add', TopicAdd, name="topic-add"),
    webapp2.Route('/topic-details/<topic_id:\d+>', TopicDetailsHandler, name="topic-details"),
    webapp2.Route('/task/email-topic-author', SendMailWorker),
], debug=True)
