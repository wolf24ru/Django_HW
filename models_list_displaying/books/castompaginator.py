class IterPaginator():
    def __init__(self, iter_object: list, now: str):
        self.iter_object = iter_object
        self.naw = now
        self.index_now = iter_object.index(now)

    def next(self):
        try:
            return self.iter_object[self.index_now + 1]
        except IndexError:
            return None

    def prev(self):
        if self.index_now - 1 >= 0:
            return self.iter_object[self.index_now - 1]
        else:
            return None
