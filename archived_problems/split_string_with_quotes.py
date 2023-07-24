#!/usr/bin/env python3

# Split a string into a list of words. If a quoted section appears, keep the
# words grouped together.
# Ex: 'This is "very creative"' --> ['This', 'is', 'very creative']


def split_words(words):
    final = []
    in_special = False
    special = ''
    
    for word in words.split(' '):
        # if in special
        if in_special:
            # if last special
            if '"' in word or "'" in word:
                in_special = False
                special += word.replace('"','').replace("'",'')
                final.append(special)
                special = ''
            
            # else not last
            else:
                special += word + '.'

        # if not in special
        else:
            # if word is special open
            if '"' in word or "'" in word:
                in_special = True
                special += word.replace('"','').replace("'",'') + '.'

            # if word not special
            else:
                final.append(word)
 
    print([word.replace('.',' ')  for word in final])
    return [word.replace('.',' ') for word in final]
    


if __name__ == "__main__":
    assert split_words('A simple test') == ['A', 'simple', 'test'], 'error 1'
    assert split_words('This is "very creative"') == ['This', 'is', 'very creative'], 'error 2'
    assert split_words('The description is "red, white, and blue"') == ['The', 'description', 'is', 'red, white, and blue'], 'error 3'
    print("TESTS PASSED")
    
