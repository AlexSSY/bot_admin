import math


def paginate(total, per_page, page):
    # корректировка page
    page = max(1, page)
    total_pages = math.ceil(total / per_page)
    page = min(total_pages, page)
    start = (page - 1) * per_page

    return start, start + per_page
