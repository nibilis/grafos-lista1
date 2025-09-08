from src.models2.directed_list_graph import DirectedListGraph

def test_directed_list_graph():
    g = DirectedListGraph(4)

    g.insert_a(0,1)
    g.insert_a(0,2)
    g.insert_a(2,1)
    g.insert_a(2,3)

    print("É completo?", g.is_complete()) # False

    g2 = DirectedListGraph(3)

    g2.insert_a(0,1)
    g2.insert_a(0,2)
    g2.insert_a(1,0)
    g2.insert_a(1,2)
    g2.insert_a(2,0)
    g2.insert_a(2,1)
   
    print("É completo?", g2.is_complete()) # True



if __name__ == "__main__":
    test_directed_list_graph()