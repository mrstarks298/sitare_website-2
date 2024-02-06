
from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

def get_connection():
    conn = psycopg2.connect(
        dbname=sitare_hiring_data',
        user='s',
        password='m5eAZw9B93e3yI3zq8VVFBDpLzyKNmQf',
        host='dpg-cn0akhmd3nmc738a4mcg-a'
    )
    return conn

@app.route('/application_form', methods=['GET', 'POST'])
def application_form():
    if request.method == 'POST':
        # Extract data from the form
        data = request.form.to_dict()

        # Connect to the database and insert the data
        conn = get_connection()
        cursor = conn.cursor()

        # Example SQL INSERT statement, adjust to your table schema
        sql = INSERT INTO jobs  (Full_Name VARCHAR(255), Email VARCHAR(255), LinkedIn VARCHAR(255), Phone VARCHAR (255), Country VARCHAR(255) )
                 VALUES (%s, %s, ...)"""
        cursor.execute(sql, (data['field1'], data['field2'], ...))

        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

        # Redirect to a success page or display a success message
        return redirect(url_for('success'))

    # Render the form for GET requests
    return render_template('application_form.html')

@app.route('/success')
def success():
    return "Your application has been submitted successfully!"

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM jobs;') # Assuming 'jobs' is the table name
    jobs = cursor.fetchall()
    conn.close()
    return render_template('application_submittion.html', jobs=jobs) # Pass jobs to the template
  @app.route('/application_form.html')
  def world():
    return render_template('application_form.html')

@app.route('/job/apply', methods=['post'])
def apply_job():
    data = request.form.to_dict()
    return render_template('application_submitted.html', application=data)


# Other routes remain unchanged...

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
