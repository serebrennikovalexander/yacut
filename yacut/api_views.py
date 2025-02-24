import re
from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsageError
from .forms import MAX_LENGTH_FOR_CUSTOM_ID
from .models import URLMap
from .views import get_unique_short_id
from settings import STRING_LENGTH


def is_valid_string(s, pattern=r"^[a-zA-Z0-9]+$"):
    return bool(re.match(pattern, s))


@app.route("/api/id/", methods=["POST"])
def create_id():
    if not request.data:
        raise InvalidAPIUsageError("Отсутствует тело запроса")
    data = request.get_json()
    if not data:
        raise InvalidAPIUsageError("Отсутствует тело запроса")
    if "url" not in data:
        raise InvalidAPIUsageError('"url" является обязательным полем!')
    custom_id = data.get("custom_id", None)
    if custom_id == "" or custom_id is None:
        data["custom_id"] = get_unique_short_id(STRING_LENGTH)
    if URLMap.query.filter_by(short=data["custom_id"]).first() is not None:
        raise InvalidAPIUsageError(
            "Предложенный вариант короткой ссылки уже существует."
        )
    if len(
        data["custom_id"]
    ) > MAX_LENGTH_FOR_CUSTOM_ID or not is_valid_string(data["custom_id"]):
        raise InvalidAPIUsageError(
            "Указано недопустимое имя для короткой ссылки"
        )
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED


@app.route("/api/id/<short_id>/", methods=["GET"])
def get_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsageError(
            "Указанный id не найден", HTTPStatus.NOT_FOUND
        )
    return jsonify({"url": url_map.original}), HTTPStatus.OK
