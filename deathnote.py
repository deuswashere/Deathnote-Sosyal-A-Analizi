import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community
import community as community_louvain


# Sosyal ağı oluşturma
G = nx.Graph()

# Karakterler (düğümler)
characters = [
    "Light", "L", "Misa", "Near", "Mello", "Aizawa", "Matsuda", "Mogi", "Soichiro Yagami",
    "Kiyomi Takada", "Teru Mikami", "Ryuk", "Rem", "Sayu Yagami", "Sachiko Yagami", 
    "Watari", "Ide", "Raye Iwamatsu", "Naomi Misora"
]

# Karakterler arasındaki ilişkiler (kenarlar)
relationships = [
    #L ve light genel ilişkiler
    ("Light", "L", "düşman"),            # Light ve L karşıt
    ("Light", "Misa", "sevgili-yandaş"),         # Misa, Light'ı destekler
    ("L", "Near", "mentor-öğrenci"),     # L ve Near, karşıt
    ("L", "Mello", "mentor-öğrenci"),             # L ve Mello, rakip
    ("Light", "Near", "düşman"),          # Light ve Near, rakip      
    ("Light", "Mello", "düşman"),
    ("Near", "Mello", "yandaş"),
    ("Light", "Kiyomi Takada", "sevgili-yandaş"),
    ("Light", "Teru Mikami", "yandaş"),
    ("Light", "Ryuk", "ölüm meleği"),
    ("Misa", "Rem", "ölüm meleği"),
    ("Light", "Ryuk", "ölüm meleği"),
    ("Light", "Sayu Yagami", "abi-kardeş"),
    ("Light", "Sachiko Yagami", "anne-oğul"),
    ("Soichiro Yagami", "Sachiko Yagami", "karı-koca"),
    ("Soichiro Yagami", "Sayu Yagami", "baba-kız"),
    ("Light", "Soichiro Yagami", "baba-oğul"), # L ve Soichiro Yagami, işbirliği
    #L ekip arkadaşları
    ("L", "Aizawa", ""),
    ("L", "Matsuda", ""),
    ("L", "Mogi", ""),
    ("L", "Ide", ""),
    ("L", "Soichiro Yagami", ""),
    ("L", "Watari", ""),
    ("Aizawa", "Matsuda", ""),
    ("Aizawa", "Mogi", ""),
    ("Aizawa", "Ide", ""),
    ("Aizawa", "Soichiro Yagami", ""),
    ("Aizawa", "Watari", ""),
    ("Matsuda", "Mogi", ""),
    ("Matsuda", "Ide", ""),
    ("Matsuda", "Soichiro Yagami", ""),
    ("Matsuda", "Watari", ""),
    ("Mogi", "Ide", ""),
    ("Mogi", "Soichiro Yagami", ""),
    ("Mogi", "Watari", ""),
    ("Ide", "Soichiro Yagami", ""),
    ("Ide", "Watari", ""),
    ("Soichiro Yagami", "Watari", ""),
    #FBI ilişkileri
    ("Light", "Raye Iwamatsu", "düşman"),
    ("Light", "Naomi Misora", "düşman"),
    ("L", "Naomi Misora", "ortak bir işte çalışmışlar"),
    ("Raye Iwamatsu", "Naomi Misora", "sevgili"),
    
    
    
]

# Ağda karakterleri ekle
G.add_nodes_from(characters)

# İlişkileri (kenarları) ekle
for relation in relationships:
    G.add_edge(relation[0], relation[1], relationship=relation[2])

# Grafiği görselleştirme
pos = nx.spring_layout(G)  # Düzenleme yöntemi
plt.figure(figsize=(10, 8))

# Düğümleri ve kenarları çizme
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=3000, font_size=12, font_weight="bold", edge_color="gray")
edge_labels = nx.get_edge_attributes(G, 'relationship')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Derece dağılımlarını hesaplama
degree_distribution = [degree for node, degree in G.degree()]

# Derece dağılımlarını görselleştirme
plt.figure(figsize=(10, 6))
plt.bar(range(len(degree_distribution)), degree_distribution, tick_label=list(G.nodes()))
plt.title("Derece Dağılımı")
plt.xlabel("Düğüm")
plt.ylabel("Derece (Bağlantı Sayısı)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Derece merkeziyeti (Degree Centrality)
degree_centrality = nx.degree_centrality(G)

# Yakınlık merkeziyeti (Closeness Centrality)
closeness_centrality = nx.closeness_centrality(G)

# Arasındaki merkeziyeti (Betweenness Centrality)
betweenness_centrality = nx.betweenness_centrality(G)

# Çıktıları yazdırma
print("Derece Merkeziyeti:")
for node, centrality in degree_centrality.items():
    print(f"{node}: {centrality:.4f}")

print("\nYakınlık merkeziyeti (Closeness Centrality):")
for node, centrality in closeness_centrality.items():
    print(f"{node}: {centrality:.4f}")

print("\nArasındaki merkeziyeti (Betweenness Centrality):")
for node, centrality in betweenness_centrality.items():
    print(f"{node}: {centrality:.4f}")

# Ağın ortalama yol uzunluğunu hesapla
average_path_length = nx.average_shortest_path_length(G)

# Kümeleme katsayısını hesapla
clustering_coefficient = nx.average_clustering(G)

# Sonuçları yazdırma
print(f"Ortalama Yol Uzunluğu: {average_path_length}")
print(f"Kümeleme Katsayısı: {clustering_coefficient}")

# K-core'ları hesaplama (k=2 örneği için)
k = 3
k_core_subgraph = nx.k_core(G, k)

# k-core'u görselleştirme
pos = nx.spring_layout(k_core_subgraph)
plt.figure(figsize=(10, 8))
nx.draw(k_core_subgraph, pos, with_labels=True, node_color="lightgreen", node_size=3000, font_size=12, font_weight="bold", edge_color="gray")
plt.title(f"{k}-Core Alt Ağı")
plt.show()

# k-core alt ağındaki düğümleri yazdırma
print("Core Alt Ağı'ndaki Düğümler:")
print(k_core_subgraph.nodes())

# Louvain yöntemi ile toplulukları bulma
partition = community_louvain.best_partition(G)

# Toplulukları görselleştirme için renkler
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 8))
color_map = []

# Her düğümü topluluğa göre renklendirme
for node in G.nodes():
    color_map.append(partition[node])

# Toplulukları çizme
nx.draw(G, pos, with_labels=True, node_size=3000, node_color=color_map, cmap=plt.cm.tab20, font_size=10, font_weight="bold")
plt.title("Louvain Yöntemi ile Topluluk Tespiti")
plt.show()

# Toplulukların detaylı çıktısı
topluluklar = {}
for node, comm_id in partition.items():
    if comm_id not in topluluklar:
        topluluklar[comm_id] = []
    topluluklar[comm_id].append(node)

print("Topluluklar:")
for comm_id, nodes in topluluklar.items():
    print(f"Topluluk {comm_id}: {nodes}")

# PageRank hesaplama
pagerank_scores = nx.pagerank(G)

# Sonuçları yazdırma
print("PageRank Değerleri:")
for node, score in pagerank_scores.items():
    print(f"{node}: {score:.4f}")


#SimRank her kişiye özel
def compute_simrank(graph, C=0.8, max_iter=100, eps=1e-4):
    nodes = list(graph.nodes())
    sim = {n: {m: (1.0 if n == m else 0.0) for m in nodes} for n in nodes}
    for _ in range(max_iter):
        prev_sim = {n: sim[n].copy() for n in nodes}
        for a in nodes:
            for b in nodes:
                if a == b:
                    continue
                a_neighbors = set(graph.neighbors(a))
                b_neighbors = set(graph.neighbors(b))
                if a_neighbors and b_neighbors:
                    sim[a][b] = C * sum(prev_sim[an][bn] for an in a_neighbors for bn in b_neighbors) / (
                        len(a_neighbors) * len(b_neighbors)
                    )
        if all(
            abs(sim[a][b] - prev_sim[a][b]) < eps
            for a in nodes
            for b in nodes
            if a != b
        ):
            break
    return sim

# SimRank hesaplama
simrank_scores = compute_simrank(G)

# Örnek çıktı
print("SimRank Benzerlikleri:")
for node, similarities in simrank_scores.items():
    print(f"{node}: {similarities}")



