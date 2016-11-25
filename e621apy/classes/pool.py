__all__ = [
    'Pool',
]

class Pool(object):

    def __init__(self):
        self.id = 0
        self.name = ''
        self.created_at = ''
        self.updated_at = ''
        self.user_id = 0
        self.is_locked = False
        self.post_count = 0
        self.description = ''
