def add_at_symbol_to_username(username):
    """ takes username as an argument, adds the @ symbol to
    the username, and returns the updated username.
        Example: if the username is user123
             the function should return user123@email.com
     """
    if isinstance(username, str) and username != "":
        return f"{username}@"

