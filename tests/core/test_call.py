"""
    Unit tests for Call
"""

import unittest

from e621apy import PostQuery, Call, Post

class CallTestCase(unittest.TestCase):

    def test_defineQuery(self):
        """
            Test if call type is set correctly
        """
        expected = 'post'
        c = Call(PostQuery())

        self.assertEqual(c.type, expected)

    def test_buildUrlReturnsCorrectPostUrl(self):
        """
            Test if buil_url builds the correct url
        """
        expected = 'https://e621.net/post/index.json'
        c = Call(PostQuery())

        self.assertEqual(c.build_url(), expected)

    def test_getReturnsData(self):
        """
            Test if get call returns data
        """
        call = Call(PostQuery())
        content = call.fetch()

        self.assertTrue(len(content) > 0)

    def test_getReturnsPosts(self):
        """
            Test if get returns appropriate data
        """
        call = Call(PostQuery())
        data = call.get()

        for post in data:
            self.assertTrue(isinstance(post, Post))

    def test_getPostsReturnsPosts(self):
        """
            Test if get_posts returns appropriate data
        """
        call = Call(PostQuery())

        for post in call.get():
            self.assertTrue(isinstance(post, Post))

