# Simulate blog posts to practice classes and objects
# Follow the instructions. Start coding here. 
class Blog:
    def __init__(self, message):
        self.message = message
        self.likes = 0

    def post(self):
        print(self.message)


# test code
b1 = Blog("I love Python.")
b1.post()
print(b1.likes)