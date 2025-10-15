from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "mysecret"  # required for flashing messages

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        flash(f"Account created for {username} 🎉")
        return redirect(url_for("signup"))
    return render_template("signup.html")


if __name__=="__main__":
    app.run(debug=True)