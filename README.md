# TCG-AI

**TCG-AI** é um sistema de inteligência artificial para reconhecimento e classificação de cartas de Trading Card Games (TCGs). Começando com Pokémon TCG, o projeto visa expandir para outros jogos como Magic: The Gathering e Yu-Gi-Oh!.

---

## Funcionalidades
- **Reconhecimento de Cartas:** Identifica cartas a partir de imagens enviadas pelo usuário.  
- **Detecção de Variações:** Reconhece edições, raridades e versões especiais (foil, reverse holo).  
- **Integração com APIs:** Busca metadados e preços em tempo real.  
- **Automação:** Respostas automáticas via WhatsApp, Discord e outros canais.  

---

## Tecnologias
- **Linguagem:** Python  
- **IA/ML:** PyTorch, Transformers, OpenCV  
- **Automação:** n8n  
- **Armazenamento:** MinIO, Redis  
- **LLMs Locais:** Ollama (Mistral, Phi-3)  

---

## Como Usar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/TCG-AI.git
   cd TCG-AI
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Baixe o dataset inicial:
   ```bash
   python scripts/fetch_cards.py
   ```
4. Treine o modelo:
   ```bash
   python scripts/train_model.py
   ```
5. Execute o sistema:
   ```bash
   python scripts/classify_card.py
   ```

---

## Roadmap
- **Fase 1 (MVP):** Reconhecimento de cartas de Pokémon TCG.  
- **Fase 2:** Expansão para Magic: The Gathering e Yu-Gi-Oh!.  
- **Fase 3:** Detecção de foil, reverse holo e outras variações.  
- **Fase 4:** Integração com marketplaces e monetização.  

---

## Contribuição
Contribuições são bem-vindas! Siga os passos abaixo:
1. Faça um fork do repositório.  
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).  
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).  
4. Faça push para a branch (`git push origin feature/nova-feature`).  
5. Abra um Pull Request.  

---

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).