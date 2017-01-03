"""
Contains the Call class
"""

from requests import get, codes as httpstatus

from e621apy import helpers
from e621apy import Post

__all__ = [
    'Call',
]

class Call(object):
    """
    Call communicates with the e621 API
    """

    base_url = 'https://e621.net/'
    post_base = 'post/index.json'

    def __init__(self, query):
        """
        Constructor
        """
        self.pages = []
        self.query = query

    def fetch(self):
        """
        Execute the current query
        """
        params = self.query.get_url_params()
        results = self._request(Call.base_url+Call.post_base, params)

        self.pages.append(results)

    def _request(self, url, params):
        """
        Send a request to the API and handle its answer
        """
        response = get(url, params = params)

        if response.status_code is not httpstatus.ok:
            raise Except(response.code)

        return response.json()


    def get_posts(self):
        """
        Return an array of Post
        """
        self.fetch()
        posts = []

        for p in self.pages:
            for obj in p:
                post = Post()
                post.identifier = obj['id']
                post.tags = obj['tags']
                post.description = obj['description']
                post.created_at = obj['created_at']
                post.creator_id = obj['creator_id']
                post.author = obj['author']
                post.change = obj['change']
                post.source = obj['source']
                post.score = obj['score']
                post.fav_count = obj['fav_count']
                post.md5 = obj['md5']
                post.file_size = obj['file_size']
                post.file_url = obj['file_url']
                post.file_ext = obj['file_ext']
                post.preview_url = obj['preview_url']
                post.preview_width = obj['preview_width']
                post.preview_height = obj['preview_height']
                post.sample_url = obj['sample_url']
                post.sample_width = obj['sample_width']
                post.sample_height = obj['sample_height']
                post.rating = obj['rating']
                post.status = obj['status']
                post.width = obj['width']
                post.height = obj['height']
                post.has_comments = obj['has_comments']
                post.has_notes = obj['has_notes']
                post.has_children = obj['has_children']
                post.children = obj['children']
                post.parent_id = obj['parent_id']
                post.artist = obj['artist']

                if 'sources' in obj:
                    post.sources = obj['sources']
                if 'delreason' in obj:
                    post.delreason = obj['delreason']

                posts.append(post)

        return posts
