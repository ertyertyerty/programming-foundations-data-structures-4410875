def has_unique_characters_1(data):
    charset = set([])
    for x in data:
        charset.add(x)
    if len(data) == len(charset):
        return True
    return False

def has_unique_characters(data):
    return len(set(data)) == len(data)

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
