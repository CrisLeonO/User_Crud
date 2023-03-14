from app.config.mysqlconnection import connectToMySQL


# definiendo el usuario, el data es un diccionario.
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # 1) READ OPERATIONS
    # Get All Users
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_squema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    # Get one User
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('users_squema').query_db(query, data)
        return cls(result[0])

    # CREATE OPERATIONS
    #  Create one User
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s, NOW()), NOW());"
        result = connectToMySQL('users_squema').query_db(query, data)
        return result

    # Delete one User
    @classmethod
    def destroy(cls, data_delete):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL("users_squema").query_db(query, data_delete)

    # Edit User
    @classmethod
    def update(cls, new_data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL("users_squema").query_db(query, new_data)
