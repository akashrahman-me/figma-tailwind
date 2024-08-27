def align_items_class(align_item):
    align_items = [
        ['flex-start', 'items-start'],
        ['flex-end', 'items-end'],
        ['center', 'items-center'],
        ['baseline', 'items-baseline'],
        ['stretch', 'items-stretch']
    ]

    for pair in align_items:
        if align_item == pair[0]:
            return pair[1]

    return ""
