from flask import Flask, jsonify

app = Flask(__name__)

class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    def has_permission(self, permission):
        return permission in self.permissions


class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def can(self, permission):
        return self.role.has_permission(permission)

# Definição de papéis
admin_role = Role("admin", ["read", "write", "delete"])
user_role = Role("user", ["read"])

# Cadastro de usuários
users = {
    "admin_user": User("admin_user", admin_role),
    "common_user": User("common_user", user_role)
}

@app.route("/permissoes/<username>/<permission>")
def check_permission(username, permission):
    user = users.get(username)
    if user and user.can(permission):
        return jsonify({"user": username, "permission": permission, "allowed": True})
    return jsonify({"user": username, "permission": permission, "allowed": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)