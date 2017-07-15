# e621-apy
e621-apy is a python implementation for the e621 api.

## Usage
The two main objects used are `PostQuery`, to formulate a query, and `Search`, to actually perform the query. Only those two objects are needed to get e621apy to work.
```python
from e621apy import PostQuery, Search
```

### List posts
Build the query:
```python
q = PostQuery().tags('equine')
```
With multiple tags:
```python
q = PostQuery().tags('equine', 'dog')
```
Get the results:
```python
for post in Search(q):
    print(post.identifier)
```
Note that the `Search` object is easily iterable.

All [tags supported](https://e621.net/help/show/cheatsheet) by e621 can be put in the `tags()` method, all functions described below (after Pages and Limits) must be seen as shortcuts to the most common ones.

### Pages and Limits
The page to look for can be set with the `page()` method while the number of posts by page is set through `limit()`.
```python
# Theses are actually the default settings
q = PostQuery().page(1).limit(75)
```

### Get a post by id or by md5
It is possible to directly get a post by its ID or by its md5 hash. If the post is not found, `None` is returned.
```python
q = PostQuery().get(393901)
post = Search(postQuery).first()
print(post.identifier)
```
Or with the md5.
```python
q = PostQuery().md5("cf75527b38777e6f153689859b5cdb67")
```

The method `.get()`  is used to make the query look for a post Id. The `.first()` method is used to avoid looping through an array when only one (or None) result is expected.

### Rating
The default rating is set to safe. It is possible to change the current rating with the `rating()` method:
```python
q = PostQuery().tags('equine').rating(PostQuery.RATING_ALL)
```
There are four ratings available, `RATING_SAFE`, `RATING_QUESTIONABLE`, `RATING_EXPLICIT` and `RATING_ALL`.

It is not possible to cumulate two ratings, but do not worry, since only three are possible, removing one of them will have the same result as cumulating the two remaining. A second argument is provided to do it.
```python
q = PostQuery().tags('equine').rating(PostQuery.RATING_EXPLICIT, True)
```

### Sorting
All Posts properties are sortable, `sort('score')` or `sort('score', False)` will sort the results by ascending score while `sort('score', True)` will sort the results by descending score.
```python
q = PostQuery().tags('equine').sort('score') # Ascending
q = PostQuery().tags('equine').sort('score', False) # Descending
```

### Filters
Filters are used to add more criteria. The currently implemented filters are `has_source()`, `has_description()` and `is_in_pool()`.
```python
q = PostQuery().has_source(True|False)
q = PostQuery().has_description(True|False)
q = PostQuery().is_in_pool(True|False)
```

### Pools and Sets
The `pool()` method is used to get posts inside a pool, the parameter is a pool id or a **pool name**.
```python
q = PostQuery().pool(4)
q = PostQuery().pool("The quick brown fox jumps, Chapter: 2")
```
The `set()` method is used to get posts inside a set, the parameter is a set id or the a **set short name**
```python
q = PostQuery().set(17)
q = PostQuery().pool("cute_rabbits")
```
## Testing
An easy way to test the package is done with the `nose` python package. Just run the following command at the root of the project.
```
nosetests
```
## Development progress
See what is going on the [kanban](https://trello.com/b/0ERpDeyo/e621-apy).
