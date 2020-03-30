"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cupcake(db.Model):
    """ Cupcake class """

    __tablename__ = "cupcake"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    flavor = db.Column(
        db.String(50),
        nullable=False
    )

    size = db.Column(
        db.String(50),
        nullable=False
    )

    rating = db.Column(
        db.Float(),
        nullable=False
    )

    image = db.Column(
        db.String(),
        nullable=False,
        default='https://tinyurl.com/demo-cupcake'
    )


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
