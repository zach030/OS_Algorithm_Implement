class Page:
    start = 0
    length = 0
    end = 0

    def __init__(self, length):
        self.length = length


class Memory:
    max_size = 0
    empty_block = {}
    empty_memory = []

    def __init__(self, max_size):
        self.max_size = max_size
        self.empty_block = {"start": 0, "end": max_size}
        self.empty_memory.append(self.empty_block)

    def sort_empty_by_addr(self):
        self.empty_memory.sort(key=lambda e: e["start"])

    def page_in(self, page):
        self.sort_empty_by_addr()
        for empty in self.empty_memory:
            if empty.get("end") > page.length:
                old_start = empty["start"]
                page.start = old_start
                page.end = page.start + page.length
                empty["start"] = page.end
                break

    def page_out(self, page):
        has_below = 0
        has_up = 0
        for empty in self.empty_memory:
            if empty.get("start") == page.end:
                has_below = 1
            if empty.get("end") == page.start:
                has_up = 1



memory = Memory(100)
page_list = [Page(10), Page(15), Page(20), Page(8), Page(40), Page(25)]
