import random, time

def loot_generator(loot_table: list):
    loot_items = list()
    print("\n\033[33mGenerating loot\033[m", end="", flush=True)
    time.sleep(1)
    for d in range(1, 4):
        print(".", end="", flush=True)
        time.sleep(1)
    print()

    for i in loot_table:
        if random.random() <= i[1] * 0.01:
            item_quant = random.randint(i[2], i[3])
            loot_items.append([i[0], item_quant])
    print("\033[32mLoot has been generated!\033[m\n")
    random.shuffle(loot_items)
    time.sleep(.5)
    
    for i in loot_items:
        print("\033[1;34m" + i[0]().item_name + "\033[m", "x", "\033[3m" + str(i[1]) + "\033[m")
        time.sleep(1)
