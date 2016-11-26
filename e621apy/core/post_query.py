"""
Contains the PostQuery class
"""

from e621apy import helpers as tools, Query

__all__ = [
    'PostQuery',
]

class PostQuery(Query):
    """
    Query designed to match Posts data
    """

    RATING_SAFE = 'safe'
    RATING_QUESTIONABLE = 'questionable'
    RATING_EXPLICIT = 'explicit'
    RATING_ALL = 'all'

    def __init__(self, limit=75, tags=None, rating=RATING_SAFE):
        """
        Initiate properties and add the rating tag
        """
        self._limit = limit
        self._tags = tags

        if self._tags is None:
            self._tags = []
        self._set_rating(rating)

    def _add_tags(self, *tags):
        """
        Add some tags to the object's list
        """
        for tag in tags:
            self._tags = tools.add_tag(self._tags, tag)

    def _set_sort(self, key, asc=True):
        """
        Add a sorting tag
        """
        sort = '_asc'
        if not asc:
            sort = '_desc'

        self._add_tags('order:%s%s' % (key, sort))

    def _set_id(self, identifier):
        """
        Add an id tag
        """
        self._add_tags('id:%i' % identifier)

    def _set_rating(self, rating):
        """
        Add the rating tag
        """
        self._add_tags('rating:%s' % rating)

    def rating(self, rating):
        """
        Set the rating
        """
        self._set_rating(rating)
        return self

    def tags(self, *tags):
        """
        Add new tags
        """
        self._add_tags(*tags)
        return self

    def species(self, *species):
        """
        Add species tags

        There is no difference between species tags and general tags in
        searches
        """
        self._add_tags(*species)
        return self

    def sort(self, key, asc=False):
        """
        Add a sorting tag
        """
        self._set_sort(key, asc)
        return self

    def get(self, identifier):
        """
        Override all tags and rating to search only with an id
        """
        self._tags = []
        self.rating(PostQuery.RATING_ALL)

        self._set_id(identifier)

        return self

    def __str__(self):
        """
        String representation with tags
        """
        return 'PostQuery: %s' % self._tags
