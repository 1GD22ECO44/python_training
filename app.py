from flask import Flask,render_template,jsonify,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='roottoor'
app.config['MYSQL_DB']='pavan_ece'
mysql=MySQL(app)



@app.route('/index')
def index():
    return 'flask flask is working'
@app.route('/store',methods = ['POST'])
def store_data():
    try:

        cur=mysql.connection.cursor()
        json=request.get_json()
        title=json.get("title")
        content=json.get("content")
        sql='insert into blog(title,content)values(%s,%s)'
        val=(title,content)
        cur.execute(sql)
        mysql.connection.commit()


        cur.close()
        return'success'
    except Exception as e:
        return f"error in insertion data:{e}"

@app.route('/')
def hello_world():
    return 'Hello World'


from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/myname')
def printMyName():
    return 'pintu'

@app.route('/home')
def loadHomeHtml():
    return render_template("home.html")

@app.route('/about')
def loadaboutHtml():
    return render_template("about.html")


@app.route('/contact')
def loadcontactHtml():
    return render_template("contact.html")


@app.route('/main')
def loadMainHtml():
    return render_template("home_bc.html")


@app.route('/user_detail')
def userDetail():
    sql="SELECT * FROM people"
    cur=mysql.connection.cursor()
    cur.execute(sql)
    results=cur.fetchall()
    cur.close()
    return jsonify(results)

@app.route("/update",methods=["post"])
def updatepeople():
    id = request.form['id']
    email = request.form['email']
    password = request.form['password']
    cur=mysql.connection.cursor()
    sql="update into people(id,email,password) values(%s,%s,%s)"
    val=[id,email,password]
    cur.execute(sql,val)
    mysql.connection.commit()

    cur.close()
    return "update success"

if __name__ == '__main__':
    app.run()