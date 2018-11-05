from flask import redirect
from flask_restful import Resource

class HomeController(Resource):
	''' redirect to api docs '''
	def get(self):
		redirect('https://storeapiv2.docs.apiary.io')