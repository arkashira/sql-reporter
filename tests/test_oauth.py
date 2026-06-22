import pytest
from src.oauth import OAuthCredentials, OAuthManager

def test_add_credentials():
    manager = OAuthManager()
    credentials = OAuthCredentials("client_id", "client_secret", "access_token")
    manager.add_credentials(credentials)
    assert manager.get_credentials("client_id") == credentials

def test_authenticate():
    manager = OAuthManager()
    credentials = OAuthCredentials("client_id", "client_secret", "access_token")
    manager.add_credentials(credentials)
    assert manager.authenticate("client_id", "client_secret") == "access_token"
