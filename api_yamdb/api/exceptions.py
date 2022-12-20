class ApiError(Exception):
    """базовый класс для всех исключений."""
    pass


class UserValueError(ApiError):
    """Имя пользователя не существет в базе."""
    pass
