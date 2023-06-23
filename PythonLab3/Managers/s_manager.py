class SetManager:

    def __init__(self, laptop_manager):

        self.laptop_manager = laptop_manager

    def __iter__(self):

        for laptop in self.laptop_manager.laptop_list:
            yield from laptop.favorite_set

    def __len__(self):

        lenght = 0
        for laptop in self.laptop_manager.laptop_list:
            lenght += len(laptop.the_best_operation_system_set)
        return lenght

    def __getitem__(self, index):
        count = 0
        for laptop in self.laptop_manager.laptop_list:
            if count <= index < count + len(laptop.the_best_operation_system_set):
                inner_index = index - count
                return list(laptop.the_best_operation_system_set)[inner_index]
            count += len(laptop.the_best_operation_system_set)
        raise IndexError("list index out of range")

    def __next__(self):
        raise StopIteration
