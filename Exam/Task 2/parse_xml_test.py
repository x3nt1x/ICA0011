import parse_xml as pxml


def test_parsing():
    assert pxml.parse_xml() == "Successful"
