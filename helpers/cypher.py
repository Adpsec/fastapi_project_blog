from passlib.hash import pbkdf2_sha512

def cypherPassword(password):
    return pbkdf2_sha512.encrypt(password)