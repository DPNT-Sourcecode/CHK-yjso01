
class HelloSolution:
    def hello(self, friend_name):
        print(f"[DEBUG] Responding to: {friend_name}")
        if not isinstance(friend_name, str):
            raise TypeError("friend_name must be a string")
        if not friend_name:
            raise ValueError("friend_name is required")
        return f"Hello, {friend_name}!"






