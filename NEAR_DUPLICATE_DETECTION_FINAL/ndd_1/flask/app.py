from flask import Flask
from flask import render_template,request,redirect


app = Flask(__name__)

@app.route("/")
def root():
    return render_template("p1.html")

@app.route("/p11")
def p11():
    return render_template("p11.html")

@app.route("/p12")
def p12():
    return render_template("p12.html")

@app.route("/p13")
def p13():
    return render_template("p13.html")

@app.route("/p14")
def p14():
    return render_template("p14.html")

@app.route("/p15")
def p15():
    return render_template("p15.html")

@app.route("/p16")
def p16():
    return render_template("p16.html")

@app.route("/p17")
def p17():
    return render_template("p17.html")

@app.route("/p18")
def p18():
    return render_template("p18.html")

@app.route("/p19")
def p19():
    return render_template("p19.html")

@app.route("/p110")
def p110():
    return render_template("p110.html")

@app.route("/p111")
def p111():
    return render_template("p111.html")

@app.route("/p112")
def p112():
    return render_template("p112.html")

if __name__=="__main__":
    app.run(debug=True,port=5000)