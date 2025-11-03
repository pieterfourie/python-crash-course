def formatted_name(first, last, middle=''):
    """Generate a full name neatly formatted."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

musician = formatted_name('jimi', 'hendrix')
print(musician)