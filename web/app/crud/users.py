from app.auth import get_password_hash
from app.models import User


class UsersCRUD:
    @staticmethod
    async def create_user(data):
        password = get_password_hash(data.pop('password'))
        return await User.create(password=password, **data)


users_crud = UsersCRUD()
