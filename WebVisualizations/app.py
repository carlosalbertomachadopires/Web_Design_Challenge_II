from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
import csv
import os
# from config import URI  
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__, template_folder="templates")



# ROOT = "./Data"
# CONN = os.getenv("CONN")

# engine = create_engine(CONN)


if __name__ == "__main__":
    app.run(debug=True)
