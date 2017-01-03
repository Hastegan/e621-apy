"""
Contains the Post class
"""

__all__ = [
    'Post',
]

class Post(object):
    """
    Represents a post
    """

    def __init__(self):
        """
        Initiate properties
        """
        self.identifier = 0
        self.tags = ''
        self.description = ''
        self.created_at = ''
        self.creator_id = ''
        self.author = ''
        self.change = 0
        self.source = ''
        self.score = 0
        self.fav_count = 0
        self.md5 = ''
        self.file_size = 0
        self.file_url = ''
        self.file_ext = ''
        self.preview_url = ''
        self.preview_width = 0
        self.preview_height = 0
        self.sample_url = ''
        self.sample_width = 0
        self.sample_height = 0
        self.rating = ''
        self.status = ''
        self.width = 0
        self.height = 0
        self.has_comments = False
        self.has_notes = False
        self.has_children = False
        self.children = ''
        self.parent_id = ''
        self.artist = []
        self.sources = []
        self.delreason = ''

    def __str__(self):
        """
        String reprensentation of a Post
        """
        return 'Post<{}>'.format(self.identifier)
