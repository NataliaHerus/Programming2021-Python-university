from app import *
from Orders.Orders import *


class Orders(Orders, db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    contract_id = db.Column(db.Integer)
    _amount = db.Column(db.Integer)
    date = db.Column(db.String(20))

    def __init__(self, **d):
        super().__init__(**d)


class OrdersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'contract_id',
                  'amount', 'date')