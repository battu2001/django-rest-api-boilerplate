import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(
        email="test@example.com",
        password="testpass123",
        first_name="Jane",
        last_name="Doe"
    )
    assert user.email == "test@example.com"
    assert user.check_password("testpass123")
    assert user.is_active is True
    assert user.is_staff is False

@pytest.mark.django_db
def test_full_name_property():
    user = User.objects.create_user(
        email="jane@example.com",
        password="testpass123",
        first_name="Jane",
        last_name="Doe"
    )
    assert user.full_name == "Jane Doe"

@pytest.mark.django_db
def test_create_superuser():
    user = User.objects.create_superuser(
        email="admin@example.com",
        password="adminpass123"
    )
    assert user.is_staff is True
    assert user.is_superuser is True
