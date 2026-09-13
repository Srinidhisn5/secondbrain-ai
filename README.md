# SecondBrain AI — Screenshot Agent (V1)

SecondBrain AI is a personal automation system that starts by automatically organizing screenshots. V1 watches a Google Drive inbox, detects duplicates, extracts OCR text, filters potentially sensitive content before AI classification, classifies safe screenshots with a local vision model, routes uncertain items to review, and records processing metadata in Google Sheets.

This is Module 1 of the broader SecondBrain AI vision. See [`VISION.md`](./VISION.md) and [`ROADMAP.md`](./ROADMAP.md).

## What V1 does

```text
Google Drive — Screenshot Inbox
            ↓
      n8n Drive Trigger
            ↓
       Download image
            ↓
       SHA256 hash
            ↓
    Duplicate lookup in Sheets
       ↙           ↘
 duplicate          new
    ↓                ↓
 log + stop      Prepare image
                     ↓
             Google Vision OCR
                     ↓
          Local sensitive filter
             ↙             ↘
       sensitive           safe
          ↓                 ↓
   Sensitive folder     Ollama + LLaVA
   + log + stop              ↓
                       Parse AI JSON
                            ↓
                    Confidence >= 70?
                     ↙            ↘
                  filed        needs review
                    ↓              ↓
              category folder   Needs Review
                     ↘            ↙
                  Google Sheets
                     registry
