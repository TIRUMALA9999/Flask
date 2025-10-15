from flask import Flask
app=Flask(__name__)

@app.route("/") #Home page
def home():
    return "Welcome to Home Page"

@app.route("/about")
def about():
    return "This is the About Page"

@app.route("/contact")

def contact():
    return "Contact us at: contact@gmail.com"

if __name__=="__main__":
    app.run(debug=True)
