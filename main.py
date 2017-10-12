#!/usr/bin/env python
import webapp2
from handlers.main import MainHandler
from handlers.cookie import CookieHandler
from handlers.topics import TopicAdd,TopicDetailsHandler, DeleteTopicHandler
from workers.send_mail_worker import SendMailWorker
from  workers.crons.delete_topics_cron import DeleteTopicsCron






app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieHandler, name="main-page"),
    webapp2.Route('/topic/add', TopicAdd, name="topic-add"),
    webapp2.Route('/topic-details/<topic_id:\d+>', TopicDetailsHandler, name="topic-details"),
    webapp2.Route('/topic-delete/<topic_id:\d+>', DeleteTopicHandler),
    webapp2.Route('/task/email-topic-author', SendMailWorker),
    webapp2.Route('/cron/delete-topics', DeleteTopicsCron),
], debug=True)
