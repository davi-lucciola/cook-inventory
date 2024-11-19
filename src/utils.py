from enum import Enum


class MessageCategory(str, Enum):
    ERROR = 'alert alert-danger'
    WARNING = 'alert alert-warning'
    SUCCESS = 'alert alert-success'


def is_image_file(filename: str) -> bool:
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS