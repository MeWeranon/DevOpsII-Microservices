from flask import Flask, request, jsonify
import datetime
import data_user as us

app = Flask(__name__)

@app.route('/update/<prename>', methods=['PUT'])
def update(prename):
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    _user = us.user_name()
    data = [x for x in _user if x["name"]==prename]
    if data:
        us.update_item(name,category,price,instock, prename)
        return jsonify({'message': 'Update successfully.'}), 200
    else:
        return jsonify({'message': 'Fail to update'}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)