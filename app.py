from flask import Flask, request, jsonify, make_response
from firebase_admin import db
from fire import initialize_app

initialize_app()

ref = db.reference("/")
users_ref = ref.child("users")
counter_ref = users_ref.child("counter")

app = Flask(__name__)
app.config["SECRET_KEY"] = "My_Secret_Key"

def add_user(data):
    current_count = counter_ref.get()
    if current_count == None:
        current_count = 0
    new_count = current_count + 1
    
    new_user = users_ref.child(f"User{new_count}")
    
    new_user.set(data)

    counter_ref.set(new_count)
    
# Create a test route
@app.route("/test", methods=["GET"])
def test():
    return make_response(jsonify({"message": "test route"}), 200)

# create a user
@app.route("/create_user", methods=["POST"])
def create_user():
    try:
        data = request.get_json()

        add_user(data)

        return make_response(jsonify({"message": "user created"}), 201)
    except:
        return make_response(jsonify({"message": f"error creating user"}), 500)

# Get all users
@app.route("/get_users", methods=["GET"])
def get_users():
    try:

        users = ref.get()

        return make_response(jsonify(users), 200)
    except:
        return make_response(jsonify({"message": "error getting users"}), 500)
    
# get a user by id
@app.route("/get_user", methods=["GET"])
def get_user():
    try:
        id = request.args.get("id")
        user = users_ref.child(f"User{id}").get()
        if user:
            return make_response(jsonify({"user": user}), 200)
        return make_response(jsonify({"message": "user not found"}), 404)
    except:
        return make_response(jsonify({"message": "error getting user"}), 500)

# update a user
@app.route("/update_user", methods=["PUT"])
def update_user():
    try:
        id = request.args.get("id")
        user = users_ref.child(f"User{id}")
        if user.get():
            data = request.get_json()

            user.update(data)
            
            return make_response(jsonify({"message": "user updated"}), 200)
        return make_response(jsonify({"message": "user not found"}), 404)
    except:
        return make_response(jsonify({"message": "error updating user"}), 500)
    
# delete a user
@app.route("/delete_user", methods=["DELETE"])
def delete_user():
    try:
        id = request.args.get("id")
        user = users_ref.child(f"User{id}")
        if user.get():
            user.delete()
            return make_response(jsonify({"message": "user deleted"}), 200)
        return make_response(jsonify({"message": "user not found"}), 404)
    except:
        return make_response(jsonify({"message": "error deleting user"}), 500)

if __name__ == "__main__":
    app.run(debug=True)
