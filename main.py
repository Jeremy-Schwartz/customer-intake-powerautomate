from fastapi import FastAPI, Header, HTTPException
from typing import Optional
import uuid

app = FastAPI()

@app.post("/v1/customers:upsert")
def upsert_customer(
    body: dict,
    idempotency_key: Optional[str] = Header(None, alias="Idempotency-Key")
):
    if not idempotency_key:
        raise HTTPException(status_code=400, detail="Missing Idempotency-Key")

    return {
        "crmRecordId": f"crm_{uuid.uuid4().hex[:8]}",
        "status": "upserted"
    }