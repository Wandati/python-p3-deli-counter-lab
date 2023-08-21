katz_deli = []
def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        index = 1
        for name in katz_deli:
            print(f"The line is currently: {index}. {name}")
            index += 1

def take_a_number(katz_deli,name):
    if name:
        katz_deli.append(name)
    # number = index
    print(f"Welcome, {name}. You are number {katz_deli.index(name) + 1} in line.")
        
take_a_number(katz_deli,"Ada")
take_a_number(katz_deli,"Grace")
take_a_number(katz_deli,"Kent")

print(katz_deli)
print(katz_deli[0])
def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}")
        katz_deli.remove(katz_deli[0])
    
