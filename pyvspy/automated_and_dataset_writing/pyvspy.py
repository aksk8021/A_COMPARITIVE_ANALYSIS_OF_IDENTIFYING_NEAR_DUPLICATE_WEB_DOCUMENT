with open("app.py","a") as f:
    s1="""print("hello world")"""
    # f.write(f"\n{s1}")
#     s2="""
# @app.route("/p11")
# def p11():
#     return render_template("p11.html")
#     """
    # f.write(f"\n{s2}")
    for i in range(300):
        s2=f"""
@app.route("/p{i+1}")
def p{i+1}():
    return render_template("p{i+1}.html")
    """
        f.write(f"\n{s2}")
    s3="""
if __name__=="__main__":
    app.run(debug=True,port=8000)
    """
    f.write(f"\n{s3}")
