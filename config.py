from os import environ


class Config:
    SECRET_KEY = environ.get("SECRET_KEY") or "you_will_never_guess"