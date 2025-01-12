from main import generate_band_name


def test_band_name():
    assert generate_band_name("city_name", "pet_name") == "Your band name could be city_name pet_name"
    