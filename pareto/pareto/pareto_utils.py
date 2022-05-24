import copy

def names(data):
    return list(map(lambda x: str(x), data))

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

