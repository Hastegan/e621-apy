__all__ = [
    'ForumPost',
]

class ForumPost(object):

    def __init__(self):
        self.id = 0
        self.parent_id = None
        self.creator = ''
        self.creator_id = 0
        self.title = ''
        self.body = ''
