import matplotlib.pyplot as plt


def step(urbrask_size, ooze_count, hp):
    ooze_size = 8
    urbrask_size += 1
    ooze_count += 1
    hp -= max(urbrask_size - ooze_count * ooze_size, 0)
    ooze_count -= int(urbrask_size / ooze_size)
    return urbrask_size, ooze_count, hp


turns = 24
urbrask_size = 0
ooze_count = 0
hp = 20

ooze_array = []
urbrask_array = []
hp_array = []

for i in range(1, turns):
    urbrask_size, ooze_count, hp = step(urbrask_size, ooze_count, hp)
    urbrask_array.append(urbrask_size)
    ooze_array.append(ooze_count)
    hp_array.append(hp)

plt.plot(urbrask_array, color="red", label="Urbrask")
plt.plot(ooze_array, color="green", label="Oozes")
plt.plot(hp_array, color="pink", label="Health")

plt.xlabel("Turns")
plt.ylabel("Damage")
plt.title("Consuming Ooze vs. Urabrask's Forge")

plt.legend()
plt.show()
