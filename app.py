
from flask import Flask, render_template, request, jsonify

# Create Flask application
app = Flask(__name__)

# Create Python list
JOBS = [{
    'id': 1,
    'title': 'Asistent prof. Python ',
    'location': 'Indore, India',
    'Salary': 'Rs. 100000'
}, {
    'id': 2,
    'title': 'Data Science Prof.',
    'location': 'Indore, India',
    'Salary': 'Rs.150000'
}, {
    'id': 3,
    'title': 'Machine Learning Prof.',
    'location': 'Lucknow ,India',
    'Salary': 'Rs.200000'
}]

# Register the route to the application
@app.route('/')
def hellow_world():
    return render_template('index.html', job=JOBS)

# Show data in JSON format
@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

#we can show data in json formate by:
@app.route('/application_form.html')
def world():
  return render_template('application_form.html')
@app.route('/apply now',methods=['post'])
def helo_duniya():
  data=request.form
  return render_template('application_submitted.html',application=data)

@app.route('/job/<id>')
def show_job(id):
    for job in JOBS:
        if str(job['id']) == id:
            return jsonify(job)
    return jsonify({"error": "Job not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
