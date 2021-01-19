from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from app import app, db
from app.models import User, Dt6010, TCUBAGEM


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/roteiro/', methods=['GET', 'POST'])
def roteiro():
    return render_template('roteiro.html')

@app.route('/consultaman/', methods=['GET', 'POST'])
def consultaman():
    print(request.method)
    if request.method == 'POST':
        man = request.form['pedcli']+"%"
        print(man)
        docto = []
        for dt6010 in Dt6010.query.filter(Dt6010.dt6_pedcli.like(man)):
            docto.append({"sorter":dt6010.dt6_sorter,"frota":dt6010.dt6_frota,"cte":dt6010.dt6_doc, "cep":dt6010.dt6_cep,
                          "destinatario":dt6010.dt6_destinatario,"caixa":dt6010.dt6_qtdvol},)        
        print(docto)
        return render_template('roteiro.html', docto = docto)

@app.route('/consultapn/', methods=['GET', 'POST'])
def consultapn():
    print(request.method)
    if request.method == 'POST':
        pn = request.form['pn']+"%"
        print(pn)
        etiq = []
        for tcubagem in TCUBAGEM.query.filter(TCUBAGEM.etiqueta.like(pn)):
            etiq.append({"etiqueta":tcubagem.etiqueta,"comprimento":tcubagem.comprimento,"largura":tcubagem.largura,
                          "altura":tcubagem.altura,"saida_prog":tcubagem.saida_prog,"saida_env":tcubagem.saida_env,
                          "data":tcubagem.data})        
        print(etiq)
        return render_template('pn.html', etiq = etiq)


@app.route('/user/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']

        user = User(name, email, pwd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
        
    return render_template('user.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))        

        login_user(user)
        return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

app.run(debug=True)