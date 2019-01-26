import unittest
from presenter.xmler import *
from model.globalsvar import *


class Test(unittest.TestCase):


    def setUp(self):
        self.parser = xmler() 
        self.parser.loadXML(START_FILE) 


    def tearDown(self):
        pass


    def test_formatedstringlist_from_hubsetings_UPTIME_UNIT(self):
        test_result = self.parser.formatedstringlist_from_hubsetings()
        self.assertEqual(
                test_result[8], 
                "UPTIME = 39245 sec",
                'Test error test_result is not equal "UPTIME = 39245"'
        )


    def test_formatedstringlist_from_hubsetings_MBDEVICEID_MBUSHEX(self):
        test_result = self.parser.formatedstringlist_from_hubsetings()
        self.assertEqual(
                test_result[4], 
                "       |_____MBDEVICEID = 1430388992 (MBUSHEX)",
                'Test error test_result is not equal "MBDEVICEID = 1430388992"'
        )


    def test_formatedstringlist_from_hubsetings_FVERS_HEX(self):
        test_result = self.parser.formatedstringlist_from_hubsetings()
        self.assertEqual(test_result[1], "FVERS = 49",
                'Test error test_result is not equal "FVERS = 49"' )


    def test_formatedstringlist_from_hubsetings_HVERS(self):
        test_result = self.parser.formatedstringlist_from_hubsetings()
        self.assertEqual(test_result[0], "HVERS = 1",
                'Test error test_result is not equal "HVERS = 1"' )


    def test_formatedstringlist_from_telemetry_T0000(self):
        test_result = self.parser.formatedstringlist_from_telemetry()
        self.assertEqual(test_result[0], "T0000",
                'Test error test_result is not equal "T0000"' )


    def test_formatedstringlist_from_telemetry_ALMSTAT(self):
        test_result = self.parser.formatedstringlist_from_telemetry()
        self.assertEqual(test_result[2], "ALMSTAT = 00",
                'Test error test_result is not equal "ALMSTAT = 00"' )


    def test_formatedstringlist_from_telemetry_MBTIME(self):
        test_result = self.parser.formatedstringlist_from_telemetry()
        self.assertEqual(test_result[1], "MBTIME = 1970-02-12 00:48:07",
                'Test error test_result is not equal "MBTIME = 1970-02-12 00:48:06"' )


    def test_formatedstringlist_from_telemetry(self):
        self.parser.formatedstringlist_from_telemetry()


    def test_printxml(self):
        self.parser.testprintxml()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
