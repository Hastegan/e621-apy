"""
Contains the Artist class
"""

__all__ = [
    'Artist',
]

class Artist(object):
    """
    Represents an artist
    """

    def __init__(self):
        """
        Initiate properties
        """
        self.identifier = 0
        self.name = ''
        self.other_names = ''
        self.group_name = ''
        self.urls = ''
        self.is_active = False
        self.version = 0
        self.updater_id = 0
