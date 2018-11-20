from api import app
from api.db_config import con, cur

class Validations():

	def email_check(self, email):
		email_check = cur.execute ("SELECT * FROM users WHERE email = %s", ([email]))
		email_check = cur.fetchone()
		return email_check

	def role_check(self, email):
		role_check = cur.execute ("SELECT role FROM users WHERE email = %s", ([email]))
		role_check = cur.fetchone()[0]
		return role_check