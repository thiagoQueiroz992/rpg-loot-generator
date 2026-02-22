import random, time

def loot_generator(loot_table: list):
    loot_items = list()
    print("Generating loot", end="", flush=True)
    time.sleep(1)
    for d in range(1, 4):
        print(".", end="", flush=True)
        time.sleep(1)
    print()
    print("Loot has been generated!")
    time.sleep(.5)
    for i in loot_table:
        if random.random() <= i[1] * 0.01:
            item_quant = random.randint(i[2], i[3])
            loot_items.append([i[0], item_quant])
            print(loot_items[-1][0]().item_name, "x", loot_items[-1][1])
            time.sleep(1)
