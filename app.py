
from flask import Flask
#create flask aplication
app=Flask(__name__)
#rejister the rout to the aplication
#inside the rout the path of the page will mention
@app.route('/')
def hellow_world():
   return "siya ke raam"
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)

  