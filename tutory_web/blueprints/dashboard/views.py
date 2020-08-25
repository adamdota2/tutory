from flask import Blueprint, render_template, url_for, redirect, request, flash,session, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from models.user import User
from models.announcement import Announcement
from werkzeug.security import check_password_hash
# from instagram_web.util.google_oauth import oauth

dashboard_blueprint = Blueprint('dashboard',
                                __name__,
                                template_folder='templates')


# @dashboard_blueprint.route('/new', methods=['GET'])
# @login_required
# # @roles_required ('staff')
# def new():
#     if current_user.roles == "staff":
#         return render_template('dashboard/new.html')


# @dashboard_blueprint.route('/', methods=["POST"])
# # @login_required
# def create():
#     # params = request.form
#     print(params.get("staff"))
#     new_announcement = Announcement(staff=params.get("staff"), post=params.get("post"))
#     if new_announcement.save():
#         response = {
#             "message": "Sucessfully added new announcement"
#             "status": "success"
#         }
#         return jsonify(response)
#     else:
#         response = {
#             "message": "Something happened"
#             "status": "fail"
#         }
#         return jsonify(response)

# request.json = {
#     # staff_id: 1,
#     post: "bomba  coming"
# }