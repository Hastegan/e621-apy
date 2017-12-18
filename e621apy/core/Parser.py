"""
	Contains the Parser class
"""

from e621apy import Post

__all__ = [
    'Parser',
]

class Parser(object):

    def __init__(self, type):
        self._type = type

    def parse(self, data):
        """
        Return an object or a list of objects from a dict or a list
        """
        for item in data:
            if type(data) is dict:
                return self.parse_element(data)
            elif type(data) is list:
                return self.parse_list(data)

    def parse_element(self, data):
        """
        Return object from dict
        """
        if (self._type == 'post'):
            return self.parse_post(data)

    def parse_list(self, data):
        """
        Return list of object from a list
        """
        items = []
        for item in data:
            items.append(self.parse_element(item))

        return items

    def parse_post(self, data):
        """
        Return a Post object from a dict
        """
        post = Post()
        post.identifier = data['id']
        post.tags = data['tags']
        post.description = data['description']
        post.created_at = data['created_at']
        post.creator_id = data['creator_id']
        post.author = data['author']
        post.change = data['change']
        post.source = data['source']
        post.score = data['score']
        post.fav_count = data['fav_count']
        post.md5 = data['md5']
        post.file_size = data['file_size']
        post.file_url = data['file_url']
        post.file_ext = data['file_ext']
        post.preview_url = data['preview_url']
        post.preview_width = data['preview_width']
        post.preview_height = data['preview_height']
        post.sample_url = data['sample_url']
        post.sample_width = data['sample_width']
        post.sample_height = data['sample_height']
        post.rating = data['rating']
        post.status = data['status']
        post.width = data['width']
        post.height = data['height']
        post.has_comments = data['has_comments']
        post.has_notes = data['has_notes']
        post.has_children = data['has_children']
        post.children = data['children']
        post.parent_id = data['parent_id']
        post.artist = data['artist']

        if 'sources' in data:
            post.sources = data['sources']
        if 'delreason' in data:
            post.delreason = data['delreason']

        return post