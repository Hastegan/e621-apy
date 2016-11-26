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

    for i, item in enumerate(tags):
        # Look for simple duplicates
        if item == tag:
            return tags

        # Look for key duplicates
        if key and key in item:
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
