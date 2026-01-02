from recursion.phone_number_mnemonic import phoneNumberMnemonics


def test_phone_number_mnemonic():
    phoneNumber = "1905"
    expected = ["1w0j", "1w0k", "1w0l", "1x0j", "1x0k", "1x0l", "1y0j", "1y0k", "1y0l", "1z0j", "1z0k", "1z0l"]
    actual = phoneNumberMnemonics(phoneNumber)
    print(actual)
    assert actual == expected