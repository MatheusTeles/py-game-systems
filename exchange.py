from datetime import datetime


class product:

    global_id = 1

    def __init__(self, name: str):
        self.product_id = product.global_id
        product.global_id += 1
        self.name = name

    def __repr__(self):
        return f"<Product {self.name}>"

    def __str__(self):
        return self.__repr__()


class order:

    global_id = 1

    def __init__(self, _product: product, amount: int, _type: str, price_per_item: int):
        self.order_id = order.global_id
        order.global_id += 1
        self.product = _product
        self.amount = amount
        self.remaining = self.amount
        self.finished = False
        self.type = _type
        self.price_per_item = price_per_item
        self._return = self.amount * self.price_per_item if self.type == 'buy' else 0
        self.timestamp: datetime = datetime.now()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"<{self.type.capitalize()} {self.amount} {self.product.name} @ {self.price_per_item} tk ea. ({f'{self.remaining} remaining'if self.remaining > 0 else 'Finished'}) {self.timestamp.strftime('%d/%m/%Y %H:%M:%S')}>"


class broker:
    def __init__(self):
        self.sell_orders = {}
        self.buy_orders = {}

    def add_order(self, order: order):
        if order.type == 'sell':
            if not order.product.product_id in self.sell_orders:
                self.sell_orders[order.product.product_id] = [order]
            else:
                for index, value in enumerate(self.sell_orders[order.product.product_id]):
                    if order.price_per_item < value.price_per_item:
                        self.sell_orders[order.product.product_id].insert(
                            index, order)
                        break
                    self.sell_orders[order.product.product_id].append(order)
                    break
        elif order.type == 'buy':
            if not order.product.product_id in self.buy_orders:
                self.buy_orders[order.product.product_id] = [order]
            else:
                self.buy_orders[order.product.product_id].append(order)

    def update(self):
        for product in self.buy_orders:
            for order in self.buy_orders[product]:
                self.process_buy_order(order)

    def process_buy_order(self, buy_order: order):
        print('----------- BUY ORDER START -------------')
        for sell_order in self.sell_orders[buy_order.product.product_id]:
            if not sell_order.finished and sell_order.price_per_item <= buy_order.price_per_item:
                purchased = min(sell_order.remaining, buy_order.remaining)
                buy_order.remaining -= purchased
                sell_order.remaining -= purchased
                buy_order._return -= purchased * sell_order.price_per_item
                sell_order._return += purchased * sell_order.price_per_item
                print(
                    f'{buy_order} progressed, bought {purchased} from {sell_order}')
                if buy_order.remaining == 0:
                    self.finished = True
                    print(f'{buy_order} finished')
                    break
                print(f'{sell_order} finished')
                sell_order.finished = True
        print('----------- BUY ORDER END -------------')


if __name__ == "__main__":
    from time import sleep

    b = broker()
    p = product('Iron Ore')
    buys = [order(p, 120, 'buy', 167), order(p,  30, 'buy', 189),
            order(p, 500, 'buy', 195), order(p, 245, 'buy', 135)]
    sells = [order(p, 205, 'sell', 165), order(p, 178, 'sell', 177),
             order(p,  830, 'sell', 129), order(p, 335, 'sell', 145)]
    for o in buys:
        b.add_order(o)
        sleep(0.1)
    del o

    for o in sells:
        b.add_order(o)
        sleep(0.1)
    del o

    print(b.buy_orders)
    print(b.sell_orders)

    b.update()

    for key in b.buy_orders:
        for value in b.buy_orders[key]:
            print(value, value._return)

    for key in b.sell_orders:
        for value in b.sell_orders[key]:
            print(value, value._return)
