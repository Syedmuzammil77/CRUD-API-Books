from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def home():
    return "Welcome to the HomePage Syed!"
 
@app.route("/educative")
def learn():
    return "Happy Learning at Educative Syed!"
 
 
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)