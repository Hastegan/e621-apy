"""
Contains the Comment class
"""

__all__ = [
    'Comment',
]

class Comment(object):
    """
    Represents a comment
    """

    def __init__(self):
        """
        Initiate properties
        """
        self.identifier = 0
        self.created_at = ''
        self.post_id = 0
        self.creator = ''
        self.creator_id = 0
        self.body = ''
        self.score = 0
