def add_prefix_for_cache(prefix, value):
    if value is None:
        value = prefix
    else:
        value = prefix + value
    return value
