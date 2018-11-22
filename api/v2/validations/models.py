from api import app
from api.db_config import con, cur

class Validations():

	def email_check(self, email):

		""" Check if email provided has been registered in the system """

		cur.execute ("SELECT * FROM users WHERE email = %s", ([email]))
		return cur.fetchone()

	def role_check(self, email):

		""" Check the role assigned to a user account """

		cur.execute ("SELECT role FROM users WHERE email = %s", ([email]))
		return cur.fetchone()[0]

