def runTests(func):
    matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    result = func(matrix)
    print(f"Result: {result}")

def Solution(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    expected_set = set(range(1, n + 1))
    
    for row in matrix:
        if set(row) != expected_set:
            return False
                
    for col in range(n):
        column_set = {matrix[row][col] for row in range(n)}
        if column_set != expected_set:
            return False
        
    return True            
    
runTests(Solution)