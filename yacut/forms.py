from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

MIN_LENGTH_FOR_ORIGINAL_LINK = 1
MAX_LENGTH_FOR_ORIGINAL_LINK = 256
MIN_LENGTH_FOR_CUSTOM_ID = 1
MAX_LENGTH_FOR_CUSTOM_ID = 16


class URLMapForm(FlaskForm):
    original_link = StringField(
        "Длинная ссылка",
        validators=[
            DataRequired(message="Обязательное поле"),
            Length(MIN_LENGTH_FOR_ORIGINAL_LINK, MAX_LENGTH_FOR_ORIGINAL_LINK),
        ],
    )
    custom_id = StringField(
        "Ваш вриант короткой ссылки",
        validators=[
            Length(MIN_LENGTH_FOR_CUSTOM_ID, MAX_LENGTH_FOR_CUSTOM_ID),
            Optional(),
        ],
    )
    submit = SubmitField("Создать")
