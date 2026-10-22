"""Append predicted MSQs and normalize multi-select flags."""
import json
from pathlib import Path

path = Path(__file__).resolve().parent.parent / "data" / "predicted.json"
data = json.loads(path.read_text(encoding="utf-8"))

for q in data["questions"]:
    if isinstance(q.get("answer"), list):
        q["type"] = "msq"
        q["multi"] = True
        q["answer"] = sorted(str(x).lower() for x in q["answer"])
    else:
        q["multi"] = False
        if q.get("answer") is not None:
            q["answer"] = str(q["answer"]).lower()

new_msqs = [
    {
        "id": "p121",
        "week": 1,
        "type": "msq",
        "multi": True,
        "category": "definition",
        "likelihood": "high",
        "stem": "Which of the following are correctly treated as renewable natural resources?",
        "options": [
            {"key": "a", "text": "Solar radiation"},
            {"key": "b", "text": "Freshwater renewed by the hydrologic cycle"},
            {"key": "c", "text": "Coal seams"},
            {"key": "d", "text": "Wind"},
        ],
        "answer": ["a", "b", "d"],
        "explanation": "Solar and wind renew continuously; freshwater renews via the hydrologic cycle. Coal is non-renewable.",
    },
    {
        "id": "p122",
        "week": 1,
        "type": "msq",
        "multi": True,
        "category": "concept",
        "likelihood": "high",
        "stem": "Which combinations indicate an ecological deficit (EF = footprint, BC = biocapacity)?",
        "options": [
            {"key": "a", "text": "EF = 3, BC = 2"},
            {"key": "b", "text": "EF = 2, BC = 3"},
            {"key": "c", "text": "EF = 5, BC = 4"},
            {"key": "d", "text": "EF = 4, BC = 4"},
        ],
        "answer": ["a", "c"],
        "explanation": "Deficit when EF > BC.",
    },
    {
        "id": "p123",
        "week": 2,
        "type": "msq",
        "multi": True,
        "category": "concept",
        "likelihood": "high",
        "stem": "Which of the following are among the classic pillars of sustainable development?",
        "options": [
            {"key": "a", "text": "Social equity"},
            {"key": "b", "text": "Environmental / ecological integrity"},
            {"key": "c", "text": "Economic viability"},
            {"key": "d", "text": "Military expansion"},
        ],
        "answer": ["a", "b", "c"],
        "explanation": "Social, environmental, and economic pillars — not militarization.",
    },
    {
        "id": "p124",
        "week": 3,
        "type": "msq",
        "multi": True,
        "category": "definition",
        "likelihood": "high",
        "stem": "Which of the following are primary precursors of ground-level (tropospheric) ozone?",
        "options": [
            {"key": "a", "text": "Carbon monoxide only"},
            {"key": "b", "text": "Nitrogen oxides (NOx)"},
            {"key": "c", "text": "Elemental mercury"},
            {"key": "d", "text": "Volatile organic compounds (VOCs)"},
        ],
        "answer": ["b", "d"],
        "explanation": "Tropospheric O3 forms from NOx + VOCs in sunlight.",
    },
    {
        "id": "p125",
        "week": 3,
        "type": "msq",
        "multi": True,
        "category": "concept",
        "likelihood": "high",
        "stem": "Which are ozone-depleting substances (ODSs) targeted in classic Montreal Protocol teaching?",
        "options": [
            {"key": "a", "text": "CFCs"},
            {"key": "b", "text": "CO2"},
            {"key": "c", "text": "Halons"},
            {"key": "d", "text": "Some chlorinated ODS solvents historically used"},
        ],
        "answer": ["a", "c", "d"],
        "explanation": "CFCs/halons (and related ODSs) deplete stratospheric ozone; CO2 is mainly a GHG.",
    },
    {
        "id": "p126",
        "week": 4,
        "type": "msq",
        "multi": True,
        "category": "concept",
        "likelihood": "high",
        "stem": "Which major greenhouse gases also occur naturally in Earth's atmosphere?",
        "options": [
            {"key": "a", "text": "Carbon dioxide (CO2)"},
            {"key": "b", "text": "Methane (CH4)"},
            {"key": "c", "text": "Synthetic CFCs only (no natural source)"},
            {"key": "d", "text": "Water vapor (H2O)"},
        ],
        "answer": ["a", "b", "d"],
        "explanation": "CO2, CH4, and water vapor occur naturally; CFCs are synthetic.",
    },
    {
        "id": "p127",
        "week": 4,
        "type": "msq",
        "multi": True,
        "category": "concept",
        "likelihood": "medium",
        "stem": "Which are primary functions of the IPCC?",
        "options": [
            {"key": "a", "text": "Review and synthesize peer-reviewed climate science"},
            {"key": "b", "text": "Run its own global climate laboratory experiments as its main role"},
            {"key": "c", "text": "Assess impacts including socioeconomic dimensions"},
            {"key": "d", "text": "Produce assessment reports that inform policy"},
        ],
        "answer": ["a", "c", "d"],
        "explanation": "IPCC assesses literature and informs policy; it is not primarily an experimental lab.",
    },
    {
        "id": "p128",
        "week": 5,
        "type": "msq",
        "multi": True,
        "category": "formula",
        "likelihood": "high",
        "stem": "Which factors commonly limit practical solar PV electricity yield at a site?",
        "options": [
            {"key": "a", "text": "Available land or rooftop area"},
            {"key": "b", "text": "Solar resource / irradiance"},
            {"key": "c", "text": "Module conversion efficiency"},
            {"key": "d", "text": "The Betz limit for wind turbines"},
        ],
        "answer": ["a", "b", "c"],
        "explanation": "Betz limit applies to wind, not PV.",
    },
    {
        "id": "p129",
        "week": 5,
        "type": "msq",
        "multi": True,
        "category": "concept",
        "likelihood": "medium",
        "stem": "Which are recognized environmental concerns associated with wind energy?",
        "options": [
            {"key": "a", "text": "Bird and bat collisions"},
            {"key": "b", "text": "Habitat fragmentation from infrastructure"},
            {"key": "c", "text": "Noise and visual impacts"},
            {"key": "d", "text": "Direct CO2 emissions during operation comparable to coal plants"},
        ],
        "answer": ["a", "b", "c"],
        "explanation": "Operating turbines are not coal-like CO2 emitters; wildlife/noise/visuals are typical concerns.",
    },
    {
        "id": "p130",
        "week": 6,
        "type": "msq",
        "multi": True,
        "category": "concept",
        "likelihood": "high",
        "stem": "Which are potential benefits of biomass pretreatment for biofuel production?",
        "options": [
            {"key": "a", "text": "Increase surface area for enzymatic hydrolysis"},
            {"key": "b", "text": "Reduce cellulose crystallinity / improve digestibility"},
            {"key": "c", "text": "Help remove or alter lignin barriers"},
            {"key": "d", "text": "Directly finish conversion to retail gasoline with no further steps"},
        ],
        "answer": ["a", "b", "c"],
        "explanation": "Pretreatment prepares feedstock; it does not itself finish fuel production.",
    },
    {
        "id": "p131",
        "week": 6,
        "type": "msq",
        "multi": True,
        "category": "concept",
        "likelihood": "medium",
        "stem": "Which are common direct-use applications of geothermal energy?",
        "options": [
            {"key": "a", "text": "Space/district heating"},
            {"key": "b", "text": "Greenhouse heating"},
            {"key": "c", "text": "Some industrial process heat"},
            {"key": "d", "text": "Powering photosynthesis inside leaves"},
        ],
        "answer": ["a", "b", "c"],
        "explanation": "Direct-use geothermal heats buildings/processes; photosynthesis is solar-driven.",
    },
    {
        "id": "p132",
        "week": 7,
        "type": "msq",
        "multi": True,
        "category": "definition",
        "likelihood": "high",
        "stem": "Which strategies align with a circular economy (not linear take-make-dispose)?",
        "options": [
            {"key": "a", "text": "Product reuse and remanufacturing"},
            {"key": "b", "text": "Design for disassembly and recycling"},
            {"key": "c", "text": "Industrial symbiosis"},
            {"key": "d", "text": "Maximizing single-use disposal without recovery"},
        ],
        "answer": ["a", "b", "c"],
        "explanation": "Circular strategies keep materials in use.",
    },
    {
        "id": "p133",
        "week": 8,
        "type": "msq",
        "multi": True,
        "category": "definition",
        "likelihood": "high",
        "stem": "Which statements about water withdrawal vs consumption are correct?",
        "options": [
            {"key": "a", "text": "Withdrawal is water taken from a source"},
            {"key": "b", "text": "Consumption is the portion not returned to the source"},
            {"key": "c", "text": "Withdrawal and consumption are always identical"},
            {"key": "d", "text": "Cooling water returned to a river is largely withdrawn but not fully consumed"},
        ],
        "answer": ["a", "b", "d"],
        "explanation": "Returned water counts as withdrawal more than consumption.",
    },
    {
        "id": "p134",
        "week": 9,
        "type": "msq",
        "multi": True,
        "category": "concept",
        "likelihood": "high",
        "stem": "Which belong near the top of the ISWM hierarchy (preferred first)?",
        "options": [
            {"key": "a", "text": "Prevention / reduction at source"},
            {"key": "b", "text": "Reuse"},
            {"key": "c", "text": "Recycling / recovery"},
            {"key": "d", "text": "Uncontrolled open dumping as first choice"},
        ],
        "answer": ["a", "b", "c"],
        "explanation": "Prevention, reuse, recycling beat dumping.",
    },
    {
        "id": "p135",
        "week": 10,
        "type": "msq",
        "multi": True,
        "category": "definition",
        "likelihood": "high",
        "stem": "Which statements about TTS vs PTS are correct?",
        "options": [
            {"key": "a", "text": "TTS is temporary hearing sensitivity loss that can recover"},
            {"key": "b", "text": "PTS is lasting hearing damage"},
            {"key": "c", "text": "PTS always recovers fully within minutes"},
            {"key": "d", "text": "Repeated TTS exposures can raise risk of permanent damage"},
        ],
        "answer": ["a", "b", "d"],
        "explanation": "TTS recovers; PTS does not.",
    },
    {
        "id": "p136",
        "week": 11,
        "type": "msq",
        "multi": True,
        "category": "concept",
        "likelihood": "high",
        "stem": "Which are examples of regulating ecosystem services?",
        "options": [
            {"key": "a", "text": "Climate regulation by forests"},
            {"key": "b", "text": "Flood regulation"},
            {"key": "c", "text": "Nutrient cycling (typically a supporting service)"},
            {"key": "d", "text": "Disease regulation"},
        ],
        "answer": ["a", "b", "d"],
        "explanation": "Nutrient cycling is classically supporting, not regulating.",
    },
    {
        "id": "p137",
        "week": 11,
        "type": "msq",
        "multi": True,
        "category": "concept",
        "likelihood": "medium",
        "stem": "Which statements about ecosystem energy flow are correct?",
        "options": [
            {"key": "a", "text": "Energy transfer between trophic levels is 100% efficient"},
            {"key": "b", "text": "Solar energy is the primary energy source for most ecosystems"},
            {"key": "c", "text": "Chemical energy in biomass moves through food webs"},
            {"key": "d", "text": "Energy is fully recycled like nutrients in closed loops"},
        ],
        "answer": ["b", "c"],
        "explanation": "Energy flows and dissipates; nutrients cycle.",
    },
    {
        "id": "p138",
        "week": 12,
        "type": "msq",
        "multi": True,
        "category": "law",
        "likelihood": "high",
        "stem": "Which legal ideas are strongly associated with landmark Indian environmental cases in this course?",
        "options": [
            {"key": "a", "text": "Absolute liability (Oleum Gas Leak)"},
            {"key": "b", "text": "Polluter Pays (e.g., Vellore)"},
            {"key": "c", "text": "Public Trust Doctrine (e.g., Kamal Nath)"},
            {"key": "d", "text": "Unlimited right to pollute if any tax is paid"},
        ],
        "answer": ["a", "b", "c"],
        "explanation": "Oleum, Vellore, and Kamal Nath map to absolute liability, polluter pays, and public trust.",
    },
    {
        "id": "p139",
        "week": 12,
        "type": "msq",
        "multi": True,
        "category": "law",
        "likelihood": "medium",
        "stem": "Which statements about the National Green Tribunal (NGT) are generally correct?",
        "options": [
            {"key": "a", "text": "It is a specialized forum for environmental disputes"},
            {"key": "b", "text": "It can apply principles like polluter pays and precautionary principle"},
            {"key": "c", "text": "It replaces the need for any environmental statutes in India"},
            {"key": "d", "text": "It was created by statute to provide faster environmental adjudication"},
        ],
        "answer": ["a", "b", "d"],
        "explanation": "NGT is a specialized statutory tribunal; it does not erase other env. laws.",
    },
    {
        "id": "p140",
        "week": 3,
        "type": "msq",
        "multi": True,
        "category": "concept",
        "likelihood": "medium",
        "stem": "Under a strong elevated inversion, which statements are plausible for stack emissions?",
        "options": [
            {"key": "a", "text": "Pollutants emitted below the inversion can be trapped near the surface"},
            {"key": "b", "text": "Poor dispersion can worsen local air quality"},
            {"key": "c", "text": "Inversions always improve vertical mixing"},
            {"key": "d", "text": "Emission height relative to the inversion layer matters"},
        ],
        "answer": ["a", "b", "d"],
        "explanation": "Inversions suppress mixing; trapping and stack height relative to the lid matter.",
    },
]

existing = {q["id"] for q in data["questions"]}
added = 0
for q in new_msqs:
    if q["id"] not in existing:
        data["questions"].append(q)
        added += 1

msq_count = sum(
    1
    for q in data["questions"]
    if q.get("type") == "msq" or isinstance(q.get("answer"), list)
)
data["meta"] = {
    "count": len(data["questions"]),
    "msqCount": msq_count,
    "note": "High-chance exam-style MCQs + MSQs from weekly patterns",
}

path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Total={data['meta']['count']} MSQ={msq_count} added={added}")
