from seasons import print_minutes
from datetime import date


def test_default_date_print_minutes():
    assert print_minutes("1970-01-01",
                         ) == "Fifteen million, seven hundred seventy-eight thousand eighty minutes"
    assert print_minutes("1999-01-01",
                         ) == "Five hundred twenty-five thousand, six hundred minutes"

    assert print_minutes("1998-06-20",
                         ) == "Eight hundred six thousand, four hundred minutes"


def test_today_date_print_minutes():
    assert print_minutes(
        "2022-04-21") == "Five hundred twenty-five thousand, six hundred minutes"
    assert print_minutes(
        "2023-4-01") == "Twenty-eight thousand, eight hundred minutes"
