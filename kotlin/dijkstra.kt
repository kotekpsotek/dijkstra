val SOURCE = "Berlin"
val DESTINATION = "Warszawa";

/*
    * Wow. Clearance and clear, makes from Kotlin the clearest manner to produce dijkstra algorithm
*/
fun dijkstra(distances: Map<String, Map<String, Int>?>): MutableList<Pair<String, Int>> {
    val path = mutableListOf<Pair<String, Int>>(SOURCE to 0)

    var currentPoint = SOURCE
    while (currentPoint != DESTINATION) {
        val currentOpportunities = distances.get(currentPoint)
        
        if (currentOpportunities != null) {
            var previousIteartion = "" to 0
            currentOpportunities.forEach { entrie ->
                if ((previousIteartion.second == 0 && previousIteartion.first == "") || previousIteartion.second > entrie.value) previousIteartion = entrie.key to entrie.value;  
            }
    
            currentPoint = previousIteartion.first;
            path.add(previousIteartion)
        }
    }

    return path
}

fun main() {
    val distances = mapOf(
        "Berlin" to mapOf("Chociebuż" to 5, "Frankfurt nad Odrą" to 2),
        "Chociebuż" to mapOf("Zielona Góra" to 5),
        "Frankfurt nad Odrą" to mapOf("Zielona Góra" to 4),
        "Zielona Góra" to mapOf("Leszno" to 4, "Poznań" to 5),
        "Leszno" to mapOf("Kalisz" to 3, "Konin" to 5),
        "Poznań" to mapOf("Konin" to 4),
        "Kalisz" to mapOf("Warszawa" to 14),
        "Konic" to mapOf("Warszawa" to 12),
        "Warszawa" to null
    );

    val path = dijkstra(distances);
    print("${path}")
}