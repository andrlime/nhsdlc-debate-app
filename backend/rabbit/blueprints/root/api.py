"""
API routes for parser blueprint
"""

from http import HTTPStatus

from flask import Blueprint, Response
from flask_cors import cross_origin

from rabbit.core.util import make_json_response

bp = Blueprint("root", __name__)


@bp.route("/", methods=["GET"])
@cross_origin()
def get_root_page() -> Response:
    """
    Template route
    """

    return make_json_response("Hello world!!", HTTPStatus.OK)
