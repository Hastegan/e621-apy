__all__ = [
    'Artist',
]

class Artist(object):

    def __init__(self):
        self.id = 0
        self.name = ''
        self.other_names = ''
        self.group_name = ''
        self.urls = ''
        self.is_active = False
        self.version = 0
        self.updater_id = 0
