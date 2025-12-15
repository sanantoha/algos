from arrays.apartment_hunting import apartmentHunting


def test_apartment_hunting():
    blocks = [
        {"gym": False, "school": True, "store": False},
        {"gym": True, "school": False, "store": False},
        {"gym": True, "school": True, "store": False},
        {"gym": False, "school": True, "store": False},
        {"gym": False, "school": True, "store": True},
    ]
    reqs = ["gym", "school", "store"]
    assert apartmentHunting(blocks, reqs) == 3