import json
import pandas as pd
from tqdm import tqdm
import time

def extract_key_metadata():
    with open("data/pokemon/cards.json", "r", encoding="utf-8") as f:
        cards = json.load(f)
    
    metadata = []
    start_time = time.time()
    
    for card in tqdm(cards, desc="Processando metadados", unit="cartas"):
        metadata.append({
            "id": card.get("id"),
            "name": card.get("name"),
            "set_id": card.get("set", {}).get("id"),
            "rarity": card.get("rarity"),
            "market_price": card.get("cardmarket", {}).get("prices", {}).get("averageSellPrice"),
            "local_image": card.get("local_images", {}).get("large")
        })
    
    df = pd.DataFrame(metadata)
    
    with tqdm(total=2, desc="Salvando arquivos") as pbar:
        df.to_csv("data/pokemon/metadata.csv", index=False)
        pbar.update(1)
        df.to_json("data/pokemon/metadata.json", orient="records", indent=2)
        pbar.update(1)
    
    print(f"\n⏱️ Tempo total: {time.time() - start_time:.2f} segundos")

if __name__ == "__main__":
    extract_key_metadata()