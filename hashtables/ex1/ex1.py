#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for index in range(length):
        hash_table_insert(ht, weights[index], index)

    for index in range(length):
        weight_item_difference = limit - weights[index]

        difference = hash_table_retrieve(ht, weight_item_difference)

        if difference is not None:
            if difference >= index:
                return (difference, index)
            else:
                return (index, difference)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
