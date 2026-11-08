# 🚀 Automated Google Maps B2B Lead Generation, Decision-Maker Email Enricher & AI Icebreakers (n8n + Apify + Google Sheets)

[![n8n Workflow](https://img.shields.io/badge/n8n-Workflow_Template-FF6D5A?style=for-the-badge&logo=n8n&logoColor=white)](./Weekly%20Google%20Maps%20Leads%20with%20Verified%20Emails%20%26%20AI%20Icebreakers%20to%20Google%20Sheets%20(Apify).json)
[![Apify Actor](https://img.shields.io/badge/Apify-B2B_Decision_Maker_Enricher-00C853?style=for-the-badge&logo=apify&logoColor=white)](https://apify.com/amitabh_312/b2b-website-decision-maker-email-enricher)
[![YouTube Demo](https://img.shields.io/badge/YouTube-Watch_5_Min_Walkthrough-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=JIFyaEh-wvk)

An end-to-end, self-healing **n8n B2B lead generation workflow** that scrapes local businesses from **Google Maps** (or enriches an existing **Google Sheet** in-place), resolves the **Owner / Founder / Medical Director**, verifies their **Direct Executive Email** via a 9-provider verification pool, detects active **Meta, Google, and TikTok Ad Pixels**, and writes a hyper-personalized **GPT-4o-mini Cold Email Icebreaker** back to your Google Sheet.

---

## 🎥 Watch the Live Walkthrough & Benchmark Demo

[![Watch the n8n Google Maps Lead Enrichment Tutorial](https://img.youtube.com/vi/JIFyaEh-wvk/maxresdefault.jpg)](https://www.youtube.com/watch?v=JIFyaEh-wvk)

> **Click above to watch on YouTube:** See how this workflow takes 50 raw Austin Med Spa leads in Google Sheets and enriches 75%+ with named Decision Makers, verified executive emails, ad-pixel intent tiers, and AI openers in a single run.

---

## ✨ Why This Workflow Beats Outscraper, Apollo & Basic Scrapers

Most Google Maps workflows only scrape surface-level directory data (`info@` emails or blank fields), forcing you to pay for expensive monthly subscriptions across Apollo, Clay, and NeverBounce. This workflow combines discovery, deep executive resolution, and verification into a single canvas:

| Feature | This n8n + Apify Pipeline | Basic Maps Scrapers (Outscraper / Phantombuster) | Static B2B Databases (Apollo / ZoomInfo) |
| :--- | :--- | :--- | :--- |
| **Data Freshness** | **100% Live Crawl + Real-Time SERP X-Ray** | Raw directory scrape only | 6–18 months stale (high bounce rates) |
| **Decision-Maker Resolution** | **On-Site HTML + LinkedIn X-Ray + US NPI Registry** | None (`info@` or `contact@` only) | Missing 70%+ of local SMBs & clinics |
| **Email Verification** | **Built-in 9-Provider Verifier Pool + DNS MX + Permutator** | Unverified guesses | Costs extra export credits |
| **Ad-Pixel Intent Scoring** | **Detects Meta Pixel, Google Ads/GTM, TikTok, Klaviyo, Shopify** | Not supported | Enterprise plan only |
| **Google Sheet Handling** | **In-Place Upsert + Self-Healing Headers + Multi-Location Fan-Out** | Appends duplicate rows at the bottom | Manual CSV import/export |
| **Cost per Enriched Lead** | **~$0.025–$0.035 modular Pay-Per-Event (only pay for fields found)** | Charges for blank rows | $99–$499/mo recurring seat lock-in |

---

## 🧠 Key Architecture & Features

### 1. Three Flexible Execution Modes (`run_mode`)
Control the entire pipeline from a single `Config` node without rewiring a single connection:
* **`both` (Default):** Enriches all un-enriched rows already sitting in your Google Sheet **and** scrapes up to `max_leads` brand-new listings from Google Maps on top.
* **`enrich_existing` ($0 Google Maps Cost):** Skips Google Maps scraping completely and enriches every un-enriched row in your existing Google Sheet (up to 2,000 domains per batch). Perfect when you already exported a CSV from Outscraper, D7 Lead Finder, or Instant Data Scraper.
* **`scrape_new`:** Ignores existing un-enriched rows in your sheet and only scrapes + enriches up to `max_leads` net-new places from Google Maps.

### 2. Multi-Source Decision-Maker & Direct Email Resolution
Powered by **[B2B Website Decision Maker, LinkedIn & Email Enricher](https://apify.com/amitabh_312/b2b-website-decision-maker-email-enricher)**, each business domain goes through a 5-stage waterfall:
1. **High-Concurrency Async Website Crawl:** Scans `/`, `/about`, `/team`, `/our-team`, `/providers`, `/leadership`, and `/contact` pages for founder/owner bios, `mailto:` links, JSON-LD schema, and contact form URLs.
2. **US Federal CMS NPI Registry Lookup:** Automatically queries the official US National Provider Identifier API by organization name and city/state to uncover the legal `Authorized Official` (Owner, President, or Medical Director) for healthcare, dental, and aesthetics clinics.
3. **LinkedIn & Web SERP X-Ray:** Executes targeted search dorks to identify the Owner, Founder, CEO, Managing Partner, or Practice Manager along with their personal LinkedIn profile URL.
4. **Corporate Email Permutator + 9-Provider Verification Pool:** When a website only lists a generic `info@` or `hello@` address—or hides emails behind a contact form—the engine constructs executive permutations (`first@domain.com`, `flast@domain.com`) and verifies deliverability against a 9-provider email verification pool + catch-all guard.
5. **Ad-Pixel & Tech Stack Fingerprinting:** Inspects live DOM script tags to detect active **Meta Pixel**, **Google Ads / GTM**, **TikTok Pixel**, **Shopify**, **Klaviyo**, and **Mindbody** installations, automatically tagging businesses running paid traffic as `🔥 High Intent (Running Ads)`.

### 3. Self-Healing Google Sheet Schema (`!1:1` Header Inspector)
* **Blank Sheet?** Automatically writes all 14 canonical CRM headers to Row 1 before upserting leads.
* **Raw Google Maps Export?** Automatically renames `title` $\rightarrow$ `Company_Name`, `website` $\rightarrow$ `Website`, `phone` $\rightarrow$ `Phone`, and `city` $\rightarrow$ `City_State` in-place while preserving all of your original columns (`totalScore`, `reviewsCount`, `street`, `categories`, `url`) untouched.

### 4. Multi-Location Chain Deduplication & Fan-Out
If a local chain has multiple branches in your Google Sheet sharing the same root domain (e.g., 3 locations of *Viva Day Spa* or *VIO Med Spa*), the workflow enriches the root domain **once** (saving you Apify credits) and automatically fans the enriched Decision Maker, Verified Email, and Ad Pixels back out to **every branch row** in your Google Sheet.

---

## 📊 Sample Output Columns (14 Enriched Fields)

| Column | Example Value | Description |
| :--- | :--- | :--- |
| `Company_Name` | `Face to Face Spa at Avery Ranch` | Business name preserved from your Sheet or Google Maps |
| `Decision_Maker` | `Jenny Woodcock` | Verified Owner, Founder, CEO, or Medical Director |
| `Job_Title` | `Founder and CEO` | Clean executive title |
| `Verified_Email` | `jenny@facetofacespa.com` | Verified deliverable email address |
| `Email_Type` | `Direct Executive Inbox (Name-Matched)` | Classification (`Direct Executive Inbox`, `Custom Corporate Domain`, `Personal / Studio Inbox`) |
| `Phone` | `(512) 614-0821` | Business or mobile phone number |
| `LinkedIn_Profile` | `https://www.linkedin.com/in/jenny-woodcock-...` | Direct personal LinkedIn profile URL |
| `Website` | `https://facetofacespa.com/avery-ranch/` | Exact original URL (preserves UTM parameters & subpaths for 1:1 row matching) |
| `City_State` | `Austin, TX` | Normalized city and state |
| `Ad_Pixels` | `Meta Pixel, Google Ads / GTM` | Active advertising & retargeting pixels detected on-site |
| `Intent_Tier` | `🔥 High Intent (Running Ads)` | `🔥 High Intent (Running Ads)` or `Standard Outbound` |
| `Cold_Email_Icebreaker` | *Hi Jenny, saw Face to Face Spa is running Google Ads in Austin...* | 1-sentence GPT-4o-mini opener (with automatic rule-based fallback) |
| `Contact_Form_URL` | `https://facetofacespa.com/contact-us/` | Direct URL to the site's contact form when no email exists |
| `Instagram_URL` | `https://www.instagram.com/facetofacespa` | Extracted Instagram profile URL |

---

## 🛠️ Quick Setup Guide (5 Minutes)

### Step 1: Import the Workflow into n8n
1. Download [`Weekly Google Maps Leads with Verified Emails & AI Icebreakers to Google Sheets (Apify).json`](./Weekly%20Google%20Maps%20Leads%20with%20Verified%20Emails%20%26%20AI%20Icebreakers%20to%20Google%20Sheets%20(Apify).json) from this repository.
2. In your n8n canvas, click **`...` (top-right menu)** $\rightarrow$ **Import from File...** and select the downloaded JSON file.

### Step 2: Connect Your Credentials
1. **Apify API Credential:** Connect your Apify account to the **`Scrape Google Maps`** and **`Enrich Leads`** nodes.
   * Grab your free Apify API token at [console.apify.com/settings/integrations](https://console.apify.com/settings/integrations).
2. **Google Sheets OAuth2 Credential:** Connect your Google account to:
   * `Fetch Existing Sheets Leads`
   * `Read Sheets Headers`
   * `Auto Create Headers`
   * `Upsert email leads to sheet`
   * `Upsert phone/social leads to sheet`
3. **Optional Credentials:**
   * **OpenAI API:** Connect to **`AI Cold Email Icebreaker`** (uses `gpt-4o-mini`). If omitted or disabled, the workflow automatically uses a clean rule-based icebreaker.
   * **Gmail OAuth2:** Connect to **`Bad Schema Email`** if you want email alerts when a sheet is missing a `Website` column.

### Step 3: Edit the `Config` Node & Run
Open the **`Config`** node at the start of the workflow and set your 8 parameters:
```json
{
  "run_mode": "both",
  "location (city; state)": "Austin, TX",
  "category": "Med Spa",
  "max_leads": 25,
  "sheet_document_id": "YOUR_GOOGLE_SHEET_ID_HERE",
  "sheet_name": "Sheet1",
  "alert_email": "you@yourdomain.com",
  "summaryWebhookURL": ""
}
```
Click **Execute Workflow** to test with `max_leads: 25`, then toggle **Active** to run automatically every week!

---

## 🌐 The 10-Actor B2B Lead Generation Ecosystem on Apify

Need deeper niche-specific extraction (like **Skool community MRR**, **Shopify average product prices**, **JaneApp/GlossGenius practitioners**, or **ThomasNet-style ISO-certified manufacturers**)? Check out the full suite of specialized extractors powering this workflow:

1. **[B2B Website Decision Maker, LinkedIn & Email Enricher](https://apify.com/amitabh_312/b2b-website-decision-maker-email-enricher)** — *Turn any list of domains or Google Maps URLs into verified executive emails, LinkedIn profiles, and ad pixels.*
2. **[MedSpa, Chiropractic & Physical Therapy Clinic Leads Scraper](https://apify.com/amitabh_312/medspa-wellness-clinic-leads-scraper)** — *Extracts Jane App (`janeapp.com`), Mindbody, and standalone wellness clinics with Medical Directors & Owners.*
3. **[Aesthetics, Beauty Salon & Solo Esthetician Leads Scraper](https://apify.com/amitabh_312/aesthetics-beauty-salon-leads-scraper)** — *Extracts GlossGenius, Fresha, Booksy, and Vagaro salon owners, direct mobile phones, and studio emails.*
4. **[US Dental & Medical Practice Owner Leads Scraper](https://apify.com/amitabh_312/dental-medical-practice-leads-scraper)** — *Finds private dental practices (DDS/DMD) and medical clinic owners with NPI verification.*
5. **[Skool Community Founder, MRR & Verified Email Scraper](https://apify.com/amitabh_312/skool-community-founder-mrr-leads-scraper)** — *Extracts paid Skool.com communities sorted by Estimated Monthly Recurring Revenue (MRR) and founder contact info.*
6. **[Shopify & D2C Ecommerce Brand Founder Leads Scraper](https://apify.com/amitabh_312/shopify-ecommerce-brand-founder-leads-scraper)** — *Scrapes active Shopify brands with live catalog metrics (`Avg_Product_Price`), Klaviyo/Meta pixels, and founder emails.*
7. **[Apple Podcasts Host & Booking Email Leads Scraper](https://apify.com/amitabh_312/podcast-host-email-leads-scraper)** — *Extracts direct host/producer booking emails from live Apple Podcasts RSS feeds for PR agencies.*
8. **[Local Contractor, Roofing, HVAC & Solar Leads Scraper](https://apify.com/amitabh_312/local-contractor-home-services-leads-scraper)** — *Finds high-ticket home service contractors with ServiceTitan/Jobber & Google Ads intent signals.*
9. **[Boutique Fitness, Gym, Pilates & CrossFit Studio Leads Scraper](https://apify.com/amitabh_312/fitness-gym-pilates-studio-leads-scraper)** — *Extracts independent gym, Pilates, Lagree, and CrossFit studio owners.*
10. **[US Industrial Manufacturer, CNC & Procurement Leads Scraper](https://apify.com/amitabh_312/us-manufacturer-procurement-leads-scraper)** — *Finds ISO 9001 / AS9100 / ITAR US custom manufacturers, CNC machine shops, and procurement/VP Ops contacts.*

---
