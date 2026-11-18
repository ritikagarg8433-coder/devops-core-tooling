
# User Dashboard Module

def get_user_dashboard(username):
    dashboard = {
        "username": username,
        "status": "Inactive",
        "role": "Developer",
        "department": "DevOps"
    }

    return dashboard


if __name__ == "__main__":
    user = get_user_dashboard("Ritika")
    print("User Dashboard")
    print("--------------")
    print(user)
