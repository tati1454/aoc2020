import part01

def test_searchRow():
    assert part01.searchRow("FBFBBFF") == 44

def test_searchColumn():
    assert part01.searchColumn("RLR") == 5