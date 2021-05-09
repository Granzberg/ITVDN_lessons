class Goods(object):
    def __init__(self, name, price, price_list=None):
        self.name = name
        self.price = price
        self.price_list = price_list or []

    def __repr__(self):
        return 'Goods({name}, {price}, {price_list})'.format_map(self.__dict__)

    @staticmethod
    def make_sets(first, second):
        first.price_list.append(second)
        second.price_list.append(first)
