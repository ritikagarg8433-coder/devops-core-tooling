
#user Dasboard Module

def get_user_dashboard(username):
    user_dashboard = {
          "username": username,
          "status": "Active",
          "role":  "Developer",
          "department": "DevOps"
    }

    return user_dashboard


if __name__ == "__main__":
     user = get_user_dashboard("Ritika")
     print("User Dashboard")
     print("--------------")
     print(user)
