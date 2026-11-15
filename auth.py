# Mock Authentication Module

def authenticate(username, password):

    if username == "admin" and password == "admin123":
        return "Authencation successful"

if __name__ == "__main__":
     print(authenticate("admin","admin123"))
