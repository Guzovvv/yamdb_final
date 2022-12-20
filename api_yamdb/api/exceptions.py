class ApiError(Exception):
    """базовый класс для всех исключений."""
    pass


class UserValueException(ApiError):
    """Имя пользователя не существет в базе."""
    pass
