from flask import Flask
app = Flask(__name__)

@app.route("/")
def greet():
  return "<p>Hello this is my first actions</p>"

if __name__=="__main__":
  app.run(debug=True)
