def paginate(items, page, size):
    """Return the items on 1-based page `page`."""
    start = page * size
    return items[start:start + size]
