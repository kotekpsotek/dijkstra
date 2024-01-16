# Possibilities
    # 1. Chociebuż (5) -> Zielona Góra (5) -> Leszno (4) -> Kalisz (3) -> Warszawa (14) = 31
    # 2. Chociebuż (5) -> Zielona Góra (5) -> Leszno (4) -> Konin (5) -> Warszawa (12) = 31
    # 3. Chociebuż (5) -> Zielona Góra (5) -> Poznań (5) -> Konin (4) -> Warszawa (12) = 31
    # 4. Frankfurt nad Odrą (2) -> Zielona Góra (4) -> Leszno (4) -> Kalisz (3) -> Warszawa (14) = 27
    # 5. Frankfurt nad Odrą (2) -> Zielona Góra (4) -> Poznań (5) -> Konin (4) -> Warszawa (12) = 27
    # 6. Frankfurt nad Odrą (2) -> Zielona Góra (4) -> Leszno (4) -> Konin (5) -> Warszawa (12) = 27
distances = {
    'Berlin': { 'Chociebuż': 5, 'Frankfurt nad Odrą': 2 },
    'Chociebuż': { 'Zielona Góra': 5 },
    'Frankfurt nad Odrą': { 'Zielona Góra': 4 },
    'Zielona Góra': { 'Leszno': 4, 'Poznań': 5 },
    'Leszno': { 'Kalisz': 3, 'Konin': 5 },
    'Poznań': { 'Konin': 4 },
    'Kalisz': { 'Warszawa': 14 },
    'Konin': { 'Warszawa': 12 }
}
source = "Berlin"
destination = "Warszawa"

def dijkstra(distances: dict[str, dict[str, int]]):
    # All rely on find the shortest path from current point to source
    route: list[tuple[int, str]] = []
    c_point = source

    # When multiple routes has same distance will be returning first the shortest
    while c_point != destination:
        pv = (None, "")
        for key in distances[c_point].keys():
            val = distances[c_point][key]
            if not pv[0] or pv[0] > val:
                pv = (val, key)

        c_point = pv[1]
        route.append(pv)

    return route

if __name__ == "__main__":
    route = dijkstra(distances)

    path = ""
    distance = 0
    for int in range(0, len(route)):
        # Determine path
        path_point = route[int][1]
        if len(path) == 0:
            path = path_point
        else:
            path = f"{path} -> {path_point}"

        # Determine distance
        distance += route[int][0]

    print("Your destination route")
    print(path)
    print(f"Distance is {distance}")