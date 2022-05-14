from bike import *
import copy


bikes = [
	Bike("141 GX", Sram.gx, Shimano.none, Wheel.w29, Manufactuer.privateer, Price(4760)),
	Bike("Proccess 134", Sram.nx, Shimano.none, Wheel.w29, Manufactuer.kona, Price(3699)),
	Bike("Stumpjumper", Sram.none, Shimano.slx, Wheel.w29, Manufactuer.specialized, Price(3599)),
    Bike("141 ohlines", Sram.none, Shimano.slx, Wheel.w29, Manufactuer.privateer, Price(5806)),
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

def datasets(data, catagories):
    return list(map(lambda x: [vars(x).get(key).value for key in catagories], data))

def removed_labels(data):
    categories = list(vars(data[0]).keys())
    categories.remove("model")
    categories.remove("manufactuer")
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



