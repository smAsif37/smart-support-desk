# Demo video script (about 7 minutes)

| Time | Show | Say |
|---|---|---|
| 0:00 | Title slide / live URL | Team, domain, problem in one sentence |
| 0:30 | Architecture diagram (README) | UI -> API -> 3 models + RAG; 5 sub-tasks |
| 1:15 | Colab training screenshot + metrics tables | Dataset, DistilBERT, results, **why 99% on synthetic data is suspicious**, what you did (dedupe, OTHER class, noisy data, messy test set, zero-shot baseline) |
| 2:30 | App -> sample "Angry refund complaint" | Category, sentiment, priority reasons, PII redaction, empathetic drafted reply with sources |
| 3:30 | "Possible fraud" ticket | Security keyword forces High priority |
| 4:00 | "Out-of-scope" ticket | OTHER category -> routed to human, no hallucinated reply |
| 4:30 | Chatbot: question, follow-up ("and for COD?"), then out-of-scope question | Sources with page numbers; memory works; "I could not find this" |
| 5:45 | RAG eval table + `/docs` page + GitHub/CI | Hit@4, rejection rate, tests |
| 6:30 | Situated Learning summary | Workplace, measured results, risks, ONE improvement chosen |
