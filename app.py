from flask import Flask, render_template, jsonify
from databases import load_jobs_from_db
# from sqlalchemy.sql import text

app = Flask(__name__)

# JOBS = [
# {
#   'id':1,
#   'title':'Data Analyst',
#   'location':'Chandigarh, India',
#   'salary':'Rs.1,00,000'
# },
# {
#   'id':2,
#   'title':'Data Scientist',
#   'location':'Delhi, India',
#   # 'salary':'Rs.2,50,000'
# },
# {
#   'id':3,
#   'title':'Frontend Engineer',
#   'location':'Remote',
#   'salary':'Rs.15,00,000'
# },
# {
#   'id':4,
#   'title':'backend Engineer',
#   'location':'San Francisco , USA',
#   'salary':'$ 120,000'
# }
# ]



  
@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html',
                         jobs=jobs,
                        company_name='Johnson')
@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

# print(__name__)
if __name__ == '__main__':
  # print("I'm inside the if now")
  app.run(host='0.0.0.0',debug=True)