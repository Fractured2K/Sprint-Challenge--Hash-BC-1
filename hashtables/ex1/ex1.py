#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # iterate over weights
    for i in range(len(weights)):
        # insert weight as key and index as value into hashtable
        hash_table_insert(ht, weights[i], i)

    # iterate over weights
    for i in range(len(weights)):
        # create reference to current weight
        weight = weights[i]

        # determine key
        key = limit - weight

        # retrieve value from index
        value = hash_table_retrieve(ht, key)

        # return indices, that equate to limit when summed
        if value is not None:
            return(value, i)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
