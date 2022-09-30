import unittest
from unittest import mock
import pulls

mock_data = [
    {
        "draft": False,
        "html_url": "https://github.com/1610oct24java/AssociateEvaluationSystem/pull/132",
        "title": "Selenium Webdriver Automation Testing",
        "head": {
            "label": "1610oct24java:develop",
            "ref": "develop",
            "sha": "86434db09e2a86d8a5e6b62738db9f06481349ac"
        },
        "base": {
            "label": "1610oct24java:main",
            "ref": "main",
            "sha": "fdbeeca0e31b751fa6da293c6635400f148d52f3"
        }
    },
    {
        "draft": True,
        "html_url": "https://github.com/1610oct24java/AssociateEvaluationSystem/pull/113",
        "title": "Second dev testing johnj",
        "head": {
            "label": "1610oct24java:develop",
            "ref": "develop",
            "sha": "86434db09e2a86d8a5e6b62738db9f06481349ac"
        },
        "base": {
            "label": "1610oct24java:main",
            "ref": "master",
            "sha": "fdbeeca0e31b751fa6da293c6635400f148d52f3"
        }
    },
    {
        "draft": True,
        "html_url": "https://github.com/1610oct24java/AssociateEvaluationSystem/pull/114",
        "title": "my improper base",
        "head": {
            "label": "1610oct24java:second-dev-testing-johnj",
            "ref": "second-dev-testing-johnj",
            "sha": "86434db09e2a86d8a5e6b62738db9f06481349ac"
        },
        "base": {
            "label": "1610oct24java:main",
            "ref": "main",
            "sha": "fdbeeca0e31b751fa6da293c6635400f148d52f3"
        }
    }
]


class MyTestCase(unittest.TestCase):
    @mock.patch('pulls.get_data', autospec=True)
    def test_something(self, my_mock):
        my_mock.return_value = mock_data
        pr = pulls.PullRequests()
        bad_base, drafts, open_pulls = pr.get_pulls()
        self.assertEqual(bad_base[0]['title'], mock_data[2]['title'])
        self.assertEqual(drafts[0]['title'], mock_data[1]['title'])
        self.assertEqual(open_pulls[0]['title'], mock_data[0]['title'])


if __name__ == '__main__':
    unittest.main()
