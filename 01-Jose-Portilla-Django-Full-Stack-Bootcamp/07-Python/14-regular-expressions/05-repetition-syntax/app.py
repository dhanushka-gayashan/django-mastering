import re


def multi_re_find(patterns, phrase):
    for pattern in patterns:
        print("Searching for pattern {}".format(pattern))
        print(re.findall(pattern, phrase))
        print("\n")


test_phrase = 'sdsd..sssddd..sdddsddd...dsds....dssssss...sddddd'

# Exactly sd
test_patterns = ['sd']
multi_re_find(test_patterns, test_phrase)


# 0 or more d's with rest
test_patterns = ['sd*']
multi_re_find(test_patterns, test_phrase)


# 1 or more d's with rest
test_patterns = ['sd+']
multi_re_find(test_patterns, test_phrase)


# 0 or 1 d with rest
test_patterns = ['sd?']
multi_re_find(test_patterns, test_phrase)


# 3 d's with rest
test_patterns = ['sd{3}']
multi_re_find(test_patterns, test_phrase)


# 1 or 3 d's with rest
test_patterns = ['sd{1,3}']
multi_re_find(test_patterns, test_phrase)


# s followed by s or d with rest
test_patterns = ['s[sd]+']
multi_re_find(test_patterns, test_phrase)


test_phrase = 'This is a string! But is has punctuation. How can we remove it?'

# exclude patterns like ! . ?
test_patterns = ['[^!.?]+']
multi_re_find(test_patterns, test_phrase)


# return all lowe case characters
test_patterns = ['[a-z]+']
multi_re_find(test_patterns, test_phrase)


# return all upper case characters
test_patterns = ['[A-Z]+']
multi_re_find(test_patterns, test_phrase)


test_phrase = 'This is a string with numbers 12345 and a symbo #hashtag'

# search for digits
test_patterns = [r'\d+']
multi_re_find(test_patterns, test_phrase)


# search for non digits
test_patterns = [r'\D+']
multi_re_find(test_patterns, test_phrase)


# search for white spaces
test_patterns = [r'\s+']
multi_re_find(test_patterns, test_phrase)


# search for non white spaces
test_patterns = [r'\S+']
multi_re_find(test_patterns, test_phrase)


# search for alpha-numeric
test_patterns = [r'\w+']
multi_re_find(test_patterns, test_phrase)


# search for non alpha-numeric
test_patterns = [r'\W+']
multi_re_find(test_patterns, test_phrase)