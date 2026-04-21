class User:
    def __init__(self, id, name, role):
        self.id = id
        self.name = name
        self.role = role
        self.permissions = []

class Role:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.permissions = []

class Permission:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class UserPermissionSystem:
    def __init__(self):
        self.users = []
        self.roles = []
        self.permissions = []

    def add_user(self, id, name, role_id):
        user = User(id, name, role_id)
        self.users.append(user)
        return user

    def add_role(self, id, name):
        role = Role(id, name)
        self.roles.append(role)
        return role

    def add_permission(self, id, name):
        permission = Permission(id, name)
        self.permissions.append(permission)
        return permission

    def assign_permission_to_role(self, role_id, permission_id):
        for role in self.roles:
            if role.id == role_id:
                for permission in self.permissions:
                    if permission.id == permission_id:
                        role.permissions.append(permission)
                        return
                print("Permission not found")
                return
        print("Role not found")

    def assign_role_to_user(self, user_id, role_id):
        for user in self.users:
            if user.id == user_id:
                for role in self.roles:
                    if role.id == role_id:
                        user.role = role
                        return
                print("Role not found")
                return
        print("User not found")

    def check_permission(self, user_id, permission_name):
        for user in self.users:
            if user.id == user_id:
                for permission in user.role.permissions:
                    if permission.name == permission_name:
                        return True
                return False
        print("User not found")
        return False

system = UserPermissionSystem()

# Userlar yaratish
user1 = system.add_user(1, "John", 1)
user2 = system.add_user(2, "Alice", 2)

# Rolalar yaratish
role1 = system.add_role(1, "Admin")
role2 = system.add_role(2, "Moderator")

# Ruxsatlar yaratish
permission1 = system.add_permission(1, "Create Post")
permission2 = system.add_permission(2, "Delete Post")

# Roli userga berish
system.assign_role_to_user(1, 1)
system.assign_role_to_user(2, 2)

# Ruxsatni rolgacha berish
system.assign_permission_to_role(1, 1)
system.assign_permission_to_role(2, 2)

# Ruxsatni tekshirish
print(system.check_permission(1, "Create Post"))  # True
print(system.check_permission(1, "Delete Post"))  # False
print(system.check_permission(2, "Create Post"))  # False
print(system.check_permission(2, "Delete Post"))  # True
