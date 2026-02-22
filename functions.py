import random

def loot_generator(loot_table: list, generated_item_max_quant: int):
    loot_items = list()
    for i in loot_table:
        if i[1] * 0.01 <= random.random():
            item_quant = random.randint(i[2], i[3])
            loot_items.append([i[0], item_quant])
            print(loot_items[-1])
            if generated_item_max_quant >= len(loot_items): break