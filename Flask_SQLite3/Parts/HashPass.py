import hashlib
import os


def encode_to_hash(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'), salt, 100000)
    return key, salt


def check_password(old_password_key, new_password, salt):
    new_password_key = hashlib.pbkdf2_hmac('sha256', new_password.encode('utf-8'), salt, 100000)
    if old_password_key == new_password_key:
        pass_correct = True
    else:
        pass_correct = False
    return pass_correct



