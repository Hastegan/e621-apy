"""
Contains the Pool class
"""

__all__ = [
    'Pool',
]

class Pool(object):
    """
    Represents a pool
    """

    def __init__(self):
        """
        Initiate properties
        """
        self.identifier = 0
        self.name = ''
        self.created_at = ''
        self.updated_at = ''
        self.user_id = 0
        self.is_locked = False
        self.post_count = 0
        self.description = ''

    def __str__(self):
        """
        String representation of the object
        """
        return 'Pool<{}>'.format(self.identifier)
