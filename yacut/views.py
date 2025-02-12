import random
import string

from flask import flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from settings import STRING_LENGTH


def get_unique_short_id(length):
    """ Функция реализует алгоритм формирования случайного
    короткого идентификатора заданной длины.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


@app.route('/', methods=['GET', 'POST'])
def main_page_view():
    form = URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if custom_id == '' or custom_id is None:
            custom_id = get_unique_short_id(STRING_LENGTH)
        if URLMap.query.filter_by(short=custom_id).first() is not None:
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('main_page.html', form=form)
        url_map = URLMap(
            original=form.original_link.data,
            short=custom_id
        )
        db.session.add(url_map)
        db.session.commit()
        return render_template('main_page.html', form=form, url_map=url_map)
    return render_template('main_page.html', form=form)


@app.route('/<short>')
def redirect_page_view(short):
    url_map = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url_map.original)
