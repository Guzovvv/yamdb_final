class APIError(Exception):
    """базовый класс для всех исключений."""
    pass


class UserValueException(APIError):
    """Имя пользователя не существет в базе."""
    pass
