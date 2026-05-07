import pytest
from core.models import Student, Teacher
from core.manager import LMSManager

@pytest.fixture
def lms():
    return LMSManager()

def test_student_role():
    s = Student(1, "Ali", "ali@test.com")
    assert s.get_role() == "Student"

def test_add_user_success(lms):
    s = Student(1, "Ali", "ali@test.com")
    lms.register_user(s)
    assert lms.get_user_count() == 1

def test_duplicate_id_error(lms):
    s1 = Student(1, "Ali", "ali@test.com")
    s2 = Student(1, "Sara", "sara@test.com")
    lms.register_user(s1)
    with pytest.raises(ValueError): # Testing Error Handling
        lms.register_user(s2)
