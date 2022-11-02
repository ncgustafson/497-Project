"""Closet development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\x12\xdd^\xae\xf6\xd7t\x0c\
    \xd9\x1a\x8a\r\x7f3\xe3D\xf2\xa7\xf5La"J\xfc'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
CLOSET_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = CLOSET_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/closet.sqlite3
DATABASE_FILENAME = CLOSET_ROOT/'var'/'closet.sqlite3'
