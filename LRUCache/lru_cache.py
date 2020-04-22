class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # fields
        # limit
        # size
        # order
        # storage

        pass

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if the key exists in the storage
            # extrapolate the node from the storage at the index of key
            # move the node to the end of the order list
            # return the value from the node
        # otherwise
            # return None
        pass

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if the key exists in the storage
            # extrapolate the node from the storage at the index of key
            # set the nodes value to the (key, value) pair
            # move the node to the end of the order list
            # just return from the method
        # if the size is equal to the limit
            # delete the storage entry at the key from the order lists head
            # remove the head of the order
            # decrement the size
        
        # add the (key, value) pair to the tail of the order
        # set the storage at the key to the order tail
        # increment the size
        pass