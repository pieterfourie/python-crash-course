language = ' python '
language.rstrip()
print( language )
language.lstrip()
print( language )
language.strip()
print( language )

example_url = 'https://example.com'

simple_url = example_url.removeprefix('https://')
print( simple_url )

filename = 'example.txt'
simple_filename = filename.removesuffix('.txt')
print( simple_filename )
