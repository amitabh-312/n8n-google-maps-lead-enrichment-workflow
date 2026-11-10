import httpx

async def lookup_npi_official(company: str, city_state: str, client: httpx.AsyncClient) -> dict:
    out = {"Decision_Maker": "N/A", "Job_Title": "N/A"}
    if not company or company == "N/A":
        return out
    parts = [p.strip() for p in (city_state or "").split(",") if p.strip()]
    city = parts[0] if parts else ""
    state = parts[1][:2].upper() if len(parts) > 1 and len(parts[1].strip()) == 2 else ""
    clean_co = company.split("|")[0].split("-")[0].strip()
    params = {"version": "2.1", "organization_name": f"{clean_co}*", "limit": 5}
    if city: params["city"] = city
    if state: params["state"] = state
    try:
        r = await client.get("https://npiregistry.cms.hhs.gov/api/", params=params, timeout=5.0)
        for res in (r.json().get("results") or []) if r.status_code == 200 else []:
            b = res.get("basic") or {}
            fn, ln = (b.get("authorized_official_first_name") or "").strip(), (b.get("authorized_official_last_name") or "").strip()
            if fn and ln:
                cred = (b.get("authorized_official_credential") or "").strip()
                role = (b.get("authorized_official_title_or_position") or "Authorized Official / Owner").strip().title()
                out["Decision_Maker"] = f"{fn.title()} {ln.title()}"
                out["Job_Title"] = f"{role} ({cred})" if cred else role
                return out
    except Exception:
        pass
    return out
