ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# List
ft_list[1] = "World!"

# Tuple
buffer = list(ft_tuple)
buffer[1] = "Brazil!"
ft_tuple = tuple(buffer)

# Set
ft_set.remove("tutu!")
ft_set.add("Rio de Janeiro!")

# Dict
ft_dict["Hello"] = "42Rio!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
