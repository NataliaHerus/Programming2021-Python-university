from sqlalchemy import desc, cast
from sqlalchemy.inspection import inspect
from flask import request, jsonify, flash
from ContractNeww.ContractNewSchema import *
import hashlib
from User.User_Schema import *
from Orders.OrdersSchema import *
from flask_jwt_extended import verify_jwt_in_request, create_access_token, get_jwt_claims
from flask_login import logout_user, login_required, login_user
from datetime import date

contract_schema = ContractSchema()
contracts_schema = ContractSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

order_schema = OrdersSchema()
orders_schema = OrdersSchema(many=True)


@app.route('/api/orders', methods=['POST'])
def create_order():
    verify_jwt_in_request()
    claims = get_jwt_claims()
    try:
        order = Orders(id=request.json["id"],
                       user_id=claims["id"],
                       contract_id=request.json["contract_id"],
                       amount=request.json["amount"],
                       date=str(date.today()))
        contract = Contract.query.get_or_404(request.json["contract_id"])
        contract.amount = contract.amount - request.json["amount"]
        db.session.add(order)
        db.session.commit()
        return order_schema.jsonify(order), 201
    except Exception as e:
        return jsonify(status='404', message=str(e)), 404


@app.route('/api/orders', methods=['GET'])
def orders():
    try:
        verify_jwt_in_request()
        claims = get_jwt_claims()
        orders = Orders.query.filter(Orders.user_id == claims['id'])
        len_orders = len(orders_schema.dump(orders))
        orders = orders_schema.dump(orders)
        return jsonify({'contracts': orders},
                       {'count': len_orders}), 201
    except Exception as e:
        return jsonify(status='404', message=str(e)), 404


@app.route('/api/orders/<id>', methods=['GET'])
def order_detail(id):
    try:
        verify_jwt_in_request()
        claims = get_jwt_claims()
        order = Orders.query.get_or_404(id)
        if order.user_id == claims['id']:
            return order_schema.jsonify(order), 201
        else:
            return jsonify(status='404', message="Id is not found"), 404
    except Exception as e:
        return jsonify(status='404', message=str(e)), 404


@app.route('/api/users', methods=['POST'])
def register():
    form = request.json
    try:
        hashed_password = hashlib.sha256(form['password'].encode('utf-8')).hexdigest()
        new_user = User(last_name=form["last_name"], first_name=form["first_name"], email=form["email"],
                        password=hashed_password, role=form["role"])

        db.session.add(new_user)
        db.session.commit()
        flash('You have successfully registered', 'success')
        return user_schema.jsonify(new_user), 201

    except Exception as e:
        return jsonify({'status': '404', 'message': str(e)}), 400


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return {"id": identity}


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    try:
        logout_user()
        return jsonify({'status': 'success'}), 204
    except Exception as e:
        return jsonify({'status': '404', 'message': str(e)}), 404


@app.route('/login', methods=['POST'])
def login():
    form = request.json
    hashed_password = hashlib.sha256(form['password'].encode('utf-8')).hexdigest()
    email = form["email"]
    user = User.find_by_email(email)
    if not user:
        return jsonify({'status': '404', 'message': 'Incorrect login'}), 404
    if user.password == hashed_password:
        access_token = create_access_token(user.id)
        login_user(user)
        return jsonify(access_token=access_token), 201
    else:
        return jsonify({'status': '404', 'message': 'Incorrect login or password.'}), 404


@app.route("/contracts", methods=["GET"])
def posts():
    sort_by = request.args.get('sort_by')
    sort_type = request.args.get('sort_type', default='desc')
    s = request.args.get('s')
    offset = request.args.get('offset', default=0, type=int)
    limit = request.args.get('limit', type=int)
    contracts = Contract.query
    #len_contracts = len(contracts_schema.dump(contracts))

    if sort_by is not None:
        try:
            if sort_type == "asc":
                contracts = contracts.order_by(sort_by)

            else:
                contracts = contracts.order_by(desc(sort_by))
        except Exception:
            return jsonify({'status': '404', 'message': 'Cant be sort in such way'})

    if s is not None:
        b = Contract._name.like('%' + s + '%')
        for column in inspect(Contract).c:
            b |= cast(getattr(Contract, column.name), db.String).like('%' + s + '%')
        contracts = contracts.filter(b)
    len_contracts = len(contracts_schema.dump(contracts))

    if limit is not None:
        contracts = contracts.offset(offset * limit).limit(limit)

    contracts = contracts_schema.dump(contracts)
    return jsonify({'contracts': contracts},
                   {'count': len_contracts})


@app.route("/contracts/<int:id>", methods=["GET"])
def posts_detail(id):
    contract = Contract.query.get(id)
    if not contract:
        return jsonify({'status': '404', 'message': 'Contract is not found'})
    return contract_schema.jsonify(contract)


@app.route("/contracts", methods=["POST"])
def create():
    try:
        verify_jwt_in_request()
        claims = get_jwt_claims()
        user_admin = User.query.get(claims["id"])
        Validation.validate_admin(user_admin.role)
        contract = Contract(id=request.json['id'], name=request.json['name'], email=request.json['email'],
                            phone=request.json['phone'], iban=request.json['iban'],
                            start_date=request.json['start_date'],
                            end_date=request.json['end_date'], user_id=claims["id"], amount=request.json['amount'])
        db.session.add(contract)
        db.session.commit()
        return contract_schema.jsonify(contract)
    except Exception as e:
        return jsonify({'status': '400', 'error': str(e)})


@app.route("/contracts/<int:id>", methods=["PUT"])
def post_update(id):
    verify_jwt_in_request()
    claims = get_jwt_claims()
    user_admin = User.query.get(claims["id"])
    try:
        Validation.validate_admin(user_admin.role)
        contract = Contract.query.get_or_404(id)
        contract.name = request.json['name']
        contract.email = request.json['email']
        contract.phone = request.json['phone']
        contract.iban = request.json['iban']
        contract.start_date = request.json['start_date']
        contract.end_date = request.json['end_date']
        contract.user_id = claims["id"]
        contract.amount = request.json['amount']
        db.session.commit()
    except Exception as e:
        return jsonify({'status': '404', 'error': str(e)})
    return contract_schema.jsonify(contract)


@app.route("/contracts/<int:id>", methods=["DELETE"])
def posts_delete(id):
    verify_jwt_in_request()
    claims = get_jwt_claims()
    user_admin = User.query.get(claims["id"])
    try:
        Validation.validate_admin(user_admin.role)
        contract = Contract.query.get_or_404(id)
        db.session.delete(contract)
        db.session.commit()
        return jsonify({'status': '200', 'message': "Contract has been successfully deleted"})
    except Exception as e:
        return jsonify({'status': '404', 'error': str(e)})

