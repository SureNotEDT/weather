from dao.base import BaseDao
from users.user_model import Users


class UserDao(BaseDao):
    model = Users
