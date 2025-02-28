from qdrant_client import QdrantClient, models # type: ignore

def create_collection(collection_name="solgar_collection"):
    """Best practice yapısına göre Qdrant koleksiyon oluşturma"""
    try:
        client = QdrantClient(url="http://10.150.98.217:30333")

        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=384,  # MiniLM-L6-v2 modeline göre vektör boyutu
                distance=models.Distance.COSINE  # Metin verisi için en iyi mesafe fonksiyonu
            ),
            hnsw_config=models.HnswConfigDiff(
                m=16, # Maksimum bağlantı sayısı: Her bir noktada HNSW grafında tutulacak maksimum komşu (bağlantı) sayısını belirler. Daha yüksek bir değer, daha fazla bellek kullanır ama sorgu performansı artabilir.
                ef_construct=100, # İndeks oluşturulurken her bir noktaya en yakın komşuları bulmak için kullanılan aday kümenin boyutunu tanımlar. Daha yüksek değer, daha iyi indeks kalitesi sağlar ama indeksleme süresi ve bellek kullanımı artar.
                full_scan_threshold=10000 # Tam tarama eşiği: Eğer koleksiyondaki vektör sayısı bu eşiğin altındaysa, HNSW yerine tam tarama (full scan) yapılır. Bu, küçük veri setlerinde performansı optimize etmek için kullanılır.
            ),
            optimizers_config=models.OptimizersConfigDiff(
                memmap_threshold=10000
            )
        )
        
        print(f"Koleksiyon '{collection_name}' başarıyla oluşturuldu.")

    except Exception as e:
        print("Koleksiyon oluşturma başarısız! Hata:", str(e))

# Test için çalıştır
if __name__ == "__main__":
    create_collection()