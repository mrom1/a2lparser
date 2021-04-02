from tests.testhandler import Testhandler

class TestEncoding(Testhandler):
    def test_encoding_utf8(self):
        val = ""
        s = "/begin ANNOTATION\nANNOTATION_TEXT " + '"' + val + '"' + "\n/end ANNOTATION"


    def test_encoding_latin1(self):
        pass

    def test_encoding_iso_8859_1(self):
        pass
