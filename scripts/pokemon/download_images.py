import requests
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import json
import time

def download_image(card):
    try:
        set_id = card.get("set", {}).get("id", "unknown_set")
        card_dir = os.path.join("data/pokemon/images", set_id, card["id"])
        os.makedirs(card_dir, exist_ok=True)
        
        image_url = card.get("images", {}).get("large")
        if image_url:
            response = requests.get(image_url, stream=True, timeout=10)
            if response.status_code == 200:
                image_path = os.path.join(card_dir, "large.png")
                total_size = int(response.headers.get('content-length', 0))
                
                with open(image_path, "wb") as f, tqdm(
                    desc=f"{card['id']}".ljust(15),
                    total=total_size,
                    unit='B',
                    unit_scale=True,
                    leave=False
                ) as pbar:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                        pbar.update(len(chunk))
                
                card["local_images"] = {"large": image_path.replace("data/pokemon/", "")}
                
    except Exception as e:
        tqdm.write(f"Erro em {card['id']}: {str(e)}")
    
    return card

def process_images():
    with open("data/pokemon/cards.json", "r", encoding="utf-8") as f:
        cards = json.load(f)
    
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(tqdm(
            executor.map(download_image, cards),
            total=len(cards),
            desc="Progresso Geral",
            unit="cartas"
        ))
    
    with open("data/pokemon/cards.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n⏱️ Tempo total: {time.time() - start_time:.2f} segundos")

if __name__ == "__main__":
    process_images()