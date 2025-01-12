import pytest

from main import generate_band_name


def test_band_name():
    assert generate_band_name("city_name", "pet_name") == "city_name pet_name"
    