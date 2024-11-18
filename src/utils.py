from enum import Enum


class MessageCategory(str, Enum):
    ERROR = 'alert alert-danger'
    WARNING = 'alert alert-warning'
    SUCCESS = 'alert alert-success'