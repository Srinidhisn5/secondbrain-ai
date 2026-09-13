# Architecture — Node by Node

This document describes the current 27-node workflow exported as `n8n/workflow.json`.

## End-to-end flow

```text
Google Drive Trigger
        ↓
Download Screenshot
        ↓
Compute SHA256 Hash
        ↓
Check Duplicate Hash
        ↓
IF Duplicate Found
   ├── TRUE → Log Duplicate Skipped → END
   │
   └── FALSE
          ↓
   Prepare Image for OCR
          ↓
   Google Vision OCR
          ↓
   Extract OCR Text
          ↓
   Sensitive Filter Check
      ├── TRUE → Move to Sensitive Folder
      │              ↓
      │          Log Sensitive Filtered
      │              ↓
      │             END
      │
      └── FALSE
             ↓
      Vision AI Classification
             ↓
      Parse AI Response
             ↓
      IF Confidence >= 70
        ├── TRUE
        │     ↓
        │  Build Filename (Filed)
        │     ↓
        │  Find Category Folder
        │     ↓
        │  Copy to Category Folder
        │     ↓
        │  Log Metadata
        │
        └── FALSE
              ↓
        Build Filename (Review)
              ↓
        Copy to Needs Review Folder
              ↓
        Log Review Metadata

Processing failure
        ↓
Move to Processing Failed
        ↓
Log Processing Failed