
 
def roll_call_dwarves(dwarves):
   index = 0
   for x in dwarves:
       index += 1
       print(f"{index}. {x}")

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]

def summon_captain_planet(planeteer_calls):
    exclaim = [element.capitalize() + "!" for element in planeteer_calls]
    return exclaim


def long_planeteer_calls(calls):
    for call  in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(food):
    if "cheddar" in food:
        return "cheddar"
    elif "gouda" in food:
        return "gouda"
    elif "camembert" in food:
        return "camembert"
    else:
        return None
