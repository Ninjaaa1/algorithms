from collections import deque

friends = {
    "Ja": ["Klaudia", "Natalia", "Mateusz", "Julia", "Jan"],
    "Klaudia": ["Natalia", "Marek", "Maciek"],
    "Mateusz": ["Krystyna", "Zosia", "Łukasz"],
    "Natalia": [],
    "Julia": [],
    "Jan": []
}

sellers = ["Julia", "Zosia"]

def is_seller(name):
    if name in sellers:
        return True

def search(name):
    queue = deque() 
    tuple(queue)
    queue += friends[name]
    searched = []
    while queue:
        person = queue.popleft()
        if not person in searched:
            if is_seller(person):
                print(f"{person} sells robots!")
                break
            else:
                queue.append(person)
                searched.append(person)
    return False

search("Ja")