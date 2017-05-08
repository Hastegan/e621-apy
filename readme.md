# e621-apy
e621-apy is a python implementation for the e621 api.

## Usage
### List posts

```python
from e621apy import PostQuery, Search

q = PostQuery().tags('equine')

for post in Search(q):
    print(post.identifier)

```

#### Rating

The default rating is set to safe. It is possible to change the current rating with the `rating()` method:
```python
q = PostQuery().tags('equine').rating(PostQuery.RATING_ALL)
```
There are four ratings available, `RATING_SAFE`, `RATING_QUESTIONABLE`, `RATING_EXPLICIT` and `RATING_ALL`.

You can exclude a rating by providing a third argument to the method.
```python
q = PostQuery().tags('equine').rating(PostQuery.RATING_QUESTIONABLE, True)
```

#### Sorting
All Posts properties are sortable, `sort('score')` or `sort('score', False)` will sort the results by ascending score while `sort('score', True)` will sort the results by descending score.
```python
q = PostQuery().tags('equine').sort('score') # Ascending
q = PostQuery().tags('equine').sort('score', False) # Descending
```
### Get a post by id
It is possible to directly get a post by its ID. If the post is not found, `None` is returned.
```python
from e621apy import PostQuery, Search

q = PostQuery().get(393901)

post = Search(postQuery).first()

print(post.identifier)
```
In this case the method `.get()` is used to make the query look for a post Id. Then the method `.first()` is used to avoid looping through an array when only one (or None) result is expected.

## Testing
An easy way to test the package is done with the `nose` python package. Just run the following command at the root of the project.
```
nosetests
```
