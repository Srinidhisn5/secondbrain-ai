# Evaluation Dataset

Before pointing this workflow at your live Screenshot Inbox, build a labeled test set and measure real accuracy. "It uses AI" is not a result. "94% accuracy on 100 labeled screenshots" is.

## Target composition (100 screenshots)

| Category | Count |
|---|---|
| LinkedIn | 15 |
| Finance | 15 |
| Tech | 20 |
| Shopping | 10 |
| Travel | 10 |
| Documents | 10 |
| Sensitive/OTP (use fake/dummy OTPs, never real ones) | 10 |
| Memes/Other | 10 |

## How to build it
1. Screenshot real content you'd naturally capture (LinkedIn posts, terminal output, AWS console, receipts, boarding passes, etc.)
2. For the "Sensitive" category, **generate fake OTP screenshots** (mock up a message with a random 6-digit code and words like "OTP", "verification code") — never use real ones for testing.
3. Save each into `dataset/sample_screenshots/` with a filename prefix matching its true label, e.g. `tech_001.png`, `finance_002.png`, `sensitive_001.png`. This prefix is your ground truth for scoring.
4. Keep a `labels.csv` alongside it: `filename,true_category,is_sensitive`

## Running the evaluation
1. Manually upload the 100 test images to your Screenshot Inbox (in batches, so you don't hit rate limits) — or run them through the workflow in a test environment separate from your live inbox.
2. Let the workflow process all of them.
3. Pull the resulting Google Sheet and compare `category` (predicted) against `true_category` (from `labels.csv`) for each `sha256_hash`/filename match.
4. Compute:
   - **Overall accuracy** = correct classifications / 100
   - **Sensitive detection rate** = correctly flagged sensitive / total actual sensitive (this one matters most — false negatives here are the real risk)
   - **False sensitive-positive rate** = non-sensitive items wrongly flagged as sensitive (annoying but safe — better to err this direction than the reverse)
   - **Needs Review rate** = % routed to review (a healthy system: not 0%, not 50%)

## Report format (use this in your README/LinkedIn post)
```
Tested on: 100 labeled screenshots
Correct classification: 94/100 (94%)
Sensitive detection: 10/10 caught (100%)
False sensitive-positives: 1/90 (1.1%)
Duplicates correctly skipped: 8/8 (tested by re-uploading 8 originals)
Needs Review rate: 6%
```

Only after these numbers look solid should the workflow be pointed at your real, live Screenshot Inbox folder.
