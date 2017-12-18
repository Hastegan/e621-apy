"""
Contains the ForumPost class
"""

__all__ = [
    'ForumPost',
]

class ForumPost(object):
    """
    Represents a forum post
    """

    def __init__(self):
        """
        Initiate properties
        """
        self.identifier = 0
        self.parent_id = None
        self.creator = ''
        self.creator_id = 0
        self.title = ''
        self.body = ''

    def __str__(self):
        """
        String representation of the object
        """
        return 'ForumPost<{}>'.format(self.identifier)
