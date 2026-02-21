class Item:
    def __init__(self):
        self.item_id = "item:null"
        self.item_name = "Null"

class String(Item):
    def __init__(self):
        super().__init__()
        self.item_id = "item:string"
        self.item_name = "String"

class RottenFlesh(Item):
    def __init__(self):
        super().__init__()
        self.item_id = "item:rotten_flesh"
        self.item_name = "Rotten Flesh"

class Gunpowder(Item):
    def __init__(self):
        super().__init__()
        self.item_id = "item:gunpowder"
        self.item_name = "Gunpowder"

class Arrow(Item):
    def __init__(self):
        super().__init__()
        self.item_id = "item:arrow"
        self.item_name = "Arrow"

class SpiderEye(Item):
    def __init__(self):
        super().__init__()
        self.item_id = "item:spider_eye"
        self.item_name = "Spider Eye"

class IronIngot(Item):
    def __init__(self):
        super().__init__()
        self.item_id = "item:iron_ingot"
        self.item_name = "Iron Ingot"

class Coal(Item):
    def __init__(self):
        super().__init__()
        self.item_id = "item:coal"
        self.item_name = "Coal"

class Stick(Item):
    def __init__(self):
        super().__init__()
        self.item_id = "item:stick"
        self.item_name = "Stick"

class Feather(Item):
    def __init__(self):
        super().__init__()
        self.item_id = "item:feather"
        self.item_name = "Feather"

class Wool(Item):
    def __init__(self):
        super().__init__()
        self.item_id = "item:wool"
        self.item_name = "Wool"
