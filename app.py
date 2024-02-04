from flask import Flask, render_template
from database import engine
from sqlalchemy import text
#create flask aplication
app = Flask(__name__)

#crete python list


#rejister the rout to the aplication
#inside the rout the path of the page will mention
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs


@app.route('/')
def hellow_world():
  jobs = load_jobs_from_db
  return render_template('index.html', jobs=jobs, company_name='Sitare')


#we can show data in json formate by:
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
