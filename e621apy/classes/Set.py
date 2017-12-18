"""
Contains the Set class
"""

__all__ = [
    'Set',
]

class Set(object):
    """
    Represent a set
    """

    def __init__(self):
        """
        Initiate properties
        """
        self.identifier = ''
        self.name = ''
        self.shortname = ''
        self.description = ''
        self.created_at = ''
        self.updated_at = ''
        self.post_count = 0
        self.public = True
        self.transfert_to_parent_on_delete = True
        self.uesr_id = 0

    def __str__(self):
        """
        String representation of the object
        """
        return 'Set<{}>'.format(self.identifier)
