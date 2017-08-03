"""
Contains the PostQuery class
"""

from e621apy import Query, helpers

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

    def __init__(self, limit=75, page=1, tags=None, rating=RATING_SAFE):
        """
        Initiate properties and add the rating tag
        """

        Query.__init__(self)

        self._limit = limit
        self._page = page
        self._tags = tags

        if self._tags is None:
            self._tags = []
        self.rating(rating)

    def enable_unique_mode(self):
        """
        Set the query in unique mode, prepared to get only one result
        """
        self.unique_mode = True

        self._tags = []
        self.page = 1
        self._limit = 1

    def _add_tags(self, *tags):
        """
        Add some tags to the object's list
        """
        for tag in tags:
            self._tags = helpers.add_tag(self._tags, tag)

    def _set_sort(self, key, asc=True):
        """
        Add a sorting tag
        """
        sort = '_asc'
        if not asc:
            sort = '_desc'

        self._add_tags('order:%s%s' % (key, sort))

    def _set_rating(self, rating, remove):
        """
        Add the rating tag
        """
        if remove:
            self._add_tags('-rating:%s' % rating)
        else:
            self._add_tags('rating:%s' % rating)

    def rating(self, rating, remove=False):
        """
        Set the rating
        """
        self._set_rating(rating, remove)
        return self

    def tags(self, *tags):
        """
        Add new tags
        """
        self._add_tags(*tags)
        return self

    def pool(self, pool):
        """
        Add the pool tag
        """
        self._add_tags("pool:%s" % pool)
        return self

    def set(self, set):
        """
        Add the set tag
        """
        self._add_tags("set:%s" % set)
        return self

    def has_source(self, has_source=True):
        """
        Set if posts must have a source or not
        """
        self._add_tags("hassource:%s" % has_source)
        return self

    def has_description(self, has_description=True):
        """
        Set if posts must have a description or not
        """
        self._add_tags("hasdescription:%s" % has_description)
        return self

    def is_in_pool(self, is_in_pool=True):
        """
        Set if posts must be in a poll or not
        """
        self._add_tags("inpool:%s" % is_in_pool)
        return self

    def sort(self, key, asc=True):
        """
        Add a sorting tag
        """
        self._set_sort(key, asc)
        return self

    def limit(self, limit):
        """
        Add the limit
        """
        self._limit = limit

        return self

    def page(self, page):
        """
        Add the page
        """
        self._page = page

        return self

    def get(self, identifier):
        """
        Override all tags and ratings to search only with an id
        """
        self.enable_unique_mode()
        self._add_tags("id:%s" % identifier)

        return self

    def md5(self, md5):
        """
        Override all tags and ratings to search only with a md5
        """
        self.enable_unique_mode()

        self._add_tags("md5:%s" % md5)

        return self

    def next_page(self):
        """
        Set the postQuery to get the next page
        """
        self._page += 1

        return self

    def get_page(self):
        return self._page

    def get_limit(self):
        return self._limit

    def get_tags(self):
        return self._tags

    def get_url_params(self):
        """
        Return a dictionary of the url parameters
        """
        params = {
            'limit': self._limit,
            'page': self._page,
            'tags': '',
        }

        for tag in self._tags:
            params['tags'] = '{} {}'.format(tag, params['tags'])
        params['tags'] = params['tags'].strip()

        return params

    def __str__(self):
        """
        String representation with tags
        """
        return "PostQuery: {}, page {}, limit {}".format(self._tags, self._page, self._limit)
