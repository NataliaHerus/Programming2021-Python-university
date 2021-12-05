from sqlalchemy import desc, cast
from sqlalchemy.inspection import inspect
from flask import request, jsonify
from Contract_Schema import *

contract_schema = ContractSchema()
contracts_schema = ContractSchema(many=True)


@app.route("/contracts", methods=["GET"])
def posts():
    sort_by = request.args.get('sort_by')
    sort_type = request.args.get('sort_type', default='desc')
    s = request.args.get('s')
    offset = request.args.get('offset', default=0, type=int)
    limit = request.args.get('limit', type=int)
    contracts = ContractTab.query
    len_contracts = len(contracts_schema.dump(contracts))

    if sort_by is not None:
        try:
            if sort_type == "asc":
                contracts = contracts.order_by(sort_by)

            else:
                contracts = contracts.order_by(desc(sort_by))
        except Exception:
            return jsonify({'status': '404', 'message': 'Cant be sort in such way'})

    if s is not None:
        b = ContractTab.name.like('%' + s + '%')
        for column in inspect(ContractTab).c:
            b |= cast(getattr(ContractTab, column.name), db.String).like('%' + s + '%')
        contracts = contracts.filter(b)

    if limit is not None:
        contracts = contracts.offset(offset * limit).limit(limit)

    contracts = contracts_schema.dump(contracts)
    return jsonify({'contracts': contracts},
                   {'count': len_contracts})


@app.route("/contracts/<int:id>", methods=["GET"])
def posts_detail(id):
    contract = ContractTab.query.get(id)
    if not contract:
        return jsonify({'status': '404', 'message': 'Contract is not found'})
    return contract_schema.jsonify(contract)


@app.route("/contracts", methods=["POST"])
def create():
    try:
        contract = ContractTab(id=request.json['id'], name=request.json['name'], email=request.json['email'],
                               phone=request.json['phone'], iban=request.json['iban'],
                               start_date=request.json['start_date'],
                               end_date=request.json['end_date'])
        db.session.add(contract)
        db.session.commit()
        return contract_schema.jsonify(contract)
    except Exception as e:
        return jsonify({'status': '400', 'error': str(e)})


@app.route("/contracts/<int:id>", methods=["PUT"])
def post_update(id):
    contract = ContractTab.query.get(id)
    if not contract:
        return jsonify({'status': '404', 'message': 'Contract is not found'})
    try:
        contract.id = request.json['id']
        contract.name = request.json['name']
        contract.email = request.json['email']
        contract.phone = request.json['phone']
        contract.start_date = request.json['start_date']
        contract.end_date = request.json['end_date']
        db.session.commit()
    except Exception as e:
        return jsonify({'status': '400', 'error': str(e)})

    return contract_schema.jsonify(contract)


@app.route("/contracts/<int:id>", methods=["DELETE"])
def posts_delete(id):
    product = ContractTab.query.get_or_404(id)

    db.session.delete(product)
    db.session.commit()
    return jsonify({'status': '200', 'message': "Contract has been successfully deleted"})