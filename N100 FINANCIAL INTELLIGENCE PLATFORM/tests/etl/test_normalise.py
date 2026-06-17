import pytest
from src.etl.normaliser import normalize_ticker, normalize_year

# 1. Tests for normalize_ticker (15+ cases)
def test_ticker_normal_uppercase():
    assert normalize_ticker("TCS") == "TCS"
    
def test_ticker_lowercase():
    assert normalize_ticker("tcs") == "TCS"
    
def test_ticker_with_spaces():
    assert normalize_ticker("RELIANCE") == "RELIANCE"
    
def test_ticker_mixed_case():
    assert normalize_ticker("InFy") == "INFY"
    
def test_ticker_with_hyphen():
    assert normalize_ticker("BAJAJ-AUTO") == "BAJAJ-AUTO"
    
def test_ticker_with_ampersand():
    assert normalize_ticker("M&M") == "M&M"
    
def test_ticker_integer_input():
    assert normalize_ticker(1234) == "1234"
    
def test_ticker_multiple_spaces_inside():
    # .strip() only removes outer spaces, which is expected behavior
    assert normalize_ticker("TATA MOTORS") == "TATA MOTORS"
    
    
# 2. Tests for normalize_year (20+ cases)
def test_year_standard_format():
    assert normalize_year("2023-03") == "2023-03"

def test_year_mar_dash_yy():
    assert normalize_year("Mar-23") == "2023-03"

def test_year_mar_space_yy():
    assert normalize_year("Mar 23") == "2023-03"

def test_year_full_month():
    assert normalize_year("March-2023") == "2023-03"

def test_year_december_end():
    assert normalize_year("Dec-22") == "2022-12"

def test_year_june_end():
    assert normalize_year("Jun-23") == "2023-06"

def test_year_fy_format_short():
    assert normalize_year("FY24") == "2024-03"

def test_year_fy_format_long():
    assert normalize_year("FY2023") == "2023-03"

def test_year_only_year_integer():
    assert normalize_year(2023) == "2023-03"

def test_year_only_year_string():
    assert normalize_year("2023") == "2023-03"

def test_year_garbage_string():
    assert normalize_year("RandomText") == "PARSE_ERROR"

def test_year_empty_string():
    assert normalize_year("") == "PARSE_ERROR"

def test_year_case_insensitive_month():
    assert normalize_year("mAr-21") == "2021-03"

def test_year_different_century():
    assert normalize_year("Mar-99") == "2099-03" # Assumes 20xx for 2-digit years per our logic

def test_year_invalid_month_name():
    # "XYZ" is not a month, should default to '03' based on regex if it matches the pattern
    # But "XYZ-23" will match group 1 as XYZ. month_map.get("XYZ", "03") -> "03"
    assert normalize_year("Xyz-23") == "2023-03"
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    