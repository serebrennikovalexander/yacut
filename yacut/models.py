from datetime import datetime
from urllib.parse import urljoin

from flask import request

from . import db
from .forms import MAX_LENGTH_FOR_ORIGINAL_LINK, MAX_LENGTH_FOR_CUSTOM_ID


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(
        db.String(MAX_LENGTH_FOR_ORIGINAL_LINK), nullable=False
    )
    short = db.Column(db.String(MAX_LENGTH_FOR_CUSTOM_ID))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return {
            'url': self.original,
            'short_link': urljoin(request.host_url, self.short)
        }

    def from_dict(self, data):
        if 'url' in data:
            setattr(self, 'original', data['url'])
        if 'custom_id' in data:
            setattr(self, 'short', data['custom_id'])
