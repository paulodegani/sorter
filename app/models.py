from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)


class Dt6010(db.Model):
    __tablename__ = 'dt6010'
    dt6_fildoc = db.Column(db.String(2), nullable=False, primary_key=True)
    dt6_doc = db.Column(db.String(9), nullable=False, primary_key=True)
    dt6_serdoc = db.Column(db.String(3), nullable=False, primary_key=True)
    dt6_pedcli = db.Column(db.String(15), nullable=False)
    dt6_ceva = db.Column(db.String(9), nullable=False)
    dt6_emissao = db.Column(db.String(8), nullable=False)
    dt6_remetente = db.Column(db.String(14), nullable=False)
    dt6_qtdvol = db.Column(db.Integer, nullable=False)
    dt6_peso = db.Column(db.Float, nullable=False)
    dt6_pesom3 = db.Column(db.Float, nullable=False)
    dt6_valor = db.Column(db.Float, nullable=False)
    dt6_cep = db.Column(db.String(55), nullable=False)
    dt6_endereco = db.Column(db.String(65), nullable=False)
    dt6_destinatario = db.Column(db.String(40), nullable=False)
    dt6_frota = db.Column(db.String(7))
    dt6_sorter = db.Column(db.String(1))

    def __init__(self, dt6_fildoc, dt6_doc, dt6_serdoc,
                       dt6_pedcli, dt6_ceva, dt6_emissao,
                       dt6_remetente, dt6_qtdvol, dt6_peso,
                       dt6_pesom3, dt6_valor, dt6_cep,
                       dt6_endereco, dt6_destinatario,
                       dt6_frota, dt6_sorter):
        self.dt6_fildoc = dt6_fildoc
        self.dt6_doc = dt6_doc
        self.dt6_serdoc = dt6_serdoc
        self.dt6_pedcli = dt6_pedcli
        self.dt6_ceva = dt6_ceva
        self.dt6_emissao = dt6_emissao
        self.dt6_remetente = dt6_remetente
        self.dt6_qtdvol = dt6_qtdvol
        self.dt6_peso = dt6_peso
        self.dt6_pesom3 = dt6_pesom3
        self.dt6_valor = dt6_valor
        self.dt6_cep = dt6_cep
        self.dt6_endereco = dt6_endereco
        self.dt6_destinatario = dt6_destinatario
        self.dt6_frota = dt6_frota
        self.dt6_sorter = dt6_sorter

class TCUBAGEM(db.Model):
    __tablename__ = 'tcubagem'
    etiqueta = db.Column(db.String(50), nullable=False, primary_key=True)
    comprimento = db.Column(db.Float, nullable=False)
    largura = db.Column(db.Float, nullable=False)
    altura = db.Column(db.Float, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    multiplo = db.Column(db.Float, nullable=False)
    usuario = db.Column(db.String(30), nullable=False)
    tipo = db.Column(db.String(10), nullable=False)
    saida_prog = db.Column(db.Integer, nullable=False)
    saida_env = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    data = db.Column(db.String(8), nullable=False)
    pedcli = db.Column(db.String(15), nullable=False)
    frota = db.Column(db.String(8), nullable=False)

    def __init__(self, etiqueta, comprimento, largura,
                       altura, peso, multiplo, usuario,
                       tipo, saida_prog, saida_env,
                       status, data, pedcli, frota):
        self.etiqueta = etiqueta
        self.comprimento = comprimento
        self.largura = largura
        self.altura = altura
        self.peso = peso
        self.multiplo = multiplo
        self.usuario = usuario
        self.tipo = tipo
        self.saida_prog = saida_prog
        self.saida_env = saida_env
        self.status = status
        self.data = data
        self.pedcli = pedcli
        self.frota = frota






