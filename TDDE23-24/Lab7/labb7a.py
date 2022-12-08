"""
Simon Jakobsson, Viktor Andersson
"""



db = [[['författare', ['john', 'zelle']],
       ['titel', ['python', 'programming', 'an', 'introduction', 'to', \
        'computer', 'science']],
       ['år', 2010]],
      [['författare', ['armen', 'asratian']],
       ['titel', ['diskret', 'matematik']],
       ['år', 2012]],
      [['författare', ['j', 'glenn', 'brookshear']],
       ['titel', ['computer', 'science', 'an', 'overview']],
       ['år', 2011]],
      [['författare', ['john', 'zelle']],
       ['titel', ['data', 'structures', 'and', 'algorithms', 'using', \
       'python', 'and', 'c++']],
       ['år', 2009]],
      [['författare', ['anders', 'haraldsson']],
       ['titel', ['programmering', 'i', 'lisp']],
       ['år', 1993]]]





def search(pattern, db):
    """
    Search database of all items,
    if it matches put the new seq in a  new list
    """

    matched_list = []

    for seq in db:
        if match(seq, pattern):
            matched_list.append(seq)
    return matched_list


def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq
    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq:
        return False
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    elif isinstance(seq[0], list) and isinstance(pattern[0], list):
        return match(seq[0], pattern[0])
    else:
        return False

print(search([['författare', ['&', 'zelle']], ['titel', \
 ['--', 'python', '--']], ['år', '&']], db))
print (search(['--',['år', 2009],'--'], db))
assert search(['--','--', '--'], db) == db
assert search([['författare', ['&', '&','&','&','&']],'--', '--'], db) == []
assert search(['--',['år', 2009],'--'], db) == [db[3]]
