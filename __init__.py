from flask import Flask

app = Flask(__name__)

import db
db.create_schedule_table()