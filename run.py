import os
from os.path import join, dirname

from app import create_app

from dotenv import load_dotenv
import time
time.sleep(10)

dotenv_path = join(dirname(__file__), '.env')  # Address of your .env file
load_dotenv(dotenv_path)


config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)
# config = {
#     'user':'root',
#     'password':'akashhegde',
#     'host':'localhost',
#     'port':'3306',
#     'database':'uvce'
# }
# mydb = mysql.connector.connect(user = 'insta_dmin',password = 'insta2018',
#                                 host='db', database='uvce',auth_plugin='mysql_native_password')
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
