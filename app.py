from flask import Flask, request, jsonify
from models import db, Cupcake, connect_db

API_BASE_URL = "http://www.mapquestapi.com/geocoding/v1"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


def serialize_cupcake(cupcake):
    """ serializes a cupcake SQLAlchemy obj to dict"""

    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }


@app.route('/api/cupcakes')
def all_cupcakes_data():
    """ get data on all cupcakes """
    cupcakes = Cupcake.query.all()

    serialized = [serialize_cupcake(cupcake) for cupcake in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route('/api/cupcakes/<int:cupcake_id>')
def show_cupcake_data(cupcake_id):
    """  shows profile for an individual cupcake instance """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = serialize_cupcake(cupcake)

    return jsonify(cupcake=serialized)  # cupcake here will be in the response


@app.route('/api/cupcakes', methods=["POST"])
def create_new_cupcake():
    """ post method to create a new cupcake
    we expect we'll eventually have to come back and make this work
    for a form and use WTForms"""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"] or None

    # if request.json["image"] == '':
    #     image = None
    # else:
    #     image = request.json["image"]

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize_cupcake(new_cupcake)

    return (jsonify(cupcake=serialized), 201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    " update an existing cupcake "

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json["flavor"]
    cupcake.size = request.json["size"]
    cupcake.rating = request.json["rating"]

    if request.json["image"] == '':
        cupcake.image = 'https://tinyurl.com/demo-cupcake'
    else:
        cupcake.image = request.json["image"]

    db.session.commit()

    serialized = serialize_cupcake(cupcake)

    return (jsonify(cupcake=serialized), 200)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    "delete a cupcake"

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return (jsonify(message="Deleted"), 200)
