from flask import Flask,render_template
#create flask aplication
app = Flask(__name__)


#rejister the rout to the aplication
#inside the rout the path of the page will mention
@app.route('/')
def hellow_world():
  return render_template('index.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
