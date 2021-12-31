import db as _db

user = None


def is_first_time():
    return _db.is_table_empty('USER')


def is_logged_in():
    return (user != None)


def get_current_user():
    return None


def is_email_exists(email):
    result = _db.cursor.execute(f'SELECT COUNT(*) FROM USER WHERE EMAIL = ?', (email,)).fetchall()
    return (result[0][0] != 0)


def register(pic: str, name: str, email: str, phone: str, password: str, password2: str):
    import re
    if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
        raise Exception('Email is not valid')

    if is_email_exists(email):
        raise Exception('Email already registered')

    if (len(phone) != 11) | (not phone.isdigit()):
        raise Exception('Phone number must be 11 digits')

    if len(password) < 3:
        raise Exception('Password minimum characters length is 3')

    if len(password) > 12:
        raise Exception('Password maximum characters length is 12')

    if not any((char in ' !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~') for char in password):
        raise Exception("Password must contains a special character")

    if password != password2:
        raise Exception("Passwords don't match")

    _db.cursor.execute("""
        INSERT INTO USER
        (IS_ADMIN, PICTURE, NAME, EMAIL, PHONE, PASSWORD, PERMISSIONS)
        VALUES
        (?, ?, ?, ?, ?, ?, ?)
    """, (1 if is_first_time() else 0, pic, name, email, phone, password, "T,P,C"))
    _db.cursor.commit()


def login(email, password):
    result = _db.cursor.execute(f'SELECT * FROM USER WHERE EMAIL = ? AND PASSWORD = ?', (email, password)).fetchone()
    if result is None:
        raise Exception('Email or password is not correct')
    else:
        global user
        user = result


def logout():
    global user
    user = None
