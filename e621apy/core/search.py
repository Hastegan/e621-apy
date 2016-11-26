"""
Contains the  Search class
"""

__all__ = [
    'Search',
]

class Search(object):
    """
    Performs the actual transaction with the e621 API
    """

    def __init__(self, query):
        """
        Initiate properties
        """
        self._query = query
        self._count = 0

    def _execute_query(self):
        """
        Perform API call and treat the response
        """
        pass
