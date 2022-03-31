from flask import Blueprint, request, jsonify
from flask_login import LoginManager, login_required
from flask.helpers import make_response
import database
import controllers

urls_blueprint = Blueprint('urls', __name__,)

login_manager = LoginManager()

@urls_blueprint.route('/')
def index():
    return 'urls index route'

#### LOGIN

@login_manager.user_loader
def load_user(user_id):
    return controllers.controller_load_user(user_id)

@urls_blueprint.route("/login", methods=["POST"])
def login():
    credentials = request.get_json()
    res = controllers.controller_login(credentials)
    return make_response(jsonify(res))


@urls_blueprint.route("/logout", methods=["GET"])
@login_required
def logout():
    res = controllers.controller_logout()
    return make_response(jsonify(res))    

#######


@urls_blueprint.route('/airports', methods = ['GET'])
def get_airports():
    ret = controllers.return_airports()
    return make_response(jsonify(ret))

@urls_blueprint.route('/airports/<name>', methods = ['GET'])
def get_airports_by_origin(name):
    ret = controllers.return_airport_by_origin(name)
    return make_response(jsonify(ret))


@urls_blueprint.route('/flights/<date>', methods = ['GET'])
def get_flights_by_date(date):
    ret = controllers.return_flights_by_date(date)
    return make_response(jsonify(ret))


@urls_blueprint.route('/flights', methods = ['GET'])
def get_flights_by_price():
    data = request.get_json()
    ret = controllers.return_flights_by_price(data)
    return make_response(jsonify(ret))


@urls_blueprint.route('/booking', methods = ['POST'])
def make_reservation():
    data = request.get_json()
    ret = controllers.insert_reservations(data)
    return make_response(jsonify(ret))




@urls_blueprint.route('/usuarios', methods = ['PUT'])
def update_user():
    req_data = request.get_json()
    usuario_json = {"id": req_data['id'], "nome": req_data['nome'], "email": req_data['email']}
    ret = database.update_user(usuario_json)
    return ret

@urls_blueprint.route('/usuarios', methods = ['DELETE'])
def delete_user():
    req_data = request.get_json()
    usuario_json = {"id":req_data['id']}
    ret = database.delete_user(usuario_json)
    return ret