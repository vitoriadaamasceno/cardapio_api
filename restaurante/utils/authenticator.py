from passlib.context import CryptContext

class Authenticator:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, password_login: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(password_login, hashed_password)