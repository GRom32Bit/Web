from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))

    first=db.Column(db.Integer)
    second=db.Column(db.Integer)
    third=db.Column(db.Integer)
    forth=db.Column(db.Integer)
    fifth=db.Column(db.Integer)
    sixth=db.Column(db.Integer)
    seventh=db.Column(db.Integer)
    THL=db.Column(db.Integer)
    echo=db.Column(db.Integer)
    tyrant=db.Column(db.Integer)
    sorrow=db.Column(db.Integer)
    silverwolf=db.Column(db.Integer)
    ripper=db.Column(db.Integer)
    TCD=db.Column(db.Integer)
    Aristocrat=db.Column(db.Integer)
    Artist=db.Column(db.Integer)
    Banker=db.Column(db.Integer)
    BattleMaiden=db.Column(db.Integer)
    Beard=db.Column(db.Integer)
    Berserk=db.Column(db.Integer)
    Buried=db.Column(db.Integer)
    Butcher=db.Column(db.Integer)
    Clicker=db.Column(db.Integer)
    DorA=db.Column(db.Integer)
    DPeer=db.Column(db.Integer)
    Dreamer=db.Column(db.Integer)
    Drummer=db.Column(db.Integer)
    Drunkar=db.Column(db.Integer)
    Envy=db.Column(db.Integer)
    Faceless=db.Column(db.Integer)
    Forester=db.Column(db.Integer)
    Ghost=db.Column(db.Integer)
    Gunsmith=db.Column(db.Integer)
    Hawk=db.Column(db.Integer)
    Healer=db.Column(db.Integer)
    Hellmuse=db.Column(db.Integer)
    Hive=db.Column(db.Integer)
    Hydra=db.Column(db.Integer)
    Iceberg=db.Column(db.Integer)
    Illness=db.Column(db.Integer)
    Illusionist=db.Column(db.Integer)
    JestHarp=db.Column(db.Integer)
    Judge=db.Column(db.Integer)
    Lotus=db.Column(db.Integer)
    Mirror=db.Column(db.Integer)
    Monk=db.Column(db.Integer)
    Mortar=db.Column(db.Integer)
    Oldman=db.Column(db.Integer)
    Outcast=db.Column(db.Integer)
    Pain=db.Column(db.Integer)
    Phoenix=db.Column(db.Integer)
    Poison=db.Column(db.Integer)
    PreDark=db.Column(db.Integer)
    Raven=db.Column(db.Integer)
    Reaper=db.Column(db.Integer)
    RedThread=db.Column(db.Integer)
    Rescuer=db.Column(db.Integer)
    Rider=db.Column(db.Integer)
    Scavenger=db.Column(db.Integer)
    Splitted=db.Column(db.Integer)
    Tumbler=db.Column(db.Integer)
    Twins=db.Column(db.Integer)
    Undertaker=db.Column(db.Integer)
    Violinist=db.Column(db.Integer)
    Vulkan=db.Column(db.Integer)
    WatchMaker=db.Column(db.Integer)

    def set_pswrd(self, password):
        self.password = generate_password_hash(password)
    def check_pswrd(self, password):
        return check_password_hash(self.password, password)

class Page(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    pict=db.column(db.String(150))
    url=db.column(db.String(150))
    rating1=db.column(db.Integer)
    rating2 = db.column(db.Integer)
    rating3 = db.column(db.Integer)
    rating4 = db.column(db.Integer)
    rating5 = db.column(db.Integer)
    ratingTotal = db.column(db.Integer)

def pageprint():
    pages=Page.query.order_by(Page.ratingTotal).all()
