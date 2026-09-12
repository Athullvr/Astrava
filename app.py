"""
WhatsApp Forward FIR Report Generator
Satirical Cyber-Police FIR Generator for TinkerHub Useless Projects
Universe: Kerala Digital Satya Pramanam Vibhagam (KDSPV) / Cyber Satyameva Bureau
"""

import os
import json
import re
import html
import random
from datetime import datetime
import gradio as gr
from dotenv import load_dotenv

# Load local environment if available
load_dotenv()

# --- JOKE UNIVERSE & CONFIGURATION ---

DEPARTMENT_FULL = "KERALA DIGITAL SATYA PRAMANAM VIBHAGAM (KDSPV)"
DEPARTMENT_SUB = "Cyber Satyameva Bureau — Special Family WhatsApp Cell"
DEPARTMENT_MALAYALAM = "കേരള ഡിജിറ്റൽ സത്യ പ്രമാണ വിഭാഗം (സൈബർ ഫോർവേഡ് സെൽ)"

IO_POOL = [
    {"name": "CI Rajan 'Factcheck' Pillai", "rank": "Circle Inspector", "station": "Cyber Forward Cell, Central Squad", "badge": "KDSPV-901"},
    {"name": "SI Baby Mathew", "rank": "Sub-Inspector", "station": "Anti-Rumor Division, Kottayam West", "badge": "KDSPV-412"},
    {"name": "DySP Somanathan Nair", "rank": "Deputy Superintendent", "station": "Special Task Force on Uncle Forwards", "badge": "KDSPV-007"},
    {"name": "Inspector Anjali 'BlueTick' Varma", "rank": "Inspector", "station": "Family Group Admin Surveillance Wing", "badge": "KDSPV-554"},
    {"name": "SI Varghese 'ForwardedAsReceived' Kurian", "rank": "Sub-Inspector", "station": "Malabar Special Morning Wish Squad", "badge": "KDSPV-328"}
]

PUNISHMENT_BANK = [
    "3 days without Wi-Fi + mandatory 48-hour fact-check bootcamp and written apology to UNESCO.",
    "Demoted from WhatsApp Family Group Admin to 'Read-Only' member status for 30 calendar days.",
    "Confiscation of optical reading glasses between 06:00 AM and 08:30 AM (peak forward hours).",
    "Sentenced to typing out 500 times in Malayalam: 'ഞാൻ ഇനിമുതൽ ഗ്രൂപ്പിൽ തള്ളുകൾ ഫോർവേഡ് ചെയ്യുകയില്ല' (I will not forward tall-tales in groups).",
    "Permanent restriction to basic SMS; strictly banned from using 🙏, 🌺, and ☀️ emojis for 6 months.",
    "Mandatory community service: Must reply 'Fake news uncle' to 50 dubious family group forwards.",
    "Smartphone display brightness permanently locked to 12% until scientific temperament improves."
]

FAKE_SECTIONS_CATALOG = [
    ("Sec 420-B", "Vishwasa Chooshanam (Extreme Belief Exploitation via Forwarded Gifs)"),
    ("Sec 69-U", "Uncle Forward Pledge Act (Non-consensual 6 AM Good Morning Dissemination)"),
    ("Sec 153-M", "Uncensored Uncle Propaganda (Pseudo-Ayurvedic & Lemon Microwave Cures)"),
    ("Sec 302-G", "Murder of Common Sense in Broad Daylight"),
    ("Sec 144-W", "Unlawful Assembly of 10+ Emojis in a Single Paragraph"),
    ("Sec 404-N", "NASA / UNESCO Name-Dropping Without Prior Government Sanction"),
    ("Sec 505-K", "Kshemam Illatha Kadha (Spreading Panic Over Free 500GB Recharge Links)"),
    ("Sec 294-G", "5G Radiation Frog Mutation & Stomach Wave Conspiracy Propagation"),
    ("Sec 2000-C", "Nano-GPS Satellite Currency Tracking Rumormongering Act")
]

# Session Counter for Live Demos
SESSION_CASE_COUNTER = 1042

# --- 3 HAND-CRAFTED FEW-SHOT EXAMPLES ---

FEW_SHOT_EXAMPLES = [
    {
        "input": "BREAKING NEWS: UNESCO has just declared the Indian National Anthem as the BEST in the whole universe! Please forward this to at least 10 groups to make India proud. Do not ignore this holy duty! 🇮🇳🙏",
        "output": {
            "fir_number": "FIR/2026/KDSPV-0104",
            "date": "12-Sep-2026 06:14 AM",
            "complainant_name": "UNESCO Secretary-General (Exhausted)",
            "accused": "Suresh 'Forward' Nair (Resident Admin, Kudumbam WhatsApp Group)",
            "sections_invoked": [
                "Sec 404-N: NASA/UNESCO Name-Dropping Without Prior Sanction",
                "Sec 420-B: Vishwasa Chooshanam (Belief Exploitation)",
                "Sec 69-U: Non-Consensual Mandatory 10-Group Forward Extortion"
            ],
            "incident_summary": "Accused did willfully fabricate an international cultural award certificate from UNESCO at 06:14 AM on a Sunday morning and blackmailed family members with emotional guilt to forward to 10 WhatsApp contacts.",
            "io_remarks": "Nonsense forward. UNESCO has clarified 4,812 times that they do not conduct global anthem beauty pageants on WhatsApp. Accused's phone was found with 4.2 GB of Good Morning flower images. Phone seized.",
            "case_status": "CHARGESHEET FILED - PHONE SEIZED",
            "penalty": "3 days without Wi-Fi + mandatory 48-hour fact-check bootcamp and written apology to UNESCO."
        }
    },
    {
        "input": "ATTENTION EVERYONE: Drinking hot boiled lemon water mixed with raw ginger and rock salt at exactly 4:32 AM destroys all 5G radiation inside stomach and cures all viral diseases instantly. Big Pharma and doctors will hide this from you! Share fast before WhatsApp deletes this post! 🍋⚡",
        "output": {
            "fir_number": "FIR/2026/KDSPV-0105",
            "date": "12-Sep-2026 05:45 AM",
            "complainant_name": "Indian Medical Association & Cyber Health Cell",
            "accused": "Uncle Unnikrishnan, Self-Proclaimed Forward MD",
            "sections_invoked": [
                "Sec 153-M: Uncensored Uncle Propaganda & Pseudo-Ayurvedic Menace",
                "Sec 294-G: 5G Stomach Radiation Conspiracy Propagation",
                "Sec 302-G: Murder of Common Sense in Broad Daylight"
            ],
            "incident_summary": "Accused propagated bogus biological claim that citrus fruit juice can neutralize high-frequency electromagnetic telecommunication frequencies inside the human gastrointestinal tract.",
            "io_remarks": "Entharo entho. Lemon water will at best cause acidity at 4:32 AM, not absorb 5G towers. Accused claims he got information from 'Secret Himalayan Scientist'. Interrogation revealed information was forwarded by his brother-in-law in Dubai.",
            "case_status": "UNDER POLICE CUSTODY (TAKING ANTACID)",
            "penalty": "Confiscation of reading glasses between 06:00 AM and 08:30 AM + sentenced to type 'Lemon is not an antenna' 500 times."
        }
    },
    {
        "input": "Urgent! Jio and Tata offering FREE 500GB 5G Recharge on the occasion of Ambani grandson birthday. Click this link immediately: www.free-recharge-loot-5g-malayalam.xyz/win. Share with 15 friends to activate! Offer ends in 10 minutes! 🎁🔥",
        "output": {
            "fir_number": "FIR/2026/KDSPV-0106",
            "date": "12-Sep-2026 11:20 PM",
            "complainant_name": "Telecom Regulatory Authority & Frustrated Group Members",
            "accused": "Vijayan (Active Admin, 'Old Boys 1988 Batch')",
            "sections_invoked": [
                "Sec 505-K: Kshemam Illatha Kadha (Free Recharge Greed Baiting)",
                "Sec 420-B: Vishwasa Chooshanam (Loot Link Distribution)",
                "Sec 144-W: Unlawful Assembly of Suspicious Links and Phishing Traps"
            ],
            "incident_summary": "Accused did click a malware phishing link promising 500GB free high-speed internet and circulated the malicious URL to 42 distinct family and school reunion chatrooms at midnight.",
            "io_remarks": "Ammummade link. No telecom company gives 500GB free for Ambani family birthdays. Link opened a Russian lottery page. Accused confessed he only wanted to watch YouTube fishing videos without recharge. Warned strictly.",
            "case_status": "SIM CARD RESTRICTED TO 2G",
            "penalty": "Demoted from Group Admin to Read-Only member for 30 days + phone display brightness locked to 10%."
        }
    }
]

# --- SYSTEM PROMPT TEMPLATE ---

SYSTEM_PROMPT = """You are the Lead Cyber Investigator at Kerala Digital Satya Pramanam Vibhagam (Cyber Satyameva Bureau).
Your job is to analyze absurd, fake, or cringe WhatsApp forwards submitted by users and produce an official-looking, deadpan, highly satirical FIRST INFORMATION REPORT (F.I.R.) in JSON format.

Your output MUST be ONLY valid JSON with no markdown backticks, no commentary, matching this exact schema:
{
  "fir_number": "string (e.g. FIR/2026/KDSPV-XXXX)",
  "date": "string (e.g. 12-Sep-2026 07:30 AM)",
  "complainant_name": "string (funny exhausted authority or victim, e.g. NASA Chief Scientist / Traumatized Nephew)",
  "accused": "string (humorous WhatsApp forwarder identity, e.g. Uncle Gopinathan, High-Volume Group Admin)",
  "sections_invoked": ["string with fake IPC sections like Sec 420-B, Sec 69-U, Sec 153-M, etc."],
  "incident_summary": "string (formal, deadpan police narration of the ridiculous forward)",
  "io_remarks": "string (deadpan, humorous Manglish/English mix remarks reacting specifically to the contents of the forward)",
  "case_status": "string (e.g. BOGUS - CHARGESHEET FILED / PHONE CONFISCATED)",
  "penalty": "string (absurd punishment involving WhatsApp restrictions, Wi-Fi ban, or fact-check labor)"
}

Tone guidelines:
- Deadpan bureaucratic seriousness combined with sharp Malayalam/Manglish cultural references (e.g. 'Entharo entho', 'Ammummade link', 'Kudumbam Group Admin', 'Over-enthu uncle').
- React directly and specifically to the absurd claims in the input message.
"""

def build_few_shot_messages(user_text: str) -> list:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for ex in FEW_SHOT_EXAMPLES:
        messages.append({"role": "user", "content": ex["input"]})
        messages.append({"role": "assistant", "content": json.dumps(ex["output"])})
    messages.append({"role": "user", "content": user_text})
    return messages

# --- INTELLIGENT SATIRICAL FALLBACK ENGINE (PHASE 4 SAFETY NET) ---

def generate_satirical_fallback(user_text: str, fir_num: str, io_officer: dict) -> dict:
    """Procedurally generates a tailored satirical FIR based on keyword heuristics."""
    text_lower = user_text.lower()
    now_str = datetime.now().strftime("%d-%b-%Y %I:%M %p")
    penalty = random.choice(PUNISHMENT_BANK)

    # Contextual matching matrix
    if any(k in text_lower for k in ["unesco", "anthem", "world best", "heritage", "award"]):
        return {
            "fir_number": fir_num,
            "date": now_str,
            "complainant_name": "UNESCO Director-General & Committee on Tiring Forwards",
            "accused": "Venu 'Nationalist' Kurup (Forward Commander, 14 Family Groups)",
            "sections_invoked": [
                "Sec 404-N: UNESCO Name-Dropping Without Prior Clearance",
                "Sec 420-B: Vishwasa Chooshanam (Spiritual Guilt Tripping)",
                "Sec 69-U: Compulsory 10-Group Forward Extortion Act"
            ],
            "incident_summary": "Accused propagated counterfeit international declaration claiming an international UN body evaluates cultural anthems on WhatsApp every Sunday morning.",
            "io_remarks": "Nonsense forward. UNESCO officials have gone on indefinite medical leave due to Malayali family groups tagging them continuously. Accused admitted he forwarded without reading full text. Forwarding finger placed under house arrest.",
            "case_status": "VERIFIED BOGUS - CHARGESHEET FILED",
            "penalty": penalty
        }

    elif any(k in text_lower for k in ["lemon", "ginger", "hot water", "cure", "cancer", "radiation", "5g", "covid", "virus", "doctor", "ayurveda", "turmeric"]):
        return {
            "fir_number": fir_num,
            "date": now_str,
            "complainant_name": "Indian Medical Association & World Health Organization (Pained)",
            "accused": "Dr. (Self-Conferred) Radhakrishnan, Resident Medical Forward Specialist",
            "sections_invoked": [
                "Sec 153-M: Uncensored Uncle Propaganda & Pseudo-Ayurvedic Menace",
                "Sec 294-G: Gastrointestinal 5G Radiation Conspiracy Act",
                "Sec 302-G: Murder of Common Sense in Broad Daylight"
            ],
            "incident_summary": "Accused broadcasted dubious biochemical hypothesis asserting that boiling acidic fruits at dawn repels high-frequency cellular tower telecommunications from human organs.",
            "io_remarks": "Entharo entho. Lemon water will at best cause severe heartburn at 4 AM, not disarm telecom towers. Accused confessed he received this from 'Himalayan Siddha Group' whose admin is actually a retired clerk in Aluva.",
            "case_status": "UNDER HIGH-LEVEL SCRUTINY (TAKING GELUSIL)",
            "penalty": penalty
        }

    elif any(k in text_lower for k in ["recharge", "free", "jio", "tata", "ambani", "win", "gift", "loot", "click", "http", "www", "rupees", "crore", "lottery"]):
        return {
            "fir_number": fir_num,
            "date": now_str,
            "complainant_name": "Cyber Crime Squad & Deceived Pensioners Association",
            "accused": "Mani 'Free Loot' Asan (Admin, 'Friends Forever 1994')",
            "sections_invoked": [
                "Sec 505-K: Kshemam Illatha Kadha (Free Recharge Greed Baiting)",
                "Sec 420-B: Vishwasa Chooshanam (Phishing Link Distribution)",
                "Sec 144-W: Unlawful Assembly of Suspicious Russian URLs"
            ],
            "incident_summary": "Accused distributed high-risk suspicious hyperlink claiming corporate billionaires are distributing free 5G gigabytes to commemorate domestic family birthdays.",
            "io_remarks": "Ammummade link. No billionaire is distributing 500GB free recharge on WhatsApp. Clicking link directed victim to a fake cryptocurrency poker portal. Accused claimed he was only trying to help cousins.",
            "case_status": "SIM CARD DOWNGRADED TO 2G",
            "penalty": penalty
        }

    elif any(k in text_lower for k in ["chip", "2000", "note", "satellite", "gps", "modi", "rbi", "nasa"]):
        return {
            "fir_number": fir_num,
            "date": now_str,
            "complainant_name": "Reserve Bank of India & Department of Space",
            "accused": "Gopakumar (Nano-Tech Speculation Officer, Resident of Trivandrum)",
            "sections_invoked": [
                "Sec 2000-C: Nano-GPS Satellite Currency Tracking Rumormongering Act",
                "Sec 404-N: NASA Space Technology Fabrication Section",
                "Sec 302-G: Murder of Common Sense in Broad Daylight"
            ],
            "incident_summary": "Accused insisted that standard paper currency notes possess subterranean satellite connectivity transponders active 120 meters underground without battery source.",
            "io_remarks": "Varantha thallu. Tested 2000 note in forensic laboratory using water and torch. No satellite emerged. Accused stated news anchor on TV looked very confident while saying it. Both anchor and accused summoned.",
            "case_status": "INVESTIGATION ONGOING (MAGNIFYING GLASS DEPLOYED)",
            "penalty": penalty
        }

    elif any(k in text_lower for k in ["good morning", "morning", "flower", "blessing", "suprabatham", "have a nice day", "tea", "coffee"]):
        return {
            "fir_number": fir_num,
            "date": now_str,
            "complainant_name": "Society for Prevention of Storage Full Notifications",
            "accused": "Kunjamma Aunty (Chief Good Morning Dispatcher, 05:15 AM Shift)",
            "sections_invoked": [
                "Sec 69-U: Non-Consensual Dawn Glitter Image Transmission",
                "Sec 144-W: Unlawful Assembly of 45 Glittering Rose Emojis",
                "Sec 420-B: Vishwasa Chooshanam (Wasting 12MB Phone Storage Daily)"
            ],
            "incident_summary": "Accused did fire 24 high-resolution animated glitter flower images into 9 family groups consecutively between 05:15 AM and 05:45 AM without recipient consent.",
            "io_remarks": "Kandittu sahikkanilla. Complainant's phone storage reached 99.8% capacity with glittering hibiscus files. Accused claimed sending flowers brings positive vibration. Mobile gallery sanitized by cyber squad.",
            "case_status": "RESTRICTED TO PLAIN TEXT ONLY",
            "penalty": penalty
        }

    else:
        # Procedural fallback for custom or unique forwards
        exclamation_count = user_text.count("!")
        caps_ratio = sum(1 for c in user_text if c.isupper()) / max(1, len(user_text))
        
        accused_list = [
            "Somasekharan Nair (Chronic Forwardist, Kudumbam Group)",
            "Madhavan Pillai (Senior Unverified Content Broadcaster)",
            "Baburaj (Admin, 'Fun & Jokes Kerala Official')",
            "Anandhu (Forwarded as Received Champion)"
        ]
        
        complainant_list = [
            "Traumatized Group Members Union",
            "Special Task Force on Cringe Digital Forwards",
            "Consortium of Innocent Nephews & Nieces",
            "Cyber Satya Pramanam Automated Radar"
        ]

        sections = random.sample(FAKE_SECTIONS_CATALOG, 3)
        section_names = [f"{s[0]}: {s[1]}" for s in sections]

        remarks_list = [
            f"Varantha thallu. Forward contains {exclamation_count} exclamation marks and zero credible evidence. Accused claimed 'Somebody sent it to me in another group so I sent it here'. Classic forwarding syndrome.",
            "Entharo entho. Preliminary verification indicates message was drafted during peak afternoon boredom. Accused confessed he did not read beyond first two lines before tapping 'Share to All'.",
            "Ammummade forward. Digital forensics team verified 0% scientific truth and 100% emotional manipulation. Accused advised to drink cool water and put phone in drawer.",
            "Bhayanakam thanne. Accused circulated unverified claim across multiple family channels without 2 seconds of Google search. Phone seized for thorough memory cleaning."
        ]

        return {
            "fir_number": fir_num,
            "date": now_str,
            "complainant_name": random.choice(complainant_list),
            "accused": random.choice(accused_list),
            "sections_invoked": section_names,
            "incident_summary": f"Accused circulated unverified viral text: \"{user_text[:120]}...\" creating mass confusion, emotional exhaustion, and unnecessary storage consumption in digital chatrooms.",
            "io_remarks": random.choice(remarks_list),
            "case_status": "UNDER INVESTIGATION - PHONE SCREENSHOT CAPTURED",
            "penalty": penalty
        }

# --- JSON PARSING & LLM ENGINE ---

def clean_and_parse_json(text: str) -> dict:
    """Safely extracts and parses JSON even if wrapped in markdown codeblocks or noisy text."""
    if not text:
        return {}
    
    # Strip markdown fences
    text = re.sub(r"^```(?:json)?\s*", "", text.strip(), flags=re.MULTILINE)
    text = re.sub(r"\s*```$", "", text.strip(), flags=re.MULTILINE)
    
    # Locate first { and last }
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        text = match.group(0)
    
    try:
        return json.loads(text)
    except Exception:
        # Try basic repairs (trailing commas)
        cleaned = re.sub(r",\s*([\]}])", r"\1", text)
        return json.loads(cleaned)

def generate_fir(user_text: str = "", custom_token: str = "") -> tuple:
    """Core function to generate FIR JSON via HF Inference API with graceful fallback and transparent engine tracking."""
    global SESSION_CASE_COUNTER
    SESSION_CASE_COUNTER += 1
    
    fir_number = f"FIR/2026/KDSPV-{SESSION_CASE_COUNTER:04d}"
    io_officer = random.choice(IO_POOL)
    
    raw_text = (user_text or "").strip()
    if not raw_text:
        raw_text = "Good Morning! UNESCO declares this the best message of all time. Forward to 10 people."

    token = (custom_token or "").strip() or os.getenv("HF_TOKEN", "").strip() or os.getenv("HUGGINGFACEHUB_API_TOKEN", "").strip()
    
    fir_data = None
    engine_used = ""
    last_error = ""

    # If token available, attempt Hugging Face Chat Completion API with 10s timeout
    if token:
        try:
            from huggingface_hub import InferenceClient
            client = InferenceClient(token=token, timeout=10.0)
            
            messages = build_few_shot_messages(raw_text)
            
            # Use reliable instruct models supporting Chat Completion
            model_candidates = [
                "meta-llama/Llama-3.2-3B-Instruct",
                "Qwen/Qwen2.5-7B-Instruct",
                "mistralai/Mistral-7B-Instruct-v0.3"
            ]
            
            for model_id in model_candidates:
                try:
                    response = client.chat_completion(
                        messages=messages,
                        model=model_id,
                        max_tokens=600,
                        temperature=0.7,
                        top_p=0.9,
                    )
                    generated_text = response.choices[0].message.content
                    parsed = clean_and_parse_json(generated_text)
                    if parsed and "sections_invoked" in parsed:
                        fir_data = parsed
                        engine_used = model_id
                        break
                except Exception as model_err:
                    last_error = str(model_err)
                    print(f"HF Model {model_id} error: {model_err}")
                    continue
        except Exception as api_err:
            last_error = str(api_err)
            print(f"HF Client Initialization/Inference Error: {api_err}")

    # Fallback to local satire humor engine if HF failed or no token
    if not fir_data or not isinstance(fir_data, dict) or "sections_invoked" not in fir_data:
        fir_data = generate_satirical_fallback(raw_text, fir_number, io_officer)
        if not token:
            status_note = f"⚠️ No HF token provided — using Local Satire Engine | Case #{SESSION_CASE_COUNTER}"
        else:
            status_note = f"⚠️ HF API error ({last_error}) — used Local Satire Engine as backup | Case #{SESSION_CASE_COUNTER}"
    else:
        status_note = f"✅ Generated by Hugging Face ({engine_used}) | Case #{SESSION_CASE_COUNTER}"

    # Ensure all required keys exist (defensive schema validation)
    fir_data.setdefault("fir_number", fir_number)
    fir_data.setdefault("date", datetime.now().strftime("%d-%b-%Y %I:%M %p"))
    fir_data.setdefault("complainant_name", "Anti-Rumor Special Task Force")
    fir_data.setdefault("accused", "Unverified WhatsApp Forwarder")
    fir_data.setdefault("sections_invoked", ["Sec 420-B: Vishwasa Chooshanam", "Sec 302-G: Murder of Common Sense"])
    fir_data.setdefault("incident_summary", f"Accused forwarded message: '{raw_text[:100]}...'")
    fir_data.setdefault("io_remarks", "Entharo entho. Case registered for spreading unverified claims.")
    fir_data.setdefault("case_status", "CHARGESHEET FILED - PENDING INTERROGATION")
    fir_data.setdefault("penalty", random.choice(PUNISHMENT_BANK))
    
    # Store IO details inside data for rendering
    fir_data["io_name"] = io_officer["name"]
    fir_data["io_rank"] = io_officer["rank"]
    fir_data["io_station"] = io_officer["station"]
    fir_data["io_badge"] = io_officer["badge"]

    # Render HTML card
    card_html = render_fir_card(fir_data, raw_text)
    raw_json_str = json.dumps(fir_data, indent=2)

    return card_html, raw_json_str, status_note

# --- VINTAGE POLICE FIR CARD HTML/CSS RENDERER (PHASE 2 & 3) ---

def render_fir_card(fir: dict, raw_input: str) -> str:
    """Renders a vintage official Kerala Cyber Police FIR Report with red stamps and typewriter styling."""
    
    # Escape all strings for safety
    fir_num = html.escape(str(fir.get("fir_number", "FIR/2026/KDSPV-0000")))
    date_val = html.escape(str(fir.get("date", datetime.now().strftime("%d-%b-%Y %I:%M %p"))))
    complainant = html.escape(str(fir.get("complainant_name", "Cyber Satya Pramanam Squad")))
    accused = html.escape(str(fir.get("accused", "Unknown Forwarder")))
    summary = html.escape(str(fir.get("incident_summary", "Details pending investigation.")))
    remarks = html.escape(str(fir.get("io_remarks", "Entharo entho.")))
    status = html.escape(str(fir.get("case_status", "UNDER INVESTIGATION")))
    penalty = html.escape(str(fir.get("penalty", "3 days without Wi-Fi.")))
    io_name = html.escape(str(fir.get("io_name", "CI Rajan Pillai")))
    io_rank = html.escape(str(fir.get("io_rank", "Circle Inspector")))
    io_station = html.escape(str(fir.get("io_station", "Cyber Forward Cell")))
    io_badge = html.escape(str(fir.get("io_badge", "KDSPV-001")))
    
    escaped_raw_input = html.escape(raw_input.strip())

    # Sections Badges HTML
    sections_list = fir.get("sections_invoked", [])
    if isinstance(sections_list, str):
        sections_list = [sections_list]
    
    sections_badges = ""
    for sec in sections_list:
        sec_str = html.escape(str(sec))
        sections_badges += f'<span class="fir-sec-badge"><span class="badge-icon">⚖️</span> {sec_str}</span>\n'

    # Stamp Text (randomized or status-based)
    stamp_text = "VERIFIED BOGUS"
    if "SEIZED" in status.upper():
        stamp_text = "PHONE SEIZED"
    elif "CUSTODY" in status.upper():
        stamp_text = "UNDER ARREST"
    elif "2G" in status.upper():
        stamp_text = "SIM SEIZED (2G)"

    card_html = f"""
    <div class="fir-wrapper" id="printable-fir">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=Special+Elite&family=Anek+Malayalam:wght@400;700&display=swap');

            .fir-wrapper {{
                width: 100%;
                max-width: 820px;
                margin: 0 auto;
                background-color: #faf6ea;
                background-image: radial-gradient(#ece3cb 1px, transparent 1px);
                background-size: 20px 20px;
                color: #1a1a1a;
                font-family: 'Courier Prime', 'Courier New', monospace;
                padding: 30px;
                border: 3px double #3a2a1d;
                box-shadow: 0 10px 30px rgba(0,0,0,0.35), inset 0 0 60px rgba(210, 180, 140, 0.25);
                position: relative;
                box-sizing: border-box;
                border-radius: 4px;
                overflow: hidden;
            }}

            /* Watermark */
            .fir-watermark {{
                position: absolute;
                top: 45%;
                left: 50%;
                transform: translate(-50%, -50%) rotate(-30deg);
                font-size: 80px;
                font-weight: 900;
                color: rgba(180, 50, 50, 0.05);
                text-transform: uppercase;
                letter-spacing: 12px;
                pointer-events: none;
                user-select: none;
                white-space: nowrap;
                z-index: 0;
                font-family: 'Special Elite', monospace;
            }}

            /* Top Official Header */
            .fir-header {{
                text-align: center;
                border-bottom: 2px solid #2d241e;
                padding-bottom: 15px;
                margin-bottom: 20px;
                position: relative;
                z-index: 1;
            }}

            .fir-emblem-svg {{
                width: 54px;
                height: 54px;
                margin: 0 auto 6px auto;
                display: block;
            }}

            .fir-dept-mal {{
                font-family: 'Anek Malayalam', sans-serif;
                font-size: 15px;
                font-weight: 700;
                color: #2b3a4a;
                margin: 0;
                letter-spacing: 0.5px;
            }}

            .fir-dept-eng {{
                font-size: 16px;
                font-weight: 700;
                color: #111;
                margin: 3px 0 2px 0;
                letter-spacing: 1.5px;
                text-transform: uppercase;
            }}

            .fir-sub-cell {{
                font-size: 12px;
                color: #554433;
                font-style: italic;
                margin: 0 0 10px 0;
            }}

            .fir-main-title {{
                display: inline-block;
                background-color: #2c3e50;
                color: #ffffff;
                padding: 6px 20px;
                font-size: 15px;
                font-weight: 700;
                letter-spacing: 2px;
                border-radius: 2px;
                text-transform: uppercase;
                margin-top: 5px;
                border: 1px solid #1a252f;
            }}

            /* Meta Bar */
            .fir-meta-bar {{
                display: flex;
                justify-content: space-between;
                flex-wrap: wrap;
                background: rgba(220, 205, 175, 0.4);
                border: 1px dashed #7a6a55;
                padding: 10px 14px;
                margin-bottom: 20px;
                font-size: 13px;
                position: relative;
                z-index: 1;
            }}

            .fir-meta-item {{
                margin: 3px 10px 3px 0;
            }}

            .fir-meta-label {{
                font-weight: 700;
                color: #5a4030;
                text-transform: uppercase;
            }}

            /* Tables & Details Grid */
            .fir-grid {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 16px;
                margin-bottom: 20px;
                position: relative;
                z-index: 1;
            }}

            @media (max-width: 600px) {{
                .fir-grid {{
                    grid-template-columns: 1fr;
                }}
            }}

            .fir-box {{
                background: rgba(255, 255, 255, 0.65);
                border: 1px solid #c4b59d;
                padding: 12px;
                border-radius: 3px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            }}

            .fir-box-title {{
                font-size: 11px;
                font-weight: 700;
                color: #8b0000;
                text-transform: uppercase;
                border-bottom: 1px solid #decbb5;
                padding-bottom: 4px;
                margin-bottom: 8px;
                letter-spacing: 1px;
            }}

            .fir-box-content {{
                font-size: 13px;
                line-height: 1.45;
                color: #222;
            }}

            /* Sections Badges */
            .fir-sections-container {{
                margin-bottom: 20px;
                background: rgba(255, 245, 230, 0.75);
                border: 1px solid #d4a373;
                padding: 14px;
                border-radius: 3px;
                position: relative;
                z-index: 1;
            }}

            .fir-sec-badge {{
                display: block;
                background: #fff;
                border-left: 4px solid #b22222;
                border-right: 1px solid #e0d0c0;
                border-top: 1px solid #e0d0c0;
                border-bottom: 1px solid #e0d0c0;
                padding: 6px 10px;
                margin: 6px 0;
                font-size: 12.5px;
                font-weight: 700;
                color: #660000;
                border-radius: 0 3px 3px 0;
            }}

            /* Evidence Box */
            .fir-evidence-box {{
                background: #f1f6f1;
                border: 1px solid #a3c4a3;
                border-left: 5px solid #2e7d32;
                padding: 12px 14px;
                margin-bottom: 20px;
                font-size: 12.5px;
                position: relative;
                z-index: 1;
            }}

            .fir-evidence-title {{
                color: #1b5e20;
                font-weight: 700;
                font-size: 11px;
                text-transform: uppercase;
                margin-bottom: 6px;
                letter-spacing: 1px;
            }}

            .fir-evidence-text {{
                font-style: italic;
                color: #2c3e50;
                word-break: break-word;
            }}

            /* Remarks Box */
            .fir-remarks-box {{
                background: #fffdf7;
                border: 1.5px solid #2c3e50;
                padding: 14px;
                margin-bottom: 20px;
                position: relative;
                z-index: 1;
            }}

            .fir-remarks-title {{
                color: #1a252f;
                font-weight: 700;
                font-size: 12px;
                text-transform: uppercase;
                margin-bottom: 8px;
                border-bottom: 1px dashed #aaa;
                padding-bottom: 4px;
            }}

            .fir-remarks-text {{
                font-size: 13.5px;
                line-height: 1.5;
                color: #111;
            }}

            /* Penalty Banner */
            .fir-penalty-banner {{
                background: #fff3cd;
                border: 2px dashed #856404;
                color: #533f03;
                padding: 12px 16px;
                margin-bottom: 25px;
                font-size: 13px;
                font-weight: 700;
                position: relative;
                z-index: 1;
                display: flex;
                align-items: center;
                gap: 12px;
            }}

            .fir-penalty-icon {{
                font-size: 26px;
                flex-shrink: 0;
            }}

            /* Red Rubber Stamp */
            .fir-rubber-stamp {{
                position: absolute;
                bottom: 85px;
                right: 35px;
                border: 4px solid #b22222;
                color: #b22222;
                font-family: 'Special Elite', 'Courier Prime', monospace;
                font-size: 20px;
                font-weight: 900;
                text-transform: uppercase;
                padding: 8px 18px;
                transform: rotate(-12deg);
                opacity: 0.88;
                letter-spacing: 2px;
                mask-image: radial-gradient(circle, rgba(0,0,0,1) 70%, rgba(0,0,0,0.6) 100%);
                pointer-events: none;
                user-select: none;
                z-index: 2;
                border-radius: 4px;
                box-shadow: 0 0 0 2px #b22222;
            }}

            /* Signatures & Footer */
            .fir-footer {{
                display: flex;
                justify-content: space-between;
                align-items: flex-end;
                border-top: 1px solid #7a6a55;
                padding-top: 15px;
                margin-top: 20px;
                font-size: 11px;
                position: relative;
                z-index: 1;
            }}

            .fir-signature-block {{
                text-align: right;
            }}

            .fir-signature-line {{
                font-family: 'Special Elite', cursive, monospace;
                font-size: 16px;
                color: #1a365d;
                margin-bottom: 3px;
                transform: rotate(-2deg);
                display: inline-block;
            }}

            .fir-officer-title {{
                font-size: 11px;
                color: #444;
                font-weight: 700;
            }}

            .fir-disclaimer {{
                font-size: 10px;
                color: #887766;
                max-width: 380px;
                line-height: 1.3;
            }}

            /* Action Buttons Bar */
            .fir-action-bar {{
                display: flex;
                justify-content: center;
                gap: 12px;
                margin-top: 20px;
            }}

            .fir-btn {{
                background: #1f2937;
                color: #f9fafb;
                border: 1px solid #374151;
                padding: 8px 16px;
                font-family: inherit;
                font-size: 12px;
                font-weight: 700;
                border-radius: 4px;
                cursor: pointer;
                transition: all 0.2s ease;
                display: inline-flex;
                align-items: center;
                gap: 6px;
                text-decoration: none;
            }}

            .fir-btn:hover {{
                background: #374151;
                color: #ffffff;
                transform: translateY(-1px);
            }}

            /* Print Styles */
            @media print {{
                body * {{
                    visibility: hidden;
                }}
                #printable-fir, #printable-fir * {{
                    visibility: visible;
                }}
                #printable-fir {{
                    position: absolute;
                    left: 0;
                    top: 0;
                    width: 100% !important;
                    max-width: 100% !important;
                    box-shadow: none !important;
                    border: 2px solid #000 !important;
                }}
                .fir-action-bar {{
                    display: none !important;
                }}
            }}
        </style>

        <div class="fir-watermark">KDSPV SATIRE</div>

        <!-- Official Header -->
        <div class="fir-header">
            <!-- SVG Kerala Cyber Emblem -->
            <svg class="fir-emblem-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="50" cy="50" r="46" stroke="#2c3e50" stroke-width="4" fill="#f4ebd9"/>
                <path d="M50 15 L58 35 L80 35 L62 48 L69 70 L50 56 L31 70 L38 48 L20 35 L42 35 Z" fill="#8b0000"/>
                <circle cx="50" cy="50" r="14" fill="#2c3e50"/>
                <path d="M44 50 L48 54 L56 46" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                <text x="50" y="88" font-size="7" font-weight="bold" fill="#2c3e50" text-anchor="middle" font-family="monospace">SATYAMEVA 420</text>
            </svg>

            <p class="fir-dept-mal">{DEPARTMENT_MALAYALAM}</p>
            <h2 class="fir-dept-eng">{DEPARTMENT_FULL}</h2>
            <p class="fir-sub-cell">{DEPARTMENT_SUB} | STATUTORY FORWARD REGULATION DIVISION</p>
            <div class="fir-main-title">FIRST INFORMATION REPORT (F.I.R.) — FORM NO. 420-M</div>
        </div>

        <!-- Metadata Ribbon -->
        <div class="fir-meta-bar">
            <div class="fir-meta-item"><span class="fir-meta-label">FIR No:</span> <strong>{fir_num}</strong></div>
            <div class="fir-meta-item"><span class="fir-meta-label">Date/Time:</span> {date_val}</div>
            <div class="fir-meta-item"><span class="fir-meta-label">Jurisdiction:</span> Family WhatsApp Groups</div>
            <div class="fir-meta-item"><span class="fir-meta-label">Status:</span> <strong style="color: #b22222;">{status}</strong></div>
        </div>

        <!-- Parties Grid -->
        <div class="fir-grid">
            <div class="fir-box">
                <div class="fir-box-title">👤 Complainant / Informant</div>
                <div class="fir-box-content">
                    <strong>{complainant}</strong><br>
                    <span style="font-size: 11.5px; color: #555;">Type: Frustrated Recipient / Autonomous Fact-Check Radar</span>
                </div>
            </div>
            <div class="fir-box">
                <div class="fir-box-title">🚨 Accused Forwarder / Admin</div>
                <div class="fir-box-content">
                    <strong>{accused}</strong><br>
                    <span style="font-size: 11.5px; color: #555;">Offense: High-Volume Forwarding Without Verification</span>
                </div>
            </div>
        </div>

        <!-- Sections Invoked -->
        <div class="fir-sections-container">
            <div class="fir-box-title" style="margin-bottom: 4px;">⚖️ Penal Sections & Cyber Satire Codes Invoked</div>
            {sections_badges}
        </div>

        <!-- Raw Evidence Forward -->
        <div class="fir-evidence-box">
            <div class="fir-evidence-title">📱 Exhibit 'A' — Forwarded Message Transcript</div>
            <div class="fir-evidence-text">"{escaped_raw_input}"</div>
        </div>

        <!-- Incident Summary -->
        <div class="fir-box" style="margin-bottom: 20px;">
            <div class="fir-box-title">📜 Brief Description of Offense</div>
            <div class="fir-box-content">{summary}</div>
        </div>

        <!-- IO Remarks -->
        <div class="fir-remarks-box">
            <div class="fir-remarks-title">🕵️‍♂️ Investigating Officer (I.O.) Disposition & Remarks</div>
            <div class="fir-remarks-text">"{remarks}"</div>
        </div>

        <!-- Court Directive / Penalty -->
        <div class="fir-penalty-banner">
            <div class="fir-penalty-icon">⚖️</div>
            <div>
                <span style="text-transform: uppercase; font-size: 11px; letter-spacing: 1px; display: block; color: #856404;">Prescribed Satirical Sanction / Court Order:</span>
                {penalty}
            </div>
        </div>

        <!-- Distressed Rubber Stamp -->
        <div class="fir-rubber-stamp">{stamp_text}</div>

        <!-- Signatures & Disclaimer Footer -->
        <div class="fir-footer">
            <div class="fir-disclaimer">
                <strong>LEGAL DISCLAIMER:</strong> This is a satirical parody document generated exclusively for <em>TinkerHub Useless Projects</em>. It has no legal standing in any court, family gathering, or tea shop.
            </div>
            <div class="fir-signature-block">
                <div class="fir-signature-line">{io_name.split()[1] if len(io_name.split()) > 1 else 'Investigator'}...✍️</div>
                <div class="fir-officer-title"><strong>{io_name}</strong></div>
                <div style="font-size: 10px; color: #666;">{io_rank}, {io_station}</div>
                <div style="font-size: 9.5px; color: #888;">Badge ID: {io_badge}</div>
            </div>
        </div>

        <!-- Actions -->
        <div class="fir-action-bar">
            <button class="fir-btn" onclick="window.print()">🖨️ Print / Save FIR as PDF</button>
        </div>
    </div>
    """
    return card_html

# --- GRADIO APPLICATION INTERFACE ---

SAMPLE_FORWARDS = [
    ["UNESCO has declared the Indian National Anthem as the BEST in the universe! Share with 10 groups immediately or bad luck will follow! 🇮🇳🙏"],
    ["ATTENTION: Drinking hot lemon water with ginger and turmeric at 4:32 AM destroys all 5G radiation inside the human stomach! Forward fast before doctors delete this! 🍋⚡"],
    ["Urgent! Jio and Tata offering FREE 500GB 5G Recharge on Ambani grandson birthday. Click www.free-recharge-loot-5g-malayalam.xyz/win. Share with 15 friends! 🎁🔥"],
    ["Reserve Bank of India confirms 2000 rupee notes contain Secret Nano-GPS chips connected directly to Mangalyaan satellite 120m underground! 🛰️💵"],
    ["Good Morning! Sending 45 glittering hibiscus flower images with divine flute music to all 18 family groups. Have a blessed and vibration-filled day! 🌺☀️✨"]
]

custom_css = """
#app-container {
    max-width: 1260px;
    margin: 0 auto;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}
.header-badge {
    display: inline-block;
    background: #e63946;
    color: white;
    font-weight: bold;
    padding: 3px 10px;
    border-radius: 16px;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.status-ticker {
    font-size: 12px !important;
    color: #94a3b8 !important;
    padding: 6px 12px !important;
    border-radius: 6px !important;
    background: rgba(15, 23, 42, 0.6) !important;
    border: 1px solid #334155 !important;
    margin-bottom: 10px !important;
    display: block !important;
}
.status-ticker p {
    margin: 0 !important;
    font-size: 12px !important;
    line-height: 1.4 !important;
}
"""

def create_ui():
    custom_theme = gr.themes.Soft(
        primary_hue="red",
        secondary_hue="slate",
        neutral_hue="stone"
    )

    with gr.Blocks(title="FIR Report Generator | TinkerHub Useless Projects") as demo:
        with gr.Column(elem_id="app-container"):
            
            # App Header
            gr.Markdown(
                """
                # 🚨 WhatsApp Forward FIR Report Generator 📜
                ### *Kerala Digital Satya Pramanam Vibhagam (Cyber Satyameva Bureau — Special Family WhatsApp Cell)*
                
                <span class="header-badge">TinkerHub Useless Project 3.0</span>
                &nbsp; **Turning absurd family group forwards, fake cures, and 6 AM Good Morning spam into official-looking satirical police FIRs.**
                
                > ⚠️ **Satire Notice**: *Parody document created for hackathon entertainment. Not a real police complaint.*
                """
            )

            with gr.Row():
                # Left Column: Inputs & Controls (Lean & focused, scale=4)
                with gr.Column(scale=4):
                    gr.Markdown("### 📥 1. Paste WhatsApp Forward")
                    input_text = gr.Textbox(
                        label="Suspicious WhatsApp Forward / Rumor / Good Morning Spam",
                        placeholder="Paste suspicious forward here (e.g. UNESCO anthem award, hot lemon water 5G cure, Ambani 500GB recharge...)",
                        lines=5,
                        elem_id="input_box"
                    )

                    submit_btn = gr.Button("🚨 File FIR & Issue Arrest Warrant", variant="primary", size="lg")

                    with gr.Accordion("⚙️ Using your own HF token? Click here", open=False):
                        hf_token_input = gr.Textbox(
                            label="Hugging Face User Access Token (Optional)",
                            placeholder="hf_xxxxxxxxxxxxxxxxxxxxxxxx (uses built-in engine if blank)",
                            type="password"
                        )
                        gr.Markdown("<small>Optional. If blank or on timeout (>10s), our built-in satirical humor engine runs automatically.</small>")

                    with gr.Accordion("💡 Try a sample forward (Click to load)", open=False):
                        gr.Examples(
                            examples=SAMPLE_FORWARDS,
                            inputs=[input_text],
                            label="Common Kerala WhatsApp Forward Tropes"
                        )

                # Right Column: Generated FIR Document Hero (scale=7)
                with gr.Column(scale=7):
                    gr.Markdown("### 📜 2. Official Generated F.I.R. Document")
                    status_output = gr.Markdown("🟢 **System Ready** | Awaiting suspicious forward input...", elem_classes=["status-ticker"])
                    
                    fir_html_output = gr.HTML(
                        value="""
                        <div style="text-align: center; padding: 70px 20px; background: #faf6ea; border: 2px dashed #bbb; border-radius: 6px; color: #666; font-family: monospace;">
                            <h3>⚖️ NO ACTIVE CASE FILED</h3>
                            <p>Paste a WhatsApp forward on the left and click <strong>'File FIR'</strong> to generate an authentic official report with rubber stamps and penalties.</p>
                        </div>
                        """
                    )

            # Bottom Debug / Developer Accordion (out of primary view)
            with gr.Accordion("🛠️ Developer / Debug View (Raw JSON Schema)", open=False):
                raw_json_output = gr.Code(label="JSON Output", language="json")

            # Wire up interactions
            submit_btn.click(
                fn=generate_fir,
                inputs=[input_text, hf_token_input],
                outputs=[fir_html_output, raw_json_output, status_output]
            )

            # Footer
            gr.Markdown(
                """
                ---
                Made with ❤️ at **TinkerHub Useless Projects** | Team Astrava
                """
            )

    return demo, custom_theme, custom_css

if __name__ == "__main__":
    app, theme, css = create_ui()
    # Launch with local server
    app.launch(server_name="0.0.0.0", server_port=7860, theme=theme, css=css, share=False)

