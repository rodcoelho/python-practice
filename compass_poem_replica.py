#!/usr/bin/env python3

# Create a dictionary with the location of each word in a poem.
# The dictionary will have the word as key, and the value will
# be a list of tuples indicating the location: ie. (page, index).

_poem = [
"""A single flow'r he sent me, since we met.
    All tenderly his messenger he chose;
    Deep-hearted, pure, with scented dew still wet —
    One perfect rose.""",
"""I knew the language of the floweret;
    My fragile leaves, it said, his heart enclose.
    Love long has taken for his amulet
    One perfect rose.""",
"""Why is it no one ever sent me yet
    One perfect limousine, do you suppose?
    Ah no, it's always just my luck to get
    One perfect rose."""
]


def create_dict(poem):
    final_d = {}
    for i in range(len(poem)):
        normalized_page = ""
        page = poem[i]
        for char in page:
            if char.isalpha() or char in ['`', "'", ' ']:
                normalized_page += char.lower()
            else:
                normalized_page += ' '
        normalized_page = [word for word in normalized_page.split(' ') if word]

        for j in range(len(normalized_page)):
            word = normalized_page[j]
            if word in final_d:
                final_d[word].append((i, j))
            else:
                final_d[word] = [(i, j)]

    return final_d


if __name__ == "__main__":
    assert create_dict(_poem)["flow'r"][0] == (0, 2), 'test 1'
    assert create_dict(_poem)['rose'][-1] == (2, 26), 'test 2'
    
    print("TESTS PASSED")        
