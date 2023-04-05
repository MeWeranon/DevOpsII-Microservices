from flask import Flask, request, jsonify
import datetime

import data_user as us

app = Flask(__name__)

@app.route('/delete/<name>', methods=['DELETE'])

def delete(name):
    try:
        _user = us.user_name()
        data = [x for x in _user if x["name"]==name]

        if data:
            us.delete_user(name)
            return jsonify({'message': 'item deleted successfully'}), 200
        else: 
            return jsonify({'message': 'item Not Found'}), 404
    except:
        return jsonify({'message': 'item not found.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1