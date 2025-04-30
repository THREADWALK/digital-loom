# System Architecture 
Elara’s system integrates: 
- **X API (Tweepy)**: Monitors mentions and analyzes sentiment (`src/x_sentiment.py`). 
- **Helius API**: Tracks Solana token activity (`src/solana_token.py`). 
- **Emotion Engine**: Generates responses (`src/emotion_engine.py`, `src/community_response.py`). 
- **NFT Integration**: Memory NFTs (`config/nft_memory_001.json`). 
- **UI Portal**: Community interface (`ui/index.html`). 
