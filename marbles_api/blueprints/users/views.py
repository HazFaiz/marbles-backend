from flask import Blueprint, jsonify, request
from models.user import User  # << Merge with the models for this to work
from playhouse.shortcuts import model_to_dict

users_api_blueprint = Blueprint('users_api',
                                __name__,
                                template_folder='templates')


# --- API THAT RETURNS ALL USERS ----
@users_api_blueprint.route('/', methods=['GET'])
def index():
    users = User.select()
    user_data = []
    for user in users:
        user = model_to_dict(user)
        user_data.append(user)
    return jsonify(user_data), 200

# ------ API THAT SELECTS A USER BY ID -----------
@users_api_blueprint.route('/<id>', methods=['GET'])
def show(id):
    user = User.get_or_none(User.id == id)

    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'profile_image': user.profile_image,
            'private': user.private

            # image in static/images, but no idea how to link this.
        }), 200
    else:
        return jsonify({'message': 'user not found'}), 418

# ------ API TO CREATE A USER, RETURNS A new_user OBJECT BACK -------------
@users_api_blueprint.route('/', methods=['POST'])
def create():

    user = request.get_json()

    new_user = User(
        name=user['name'],
        password=user['password'],
        email=user['email']
    )

    if new_user.save():
        return jsonify({
            'message': 'new user created!',
            'status': 'success',
            'new_user': {
                'id': new_user.id,
                'name': new_user.name,
                'email': new_user.email
            },
        }), 200
    else:
        er_msg = []
        for error in new_user.errors:
            er_msg.append(error)
        return jsonify({'message': er_msg}), 418


# ---- API FOR UPDATING USER DETAILS--------
@users_api_blueprint.route('/<id>', methods=['POST'])
def update(id):
    user = User.get_by_id(id)

    update = request.get_json()

    user.name = update['name']
    user.email = update['email']
    user.gender = update['gender']

    if user.save():
        return jsonify({
            'message': 'successfully updated profile',
            'status': 'success',
            'updated_user': {
                'id': user.id,
                'name': user.name,
                'email': user.email,
            },
        }), 200
    else:
        er_msg = []
        for error in user.errors:
            er_msg.append(error)
        return jsonify({'message': er_msg}), 418

# +++++ ON HOLD FOR NOW. ASK MATT WHEN TEAM COMES TO THAT POINT. SAME FOR THREADS/POSTS AS WELL SINCE IT NEEDS TO BE UPLOADED TO S3 ++++----

# ----- API NEED TO DO: 1) UPLOAD PROFILE IMAGE
@users_api_blueprint.route('/upload', methods=['POST'])
def upload_profileimg():

    # +++ UPLOAD PROFILE IMAGE CODE HERE +++

    # 2) UPLOAD THREAD/POST
    pass


@users_api_blueprint.route('/<username>/upload', methods=['POST'])
def upload_thread(username):

    # +++ UPLOAD THREAD CODE HERE +++
    pass
