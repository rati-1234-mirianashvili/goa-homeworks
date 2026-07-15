my_tuple = (1, 2, 3, 4)

# Tuple უცვლელია, ამიტომ პირდაპირ ვერ დავამატებთ ელემენტს.
# ვაქცევთ list-ად, ვამატებთ ელემენტს და ისევ tuple-ად ვაქცევთ.

temp = list(my_tuple)
temp.append(5)

my_tuple = tuple(temp)

print(my_tuple)