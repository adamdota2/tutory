from flask import Blueprint, render_template, url_for, redirect, request, flash,session, jsonify
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
from models.announcement import Announcement

dashboard_api_blueprint = Blueprint('dashboard_api',
                             __name__,
                             template_folder='templates')


@dashboard_api_blueprint.route('/<id>', methods=['GET'])
@jwt_required
def home():
    username = get_jwt_identity()
    user = User.get_or_none(User.identity_card == username)

    if user:
        result = []
        for announcement in Announcement.select():
            result.append({
                "post_id": announcement.id,
                "name": announcement.full.name,
                "title": announcement.title,
                "post": announcement.post
            })
        return jsonify(result)


@dashboard_api_blueprint.route('/update', methods=['POST'])
@jwt_required
def new_announcement():
    # staff_name = request.json.get("full_name")
    # new_title = request.json.get("title")
    # new_post = request.json.get("post")

    user = get_jwt_identity
    params = request.json
    new_announcements = Announcement(full_name=params.get("full_name"), title=params.get("title"),post=params.get("post"))

    if User.get_or_none(User.full_name == staff_name) and User.roles == "staff":
        if new_announcements.save():
            pass




@dashboard_api_blueprint.route('/edit', methods=['POST'])
@jwt_required
def edit_existing_post():
    user = get_jwt_identity()
    if user.roles == 'staff':
        post_id = request.json.get("post_id")
        updated_title = request.json.get("title")
        updated_post = request.json.get("post")
        post_to_edit = Announcement.get_by_id(Announcement.id == post_id)
        post_to_edit.title = updated_title
        post_to_edit.post = updated_post

        if post_to_edit.save():
            result = []
            for announcement in Announcement.select():
                result.append({
                    "post_id": announcement.id,
                    "name": announcement.full.name,
                    "title": announcement.title,
                    "post": announcement.post
                })
            return jsonify(result)
        else:
            return jsonify({"error":"Edit failed, please try again"})



@dashboard_api_blueprint.route('/delete', methods=['DELETE'])
@jwt_required
def delete_announcement():
    pass