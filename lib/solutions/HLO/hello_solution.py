
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name):
        if isinstance(friend_name, str):
            return f"Hello world"
        else:
            raise ValueError("friend_name must be a string")



