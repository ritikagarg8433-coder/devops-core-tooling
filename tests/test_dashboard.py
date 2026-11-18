

from dashboard import get_user_dashboard


def test_dashboard_status():
    user = get_user_dashboard("Ritika")
    assert user["status"] == "Active"
