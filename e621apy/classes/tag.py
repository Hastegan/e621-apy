"""
Contains the Tag class
"""

__all__ = [
    'Tag',
]

class Tag(object):
    """
    Represents a tag
    """

    TYPES = [
        'general',
        'artist',
        'copyright',
        'character',
        'species',
    ]

    def __init__(self):
        """
        Initiate properties
        """
        self.identifier = 0
        self.name = ""
        self.count = 0
        self.type = 0

    def get_type_label(self):
        """
        Return the tag type label
        """
        return Tag.TYPES[self.type]
