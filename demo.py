from flask import Flask, render_template, url_for, request, redirect, flash, session, g
import model




app = Flask(__name__)
app.secret_key = 'minimize'


#username = ''
user = model.check_users()


@app.route('/', methods=['GET'])
def home():
    if 'username' in session:
        g.user=session['username']
        return render_template('dash.html')
    return render_template('login.html')

app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop('username', None)
        areyouuser = request.form['username']
        pwd = model.check_pw(areyouuser)
        if request.form['password'] == pwd:
            session['username'] = request.form['username']
            return render_template('dash.html')
    return render_template("login.html")


@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']



@app.route('/index', methods = ['GET', 'POST'])
def index():

    if request.method == 'GET':

        data = model.employees()
        print(data)

        return render_template("index.html", employees = data)


    

@app.route('/insert', methods=['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        model.insert(name, email, phone)
        


        return redirect(url_for('index'))


@app.route('/edit', methods=['POST'])
def edit():

    if request.method == 'POST':

        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        my_edit = model.edit(name, email, phone, id)


    else:
        return('entry not updated')

    return render_template('index.html', employees = my_edit)


@app.route('/delete/<id>/', methods=['GET', 'POST']) 
def delete(id):
    my_delete = model.delete(id)

    return (my_delete)
 

@app.route('/dash', methods = ['GET', 'POST'])
def dash():
    return render_template('dash.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')


@app.route('/newuser', methods=['GET', 'POST'])
def newuser():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        color = request.form['color']
        model.signup(username, password, color)
        message = 'user created succesfully    '
        


        return render_template('login.html', message = message)



@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')



@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/getsession')
def getsession():
    if  'username' in session:
        return session['username']
    return redirect(url_for('login'))

# admin login page
@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')

# admin login form
@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        session.pop('email', None)
        areyouuser = request.form['email']
        pwd = model.admin_pw(areyouuser)
        if request.form['password'] == pwd:
            session['email'] = request.form['email']
            return redirect(url_for('users'))
    return render_template('adminindex.html')

# admin session
@app.route('/admingetsession')
def admingetsession():
    if  'email' in session:
        return session['email']
    return redirect(url_for('admin'))


#users page 
@app.route('/users', methods=['GET', 'POST'])
def users():
    
    if request.method == 'GET':

        data = model.users()
        print(data)
        return render_template('users.html')

# deleting users from admin page
@app.route('/userdelete/<id>/', methods=['GET', 'POST']) 
def userdelete(id):
    my_delete = model.userdelete(id)

    return (my_delete)
 


# admin logout
@app.route('/adminlogout')
def adminlogout():
    session.pop('email', None)
    return redirect(url_for('admin'))

# index page for admin
@app.route('/adminindex', methods = ['GET', 'POST'])
def adminindex():

    if request.method == 'GET':

        data = model.employees()
        print(data)

        return render_template("adminindex.html", employees = data)





if __name__== "__main__":
    app.run(debug=True)