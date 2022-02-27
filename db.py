from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'mysql_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql_password'
app.config['MYSQL_DATABASE_DB'] = 'db_name'
app.config['MYSQL_DATABASE_HOST'] = 'host'
mysql.init_app(app)