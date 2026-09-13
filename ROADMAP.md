# Roadmap

Everything below is a candidate for after V1 has been evaluated. The current goal is to prove the smallest useful screenshot-organizing loop before adding more modules.

## V1 — Current Scope

- Google Drive screenshot ingestion
- SHA256 duplicate detection
- Google Vision OCR
- Deterministic sensitive-content filtering
- Local Ollama + LLaVA image classification
- Closed category set
- Confidence-based routing
- Automatic category filing
- Needs Review queue
- Sensitive folder routing
- Processing Failed routing
- Google Sheets registry
- Evaluation with real screenshots

## V1 Hardening Candidates

- Preserve the source file extension when generating renamed filenames
- Improve sensitive detection for visual-only sensitive content
- Add explicit/manual retry handling with a real retry counter
- Persist useful AI metadata such as confidence and classification reason
- Improve error reporting and observability
- Measure classification accuracy and false-sensitive rate on a labeled dataset

## V2 Candidates

- Smart search across the metadata registry
- Weekly digest of saved screenshots
- Telegram bot interface
- Better metadata and filtering

## V3+ Candidates

- PDF ingestion
- YouTube transcript ingestion
- Voice note ingestion
- Web page/article saving
- Metrics dashboard
- Config-driven category list
- Additional input modules using the same ingestion/classification/storage architecture

## Explicitly Not Planned for the Near Term

- Knowledge graph
- Vector database / RAG
- LangChain / multi-agent architecture
- Database replacement before the V1 workflow proves its value

Each module should ship, be used with real data, and be evaluated before the next major module begins.