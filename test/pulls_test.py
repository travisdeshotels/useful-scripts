import unittest
from unittest import mock
import pulls

mock_data = [
    {
        "draft": False,
        "html_url": "https://github.com/1610oct24java/AssociateEvaluationSystem/pull/132",
        "title": "Selenium Webdriver Automation Testing"
    },
    {
        "draft": True,
        "html_url": "https://github.com/1610oct24java/AssociateEvaluationSystem/pull/113",
        "title": "Second dev testing johnj"
    }
]


class MyTestCase(unittest.TestCase):
    @mock.patch('pulls.get_data', autospec=True)
    def test_something(self, my_mock):
        my_mock.return_value = mock_data
        pr = pulls.PullRequests()
        drafts, open_pulls = pr.get_pulls()
        self.assertEqual(drafts[0]['title'], mock_data[1]['title'])
        self.assertEqual(open_pulls[0]['title'], mock_data[0]['title'])


if __name__ == '__main__':
    unittest.main()
