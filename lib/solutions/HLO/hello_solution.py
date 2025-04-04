
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name):
        if not friend_name:
            raise ValueError("friend_name cannot be empty")
        else:
            return f"Hello {friend_name}"

        # raise NotImplementedError()


