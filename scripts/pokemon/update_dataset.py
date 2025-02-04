from fetch_cards import fetch_all_pokemon_cards, save_cards_to_json
from download_images import process_images
from process_metadata import extract_key_metadata
from tqdm import tqdm
import time

def main():
    start_time = time.time()
    
    with tqdm(total=3, desc="Progresso Total") as main_pbar:
        # Passo 1: Buscar novas cartas
        cards = fetch_all_pokemon_cards()
        save_cards_to_json(cards)
        main_pbar.update(1)
        
        # Passo 2: Baixar imagens
        process_images()
        main_pbar.update(1)
        
        # Passo 3: Processar metadados
        extract_key_metadata()
        main_pbar.update(1)
    
    print(f"\n🚀 Atualização concluída em {time.time() - start_time:.2f} segundos")

if __name__ == "__main__":
    main()