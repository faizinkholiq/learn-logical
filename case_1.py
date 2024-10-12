def runTests(func):
    paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    result = func(paths)
    print(f"Result: {result}")

def Solution(paths: list[list[str]]) -> str:
    starting_cities = set()
    destination_cities = set()
    
    for a, b in paths:
        starting_cities.add(a)
        destination_cities.add(b)
    
    return [b for b in destination_cities if b not in starting_cities][0]
    
runTests(Solution)