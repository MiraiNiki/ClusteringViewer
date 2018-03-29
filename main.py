# coding:utf-8
#!/usr/bin/env python
# -*- encoding : utf-8 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import cgi
import json
import kmeans as kmeans
from google.appengine.ext.webapp import template 
from google.appengine.ext import webapp
from google.appengine.ext import ndb
from google.appengine.api import users

class getCluster(webapp2.RequestHandler):
	def post(self):
		# リクエストからJSONを取得する
		json_data = self.request.body
		# JSON をオブジェクトに
		obj = json.loads(json_data)
		result = kmeans.calcKmeans(obj, 3)
		# Content-Type は application/json
		self.response.content_type = 'application/json; charset=utf-8'
		# 文字列に変換して返す
		self.response.out.write(json.dumps(result))


class MainHandler(webapp2.RequestHandler):
    def get(self):
		body = "hoge"
		template_values = {'body': body,}
		path = os.path.join(os.path.dirname(__file__) + '/', 'main.html')
		self.response.out.write(template.render(path,template_values))
		#self.response.write("".join(result))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/getCluster', getCluster)
], debug=True)
