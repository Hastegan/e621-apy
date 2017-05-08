"""
    Helper functions frequently used by the module's classes
"""

def add_tag(tags, tag):
    """
    Add a tag to a given tag list
    """

    # Format tag to e621 standards
    tag = clean_tag(tag)

    # Retrieve the tag 'key' if any
    key = None
    if ':' in tag:
        key = tag.split(':')[0]
        key = '%s:' % key
        cleaned_key = clean_key(key)

    for i, item in enumerate(tags):
        # Look for simple duplicates
        if item == tag:
            return tags


        # Look for key duplicates
        if key and (key in item or cleaned_key in item):
            tags[i] = tag
            return tags

    tags.append(tag)
    return tags

def clean_tag(tag):
    """
    Format tag to match e621 format
    """
    tag = tag.replace(' ', '_')
    return tag

def clean_key(key):
    """
    Clean up a tag key
    """
    key = key.replace(':', '')

    if len(key) >= 1 and key[0] == '-':
        key = key[1:]

    return key
