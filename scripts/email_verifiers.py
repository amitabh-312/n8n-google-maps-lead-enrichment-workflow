import os, httpx

_DEAD_PROVIDERS = set()
_UNVERIFIABLE_DOMAINS = set()
_GOOD = {"ok", "valid", "safe", "deliverable", "catch_all", "catch-all", "accept_all", "role_account", "risky"}
_BAD = {"invalid", "undeliverable", "disposable", "spamtrap", "bounce", "bad", "disabled"}
_UNKNOWN = {"unknown", "timeout", "greylisted", "unverifiable", "retry_later"}

def _get_provider_keys():
    raw = os.getenv("EMAIL_VERIFIER_API_KEYS") or os.getenv("EMAIL_VERIFIER_API_KEY") or ""
    pairs = []
    for item in raw.split(","):
        s = item.strip().strip("'\"")
        if not s or s.startswith("@"):
            continue
        prov, k = s.split(":", 1) if ":" in s else ("millionverifier", s)
        prov, k = prov.strip().lower(), k.strip()
        if prov == "emailverifier":
            prov = "millionverifier"
        if k and f"{prov}:{k}" not in _DEAD_PROVIDERS:
            pairs.append((prov, k))
    return pairs

_ENDPOINTS = {
    "reoon": ("https://emailverifier.reoon.com/api/v1/verify", lambda e, k: {"email": e, "key": k, "mode": "quick"}, "status"),
    "bouncify": ("https://api.bouncify.io/v1/verify", lambda e, k: {"apikey": k, "email": e}, "result"),
    "millionverifier": ("https://api.millionverifier.com/api/v3/", lambda e, k: {"api": k, "email": e, "timeout": 5}, "result"),
    "zerobounce": ("https://api.zerobounce.net/v2/validate", lambda e, k: {"api_key": k, "email": e}, "status"),
    "abstractapi": ("https://emailvalidation.abstractapi.com/v1/", lambda e, k: {"api_key": k, "email": e}, "deliverability"),
    "emailvalidation": ("https://api.emailvalidation.io/v1/info", lambda e, k: {"apikey": k, "email": e}, "state"),
    "emailable": ("https://api.emailable.com/v1/verify", lambda e, k: {"api_key": k, "email": e}, "state"),
    "kickbox": ("https://api.kickbox.com/v2/verify", lambda e, k: {"apikey": k, "email": e}, "result"),
    "bouncezero": ("https://api.bouncezero.com/v1/verify", lambda e, k: {"apikey": k, "email": e}, "status"),
}

async def verify_via_pool(email: str, client: httpx.AsyncClient):
    dom = email.split("@")[-1].lower().strip() if "@" in email else ""
    if dom in _UNVERIFIABLE_DOMAINS:
        return False
    for prov, key in _get_provider_keys():
        if prov not in _ENDPOINTS:
            continue
        u, p_fn, field = _ENDPOINTS[prov]
        try:
            r = await client.get(u, params=p_fn(email, key), timeout=6.0)
            if r.status_code == 200 and isinstance(r.json(), dict):
                d = r.json()
                val = str(d.get(field) or d.get("result") or d.get("status") or d.get("state") or "").strip().lower()
                if val in _GOOD:
                    return True
                if val in _BAD:
                    return False
                if val in _UNKNOWN and not d.get("error"):
                    _UNVERIFIABLE_DOMAINS.add(dom)
                    return False
            _DEAD_PROVIDERS.add(f"{prov}:{key}")
        except Exception:
            continue
    return None
