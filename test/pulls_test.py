import unittest
from unittest import mock
import pulls

mock_data = [
    {
        "draft": False,
        "html_url": "https://github.com/1610oct24java/AssociateEvaluationSystem/pull/132",
        "title": "Selenium Webdriver Automation Testing"
    }
]


class MyTestCase(unittest.TestCase):
    @mock.patch('pulls.get_data', autospec=True)
    def test_something(self, request_mock):
        request_mock.return_value = mock_data
        x = pulls.get_pulls()
        self.assertEqual(x[0], mock_data[0]['title'])


if __name__ == '__main__':
    unittest.main()
