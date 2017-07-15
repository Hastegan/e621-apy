"""
    Unit tests for PostQuery
"""

import unittest

from e621apy import PostQuery

class PostQueryTestCase(unittest.TestCase):

    def test_default_query(self):
        """
            Test if the default query is correctly set
        """
        expected_query = {
            'tags': 'rating:safe',
            'limit': 75,
            'page': 1,
        }

        q = PostQuery()

        self.assertEqual(expected_query, q.get_url_params())

    def test_string_representation(self):
        """
            Test if the string representation is correct
        """
        expected_string = "PostQuery: ['rating:safe'], page 1, limit 75"

        q = PostQuery()

        self.assertEqual(expected_string, q.__str__())

    def test_tag(self):
        """
            Test if adding tags works as expected
        """
        expected_tags = [
            "rating:safe",
            "equine",
            "pony",
        ]

        q = PostQuery().tags("equine", "pony")

        self.assertEqual(q.get_tags(), expected_tags)

    def test_rating(self):
        """
            Test if adding a rating works as expected
        """
        expected_tag = ["rating:explicit"]

        q = PostQuery().rating(PostQuery.RATING_EXPLICIT)

        self.assertEqual(q.get_tags(), expected_tag)


    def test_rating_remove(self):
        """
            Test if ignoring a rating works as expected
        """
        expected_tag = ["-rating:explicit"]

        q = PostQuery().rating(PostQuery.RATING_EXPLICIT, True)

        self.assertEqual(q.get_tags(), expected_tag)

    def test_enable_unique_mode(self):
        """
            Test if enabling the unique mode sets the correct values
        """
        expected_query = {
            'tags': '',
            'limit': 1,
            'page': 1,
        }

        q = PostQuery().tags('dummy tag')
        q.enable_unique_mode()

        self.assertTrue(q.unique_mode)
        self.assertEqual(expected_query, q.get_url_params())

    def test_get(self):
        """
            Test if get sets the correct values
        """
        identifier = "42"
        q = PostQuery().get(identifier)

        self.assertTrue(q.unique_mode)
        self.assertIn('id:%s' % identifier, q.get_tags())

    def test_md5(self):
        """
            test if md5 sets the correct values
        """
        md5 = "dummyMD5"
        q = PostQuery().md5(md5)

        self.assertTrue(q.unique_mode)
        self.assertIn('md5:%s' % md5, q.get_tags())

    def test_pool(self):
        """
            Test if pool sets the correct tag
        """
        pool = "dummy"
        q = PostQuery().pool(pool)

        self.assertIn('pool:%s' % pool, q.get_tags())

    def test_page_limit(self):
        """
            Test if page and limit are setting the page correctly
        """
        page = 20
        limit = 25

        q = PostQuery().limit(limit).page(page)

        self.assertEqual(q.get_page(), page)
        self.assertEqual(q.get_limit(), limit)

    def test_asc_sort(self):
        """
            Test if sort is setting the correct tag
        """
        sort = "score"
        exected = "score_asc"

        q = PostQuery().sort(sort)

        self.assertIn('order:%s' % exected, q.get_tags())

    def test_desc_sort(self):
        """
            Test if sort is setting the correct tag
        """
        sort = "score"
        exected = "score_desc"

        q = PostQuery().sort(sort, False)

        self.assertIn('order:%s' % exected, q.get_tags())

    def test_filters_true(self):
        """
            Test if the filters are setting the correct tags
        """
        expected_tags = [
            "inpool:True",
            "hasdescription:True",
            "hassource:True",
        ]

        q = PostQuery().is_in_pool().has_description().has_source()
        tags = q.get_tags()

        for tag in expected_tags:
            self.assertIn(tag, tags)

    def test_filters_false(self):
        """
            Test if the filters are setting the correct tags
        """
        expected_tags = [
            "inpool:False",
            "hasdescription:False",
            "hassource:False",
        ]

        q = PostQuery().is_in_pool(False).has_description(False).has_source(False)
        tags = q.get_tags()

        for tag in expected_tags:
            self.assertIn(tag, tags)

if __name__ == '__main__':
    unittest.main()
