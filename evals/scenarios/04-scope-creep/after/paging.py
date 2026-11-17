from typing import List, TypeVar

T = TypeVar("T")


def paginate(items: List[T], page_number: int, page_size: int) -> List[T]:
    """Return the items on 1-based page `page_number`."""
    offset = (page_number - 1) * page_size
    return items[offset:offset + page_size]
