from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {
        "id": "1",
        "name": "Odium",
        "planet": "Roshar",
        "affiliation": "Shard Of Adonalsium"
    },
    {
        "id": "2",
        "name": "Kaladin",
        "planet": "Roshar",
        "affiliation": "Radiant"
    },
    {
        "id": "3",
        "name": "Adolin Kohlin",
        "planet": "Roshar",
        "affiliation": "Coalition"
    },
    {
        "id": "4",
        "name": "Ja-anat",
        "planet": "Roshar",
        "affiliation": "spren of Odium"
    }
]


@app.route('/hello')
def say_hello():
    return jsonify('Welcome to the Rosharan System')


@app.route('/stormlight/<id>')
def get_user_by_id(id):
    for user in data:
        if user["id"] == id:
            return jsonify(user)
    return jsonify("user doesnt exist"), 404


if __name__ == "__main__":
    app.run(port="8086", host="0.0.0.0")
