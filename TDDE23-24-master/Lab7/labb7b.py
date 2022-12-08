def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
    """
    Går igenom tree, kollar först om tree är tomt. Går sedan vidare
    och kollar om tree är ett löv annars går den vidare
    och räknar först ut de inre noderna i vänsterled och sedan
    i det högra ledet.
    """

    def is_empty_tree(tree):
        return isinstance(tree, list) and not tree

    def is_leaf(tree):
        return isinstance(tree, int)

    def create_tree(left_tree, key, right_tree):
        return [left_tree, key, right_tree]

    def left_subtree(tree):
        return tree[0]

    def key(tree):
        return tree[1]

    def right_subtree(tree):
        return tree[2]

    def is_inner_node(tree):
        return isinstance(tree,list)

    if tree == []:
        return empty_tree_fn()

    elif is_leaf(tree):
        return leaf_fn(tree)

    elif is_inner_node(tree):
        left = traverse(left_subtree(tree),inner_node_fn, leaf_fn, \
        empty_tree_fn)
        right = traverse(right_subtree(tree),inner_node_fn, leaf_fn, \
        empty_tree_fn)

    return inner_node_fn(key(tree),left,right)


def left_tree_calc(tree):
    """
    Går igenom tree, ignorerar vänsterledet och tar
    kvadraten på lövet samt adderar värdet på alla
    nycklar som befinner sig på samma sträcka som lövet
    """

    def inner_node_fn(key, left_value, right_value):
        return key + left_value

    def empty_tree_fn():
        return 0

    def leaf_fn(key):
        return key**2

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

def contains_key(k, seq):
    """
    Går igenom hela trädet och letar efter nyckeln k.
    Om nyckeln hittas returnas True annars False
    """
    def leaf_fn(key):
        return k == key

    def empty_tree_fn():
        return False

    def inner_node_fn(key, left_value, right_value):
        if key == k or right_value or left_value:
            return True
        else:
            return False

    return  traverse(seq, inner_node_fn, leaf_fn, empty_tree_fn)

def tree_size(tree):
    """
    Går igenom trädet och lägger till 1 för varje nyckel.
    Returnar antalet nycklar som finns i trädet
    """

    def leaf_fn(key):
        return 1

    def empty_tree_fn():
        return 0

    def inner_node_fn(key, left_value, right_value):
        return 1 + left_value + right_value

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

def tree_depth(tree):
    """
    Går igenom trädet och letar efter den längsta vägen.
    Returnar sedan antal steg som krävs för att ta den längsta vägen
    """

    def leaf_fn(key):
        return 1

    def empty_tree_fn():
        return 0

    def inner_node_fn(key, left_value, right_value):
        return 1 + max(left_value, right_value)

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

def test_left_tree_calc():
    """
    Testar olika fall för att se om left_tree_calc fungerar
    """

    assert left_tree_calc([1,2,3]) == 3
    assert left_tree_calc(2) == 4
    assert left_tree_calc([]) == 0

    print("All tests passed in left_tree_calc")

def test_tree_depth():
    """
    Testar olika fall för att se om tree_depth fungerar
    """

    assert tree_depth([6,7,[1,2,[[1,2,3],2,3]]]) == 5
    assert tree_depth([]) == 0
    assert tree_depth(6) == 1

    print("All tests passed in tree_depth")

def test_contains_key():
    """
    Testar olika fall för att se om contains_key fungerar
    """

    assert contains_key(7,7)
    assert contains_key(12,[1,2,[[],5,[10,20,[15,3,12]]]])
    assert contains_key(10,[1,3,5]) == False

    print("All tests passed in contains_key")
def test_tree_size():
    """
    Testar olika fall för att se om tree_size fungerar
    """

    assert tree_size(10) == 1
    assert tree_size([1,2,[[],5,[10,20,[15,3,12]]]]) == 8
    assert tree_size([]) == 0

    print("All tests passed in tree_size")

test_left_tree_calc()
test_tree_size()
test_contains_key()
test_tree_depth()
