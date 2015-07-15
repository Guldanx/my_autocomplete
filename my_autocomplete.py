#my_autocomplete.py
import sys

# TODO: Speed when using more words
# TODO: Impletement fuzziness -> 'cmputer' should find 'computer'
# TODO: Space of the data structure handled
# TODO: How to incorporate it in a web app ?

MYDB = sorted(['Mass Effect', 'Mass Effect 2', 'Mass Effect 3', 'Mass Effect: Andromeda',
        'Sydney', 'Mayenne', 'Paris', 'Nantes', 'Melbourne', 'Barcelona', 'Tokyo', 'Beijin', 'Shanghai', 'Kyoto', 'London',
        'France', 'Australia', 'Japan', 'England', 'China', 'Spain',
        'Ant', 'Tiger', 'Wolf', 'Cat', 'Dog', 'Bird',
        'Car', 'Computer', 'Flat', 'House',
        'Google', 'Microsoft', 'Atlasian', 'Hipages', 'Smile'])

def main():
    if len(sys.argv) == 1:
        show_helper()
    else:
        my_autocomplete(sys.argv[1])
    return True

def show_helper():
    helper = "-- my_autocomplete help --\nYou need to type an argument (eg: python my_autocomplete.py appartm)"
    print(helper)
    return True

def my_autocomplete(query):
    matching_keywords = get_matching_keywords(query)
    if len(matching_keywords) == 11:
        matching_keywords[10] = '...'
    if matching_keywords:
        print('\n'.join(matching_keywords))
    return True

def get_matching_keywords(query):
    res = []
    second_res = []
    for keyword in MYDB:
        if len(res) == 11:
            break
        if keyword.lower().startswith(query.lower()):
            res.append(keyword)
    for keyword in MYDB:
        if len(res) + len(second_res) == 11:
            break
        if query.lower() in keyword.lower() and keyword not in res:
            second_res.append(keyword)
    return res + second_res

if __name__ == '__main__':
    main()