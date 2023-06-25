from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
  'id':1,
  'title':'Data Analyst',
  'location':'Chandigarh, India',
  'salary':'Rs.1,00,000'
},
{
  'id':2,
  'title':'Data Scientist',
  'location':'Delhi, India',
  # 'salary':'Rs.2,50,000'
},
{
  'id':3,
  'title':'Frontend Engineer',
  'location':'Remote',
  'salary':'Rs.15,00,000'
},
{
  'id':4,
  'title':'backend Engineer',
  'location':'San Francisco , USA',
  'salary':'$ 120,000'
}
]
@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                        company_name='Johnson')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

# print(__name__)
if __name__ == '__main__':
  # print("I'm inside the if now")
  app.run(host='0.0.0.0',debug=True)