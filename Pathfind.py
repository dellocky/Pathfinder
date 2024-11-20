from Set_Up import *


def neighbor_tile_calculator(coordinates) -> list:
        neighbors = [(coordinates[0] + 1, coordinates[1]),
            (coordinates[0] - 1, coordinates[1]),
            (coordinates[0], coordinates[1] + 1),
            (coordinates[0], coordinates[1] - 1)]
        return neighbors

def validate_neighbors(list, tile_list) -> list:

    new_list = []
    for neighbor in list:
        if neighbor[0] >= WIDTH or neighbor[0] < 0 or neighbor[1] >= HEIGHT or neighbor[1] < 0:
            continue
        for tile in tile_list:
            if tile.coordinate == neighbor and tile.is_obstacle is False and tile.is_searched is False:
                tile.is_searched = True
                tile.rgb = (100, 100 ,100)
                new_list.append(neighbor)
            #else: print(tile.coordinate)
                
    return new_list

def add(list, item) -> list:
    list.append(item)

def cascade(path_list, tiles) -> list:

    all_list = list()
    all_list.clear()
    for path in path_list:
        starting_point = path[-1]
        neighbor_list = validate_neighbors(neighbor_tile_calculator(starting_point), tiles)
        for tile in neighbor_list:
            current_list = (path[:])
            current_list.append(tile)
            all_list.append(current_list)

    return all_list



