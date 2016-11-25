import e621apy.helpers as tools

__all__ = [
    'SearchPost',
]

class SearchPost(object):

    RATING_SAFE = 'rating:safe'
    RATING_QUESTIONABLE = 'rating:questionable'
    RATING_EXPLICIT = 'rating:explicit'
    RATING_ALL = 'rating:all'

    def __init__(self, limit=75, tags=[], rating=RATING_SAFE):
        self._limit = limit
        self._matches = 0
        self._tags = tags
        self._add_tags(rating)

    def _add_tags(self, *tags):
        for tag in tags:
            self._tags = tools._add_tag(self._tags, tag)

    def _set_sort(self, key, asc):
        sort = '_asc'
        if not asc:
            sort = '_desc'

        self._add_tags('order:%s%s' % (key, sort))

    def _set_id(self, id):
        self._add_tags('id:%i' % id)

    def rating(self, rating):
        self._add_tags(rating)
        return self

    def tags(self, *tags):
        self._add_tags(tags)
        return self

    def species(self, *species):
        self._add_tags(*species)
        return self

    def sort(self, key, asc=False):
        self._set_sort(key, asc)
        return self

    def id(self, id):
        self._tags = []
        self.rating(SearchPost.RATING_ALL)

        self._set_id(id)

        return self

    def __str__(self):
        return "Search: tags: %s; matches: %i;" % (self._tags, self._matches)
