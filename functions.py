import random

def loot_generator(loot_table: list):
    loot_items = list()
    for i in loot_table:
        if random.random() <= i[1] * 0.01:
            item_quant = random.randint(i[2], i[3])
            loot_items.append([i[0], item_quant])
            print(loot_items[-1][0]().item_name, "x", loot_items[-1][1])
