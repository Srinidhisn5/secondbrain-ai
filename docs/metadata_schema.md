# Metadata Schema — Google Sheets

The current Screenshot Registry used by V1 has **five columns**, in this order:

| Column | Type | Purpose | Example |
|---|---|---|---|
| `sha256_hash` | string | Content hash used for duplicate detection | `e039e3ac0c70...` |
| `filename` | string | Filename associated with the processing result | `Finance_2026-09-13_multibagger.png` |
| `category` | string | Classification or workflow status | `Finance` |
| `tags` | string | Comma-separated AI-generated tags | `stocks,investment,market` |
| `processed_at` | datetime/string | Processing timestamp | `2026-09-13T...` |

The spreadsheet tab used by the current workflow is `Sheet1`.

## Category values

Normal AI classifications use the closed set:

```text
LinkedIn
Tech
Finance
Shopping
Travel
Documents
Other