__all__ = [
    'comment',
]

class Comment(object):

    def __init__(self):
        self.id = 0
        self.created_at = ''
        self.post_id = 0
        self.creator = ''
        self.creator_id = 0
        self.body = ''
        self.score = 0
