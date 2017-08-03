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
        self._content = Call(query).get()
        self._count = 0

    def first(self):
        if len(self._content):
            return self._content[0]
        return None

    def get_all(self):
        return self._content

    def __iter__(self):
        """
        Iterator
        """
        return self

    def __next__(self):
        if self._count < len(self._content):
            self._count += 1
            return self._content[self._count - 1]
        raise StopIteration
