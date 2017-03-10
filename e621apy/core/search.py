"""
Contains the  Search class
"""

__all__ = [
    'Search',
]

from e621apy import Call

class Search(object):
    """
    Performs the actual transaction with the e621 API
    """

    def __init__(self, query):
        """
        Initiate properties
        """
        self._query = query
        self._posts = Call(query).get_posts()
        self._count = 0

        self.counter = 0

    def __iter__(self):
        """
        Iterator
        """
        return self

    def __next__(self):
        if self._count < len(self._posts):
            self._count += 1
            return self._posts[self._count - 1]
        raise StopIteration
