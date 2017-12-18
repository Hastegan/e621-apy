"""
    Unit tests for Parser
"""

import unittest

from e621apy import Parser, Post

class ParserTestCase(unittest.TestCase):

    post = Post()
    post.identifier = 42
    post.tags = 'tag1 tag2'
    post.description = 'description'
    post.created_at = {"json_class":"Time", "s":0, "n":1}
    post.creator_id = 2
    post.author = 'author'
    post.change = 3
    post.source = 'source'
    post.score = 4
    post.fav_count = 5
    post.md5 = 'md5'
    post.file_size = 6
    post.file_url = 'file url'
    post.file_ext = 'extension'
    post.preview_url = 'preview url'
    post.preview_width = 7
    post.preview_height = 8
    post.sample_url = 'sample url'
    post.sample_width = 9
    post.sample_height = 10
    post.rating = 'rating'
    post.status = 'status'
    post.width = 11
    post.height = 12
    post.has_comments = False
    post.has_notes = False
    post.has_children = False
    post.children = 'child'
    post.parent_id = 13
    post.artist = ["artist"]
    post.sources = ["source1", "source2"]
    post.delreason = ''

    jsonPost = {"id":42, "tags":"tag1 tag2", "locked_tags":"tag3 tag4", "description":"description", "created_at":{"json_class":"Time", "s":0, "n":1 }, "creator_id":2, "author":"author", "change":3, "source":"source", "score":4, "fav_count":5, "md5":"md5", "file_size":6, "file_url":"file url", "file_ext":"extension", "preview_url":"preview url", "preview_width":7, "preview_height":8, "sample_url":"sample url", "sample_width":9, "sample_height":10, "rating":"rating", "status":"status", "width":11, "height":12, "has_comments":False, "has_notes":False, "has_children":False, "children":"child", "parent_id":13, "artist":["artist"], "sources":["source1", "source2"] }



    def test_parsePostFromDict(self):
        """
        Check if dict is correctly parsed into a Post
        """
        parser = Parser('post')
        parsed = parser.parse_post(self.jsonPost)

        self._comparePosts(self.post, parsed)

    def test_parseElementReturnsCorrectObject(self):
        """
        Check if parse_element returns a correct object
        """
        parser = Parser('post')
        parsed = parser.parse_element(self.jsonPost)

        self.assertTrue(isinstance(parsed, Post))

    def test_parsePostFromList(self):
        """
        Check if list in correctly parsed into Posts
        """
        inputList = [self.jsonPost]

        parser = Parser('post')
        parsed = parser.parse(inputList)[0]

        self._comparePosts(self.post, parsed)

    def _comparePosts(self, post, other):
        self.assertEquals(post.identifier, other.identifier)
        self.assertEquals(post.tags, other.tags)
        self.assertEquals(post.description, other.description)
        self.assertEquals(post.created_at, other.created_at)
        self.assertEquals(post.creator_id, other.creator_id)
        self.assertEquals(post.author, other.author)
        self.assertEquals(post.change, other.change)
        self.assertEquals(post.source, other.source)
        self.assertEquals(post.score, other.score)
        self.assertEquals(post.fav_count, other.fav_count)
        self.assertEquals(post.md5, other.md5)
        self.assertEquals(post.file_size, other.file_size)
        self.assertEquals(post.file_url, other.file_url)
        self.assertEquals(post.file_ext, other.file_ext)
        self.assertEquals(post.preview_url, other.preview_url)
        self.assertEquals(post.preview_width, other.preview_width)
        self.assertEquals(post.preview_height, other.preview_height)
        self.assertEquals(post.sample_url, other.sample_url)
        self.assertEquals(post.sample_width, other.sample_width)
        self.assertEquals(post.sample_height, other.sample_height)
        self.assertEquals(post.rating, other.rating)
        self.assertEquals(post.status, other.status)
        self.assertEquals(post.width, other.width)
        self.assertEquals(post.height, other.height)
        self.assertEquals(post.has_comments, other.has_comments)
        self.assertEquals(post.has_notes, other.has_notes)
        self.assertEquals(post.has_children, other.has_children)
        self.assertEquals(post.children, other.children)
        self.assertEquals(post.parent_id, other.parent_id)
        self.assertEquals(post.artist, other.artist)
        self.assertEquals(post.sources, other.sources)
        self.assertEquals(post.delreason, other.delreason)