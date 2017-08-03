"""
    Unit tests for Call
"""

import unittest

from e621apy import PostQuery, Call, Post

class CallTestCase(unittest.TestCase):

    def test_type(self):
        """
            Test if call type is set correctly
        """
        expected = 'post'

        q = PostQuery()
        call = Call(q)

        self.assertEqual(call.type, expected)

    def test_getReturnsData(self):
        """
            Test if get call returns data
        """
        q = PostQuery()
        call = Call(q)
        call.fetch()

        self.assertTrue(len(call.content) > 0)

    def test_getReturnsPosts(self):
        """
            Test if get returns appropriate data
        """
        q = PostQuery()
        call = Call(q)
        data = call.get()

        for post in data:
            self.assertTrue(isinstance(post, Post))

    def test_getPostsReturnsPosts(self):
        """
            Test if get_posts returns appropriate data
        """
        q = PostQuery()
        call = Call(q)

        for post in call.get_posts():
            self.assertTrue(isinstance(post, Post))

