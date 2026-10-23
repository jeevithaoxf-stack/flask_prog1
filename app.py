from flask import Flask, jsonify


app = Flask(__name__)


# Static list of 5 users
users = [
    {
        "id": 1,
        "name": "Alice",
        "age": 22,
        "email": "alice@example.com"
    },
    {
        "id": 2,
        "name": "Bob",


        "age": 25,
        "email": "bob@example.com"
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 28,
        "email": "charlie@example.com"
    },
    {
        "id": 4,
        "name": "David",
        "age": 24,
        "email": "david@example.com"
    },
    {
        "id": 5,
        "name": "Emma",
        "age": 21,
        "email": "emma@example.com"
    }
]


# Endpoint to return all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# Endpoint to return a specific user by ID
@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user)


    return jsonify({"message": "User not found"}), 404


# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
