def replace_spaces(s):
    return "%20".join(s.split(" "))

s=" This is not a very long sentences, but it have spaces! "
print(replace_spaces(s))

# This works as well
print(s.replace(" ", "%20"))