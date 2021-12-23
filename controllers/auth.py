import db

user_id = 1


def is_first_time():
    return db.is_table_empty('USER')


def is_logged_in():
    # TODO check database
    return (user_id != None)


def get_current_user():
    return None


def register(pic, name, email, phone, password):
    pass


def login(email, password):
    pass


def logout():
    pass
