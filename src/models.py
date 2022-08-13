from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
        }
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    haircolor = db.Column(db.String(20))
    eyecolor = db.Column(db.String(20))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "haircolor": self.haircolor,
            "eyecolor": self.eyecolor,
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    climate = db.Column(db.String(20))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character = db.relationship(Character)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'),nullable=True)
    planet = db.relationship(Planet)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'),nullable=True)
    user = db.relationship(User)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def serialize(self):
        return {
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "user_id": self.user_id,
        }