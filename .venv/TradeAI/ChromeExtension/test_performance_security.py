import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_api_key_security(client):
    # This test should check the environment configuration to ensure API keys are not hard-coded
    # For demonstration, we assume an environment check function `check_env_keys`
    assert check_env_keys() == True, "API keys are exposed"

def test_sql_injection(client):
    # Test SQL injection vulnerability at relevant endpoints
    response = client.post('/trade', data={"query": "1; DROP TABLE users;"})
    assert response.status_code == 400, "SQL Injection vulnerability detected"

def test_xss(client):
    # Test for XSS vulnerabilities
    xss_attack_script = "<script>alert('XSS')</script>"
    response = client.post('/trade', data={"query": xss_attack_script})
    assert "<script>" not in response.data.decode(), "XSS vulnerability detected"

def test_csrf(client):
    # Test for CSRF vulnerabilities
    # Assuming the app uses CSRF protection, we need to simulate a request without CSRF token
    response = client.post('/trade', data={"query": "Buy stock"}, headers={"X-CSRFToken": "invalid_token"})
    assert response.status_code == 403, "CSRF vulnerability not properly handled"