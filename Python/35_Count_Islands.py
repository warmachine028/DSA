from rich import print

LAND, WATER = "1", "0"


def mark_island_as_visited(area: list[list[str]], x: int, y: int) -> None:  # Applying Depth First Search Algorithm
    area[x][y] = WATER  # Marking as visited
    directions = {"left": (x - 1, y),
                  "right": (x + 1, y),
                  "top": (x, y + 1),
                  "bottom": (x, y - 1)}
    for direction in directions:
        i, j = directions[direction]
        if -1 < i < len(area) and -1 < j < len(area[i]):
            if area[i][j] == WATER: continue
            mark_island_as_visited(area, i, j)


def count_island(area: list[list[str]]) -> int:
    islands = 0
    for x in range(len(area)):
        for y in range(len(area[x])):
            if area[x][y] == WATER: continue
            mark_island_as_visited(area, x, y)
            islands += 1
    return islands


Area = [["1", "1", "0", "0"],
        ["1", "1", "0", "0"],
        ["0", "0", "1", "0"],
        ["0", "0", "0", "1"],
        ["1", "1", "1", "0"]]
print(count_island(Area))  # 4

Area = [["1", "1", "1", "1", "0", "0", "1", "1"],
        ["1", "1", "1", "0", "0", "1", "0", "1"],
        ["1", "1", "0", "1", "0", "1", "0", "1"],
        ["1", "0", "0", "0", "1", "0", "1", "1"],
        ["1", "0", "0", "1", "1", "0", "1", "1"],
        ["1", "0", "0", "1", "1", "0", "1", "1"]]
print(f"[bold red if '0' else blue]{Area}[/]")
print(count_island(Area))  # 3
