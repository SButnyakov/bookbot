def get_num_words(text):
	counter = 0
	for word in text.split():
		counter += 1
	return counter

def get_num_symbols(text):
    res = {}
    for symbol in list(text):
        char = symbol.lower()
        if not char in res:
            res[char] = 0
        res[char] += 1
    return res

def get_chars_sorted_dict(chars_dict):
    chars = []
    for item in chars_dict.items():
        chars.append({"char": item[0], "num": item[1]})
    chars.sort(key=lambda x:x["num"], reverse=True)
    return chars
