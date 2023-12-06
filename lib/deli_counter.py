def line(katz_deli):
    if not katz_deli:
        return "The line is currently empty."
    else:
        line_str = "The line is currently: "
        for i, customer in enumerate(katz_deli):
            line_str += f"{i + 1}. {customer} "
        return line_str.strip()

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if katz_deli:
        serving_person = katz_deli.pop(0)
        print(f"Currently serving {serving_person}.")
    else:
        print("There is nobody waiting to be served!")