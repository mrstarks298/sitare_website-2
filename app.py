from flask import Flask,render_template
#create flask aplication
app = Flask(__name__)
JOBS={
  'id':1,
  'title':'Asistent prof. Python ','location':'Indore, India','Salary':'Rs. 100000'
}
{
  'id':2,'title':'Data Science Prof. ','location':'Indore','India','Salary':'Rs.150000'
}
{
'id':3,'title':'Machine Learning Prof.','location':'Lucknow ','India','Salary':'Rs.200000'
}



#rejister the rout to the aplication
#inside the rout the path of the page will mention
@app.route('/')
def hellow_world():
  return render_template('index.html',jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
