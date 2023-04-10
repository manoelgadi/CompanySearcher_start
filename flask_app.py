# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)


import sqlite3
conn = sqlite3.connect('./database/company_balancesheet_database.db')

pd.set_option('display.float_format', lambda x: '%.3f' % x)
df = pd.read_sql("""SELECT * FROM cuentas_anuales;""", conn)

df.drop('id',inplace=True,axis=1)

df.columns = ['NIF', 'Name', 'CNAE', 'Total Assets - 2017', 'Total Assets - 2016', 'Total Assets - 2015', 'Own Resources - 2017', 'Own Resources - 2016', 'Own Resources - 2015', 'Short Debt - 2017', 'Short Debt - 2016', 'Short Debt - 2015', 'Long Debt - 2017', 'Long Debt - 2016', 'Long Debt - 2015', 'Income - 2017', 'Income - 2016', 'Income - 2015', 'Amortization - 2017', 'Amortization - 2014', 'Amortization - 2015', 'Profit - 2017', 'Profit - 2016', 'Profit - 2015', 'Status']


@app.route("/")
def index():
    return render_template("index.html", df = df, ids = list(range(len(df))))


if __name__ == '__main__': # This only runs if 
  app.run()
