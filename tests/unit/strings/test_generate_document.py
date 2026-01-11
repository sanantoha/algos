from strings.generate_document import generate_document, generate_document1


def test_generate_document():
    assert generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!")


def test_generate_document1():
    assert generate_document1("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!")