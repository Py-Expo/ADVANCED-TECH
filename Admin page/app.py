from flask import Flask,render_template,url_for,redirect,request
from flask_mysqldb import MySQL
app=Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="Muthu123"
app.config["MYSQL_DB"]="complaintbox"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app) #connection string


#loading page
@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="SELECT * FROM complaint"
    con.execute(sql)
    res=con.fetchall()
    return render_template("home.html",datas=res) #passing data to html to use the datas of mysql

#New user
@app.route("/adduser",methods=['GET','POST'])
def adduser():
    if request.method == 'POST':
        creater=request.form['creater']
        about=request.form['about']
        status=request.form['status']
        con=mysql.connection.cursor()
        sql="insert into complaint(creater,about,status) value (%s,%s,%s)"
        con.execute(sql,[creater,about,status])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
        
    return render_template("adduser.html")

#update user
@app.route("/edituser/<string:id>",methods=['GET','POST']) # id is the variable name which takes the particular data what you have selected
def edituser(id):
    con=mysql.connection.cursor()
    if request.method == 'POST':
        creater=request.form['creater']
        about=request.form['about']
        status=request.form['status']
        sql="update complaint set creater=%s,about=%s,status=%s where creater=%s"
        con.execute(sql,[creater,about,status,creater])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
        con=mysql.connection.cursor()
    sql="Select *from complaint where creater=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template("edituser.html",datas=res)


if(__name__=='__main__'):
    app.run(debug=True)