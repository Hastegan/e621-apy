def _add_tag(tags, tag):
    tag = _clean_tag(tag)

    if ':' not in tag:
        tags.append(tag)
        return tags

    parts = tag.split(':')
    if len(parts) != 2:
        return tags

    key = parts[0]
    value = parts[1]

    for i in range(len(tags)):
        if key in tags[i]:
            tags[i] = tag
            return tags

    tags.append(tag)
    return tags


def _clean_tag(tag):
    tag = tag.replace(' ', '_')
    return tag
