from flask import Flask, Response, request
from bson.objectid import ObjectId

import json
import pymongo
#mongoAlchemy 

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(host="localhost", port=27017, serverSelectionTimeoutMS = 1000)
    mongo.server_info() 
    db = mongo.company
except:
    print("Error - Cannot connect to db")

@app.route("/users", methods=["GET"])
def get_some_users():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(
                response = json.dumps(data),
                status = 500,
                mimetype = "application/json"
                )
    except:
        return Response(
                response = json.dumps({"message": "cannot read users"}),
                status = 500,
                mimetype = "application/json"
                )

@app.route("/users", methods=["POST"])
def create_user():
    try:
        user = {"name": request.args.get("name"), "lastname": request.args.get("lastname")}
        dbResponse = db.users.insert_one(user)
        return Response(
                response = json.dumps({"message": "user created", "id": f"{dbResponse.inserted_id}"}),
                status = 200,
                mimetype = "application/json"
                )
    except Exception as ex:
        return ex

@app.route("/users/<id>", methods=["PATCH"])
def update_user(id):
    try:
        if "name" in request.args and "lastname" in request.args:
            dbResponse = db.users.update_one({"_id": ObjectId(id)}, {"$set":{"name": request.args.get("name"), "lastname": request.args.get("lastname")}})
        elif "name" in request.args:
            dbResponse = db.users.update_one({"_id": ObjectId(id)}, {"$set":{"name": request.args.get("name")}})
        elif "lastname" in request.args:
            dbResponse = db.users.update_one({"_id": ObjectId(id)}, {"$set":{"lastname": request.args.get("lastname")}})
        else:
            return "no arguments provided"
        if dbResponse.modified_count == 1:
            return Response(
                    response = json.dumps({"message": "updated user"}),
                    status = 200,
                    mimetype = "application/json"
                    )
    except Exception as ex:
        return Response(
                response = json.dumps({"message": "cannot update user"}),
                status = 500,
                mimetype = "application/json"
                )

@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse = db.users.delete_one({"_id": ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(
                    response = json.dumps({"message": "deleted user", "id": f"{id}"}),
                    status = 200,
                    mimetype = "application/json"
                    )
        return "user not found"
    except Exception as ex:
        return Response(
                response = json.dumps({"message": "cannot delete user", "id": f"{id}"}),
                status = 500,
                mimetype = "application/json"
                )

if __name__ == "__main__":
    app.run(port=80, debug=True)
