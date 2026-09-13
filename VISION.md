# Vision

**SecondBrain AI** is a personal automation system that automatically captures, classifies, and organizes everything you save — starting with screenshots, and eventually PDFs, articles, and notes — so nothing you save gets lost in an unsearchable pile.

## The pitch (one sentence)
"An AI-powered system that automatically organizes everything I save, starting with my screenshots, so I can actually find and use what I capture instead of losing it in a folder of 2,000 unsorted images."

## Why screenshots first
Everyone has a chaotic screenshot folder. It's the most relatable entry point, it's genuinely useful day-to-day, and it forces the core infrastructure (ingestion → classification → safe handling of sensitive content → storage → retrieval) to exist — which is the same infrastructure every future module (PDFs, notes, etc.) will reuse.

## Design principles
1. **Privacy first.** Anything that looks sensitive (OTPs, card numbers, PINs) is filtered out with local, deterministic logic before it ever reaches an AI API — no exceptions, no "just this once."
2. **Honesty over confidence.** The system reports a confidence score and routes uncertain classifications to a review queue instead of silently guessing.
3. **Ship the smallest real version first.** Every module starts as the smallest useful loop, gets evaluated with real numbers, then grows — never the other way around.
4. **Closed categories over open-ended labels.** Predictability and reliability over cleverness.

## Where this goes (directional, not committed)
Module 1 (Screenshots) → Module 2 (Search) → Module 3 (Weekly digest) → Module 4+ (other input types: PDFs, notes, saved articles) — all writing into the same underlying metadata store, eventually queryable as one system: "what have I saved and learned about X?"

Each module ships, gets used for real, and gets evaluated before the next one starts.
