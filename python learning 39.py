# *args
def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Md", "Mehadi", "Hassan")

# *kwargs
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_address(street = "123 Fake st.",
              apt= "100",
              city= "Dhaka",
              state= "Uttara",
              zip= "123435")

# *args and **kwargs
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

shipping_label("Md", "Mehadi", "Hassan",
               street="123 Fake st.",
               apt="100",
               city="Dhaka",
               state="Uttara",
               zip="123435"
               )
