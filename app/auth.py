def is_admin(user) -> bool:
    return user is not None and user.role == "admin"
