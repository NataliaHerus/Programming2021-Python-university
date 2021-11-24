from Contract_appear import *
from app import *


class ContractTab(Contract, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False)
    email = db.Column(db.String(30), unique=False)
    phone = db.Column(db.Integer, unique=False)
    iban = db.Column(db.String(40), unique=False)
    start_date = db.Column(db.String(10), unique=False)
    end_date = db.Column(db.String(10), unique=False)

    def __init__(self, **d):
        super().__init__(**d)


class ContractSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'phone',
                  'iban', 'start_date', 'end_date')
