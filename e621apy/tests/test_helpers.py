"""
    Unit tests for the helpers functions
"""

import unittest

from e621apy import helpers as tools

class HelpersTestCase(unittest.TestCase):
    """
        Tests on the helpers functions
    """

    def test_clean_tag_spaces(self):
        """
            Test if spaces in a tag are correctly cleaned
        """

        dirty_tag = 'hi res'
        expected = 'hi_res'

        clean_tag = tools.clean_tag(dirty_tag)
        self.assertEqual(clean_tag, expected)

    def test_add_tag_simple_duplicate(self):
        """
            Test if adding a same new simple tag is not making duplicates
        """
        initial_tags = [
            'hi_res',
            'rating:safe',
        ]

        expected = list(initial_tags)

        result = tools.add_tag(initial_tags, 'hi_res')
        self.assertCountEqual(result, expected, 'Simple tag duplicate')

    def test_add_tag_complex_duplicate(self):
        """
            Test if adding a complex new tag is not making duplicates
        """
        initial_tags = [
            'hi_res',
            'rating:safe',
        ]

        expected = [
            'hi_res',
            'rating:questionable',
        ]

        result = tools.add_tag(initial_tags, 'rating:questionable')
        self.assertCountEqual(result, expected, 'Complex tag duplicate')

if __name__ == '__main__':
    unittest.main()
