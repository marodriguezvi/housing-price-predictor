from app.schemas.predict import HouseInput


def test_house_input_valid_data():
    """Verify that HouseInput accepts valid data."""
    valid_input = {
        "CRIM": 0.00632,
        "ZN": 18.0,
        "INDUS": 2.31,
        "CHAS": 0,
        "NOX": 0.538,
        "RM": 6.575,
        "AGE": 65.2,
        "DIS": 4.09,
        "RAD": 1,
        "TAX": 296.0,
        "PTRATIO": 15.3,
        "B": 396.9,
        "LSTAT": 4.98,
    }

    obj = HouseInput(**valid_input)
    assert obj.CRIM == 0.00632


def test_house_input_invalid_negative_parameters():
    """Verify that HouseInput rejects invalid data."""
    invalid = {
        "CRIM": -0.1,
        "ZN": 0,
        "INDUS": 0,
        "CHAS": 0,
        "NOX": 0.1,
        "RM": 1,
        "AGE": 0,
        "DIS": 1,
        "RAD": 1,
        "TAX": 1,
        "PTRATIO": 1,
        "B": 1,
        "LSTAT": 0,
    }
    try:
        HouseInput(**invalid)
        assert False, "Validation should have failed for negative CRIM"
    except Exception as e:
        assert "CRIM" in str(e)
