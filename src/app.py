"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<id>', methods=['GET'])
def getMember(id):
    # this is how you can use the Family datastructure by calling its methods
    ok = jackson_family.get_member(id)
    if not ok:
        return "Something went wrong looking for the ID", 400
    return jsonify(ok), 200

@app.route('/member', methods=['POST'])
def add_member():
    # this is how you can use the Family datastructure by calling its methods
    memberId = jackson_family.add_member(request.json)
    return jsonify({"memberId":memberId}), 200
    
@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    # this is how you can use the Family datastructure by calling its methods
    member=request.json
    ok = jackson_family.update_member(id, member)
    if not ok:
        return "couldnt edit the data", 400
    return jsonify({"ok": ok}), 200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    # this is how you can use the Family datastructure by calling its methods
    success = jackson_family.delete_member(id)
    if (success): 
        return jsonify({"done":True}), 200
    return "Something went wrong trying to delete, try again", 400


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)