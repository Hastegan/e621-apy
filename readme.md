# e621-apy
e621-apy is a python implementation for the e621 api.

## Usage
### List posts
#### Rating
```python
from e621apy import PostQuery, Search

q = PostQuery().tags('equine').rating(PostQuery.RATING_SAFE)

for post in Search(q):
    print(post.identifier)
```
Will output
```
1164244
1164241
1164231
[...]
```
There are four post ratings available, `RATING_SAFE`, `RATING_QUESTIONABLE`, `RATING_EXPLICIT` and `RATING_ALL`.

#### Sorting
All Posts properties are sortable, `sort('score')` or `sort('score', False)` will sort the results by ascending score while `sort('score', True)` will sort the results by descending score.
```python
q = PostQuery().tags('equine').sort('score') # Ascending
q = PostQuery().tags('equine').sort('score', False) # Descending
```
### Get one post by id
TODO
