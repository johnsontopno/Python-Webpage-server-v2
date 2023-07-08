# import sqlalchemy
# print(sqlalchemy.__version__)
from sqlalchemy import create_engine,text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
# "mysql+pymysql://525u7d1dp6e914yiyze3:pscale_pw_5GzGCzBFh275dmoMHEbXAMOlxbRoepT99xsphSiu694@aws.connect.psdb.cloud/python-website-server-v2?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl":{
      "ssl_ca": "/etc/ssl/cert.pem"
  }
})
# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))


#   result_dicts = []
#   for row in result.all():
#     result_dicts.append(dict(row))

  # print(result_dicts)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs


  
  # print("type(result):",type(result))
  # result_all =result.all()
  # print("type(result.all()):",type(result_all))
  # print("result.all():",result_all)
  # first_result =result_all[0]
  # print("type(first_result):",type(first_result))
  # first_result_dict = dict(result_all[0])
  # print("type(first_result_dict):",type(first_result_dict))
  # print(first_result_dict)ls