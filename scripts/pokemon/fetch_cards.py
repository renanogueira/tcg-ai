from pokemontcgsdk import Card
from pokemontcgsdk import RestClient
import json
import os
import time
from tqdm import tqdm


RestClient.configure('41e35230-ad8f-490e-9044-d92ef5e244c3')

# def fetch_all_pokemon_cards():
#     cards = []    
    
#     try:
#         cards = Card.all()            
#     except Exception as e:
#         print(f"Erro fatal: {str(e)}")
    
#     return cards

# def fetch_all_pokemon_cards():
#     all_cards = []
#     page = 1
#     max_retries = 3  # Número máximo de tentativas por requisição
#     progress_bar = tqdm(desc="Buscando cartas", unit="páginas")
    
#     try:
#         while True:
#             for attempt in range(max_retries):
#                 try:
#                     # Busca paginada (100 cartas por página)
#                     cards = Card.where(page=page, pageSize=100)
#                     break
#                 except Exception as e:
#                     if attempt < max_retries - 1:
#                         tqdm.write(f"Erro na página {page}. Tentando novamente em 5 segundos...")
#                         time.sleep(5)
#                     else:
#                         raise e
            
#             if not cards:
#                 break  # Sai do loop quando não há mais cartas
                
#             all_cards.extend([card.__dict__ for card in cards])
#             progress_bar.update(1)
#             page += 1
            
#     except Exception as e:
#         tqdm.write(f"Erro fatal: {str(e)}")
#     finally:
#         progress_bar.close()

#     return all_cards

def fetch_pokemon_cards(max_pages=1):  # Novo parâmetro para limitar páginas
    all_cards = []
    page = 1
    max_retries = 3
    progress_bar = tqdm(desc="Buscando cartas (Modo Teste)", total=max_pages, unit="página")

    try:
        while page <= max_pages:  # Condição alterada
            for attempt in range(max_retries):
                try:
                    cards = Card.where(page=page, pageSize=100)
                    break
                except Exception as e:
                    if attempt < max_retries - 1:
                        tqdm.write(f"Erro na página {page}. Tentando novamente em 5 segundos...")
                        time.sleep(5)
                    else:
                        raise e

            all_cards.extend([card for card in cards])
            progress_bar.update(1)
            page += 1

    except Exception as e:
        tqdm.write(f"Erro fatal: {str(e)}")
    finally:
        progress_bar.close()

    return all_cards


def save_cards_to_json(cards, directory="data/pokemon"):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, "cards.json")
    
    with tqdm(total=1, desc="Salvando dados") as pbar:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(cards, f, indent=2, ensure_ascii=False)
        pbar.update(1)
    
    print(f"\n✅ Total de cartas salvas: {len(cards)}")
    print(f"📁 Arquivo: {file_path}")


if __name__ == "__main__":
    start_time = time.time()
    cards = fetch_pokemon_cards()
    save_cards_to_json(cards)
    print(f"\n⏱️ Tempo total: {time.time() - start_time:.2f} segundos")