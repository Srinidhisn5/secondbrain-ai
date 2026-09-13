# Requirements & Costs

Kept separate from `README.md` on purpose — the README describes the product, this describes what it costs to run.

| Service | Free tier | Notes |
|---|---|---|
| Google Drive | 15GB free storage | Screenshots + copies count against this; monitor if you're a heavy screenshotter |
| Google Sheets | Free, no meaningful limit for this use case | |
| Google Cloud Vision API (OCR) | 1,000 units/month free | Each screenshot = 1 unit. Beyond that, ~$1.50 per 1,000 units |
| Ollama (local vision model) | Free, unlimited | Requires a machine that can run a vision model reasonably (8GB+ RAM recommended for smaller models like `llava`) |
| Cloud vision API alternative (e.g. Gemini) | Has a free tier | Check current limits before relying on it — free tier terms change |
| n8n (self-hosted) | Free, unlimited executions | Requires you to host it — a spare machine, a free-tier cloud VM (e.g. Oracle Cloud's always-free tier), or your own laptop running in the background |
| n8n Cloud (alternative to self-hosting) | Paid, ~$20/month | Only needed if you don't want to self-host |
| Tasker (Android, optional) | Paid, one-time ~₹250 | Only needed if Drive's built-in auto-backup isn't flexible enough for your trigger needs |

**Bottom line:** the entire V1 can run at $0/month if self-hosted with Ollama and kept within Drive/Vision API free tiers, which is comfortably enough for personal use (a few dozen screenshots a day).
