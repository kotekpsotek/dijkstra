use std::collections::HashMap;

type Distance = HashMap<&'static str, Vec<(&'static str, u16)>>;

/** One of the simplest way -> even despite rust is fairly complicated language, dijkstra here is more cleaver than in a Python  */
fn dijkstra(dst: Distance) -> Vec<(String, u16)> {
    let mut path = Vec::<(String, u16)>::new();
    path.push((SOURCE.to_string(), 0));

    let mut current_point = SOURCE;
    while !path.iter_mut().any(|v| &v.0 == TARGET) {
        let current_opurtunities = dst.get(current_point)
            .unwrap();
        let shortest = current_opurtunities.iter().reduce(|acc, p| {
            if acc.1 > p.1 {
                p
            } else {
                acc
            }
        }).unwrap();
        path.push((shortest.0.to_string(), shortest.1));
        current_point = shortest.0;
    }

    path
}

const SOURCE: &str = "Berlin";
const TARGET: &str = "Warszawa";

fn main() {
    let mut distances = HashMap::new();

    distances.insert("Berlin", vec![("Chociebuż", 1), ("Frankfurt nad Odrą", 2)]);
    distances.insert("Chociebuż", vec![("Zielona Góra", 5)]);
    distances.insert("Frankfurt nad Odrą", vec![("Zielona Góra", 4)]);
    distances.insert("Zielona Góra", vec![("Leszno", 4), ("Poznań", 3)]);
    distances.insert("Leszno", vec![("Kalisz", 3), ("Konin", 5)]);
    distances.insert("Poznań", vec![("Konin", 4)]);
    distances.insert("Kalisz", vec![("Warszawa", 14)]);
    distances.insert("Konin", vec![("Warszawa", 12)]);

    let shortest_path = dijkstra(distances);
    println!("{shortest_path:?}");
}