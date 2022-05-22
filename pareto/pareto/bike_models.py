from bike import *
import copy


bikes = [
	Bike("141 GX", Sram.gx, Shimano.none, Wheel.w29, Manufactuer.privateer, 4760.0),
	Bike("Proccess 134", Sram.nx, Shimano.none, Wheel.w29, Manufactuer.kona, 3699.0),
	Bike("Stumpjumper", Sram.none, Shimano.slx, Wheel.w29, Manufactuer.specialized, 3599.0),
    Bike("141 ohlines", Sram.none, Shimano.slx, Wheel.w29, Manufactuer.privateer, 5806.0),
]


#class resists():
#    def __init__(self, value):
#        self.value = value
    
#    def value():
#        return self.value 

#@dataclass
#class Gear:
#    model: str
#    fire: resists 
#    ice: resists
#    dex: resists
#    i: resists
    
#    def __sub__(self, other):
#        return str(self) + str(other)

#bikes = [
#        Gear("Fire Mage", resists(4), resists(-1), resists(0), resists(1)),
#        Gear("Ice Mage", resists(-1), resists(4), resists(0), resists(1)),
#        Gear("Arch Mage", resists(1), resists(1), resists(0), resists(10)),
#        Gear("Hedge", resists(2), resists(2), resists(2), resists(2))
#]

def model_names(data):
    return list(map(lambda x: x.model, data))

def get_value(x):
    if hasattr(x, "value"):
        return x.value
    return x

def datasets(data, catagories):
    return list(map(lambda x: [get_value(vars(x).get(key)) for key in catagories], data))

def removed_labels(data):
    categories = list(vars(data[0]).keys())
    for c in categories:
        if type(c) == str:
            categories.remove(c)
    return categories

def vector_mod_catagories(categories):
    return list(map(lambda x: 0, categories))

def all_data(data):
    all_data = []
    for n in data:
        all_data.append([])
        for o in data:
            all_data[-1].append(str(o-n))
    return all_data


def dataset_with_names(data, names):
    dataset = copy.deepcopy(data)
    for i, e in enumerate(dataset):
        dataset[i].insert(0, names[i])
    return dataset

