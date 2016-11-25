__all__ = [
    'Set',
]

class Set(object):

    def __init__(self):
        self.id = ''
        self.name = ''
        self.shortname = ''
        self.description = ''
        self.created_at = ''
        self.updated_at = ''
        self.post_count = 0
        self.public = True
        self.transfert_to_parent_on_delete = True
        self.uesr_id = 0
