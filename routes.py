from flask import Blueprint, request, jsonify
from ai_engine import generate_blueprint

routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    return jsonify({"message": "FoundryAI API Running"})

@routes.route("/generate", methods=["POST"])
def generate():

    data = request.json

    idea = data.get("idea")

    blueprint = generate_blueprint(idea)

    return jsonify({
        "status": "success",
        "blueprint": blueprint
    })