import pytest
from src.lab3.Num_2.survey_groups import Respondent, AgeGroup, AgeGroupManager
from io import StringIO
import sys

@pytest.fixture
def sample_respondents():
    return [
        Respondent(25, "John Doe"),
        Respondent(30, "Jane Smith"),
        Respondent(35, "Bob Johnson"),
        Respondent(40, "Alice Brown"),
        Respondent(15, "Charlie Davis"),
        Respondent(60, "Eve Wilson")
    ]

def test_respondent():
    r = Respondent(25, "John Doe")
    assert str(r) == "John Doe (25)"
    assert r.age == 25
    assert r.full_name == "John Doe"

def test_age_group():
    group = AgeGroup(20, 30)
    assert group.is_in_group(20) is True
    assert group.is_in_group(25) is True
    assert group.is_in_group(30) is True
    assert group.is_in_group(15) is False
    assert group.is_in_group(35) is False
    
    assert group.format_label() == "20-30"
    
    group_plus = AgeGroup(60, 10**9)
    assert group_plus.format_label() == "60+"


def test_age_group_sorting():
    group = AgeGroup(20, 30)
    group.add(Respondent(25, "Bob"))
    group.add(Respondent(25, "Alice"))
    group.add(Respondent(30, "Charlie"))
    
    sorted_resp = group.get_sorted_respondents()
    assert sorted_resp[0].age == 30
    assert sorted_resp[1].full_name == "Alice"
    assert sorted_resp[2].full_name == "Bob"
