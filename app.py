from flask import Flask, render_template,  request, redirect, url_for

app =Flask(__name__)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/user/', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('user.html')

@app.route('/login/', methods=['GET', 'POST'])    
def login():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('login.html')


app.run(use_reloader=True)
