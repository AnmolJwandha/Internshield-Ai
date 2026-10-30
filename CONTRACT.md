# InternShield AI: Output Contract

Agreed on Day 5. Do not change this alone. Both people must agree first.

## Rule for status
`status` is always one of: `good`, `warning`, `unknown`.
`unknown` means "could not check". It is never a scam sign.

## Person A: POST /analyze_text
Input: `text` (plus optional `email`, `website`)

```json
{
  "mechanisms": [
    {"mechanism": "urgency", "start": 41, "end": 56, "matched": "...", "why": "..."}
  ],
  "ml_score": 0.72,
  "ml_label": "High",
  "top_words": ["fee", "pay"],
  "emails": [],
  "urls": [],
  "phones": [],
  "amounts": [],
  "email_checks": [
    {"name": "free_email", "status": "warning", "detail": "..."}
  ]
}
```

## Person B: POST /analyze_web
Input: `text`, `website`, `company_name`

```json
{
  "ml_mechanisms": [
    {"mechanism": "payment_request", "prob": 0.81}
  ],
  "website_checks": [
    {"name": "https", "status": "good", "detail": "..."}
  ],
  "stipend": {"monthly_inr": 5000, "kind": "paid", "percentile": 40}
}
```

## The six mechanism names (exact spelling)
payment_request, urgency, guaranteed_placement, fake_certificate,
sensitive_document_request, off_platform_contact