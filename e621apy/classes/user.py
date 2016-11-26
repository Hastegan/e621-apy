"""
Contains the User class
"""

__all__ = [
    'User',
]

class User(object):
    """
    Represents a user
    """

    LEVEL_LABELS = {
        10: 'blocked',
        20: 'member',
        30: 'privileged',
        33: 'contributot',
        35: 'janitor',
        40: 'mod',
        50: 'admin',
    }

    def __init__(self):
        """
        Initiate properties
        """
        self.identifier = 0
        self.name = ''
        self.level = 10
        self.created_at = ''
        self.avatar_id = ''
        self.post_count = 0
        self.del_post_count = 0
        self.edit_count = 0
        self.favorite_count = 0
        self.wiki_count = 0
        self.forum_post_count = 0
        self.note_count = 0
        self.edit_count = 0
        self.comment_count = 0
        self.blip_count = 0
        self.set_count = 0
        self.pool_update_count = 0
        self.pos_user_records = 0
        self.neutral_user_records = 0
        self.neg_user_records = 0
        self.artist_tag = []

    def get_level_label(self):
        """
        Return the user level label
        """
        return User.LEVEL_LABELS[self.level]
