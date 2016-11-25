__all__ = [
    'Tag',
]

class Tag(object):

    TYPES = [
        'general',
        'artist',
        'copyright',
        'character',
        'species',
    ]

    def __init__(self):
        self.id = 0
        self.name = ""
        self.count = 0
        self.type = 0

    def get_type_label(self):
        return Tag.TYPES[self.type]
