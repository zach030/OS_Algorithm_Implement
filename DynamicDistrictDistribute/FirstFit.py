from DynamicDistrictDistribute.Memory_Page import memory, page_list


def FirstFitDistribute(memory, pages):
    for page in pages:
        memory.page_in(page)
        print(memory.empty_memory)


if __name__ == "__main__":
    FirstFitDistribute(memory=memory, pages=page_list)
