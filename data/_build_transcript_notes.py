#!/usr/bin/env python3
"""Build exam-oriented transcript-notes.json for all 60 NPTEL EVS lectures."""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).with_name("transcript-notes.json")

# Curated titles (refined from transcript headers)
TITLES = {
    1: "Major Environmental Concerns and Pollution",
    2: "Population Growth Models",
    3: "Resource Consumption and Pollution",
    4: "Measuring Impacts - IPAT and Ecological Footprint",
    5: "Earth Overshoot Day, EPI, LCA",
    6: "Principles of Sustainable Development",
    7: "Sustainable Development Goals (SDGs)",
    8: "Achieving SDGs and Sustainability Indices",
    9: "Sustainable Urbanization (Case Study I)",
    10: "Green Buildings (Case Study II)",
    11: "Air Pollution - Definition, Causes, Sources and Types",
    12: "Air Pollution - Influence of Meteorology",
    13: "Air Pollution - Local Effects and Mitigation",
    14: "Air Pollution - Regional Issues and Mitigation",
    15: "Air Pollution - Global Issues, Ozone and Indoor Air",
    16: "Climate Change - Definition and Evidence",
    17: "Climate Change - Causes and Determinants",
    18: "Climate Change - Projections and Impacts",
    19: "Climate Change - Mitigation Strategies",
    20: "Climate Change - International Treaties and Adaptation",
    21: "Renewable Energy I - Overview",
    22: "Renewable Energy I - Solar Energy I (CSP)",
    23: "Renewable Energy I - Solar Energy II (Photovoltaics)",
    24: "Renewable Energy I - Solar Energy III (Thermal and Fuels)",
    25: "Renewable Energy I - Wind Energy",
    26: "Renewable Energy II - Geothermal Energy",
    27: "Renewable Energy II - Ocean Energy I (Tidal and Wave)",
    28: "Renewable Energy II - Ocean Energy II (OTEC and Others)",
    29: "Renewable Energy II - Hydropower",
    30: "Renewable Energy II - Bioenergy",
    31: "Circular Economy - Introduction and Urban Metabolism",
    32: "Circular Economy Strategies I (9R Framework)",
    33: "Circular Economy Strategies II (Remaining Rs)",
    34: "Circular Business Models",
    35: "Industrial Symbiosis and Industrial Ecology",
    36: "Hydrologic Cycle, Water Sources and Pollution",
    37: "Water Quality Parameters - General",
    38: "Oxygen-Demanding Wastes and Microbial Indicators",
    39: "Nitrogen Species and the DO Sag Curve",
    40: "NGT, WQI and Wastewater Reuse/Recycling",
    41: "Importance and Integrated Solid Waste Management",
    42: "MSW Sources, Generation Rates and Composition",
    43: "MSW Composition and Collection",
    44: "MSW Treatment and Disposal",
    45: "E-Waste Management",
    46: "Sound, Noise and Characteristics",
    47: "Audiometry",
    48: "Effects of Noise",
    49: "Noise Rating Systems and Modeling",
    50: "Noise Control and Regulations",
    51: "Fundamentals of Ecology I",
    52: "Fundamentals of Ecology II",
    53: "Fundamentals of Ecology III",
    54: "Soil Pollution I",
    55: "Soil Pollution II",
    56: "The Environmental Movement - Global and Local Impacts",
    57: "Environmental Law and Rules in India",
    58: "Important Legal Judgments on the Environment",
    59: "NGT and Important Judgments",
    60: "Rapid EIA - River Ib Barrage Case Study",
}

# lec -> (objectives[3-5], keywords[8-12], likelyFacts[3], mnemonic|None, summary)
NOTES: dict[int, tuple] = {}

def N(lec, objectives, keywords, facts, mnemonic, summary):
    NOTES[lec] = (objectives, keywords, facts, mnemonic, summary)

# --- Week 1 ---
N(1,
  ["Distinguish pollutant from contaminant and list major media of concern (air, water, soil, biodiversity).",
   "Relate urbanization and waste heat to Urban Heat Island effects.",
   "Frame course goal: live off natural-capital interest, not the capital stock.",
   "List principles: maximize renewables, minimize non-renewables, protect biodiversity, nutrient cycling."],
  ["pollutant", "contaminant", "biodiversity", "Urban Heat Island", "natural capital", "natural services", "sustainable development", "pollution", "air-water-soil", "MC Mehta education"],
  ["A contaminant is out of place or above background; a pollutant causes adverse effects at given concentration/duration.",
   "MC Mehta vs UOI (1991) led to an environmental education mandate in India.",
   "Course framing: treat environment+economy+society as capital and live on interest, not principal."],
  "Contaminant = misplaced; pollutant = harmful.",
  "Lecture 1 opens Environmental Science by mapping major concerns—air, water, soil and biodiversity loss—to pollution. Contaminant versus pollutant is an exam staple: presence out of place versus proven harm. Urban Heat Islands show how built form and waste heat raise city temperatures above rural surrounds. Sustainable living is cast as protecting natural capital and services rather than liquidating them. The week roadmap previews population models, resource use and impact metrics (IPAT, footprint, EPI, LCA)."
)

N(2,
  ["State Brundtland (1987) definition of sustainable development.",
   "Apply arithmetic, geometric and exponential population formulas and compare results.",
   "Interpret R^2 for census curve-fitting (good >0.9; very good >0.95).",
   "Connect Tragedy of the Commons to unmanaged shared resources."],
  ["Brundtland", "Our Common Future", "arithmetic growth", "geometric growth", "exponential growth", "curve fitting", "R^2", "Tragedy of the Commons", "census", "carrying capacity foreshadow"],
  ["Pn = P0 + nX (arithmetic); Pn = P0(1+r)^n (geometric); Pn = P0 e^(rn) (exponential).",
   "For same r, exponential > geometric (e.g. r=0.1, n=10: 2718 vs 2594 from P0=1000).",
   "India census series often fit exponential with R^2>0.95 (~1.75%/y total; urban ~2.85%/y)."],
  "Geo steps yearly; expo grows every instant.",
  "Lecture 2 pairs Brundtland sustainable development (1987) with three growth models used for census curve-fitting. Arithmetic growth adds a fixed increment; geometric compounds discretely; exponential compounds continuously. High R^2 indicates a good fit to historical population. Tragedy of the Commons motivates why open-access resources degrade without institutions. These tools set up later IPAT and footprint lectures linking people to impacts."
)

N(3,
  ["Classify resources as perpetual, renewable or non-renewable (incl. deep groundwater).",
   "Define natural capital versus natural services.",
   "Contrast Agropolis, Petropolis and Ecopolis city metaphors.",
   "Contrast linear versus circular economy at introductory level."],
  ["perpetual resources", "renewable", "non-renewable", "natural capital", "natural services", "Agropolis", "Petropolis", "Ecopolis", "linear economy", "circular economy", "green design"],
  ["Perpetual: solar, wind, tides; renewable: air, water, soil, biota; non-renewable: fossil fuels, minerals, deep groundwater.",
   "Cities framed as Agropolis (agrarian), Petropolis (fossil-fuel), Ecopolis (ecological design).",
   "Linear take-make-waste vs circular borrow-use-return is introduced with green/sustainable design."],
  "Sun/wind perpetual; fossils non-renewable.",
  "Resource consumption drives pollution when throughput exceeds regeneration. Resources are perpetual (solar/wind/tides), renewable (soil, biota, water) or non-renewable (fossils, metals; deep groundwater treated as non-renewable). Natural capital is the stock; natural services are the flows supporting well-being. City types Agropolis–Petropolis–Ecopolis illustrate metabolic styles. Early circular-economy language prepares Week 7."
)

N(4,
  ["Write and interpret IPAT: I = P × A × T (Ehrlich & Holdren, 1971).",
   "Choose affluence and technology proxies (e.g. kWh/cap; kg CO2/kWh).",
   "Define ecological footprint in global hectares and contrast with biocapacity.",
   "Use EFproduction = P × EQF / Yw conceptually."],
  ["IPAT", "Ehrlich Holdren", "affluence", "technology", "ecological footprint", "biocapacity", "global hectare", "EQF", "yield", "impact metric"],
  ["I = P × A × T; growth rates of factors roughly add in percent terms when multiplying.",
   "Global course figures: ~2.8 gha footprint/person vs ~1.6 gha biocapacity/person.",
   "Footprint is demand; biocapacity is nature's supply — deficit means overshoot."],
  "I Pat the planet as P, A, T rise.",
  "IPAT multiplies Population, Affluence and Technology to estimate environmental Impact—classic for MCQs and word problems (e.g. CO2 = pop × fossil kWh/cap × kg CO2/kWh). Ecological footprint converts resource use and waste absorption into global hectares using yields and equivalence factors. Comparing footprint to biocapacity diagnoses surplus or deficit. Lecture 4 is the quantitative heart of Week 1 impact measurement."
)

N(5,
  ["Explain Earth Overshoot Day as the date demand exceeds annual biocapacity.",
   "Compute Energy Performance Index: EPI = annual kWh / floor area (kWh/m²·y).",
   "Outline Lifecycle Assessment stages from raw materials through disposal.",
   "Note why multi-year utility bills stabilize campus EPI."],
  ["Earth Overshoot Day", "biocapacity", "EPI", "Energy Performance Index", "LCA", "lifecycle assessment", "kWh/m2-y", "campus energy", "carbon footprint link", "impact metrics"],
  ["Overshoot Day marks when cumulative human demand exceeds what Earth regenerates that year (often late July recently; 22 Aug 2020 COVID anomaly).",
   "EPI = E_annual / A_floor in kWh/m²·y; use 3–5 years of bills for a stable value.",
   "LCA inventories inputs/outputs across cradle-to-grave stages for products or systems."],
  "Overshoot = Earth's yearly paycheck spent early.",
  "Earth Overshoot Day calendars ecological deficit: after that date humanity lives on overdraft. EPI normalizes building or campus electricity to floor area for fair comparison. Lifecycle Assessment prevents burden-shifting by tracking impacts from materials through use to end-of-life. Together with IPAT and footprints, these tools quantify sustainability performance for exams and campus projects."
)

# --- Week 2 ---
N(6,
  ["Recall Brundtland definition and Why SD is needed (live within ecological means).",
   "Place SD on the timeline: 1987 Brundtland → 1992 Rio.",
   "Name three pillars: environment, economy, society.",
   "Introduce planetary boundaries / safe operating space idea."],
  ["sustainable development", "Brundtland 1987", "Rio 1992", "planetary boundaries", "safe operating space", "three pillars", "Anthropocene", "ecological means", "Our Common Future"],
  ["Brundtland 1987: meet present needs without compromising future generations.",
   "Rio Earth Summit 1992 institutionalized the global sustainable development agenda.",
   "Three interdependent pillars: environment, economy, society."],
  "1987 Brundtland → 1992 Rio.",
  "Week 2 opens by arguing solutions require living within planetary means. Brundtland's 1987 definition anchors every MCQ on SD wording. Rio 1992 moved SD into international policy. Pillars insist environment cannot be traded away for GDP alone. Planetary-boundaries framing (safe operating space) motivates later SDG and Anthropocene content."
)

N(7,
  ["State SDG count (17), adoption year (2015) and horizon (2030 Agenda).",
   "Contrast MDGs (8, developing-focused) with universal SDGs.",
   "Identify environment-heavy SDGs: 6, 7, 11, 12, 13, 14, 15.",
   "Note 169 targets as the detailed to-do list under goals."],
  ["SDGs", "2030 Agenda", "MDGs", "17 goals", "169 targets", "UN 2015", "SDG 6 water", "SDG 13 climate", "universal goals", "indicators"],
  ["SDGs adopted 2015 by all UN Member States; 17 goals with 169 targets to 2030.",
   "MDGs (2000) had 8 goals mainly for developing countries; SDGs are universal and broader.",
   "Env spine often tested: SDGs 6, 7, 11, 12, 13, 14, 15."],
  "6-7-11-12-13-14-15 green spine.",
  "Lecture 7 details the 2030 Agenda: seventeen Sustainable Development Goals replacing/expanding MDGs. Universality (every country) and climate/oceans/cities content distinguish SDGs. Targets and indicators operationalize goals for monitoring. Memorize year 2015, count 17, and environment-linked goal numbers for high-yield MCQs."
)

N(8,
  ["Explain six SDG transformations as cross-cutting pathways.",
   "Define SDG Index as a composite progress score.",
   "Link Rockström/Steffen planetary boundaries to monitoring risk.",
   "Argue that dropping one transformation hurts multiple goals."],
  ["SDG transformations", "sustainability indices", "SDG Index", "Rockstrom", "Steffen", "planetary boundaries", "monitoring", "indicators 2017", "Great Acceleration"],
  ["Six transformations map onto multiple SDGs—neglecting one undermines several goals.",
   "Planetary boundaries: Rockström 2009; update Steffen 2015 — nine Earth-system processes.",
   "SDG Index aggregates country performance across indicators for ranking/progress tracking."],
  "Transformations bridge many goals at once.",
  "Achieving SDGs needs systemic transformations, not siloed projects. Sustainability indices (including SDG Index) turn sprawling targets into comparable scores. Planetary-boundary science supplies biophysical guardrails alongside socio-economic indicators. Anthropocene/Great Acceleration charts justify urgency. Exam focus: authors/years of boundaries papers and the transformations logic."
)

N(9,
  ["Explain why urbanization is central to sustainable development (SDG 11).",
   "Identify urban challenges: density, services, emissions, inequality.",
   "List levers for sustainable cities: transit, density, green space, resource efficiency.",
   "Connect urban form to earlier Petropolis/Ecopolis ideas."],
  ["sustainable urbanization", "SDG 11", "cities", "urban density", "infrastructure", "urban services", "emissions", "case study", "livability", "resource efficiency"],
  ["SDG 11 targets inclusive, safe, resilient and sustainable cities.",
   "Urbanization concentrates both impacts and solutions (efficiency of shared infrastructure).",
   "Sustainable urbanization couples housing, mobility, water/waste and energy planning."],
  "Cities are SDG 11's battleground.",
  "Case Study I applies SD principles to cities where most future growth occurs. Compact, well-served urban form can lower per-capita footprints if paired with clean energy and circular waste/water systems. Risks include sprawl, congestion and unequal access. The lecture bridges Week 2 theory to built-environment practice ahead of green buildings."
)

N(10,
  ["Define green building goals: energy, water, materials, indoor environment.",
   "Relate EPI and LCA from Week 1 to building performance.",
   "List typical certification themes (efficiency, daylight, recycled content).",
   "Explain how green buildings support sustainable urbanization."],
  ["green buildings", "energy efficiency", "indoor environmental quality", "EPI", "LCA", "sustainable design", "certification", "water efficiency", "materials", "urbanization"],
  ["Green buildings cut operational energy/water and improve indoor quality while lowering lifecycle impacts.",
   "Campus/building EPI (kWh/m²·y) is a practical performance metric from Lecture 5.",
   "Material choices and LCA prevent shifting burdens from use phase to manufacturing."],
  "Green building = less EPI, better IEQ.",
  "Concluding Week 2, green buildings operationalize sustainable urbanization: envelopes, HVAC, lighting, water fixtures and healthier interiors. Performance metrics like EPI and whole-building LCA link design to measurable outcomes. Certification schemes organize criteria but principles matter more for exams: reduce loads first, then supply efficiently, then verify."
)

# --- Week 3 ---
N(11,
  ["Define air pollution and ambient (outdoor) air.",
   "Classify primary vs secondary pollutants; criteria vs non-criteria.",
   "Map sources: stationary, mobile, area.",
   "Give examples (SO2, NO, CO, primary PM vs O3, secondary PM)."],
  ["air pollution", "ambient air", "primary pollutant", "secondary pollutant", "criteria pollutants", "stationary source", "mobile source", "area source", "PM2.5", "ozone"],
  ["Ambient air = outdoor atmospheric air supporting life.",
   "Primary emitted directly; secondary formed in air (e.g. tropospheric O3, secondary PM).",
   "Source inventory axes: stationary / mobile / area."],
  "Primary exits stack; secondary cooked in sunlight.",
  "Week 3 starts with definitions: substances at harmful concentration or duration. Criteria pollutants have ambient standards; hazardous/non-criteria include many toxics. Orthogonal classifications—primary/secondary and stationary/mobile/area—structure every air-quality MCQ. Tropospheric ozone is secondary; do not confuse with stratospheric ozone depletion later."
)

N(12,
  ["Explain how meteorology controls dilution: wind, mixing height, stability.",
   "Relate inversions to high ground-level concentrations.",
   "Describe plume behavior qualitatively (looping, lofting, fanning, fumigation).",
   "State why calm, stable nights worsen urban pollution."],
  ["meteorology", "mixing height", "atmospheric stability", "inversion", "dispersion", "wind speed", "plume", "dilution", "boundary layer", "concentration"],
  ["Higher wind and deeper mixing height increase dilution and lower concentrations.",
   "Temperature inversions trap pollutants near the surface.",
   "Stability class strongly shapes plume rise and ground-level impact."],
  "Calm + inversion = pollution trap.",
  "Once emitted, pollutants' fate depends on meteorology more than chemistry alone. Mixing height and wind set the dilution volume; inversions create lids. Plume types under different stability are classic short-answer material. This lecture links emission inventories to observed ambient peaks (e.g. winter nights)."
)

N(13,
  ["List local effects: visibility loss, vegetation injury, materials corrosion, health.",
   "Name particulate controls: cyclone, ESP, baghouse (~95–99% industrially).",
   "Introduce gaseous controls including scrubbers.",
   "Link combustion stoichiometry to SO2/ash from coal sulfur/ash content."],
  ["local effects", "ESP", "baghouse", "cyclone", "scrubber", "visibility", "health effects", "control technology", "fly ash", "SO2"],
  ["Industrial particulate controls (ESP/fabric filters) often achieve 95–99% removal.",
   "Local impacts include smog, crop damage, building soiling/corrosion and respiratory disease.",
   "Coal S → SO2 emission stoichiometry problems recur in assignments."],
  "ESP/baghouse catch the dust first.",
  "Local mitigation focuses on source controls near receptors. Particulate devices and scrubbers are high-yield tech names with efficiency ranges. Health and materials damage justify standards. Stoichiometry ties fuel composition to emission rates—practice numericals alongside qualitative effects."
)

N(14,
  ["Define transboundary / regional air pollution (acid rain, haze).",
   "Explain acid deposition from SO2/NOx precursors.",
   "Cite ASEAN Haze Agreement (2002) as regional treaty example.",
   "Contrast local stack control with regional precursor agreements."],
  ["transboundary pollution", "acid rain", "regional haze", "ASEAN Haze Agreement", "SO2", "NOx", "long-range transport", "treaty", "mitigation", "deposition"],
  ["Transboundary pollution crosses political borders via atmospheric transport.",
   "ASEAN Agreement on Transboundary Haze Pollution: 2002 (ratifications progressed later).",
   "Acid rain mitigation requires regional SO2/NOx cuts, not only local stacks."],
  "Haze ignores borders — ASEAN 2002.",
  "Regional issues arise when pollutants travel hundreds of kilometers. Acid deposition and seasonal haze need cooperative treaties and precursor controls. FGD and NOx strategies reappear as engineering tools inside policy frameworks. Distinguish regional chemistry from global ozone and climate topics in Lecture 15–20."
)

N(15,
  ["Explain stratospheric ozone depletion vs tropospheric ozone pollution.",
   "State Montreal Protocol (1987) for ODS (CFCs/halons).",
   "Describe indoor/household air pollution sources and high mortality burden.",
   "Contrast outdoor meteorology-driven exposure with confined indoor exposure."],
  ["Montreal Protocol", "ozone depletion", "CFCs", "indoor air pollution", "household fuels", "stratosphere", "ODS", "3.2 million deaths", "global issues", "mitigation"],
  ["Montreal Protocol 1987 controls ozone-depleting substances — not a climate Kyoto/Paris substitute.",
   "Course cites ~3.2 million deaths/year (2020) from household air pollution.",
   "Stratospheric O3 protects from UV; tropospheric O3 is a harmful secondary pollutant."],
  "Montreal 1987 ≠ Kyoto/Paris.",
  "Global air issues culminate in the ozone hole story and Montreal Protocol success narrative. Indoor air from cooking/heating fuels can dominate personal exposure. Keep three O3 stories separate: good stratospheric shield, bad ground-level smog, and protocol politics. This closes the air-pollution week."
)

# --- Week 4 ---
N(16,
  ["Distinguish weather (short-term) from climate (decades+ statistics).",
   "List observational indicators: temperature, ice loss, sea level, ocean heat.",
   "State warming rate ~0.18 °C/decade since 1981 (course).",
   "Argue climate change evidence is multi-indicator, not one thermometer."],
  ["weather", "climate", "climate change", "indicators", "sea level", "Arctic sea ice", "ocean heat", "temperature anomaly", "evidence", "IPCC framing"],
  ["Weather = hours–days; climate = long-term averages and extremes (often ~30-year normals).",
   "Course warming rate since 1981 ≈ 0.18 °C per decade.",
   "Sept 2012 Arctic sea ice cited as record low (~44% below long-term)."],
  "Weather is today's outfit; climate is the wardrobe.",
  "Climate-change week opens with definitions and evidence. Unequivocal warming appears across atmosphere, ocean, cryosphere and sea level. Multi-indicator consistency underpins IPCC-style certainty language. Memorize weather/climate contrast and the course's quantitative evidence hooks."
)

N(17,
  ["Explain natural vs enhanced greenhouse effect.",
   "List key GHGs: CO2, CH4, N2O, CFCs, H2O vapor.",
   "Define GWP with CO2 = 1 by definition.",
   "Describe albedo feedback from ice loss."],
  ["greenhouse effect", "GHG", "GWP", "CO2", "CH4", "N2O", "albedo", "climate forcing", "radiative forcing", "infrared"],
  ["GHGs are largely transparent to shortwave but absorb outgoing IR.",
   "GWP(CO2) = 1; other gases scaled over a chosen time horizon.",
   "Ice–albedo feedback: melting lowers albedo → more absorption → more warming."],
  "Carbon Methane Nitro CFC Water trap IR.",
  "Causes lecture covers forcings and greenhouse gases that maintain (and enhance) Earth's heat balance. GWP enables apples-to-apples comparisons. Albedo and other feedbacks amplify initial warming. Exam trap: water vapor is a GHG but mainly a feedback, while CO2 is the primary anthropogenic control knob emphasized in policy."
)

N(18,
  ["Summarize projected impacts on cryosphere, oceans, weather extremes, food systems.",
   "Link ocean warming/acidification to marine life stress.",
   "Note differential vulnerability of polar and high-mountain regions.",
   "Separate observed trends from model-based projections."],
  ["climate impacts", "projections", "cryosphere", "ocean acidification", "extremes", "agriculture", "sea level rise", "coral", "vulnerability", "IPCC scenarios"],
  ["Impacts span ice melt, sea-level rise, marine ecosystems, extreme weather and livestock/crops.",
   "Oceans absorb heat and CO2 → warming plus acidification risks for calcifiers.",
   "High mountains and poles show amplified, visible changes (glaciers, permafrost, ice sheets)."],
  "Impacts hit ice, ocean, extremes, food.",
  "Projections translate forcings into sectoral risks. Cryosphere loss and ocean change are physically linked to coastal and food-security outcomes. Extreme-event attribution language appears in modern IPCC reports. For exams, organize answers by system (ice/ocean/weather/biosphere) rather than listing unrelated calamities."
)

N(19,
  ["Define mitigation: cut emissions / enhance sinks.",
   "List mitigation wedges: efficiency, renewables, sinks, fuel switching.",
   "Contrast mitigation with adaptation (preview).",
   "Connect mitigation need to renewable-energy weeks ahead."],
  ["mitigation", "emission reduction", "carbon sinks", "renewables", "energy efficiency", "decarbonization", "afforestation", "fuel switching", "climate action"],
  ["Mitigation reduces sources or enhances sinks of GHGs.",
   "Major levers: demand reduction, clean electricity, electrification, land sinks.",
   "Mitigation addresses the cause; adaptation manages residual risk."],
  "Mitigation turns down the stove.",
  "Mitigation strategies operationalize 'avoid unmanageable' climate change. Technology and behavior packages appear as portfolios, not silver bullets. This lecture foreshadows Weeks 5–6 renewables and Week 7 circularity as mitigation-compatible pathways. Keep definition crisp for short answers."
)

N(20,
  ["Timeline: UNFCCC 1992 → Kyoto 1997 (force 2005) → Paris 2015.",
   "Contrast Kyoto Annex I binding targets vs Paris NDCs for all parties.",
   "Recall Kyoto ~5.2% below 1990; Doha ≥18% by 2020.",
   "Define adaptation and note IPCC/Nobel 2007 context."],
  ["UNFCCC", "Kyoto Protocol", "Paris Agreement", "NDC", "COP21", "adaptation", "Annex I", "IPCC", "Nobel 2007", "Doha Amendment"],
  ["UNFCCC opened 1992 at Rio; Kyoto 1997 entered force 2005; Paris 2015 (COP21).",
   "Kyoto bound Annex I (~5.2% below 1990); Paris uses nationally determined contributions toward well-below-2 °C / 1.5 °C.",
   "IPCC and Al Gore shared Nobel Peace Prize 2007."],
  "Kyoto bound Annex I; Paris asks all for NDCs.",
  "Governance lecture closes climate week: science meets treaties. Kyoto's gas list and Annex I logic differ from Paris's universal NDC architecture. Adaptation reduces vulnerability to locked-in impacts alongside mitigation. Timeline years are among the highest-frequency MCQs in the course."
)

# --- Week 5 ---
N(21,
  ["Define renewable energy (replenished ≥ rate of use).",
   "State energy trilemma SEE: Security, Equity, Environmental sustainability.",
   "Cite course stats: solar input ~5.4M EJ/y; renewables ~12.6% TFEC (2020).",
   "Argue renewables for climate mitigation and SDG 7."],
  ["renewable energy", "energy trilemma", "SEE", "SDG 7", "technical potential", "capacity factor", "intermittency", "final energy", "climate mitigation", "overview"],
  ["Renewable = replenished at least as fast as consumed.",
   "Energy trilemma: Security, Equity, Environmental sustainability (SEE).",
   "Course: incoming solar ~5.4 million EJ/year; renewables ~12.6% of TFEC (2020)."],
  "Healthy grids must SEE clearly.",
  "Overview frames why renewables matter: climate, energy access and security. Trilemma SEE organizes trade-offs on exams. Distinctions among resource, technical potential and capacity factor prevent confusion with nameplate capacity. Intermittency foreshadows storage needs before solar and wind deep-dives."
)

N(22,
  ["Explain concentrating solar power (CSP) using mirrors to raise temperature.",
   "Contrast CSP thermal generation with later PV electricity.",
   "Note thermal storage advantage of some CSP designs.",
   "List typical CSP optics: troughs, towers, dishes (conceptually)."],
  ["CSP", "concentrating solar", "mirrors", "solar thermal power", "heliostat", "thermal storage", "direct normal irradiance", "solar field", "heat transfer fluid"],
  ["CSP concentrates sunlight with mirrors to drive heat engines / steam turbines.",
   "Some CSP plants integrate thermal storage for after-sunset generation.",
   "CSP needs strong direct normal irradiance — geography matters."],
  "CSP = mirrors make heat, then power.",
  "Solar Energy I emphasizes concentration pathways. Unlike PV, CSP is a thermal power plant with optical fields. Storage in molten salt systems is a frequent comparison point versus battery-backed PV. Site quality (DNI) is as important as collector efficiency."
)

N(23,
  ["Describe photovoltaic conversion of light to DC electricity.",
   "Contrast PV with CSP (photons→electrons vs heat→turbine).",
   "Note modularity and distributed generation strengths of PV.",
   "Mention inverter role and capacity-factor dependence on irradiance."],
  ["photovoltaics", "PV", "solar cell", "semiconductor", "inverter", "distributed generation", "irradiance", "module", "DC to AC", "solar energy"],
  ["PV converts sunlight directly to electricity via semiconductor junctions.",
   "PV is modular from rooftop to utility scale; CSP is typically utility thermal.",
   "Output tracks irradiance; capacity factor is climate- and tilt-dependent."],
  "PV: light in, electrons out.",
  "Solar Energy II centers on photovoltaics as the rapidly scaling solar pathway. Exam answers should contrast energy conversion physics and suitable applications versus CSP. Balance-of-system (inverters, mounting) and intermittency remain practical constraints linking to storage discussion."
)

N(24,
  ["Differentiate active solar thermal systems (collectors, pumps) for heat.",
   "Introduce solar fuels / solar-driven chemical pathways conceptually.",
   "Relate low-grade solar heat to buildings and process heat.",
   "Position solar thermal heat as distinct from CSP electricity."],
  ["solar thermal", "active solar", "solar collectors", "solar fuels", "process heat", "domestic hot water", "passive vs active", "thermal energy", "solar chemistry"],
  ["Active solar thermal uses collectors and often pumps/controls to deliver heat.",
   "Solar fuels aim to store solar energy in chemical form for later use.",
   "Building/process heat can be a higher-efficiency use of sunlight than electricity alone."],
  "Thermal solar heats; fuels store sunshine chemically.",
  "Solar Energy III widens the portfolio beyond electricity: water heating, industrial heat and emerging solar fuels. Active systems contrast with passive building design. For exams, keep three solar buckets clear—CSP power, PV power, and thermal/fuel pathways."
)

N(25,
  ["Write wind power P = ½ ρ A v³ and Betz limit CP,max = 16/27 ≈ 59.3%.",
   "Derive Pmax = (8/27) ρ A v³.",
   "Explain why velocity cubed dominates siting.",
   "Note intermittency and capacity factor for wind farms."],
  ["wind energy", "Betz limit", "power coefficient", "air density", "rotor area", "v cubed", "capacity factor", "turbine", "intermittency", "storage"],
  ["Available power ∝ ρ A v³; double v → ~8× power.",
   "Betz limit: CP,max = 16/27 ≈ 59.3%; Pwind,max = (8/27) ρ A v³.",
   "Real turbines operate below Betz; capacity factor << 100% due to wind variability."],
  "Sixteen over twenty-seven — wind hard ceiling.",
  "Wind lecture is formula-heavy: kinetic flux through the rotor, Betz ceiling, and cubic speed dependence. Siting beats blade diameter for many projects because of v³. Pair with storage/grid flexibility from the overview. Numerical drills using ρ, A, v and capacity factor are exam favorites."
)

# --- Week 6 ---
N(26,
  ["Identify geothermal heat sources: primordial, radiogenic, shallow solar-heated ground.",
   "Define EGS: stimulate permeability in hot dry rock.",
   "Apply Q = ṁ cp ΔT for direct-use heat.",
   "Note low lifecycle GHG for many geothermal plants (course <50 g CO2eq/kWh flash)."],
  ["geothermal", "EGS", "hot dry rock", "GSHP", "direct use", "flash steam", "radiogenic heat", "district heating", "permeability", "DeltaT"],
  ["EGS engineers connectivity where natural hydrothermal productivity is poor.",
   "Heat extraction example pattern: Q = ṁ cp ΔT (course ~42 TJ/y worked example).",
   "Shallow ground-source heat pumps exploit stable near-surface temperatures."],
  "EGS = crack hot rock, circulate fluid.",
  "Geothermal taps Earth's internal heat for electricity or direct heating. Hydrothermal systems cluster tectonically; EGS expands the map. Open- vs closed-loop and GSHP distinctions matter. Lifecycle emissions are typically low versus fossils—useful comparison fact."
)

N(27,
  ["Distinguish tidal range (barrage) vs tidal stream (kinetic) technologies.",
   "State tidal theoretical potential ~1200 TWh/y (smallest ocean class in course).",
   "Give tidal stream useful speeds ~≥1.5–2 m/s; spring vs neap tides.",
   "Use wave energy density E = (1/8) ρ g H² and deep-water power ∝ H² T."],
  ["tidal energy", "tidal barrage", "tidal stream", "wave energy", "spring tide", "neap tide", "wave height", "energy density", "ocean energy", "1200 TWh"],
  ["Course ocean potentials: tidal ~1200, wave ~29500, OTEC ~44000 TWh/y.",
   "Spring tides: Sun–Moon–Earth aligned; neap when ~90° apart.",
   "Deep-water wave power per unit crest ≈ (ρ g² H² T)/32."],
  "OTEC titan; tide tiny (as taught).",
  "Ocean Energy I covers tides and waves. Barrages use head; streams use current KE. Wave formulas reward careful H and T. Ranking potentials (tidal smallest) is a repeated MCQ. Environmental/social siting constraints are as important as theoretical TWh."
)

N(28,
  ["Define OTEC: power from warm surface vs cold deep water ΔT.",
   "Contrast open-cycle (seawater vapor) vs closed-cycle (e.g. ammonia).",
   "Mention salinity gradient and ocean current energy briefly.",
   "Note OTEC's large technical potential but geographic limits (tropics)."],
  ["OTEC", "open cycle", "closed cycle", "salinity gradient", "ocean current", "thermal gradient", "ammonia working fluid", "tropical oceans", "44000 TWh", "hybrid OTEC"],
  ["OTEC technical potential ~44000 TWh/y (largest in course ranking).",
   "Open boils/flashes seawater; closed evaporates a low-BP secondary fluid.",
   "Needs sustained vertical temperature difference — mainly tropical waters."],
  "Open boils seawater; closed boils ammonia-like fluid.",
  "Ocean Energy II emphasizes OTEC and other ocean pathways beyond tide/wave. Cycle choice and cold-water pipe engineering dominate feasibility. Environmental concerns (nutrient upwelling, marine life) appear alongside resource estimates. Keep open/closed contrast ready for compare questions."
)

N(29,
  ["Classify hydro: storage dam, run-of-river, pumped storage; multipurpose dams.",
   "Use PE = m g z and e_hydro = P_elec / (ṁ g z).",
   "Explain operating head z as the key elevation difference.",
   "Discuss environmental/social impacts of large reservoirs."],
  ["hydropower", "operating head", "run-of-river", "pumped storage", "multipurpose dam", "efficiency", "reservoir", "fish passage", "flood control", "PE = mgz"],
  ["Hydropower energy is primarily potential energy of head z, not free-river kinetic alone.",
   "Efficiency e_hydro = electric power / (ṁ g z); course example pattern 150 MW, z=35 m, Q=500 m³/s.",
   "Pumped storage is grid storage using two reservoirs, not a primary energy source."],
  "Hydro lives on head z.",
  "Hydropower remains the largest established renewable electricity source globally. Plant types and multipurpose benefits (irrigation, flood control) are definitional. Head-and-flow numericals test PE and efficiency. Social displacement and ecological alteration balance the 'clean energy' narrative on exams."
)

N(30,
  ["Assess when bioenergy is sustainable (feedstock, land, lifecycle).",
   "List conversion pathways: combustion, gasification, pyrolysis, anaerobic digestion.",
   "Define fast pyrolysis: ~400–600 °C, near-absent O2 → bio-oil, gas, char.",
   "Contrast pyrolysis with combustion in excess air."],
  ["bioenergy", "biomass", "feedstock", "pyrolysis", "gasification", "bio-oil", "anaerobic digestion", "sustainability", "land use", "syngas"],
  ["Fast pyrolysis: 400–600 °C without oxygen favoring liquid bio-oil plus gas and char.",
   "If oxygen is plentiful, the process is combustion, not classical pyrolysis.",
   "Sustainability hinges on feedstock origin, competition with food, and full lifecycle GHG."],
  "Pyrolysis = heat, no O2; combustion = burn with air.",
  "Bioenergy closes the renewable series with chemistry and land-use caveats. Pathway identification (especially pyrolysis temperature/atmosphere) is high-yield. Sustainability is conditional—not automatic carbon neutrality. Link to circular use of residues versus dedicated energy crops."
)

# --- Week 7 ---
N(31,
  ["Define urban metabolism (anabolism + catabolism of cities).",
   "Contrast linear Take-Make-Waste with circular Borrow-Use-Return.",
   "Explain limits of linear throughput for natural capital.",
   "List circular-economy benefits: less extraction, waste, emissions."],
  ["circular economy", "urban metabolism", "linear economy", "take-make-waste", "borrow-use-return", "material flows", "closing loops", "natural capital", "SDG 12"],
  ["Urban metabolism maps city material/energy inflows and waste outflows.",
   "Linear slogan: Take-Make-Waste; circular: Borrow-Use-Return.",
   "Circular economy supports responsible consumption/production (SDG 12)."],
  "Do not take forever — borrow and bring back.",
  "Introduction frames cities as metabolic systems whose linear throughput depletes ecosystems. Circular economy redesigns flows to keep materials circulating. Benefits are environmental and economic (new models). This conceptual base supports 9R strategies and industrial symbiosis later in the week."
)

N(32,
  ["State purpose of the 9R framework for circularity.",
   "Prioritize smarter Rs (refuse/rethink/reduce) over downstream recycling.",
   "Give examples of early-R strategies in product/service design.",
   "Explain how 9R changes business and consumer behavior."],
  ["9R framework", "refuse", "rethink", "reduce", "reuse", "circular strategies", "design", "priority order", "resource efficiency", "waste prevention"],
  ["9R strategies ladder from smarter product use to useful end-of-life application.",
   "Upstream strategies (refuse/rethink/reduce) generally beat end-of-pipe recycling.",
   "Framework is a practical checklist for transitioning from linear models."],
  "Refuse/Rethink before Recycle.",
  "Strategies I introduces building a circular economy via the 9R model. Hierarchy among Rs mirrors waste hierarchy logic: prevention first. Examples show redesign and dematerialization. Exam answers should order strategies by preference, not list them randomly."
)

N(33,
  ["Complete remaining R strategies with examples (repair, remanufacture, recycle, recover).",
   "Show how cascading Rs keep value in the economy longer.",
   "Relate 9R totality to measurable sustainability outcomes.",
   "Warn that recycling alone is not a full circular transition."],
  ["repair", "refurbish", "remanufacture", "repurpose", "recycle", "recover", "9R", "value retention", "cascading use", "circularity"],
  ["Downstream Rs still matter but sit below refuse/reduce in preference.",
   "Remanufacturing retains more embodied energy than material recycling.",
   "Full 9R set is needed to illustrate a complete circular strategy story on exams."],
  "Repair beats recycle when possible.",
  "Strategies II finishes the 9R ladder with life-extension and end-of-life options. Value retention hierarchy is the conceptual prize: keep products whole before shredding materials. Combined with Lecture 32, students should narrate a coherent refuse→recover pathway."
)

N(34,
  ["Name five circular business models: circular supply, product-as-service, life extension, sharing, recover/recycle.",
   "Explain product-as-service shifting ownership incentives to durability.",
   "Link sharing platforms to higher utilization of assets.",
   "Show how firms operationalize 9R via business model choice."],
  ["circular supply chain", "product as a service", "product life extension", "sharing platform", "recovery recycle", "business model", "servitization", "utilization", "EPR link"],
  ["Five models: circular supply chain; product-as-service; life extension; sharing platforms; recovery & recycle.",
   "Product-as-service aligns producer profit with longevity and take-back.",
   "Sharing raises asset utilization, reducing demand for new production."],
  "Own the service, not the stuff.",
  "Business-model lecture translates circular principles into firm strategy. Servitization and sharing change incentives versus selling disposable units. Recovery models close loops commercially. Useful for application/case MCQs connecting theory to practice."
)

N(35,
  ["Define industrial ecology and industrial symbiosis.",
   "Explain waste-of-one = feedstock-of-another networks.",
   "Relate symbiosis to closing loops at park/regional scale.",
   "Give conceptual benefits: cost, resource, emission reductions."],
  ["industrial ecology", "industrial symbiosis", "eco-industrial park", "byproduct exchange", "closing loops", "Kalundborg-type", "material cascade", "system design"],
  ["Industrial ecology designs industry like ecosystems with cyclic flows.",
   "Industrial symbiosis: firms exchange byproducts, energy and water.",
   "Symbiosis is circular economy at inter-firm scale."],
  "One plant's waste is another's feedstock.",
  "Week 7 closes with industrial ecology/symbiosis—classic eco-industrial park logic. It complements product-level 9R and firm-level business models with network-level exchanges. Exam definition: symbiotic byproduct exchange mimicking food webs."
)

# --- Week 8 ---
N(36,
  ["State global water split ~97.5% salt / ~2.5% fresh; usable freshwater tiny.",
   "Define withdrawal vs consumption; returns to environment.",
   "Outline hydrologic cycle stocks and fluxes.",
   "Introduce point vs non-point water pollution sources."],
  ["hydrologic cycle", "freshwater", "withdrawal", "consumption", "water pollution", "point source", "non-point source", "groundwater", "environmental flows", "scarcity"],
  ["Salt water ~97.5%; freshwater ~2.5% of global water.",
   "Withdrawals = consumption + returns; consumption is not returned.",
   "Municipal wastewater often ~80% of urban water use (India cities ~87% cited)."],
  "Withdrawal ≠ consumption.",
  "Water week begins with quantity and cycle literacy. Scarcity is about accessible freshwater, not ocean volume. Withdrawal/consumption accounting underpins reuse lectures. Pollution framing (point/non-point) sets up quality parameters next."
)

N(37,
  ["List general WQ parameters: pH, SS, temperature, oil & grease, residual Cl2, nutrients.",
   "Explain why multiple parameters are needed (no single 'pollution number').",
   "Connect parameters to uses (drinking, irrigation, ecology).",
   "Preview oxygen and nitrogen focus of later lectures."],
  ["water quality", "pH", "suspended solids", "temperature", "oil and grease", "residual chlorine", "nutrients", "standards", "monitoring", "parameters"],
  ["Water quality is multi-parameter: physical, chemical, biological.",
   "Standards depend on designated best use of the water body.",
   "Temperature and SS affect DO and aquatic life even without toxins."],
  "Many dials, not one pollution meter.",
  "General parameters lecture builds the monitoring toolkit. Students should know what each parameter indicates and why context (use class) matters. This sets baseline before BOD/COD and DO-sag theory."
)

N(38,
  ["Define BOD (India often BOD3 @ 27 °C) vs COD.",
   "Explain oxygen-demanding wastes and microbial indicators (e.g. fecal coliform).",
   "State COD usually ≥ BOD for a sample.",
   "Link organic loading to downstream oxygen stress."],
  ["BOD", "COD", "BOD3", "27 C", "fecal coliform", "oxygen demand", "organic pollution", "microbial indicators", "wastewater", "stabilization"],
  ["BOD = oxygen microbes use to stabilize organics; Indian convention often BOD3 at 27 °C.",
   "COD uses chemical oxidant; typically COD ≥ BOD.",
   "Fecal coliform indicates possible pathogen contamination from sewage."],
  "BOD = bugs' appetite; COD = chemical oxidant appetite.",
  "Oxygen-demanding wastes are central to river pollution exams. BOD/COD definitions, Indian test conditions and microbial indicators are high-frequency facts. Organic load without treatment drives the DO sag developed next."
)

N(39,
  ["Describe DO sag curve: deficit downstream of BOD load then recovery.",
   "Name nitrogen species: NH3/NH4+, NO2-, NO3-, organic N / TKN.",
   "Link nitrification to additional oxygen demand.",
   "Explain eutrophication risk from excess N (and P)."],
  ["DO sag", "oxygen deficit", "ammonia", "nitrate", "nitrite", "TKN", "nitrification", "eutrophication", "Streeter-Phelps idea", "re-aeration"],
  ["DO sag: DO falls after organic load, then rises with re-aeration/decay of BOD.",
   "Nitrogen species transformations affect toxicity (ammonia) and oxygen demand.",
   "Nutrient enrichment drives algal blooms and secondary DO problems."],
  "Sag: dump BOD → DO dips → river recovers.",
  "Nitrogen and DO-sag lecture is conceptual/quantitative. Sketch the sag, mark critical deficit, and discuss nitrification. Nutrient species connect wastewater treatment goals to ecological outcomes. Strong short-answer territory."
)

N(40,
  ["Compute NSF-WQI idea: Σ Qi Wi; DO weight 0.17 highest; FC 0.16.",
   "Recall WQI bands: 90–100 Excellent … 0–25 Very Bad.",
   "State NGT established 18 Oct 2010; aim dispose in 6 months; benches.",
   "Explain reuse/recycling and discharge standards by destination."],
  ["WQI", "NSF-WQI", "NGT", "reuse", "recycling", "discharge standards", "DO weight 0.17", "zero liquid discharge", "STP standards", "18.10.2010"],
  ["NSF-WQI DO weight 0.17 (highest); fecal coliform 0.16.",
   "NGT: 18.10.2010; principal bench New Delhi; also Bhopal, Pune, Kolkata, Chennai.",
   "Effluent limits differ for inland surface, sewers, irrigation, marine (e.g. BOD 30 vs 350 vs 100 mg/L)."],
  "Dissolved Oxygen Dominates the index.",
  "Capstone water lecture joins index math, tribunal context and reuse policy. WQI enables comparison; NGT enforces standards; reuse closes urban water loops. Memorize DO weight, NGT date/seats and destination-specific BOD/SS limits."
)

# --- Week 9 ---
N(41,
  ["Define solid waste (incl. containerized liquids/gases in regulatory sense).",
   "State waste hierarchy: Prevent > Reuse > Recycle > Recover > Dispose.",
   "List 4Rs with source reduction first.",
   "Explain ISWM as coordinated system across the waste chain."],
  ["ISWM", "waste hierarchy", "4Rs", "reduce", "reuse", "recycle", "recover", "solid waste", "prevention", "source reduction"],
  ["Hierarchy: Prevent > Reuse > Recycle > Recover > Dispose.",
   "4Rs: Reduce, Reuse, Recycle, Recover — reduce sits at the top.",
   "Solid waste definition can include containerized liquid/gaseous wastes."],
  "Please Reduce Really Revolting Dumps (PRRRD).",
  "ISWM lecture sets philosophy before technology. Hierarchy and 4Rs beat incinerator name-dropping on exams. Integration means matching collection, treatment and disposal to composition and goals. Open dumps are explicitly rejected later—prevention is cheaper than remediation."
)

N(42,
  ["Relate MSW generation rates to income and urbanization.",
   "Describe typical composition categories (organics, paper, plastic, metal, inert).",
   "Note organics often dominate Indian city MSW.",
   "Explain why composition drives technology choice."],
  ["MSW", "generation rate", "composition", "organics", "urbanization", "per capita waste", "characterization", "income", "plastics", "moisture"],
  ["Generation rates generally rise with affluence and urban lifestyles.",
   "Indian MSW often has high biodegradable organic fraction.",
   "Composition determines suitability of composting, recycling, RDF, landfill design."],
  "Wealthier cities usually waste more per capita.",
  "Sources and rates lecture quantifies the problem. Per-capita figures and composition pie charts are exam visuals. High moisture organics favor biological treatment; dry recyclables favor sorting. Data quality in characterization studies matters for planning."
)

N(43,
  ["Detail collection systems: storage, segregation, transport frequency.",
   "Emphasize source segregation for recycling/organics.",
   "Connect collection efficiency to public health and dumping.",
   "Discuss informal sector role conceptually in Indian cities."],
  ["collection", "segregation", "storage bins", "transport", "door-to-door", "transfer station", "informal recycling", "MSW composition", "primary collection", "secondary transport"],
  ["Source segregation multiplies recycling success and compost quality.",
   "Poor collection leads to open dumping and drain clogging.",
   "Collection is often the costliest visible part of MSW systems."],
  "Segregate at source or suffer at dump.",
  "Composition/collection lecture bridges characterization to logistics. Without reliable collection and segregation, downstream plants fail. Public participation and informal recyclers shape real Indian systems—acknowledge both in answers."
)

N(44,
  ["Compare open dump vs sanitary landfill (leachate, LFG, cover).",
   "List treatment options: biological, thermal, recycling, landfill.",
   "Compute moisture/TS/VS relationships for characterization maths.",
   "Name twin landfill hazards: methane and leachate."],
  ["sanitary landfill", "open dump", "leachate", "landfill gas", "composting", "incineration", "volatile solids", "total solids", "moisture content", "treatment"],
  ["Open dumps uncontrolled; sanitary landfills use liners, cover, leachate/LFG management.",
   "Example: 40% moisture → TS=60%; if 50/60 lost on ignition → VS=83.3% of TS.",
   "Hierarchy still places landfill as last resort even when engineered."],
  "Methane + leachate = twin landfill hazards.",
  "Treatment/disposal lecture is technology + safety. Characterization maths (moisture, TS, VS) appear in numericals. Contrasting dumps vs sanitary landfills is mandatory. Biological and thermal options depend on wet/dry fractions from earlier lectures."
)

N(45,
  ["Define e-waste and why it grows rapidly.",
   "Identify toxic and valuable fractions (Pb, Hg, Au, Cu, rare earths).",
   "State India E-waste Rules 2011 and EPR concept.",
   "Require authorized recyclers; avoid informal burning/acid baths."],
  ["e-waste", "EPR", "E-waste Rules 2011", "authorized recycler", "heavy metals", "WEEE", "take-back", "informal sector hazards", "precious metals", "circular electronics"],
  ["India E-waste Rules 2011 introduced formal EPR-oriented management.",
   "E-waste holds both toxics and recoverable valuables — improper recycling poisons workers/environment.",
   "Authorized channels and producer take-back beat backyard smelting."],
  "E-waste: toxic treasure — recycle right.",
  "Dedicated e-waste lecture highlights a fast-growing hazardous stream. Rules, EPR and authorized recycling are legal-technical musts. Links forward to Week 12 rules timeline and back to circular business models (take-back)."
)

# --- Week 10 ---
N(46,
  ["Define noise as unwanted sound with adverse effects.",
   "Use λ = c/f and p = 1/f; c ≈ 20.05√T (T in K).",
   "Write Lp = 20 log(Prms/P0) with P0 = 20 μPa = 0 dB.",
   "Note human hearing span many orders of magnitude → dB scale."],
  ["noise", "sound", "wavelength", "frequency", "SPL", "decibel", "20 uPa", "speed of sound", "compression rarefaction", "threshold of hearing"],
  ["λ = c/f; reference pressure P0 = 20 μPa defines 0 dB SPL.",
   "Lp = 20 log10(Prms/P0); 10× pressure → +20 dB.",
   "Noise = unwanted sound causing physiological/psychological harm or interference."],
  "0 dB is hearing threshold, not silence.",
  "Fundamentals lecture builds physics for all noise MCQs. Wavelength, frequency, SPL and the log scale are non-negotiable. Distinguish sound power, intensity and pressure conceptually even if instruments read pressure."
)

N(47,
  ["Explain audiometry as hearing-threshold testing by frequency.",
   "Interpret audiograms for hearing loss patterns.",
   "Relate frequency bands to speech intelligibility.",
   "Connect occupational monitoring to baseline audiograms."],
  ["audiometry", "audiogram", "hearing threshold", "frequency", "Hearing Level", "speech frequencies", "sensorineural", "occupational health", "baseline test"],
  ["Audiometry maps quietest audible tones across frequencies.",
   "Occupational programs use periodic audiograms to detect noise-induced loss early.",
   "Speech frequencies are critical for communication disability assessment."],
  "Audiogram = hearing map by frequency.",
  "Audiometry provides the clinical measurement bridge between physical dB and human hearing damage. Pattern recognition on audiograms (notch losses) appears in applied questions. Ties to 85 dB(A) occupational caution in later lectures."
)

N(48,
  ["List health effects: TTS, PTS, annoyance, sleep loss, cardiovascular stress.",
   "State ≥85 dB(A) over 8 h as occupational risk threshold (course).",
   "Differentiate temporary vs permanent threshold shift.",
   "Note non-auditory effects matter for environmental noise standards."],
  ["TTS", "PTS", "hearing loss", "annoyance", "sleep disturbance", "85 dBA", "occupational noise", "non-auditory effects", "stress", "NIHL"],
  ["≥85 dB(A) for 8 h is a key occupational caution level in the course.",
   "TTS may recover; PTS is permanent noise-induced hearing loss.",
   "Environmental noise also drives sleep and stress outcomes beyond hearing."],
  "TTS temporary; PTS permanent.",
  "Effects lecture justifies regulations. Dose (level × time) drives NIHL risk. Non-auditory impacts support ambient standards even below occupational limits. Use TTS/PTS vocabulary precisely in answers."
)

N(49,
  ["Define Leq as energy-equivalent continuous level.",
   "Explain Ldn night penalty and LN percentile levels.",
   "Apply inverse square: point source −6 dB per distance doubling; line ~−3 dB.",
   "Combine levels: two equal sources → +3 dB; energy sum formula."],
  ["Leq", "Ldn", "LN", "A-weighting", "inverse square", "point source", "line source", "decibel addition", "+3 dB", "noise modeling"],
  ["Point source free field: ΔLp ≈ −20 log(r2/r1) → −6 dB when distance doubles.",
   "Line sources (roads): ~−3 dB per doubling; intensity ∝ 1/r.",
   "Two equal incoherent sources: L + 3 dB; if ΔL ≥ 10 dB, total ≈ louder source."],
  "Twice as far, six dB quieter (point).",
  "Rating/modeling lecture is calculation central. Leq/Ldn/A-weighting appear in standards. Propagation laws and dB arithmetic are weekly numerical staples. Know when −6 vs −3 dB applies."
)

N(50,
  ["Structure control: source, path (barriers), receiver (PPE).",
   "Recall CPCB ambient zone standards concept.",
   "Prefer engineering/admin controls before PPE.",
   "Link regulations to earlier Leq metrics."],
  ["noise control", "barrier", "PPE", "CPCB", "zoning", "source control", "path control", "receiver protection", "regulations", "silencer"],
  ["Control hierarchy: reduce at source → interrupt path → protect receiver.",
   "Ambient standards vary by zone (silence, residential, commercial, industrial) in Indian practice.",
   "Ear protection is last line, not first, for occupational programs."],
  "Source, path, then ear muffs.",
  "Control and regulations close noise week with practical hierarchy and legal limits. Barriers, enclosures, quieter machinery and land-use buffers are path/source tools. Cite CPCB zoning and metric (often dB(A)/Leq) in policy answers."
)

# --- Week 11 ---
N(51,
  ["Define ecology (oikos = house) and ecosystem = community + abiotic environment.",
   "State energy flows one-way; nutrients cycle.",
   "Introduce producers and photosynthesis as foundational energy capture.",
   "Place biosphere as aggregate of ecosystems."],
  ["ecology", "ecosystem", "biosphere", "abiotic", "biotic", "energy flow", "nutrient cycling", "photosynthesis", "producers", "oikos"],
  ["Ecology studies organisms 'at home' with environment; oikos = house.",
   "Energy flow is unidirectional; mass/nutrients cycle.",
   "Ecosystem = biotic community + abiotic environment with functional stability."],
  "Energy one-way; nutrients loop.",
  "Ecology I builds vocabulary and system boundaries. Distinguishing energy versus nutrient pathways prevents conceptual errors in food-web lectures. Photosynthesis links solar energy to all trophic structure."
)

N(52,
  ["Define ecological niche as species' functional role/position.",
   "Describe food chains vs food webs and trophic levels.",
   "Interpret pyramids of numbers, biomass and energy.",
   "Introduce competition and niche differentiation conceptually."],
  ["ecological niche", "food chain", "food web", "trophic level", "pyramid of energy", "herbivore", "carnivore", "producer", "consumer", "decomposer"],
  ["Niche = functional role including resources and interactions.",
   "Trophic levels: producers → herbivores → carnivores (then higher predators).",
   "Energy pyramids always narrow upward due to transfer losses."],
  "Niche is the job; habitat is the address.",
  "Ecology II focuses on structure of feeding relationships. Niche vs habitat wording is a classic trap. Pyramid types and why energy pyramids cannot invert like some number pyramids are exam favorites."
)

N(53,
  ["Write logistic growth dN/dt = rN(1 − N/K) vs unlimited exponential.",
   "Define carrying capacity K.",
   "Explain biomagnification with classic DDT-style examples.",
   "Preview BCF linkage to chemistry in soil lectures."],
  ["logistic growth", "carrying capacity", "exponential growth", "biomagnification", "food chain concentration", "J-curve", "S-curve", "population ecology", "DDT"],
  ["Logistic: dN/dt = rN(1 − N/K); S-curve approaches K.",
   "When N ≪ K, logistic ≈ exponential.",
   "Biomagnification raises contaminant concentrations up trophic levels."],
  "J-curve unlimited; S-curve hits K.",
  "Ecology III adds population dynamics and contaminant transfer up food webs. Logistic vs exponential pairs with Week 1 human population models. Biomagnification sets up BCF/Kow quantitative treatment in soil pollution."
)

N(54,
  ["Define soil pollution pathways: chemicals, salts, wastes, deposition.",
   "Introduce BCF = C_biota / C_water; link to Kow hydrophobicity.",
   "Distinguish bioconcentration, bioaccumulation, biomagnification.",
   "Cite extreme BCF examples (e.g. DDT ~10^5)." ],
  ["soil pollution", "BCF", "Kow", "bioconcentration", "bioaccumulation", "biomagnification", "hydrophobic organics", "heavy metals", "adsorption", "contamination"],
  ["BCF = Cbiota/Cwater (L/kg); often rises with log Kow.",
   "Bioconcentration vs water; bioaccumulation all routes; biomagnification across trophic levels.",
   "DDT gull example up to ~120,000× versus water (course)."],
  "Water → Body → Bigger predators (BBB).",
  "Soil Pollution I emphasizes contaminant behavior and biological uptake metrics. BBB trio definitions are mandatory. Kow–BCF correlation explains why oily organics haunt fatty tissues and food chains."
)

N(55,
  ["Write USLE: A = R K L S C P and name each factor.",
   "Recall unit plot 72.6 ft × 5.5 ft, 9% slope.",
   "Identify management levers mainly C (cover) and P (practice).",
   "List soil degradation forms: erosion, salinization, contamination."],
  ["USLE", "soil erosion", "rainfall erosivity", "erodibility", "LS factor", "cover factor", "practice factor", "unit plot", "soil conservation", "A=RKLSCP"],
  ["USLE: A = R K L S C P for average annual sheet/rill soil loss.",
   "Unit plot defining factors: 5.5 ft × 72.6 ft on 9% slope.",
   "Cover (C) and conservation practice (P) are primary management controls."],
  "Rain Kills Loose Soil; Cover and Practice save it.",
  "Soil Pollution II foregrounds erosion estimation via USLE. Factor names and unit-plot definition are pure MCQ bait. Conservation practices reconnect ecology (cover) to engineering (terraces, contours)."
)

# --- Week 12 ---
N(56,
  ["Trace movements: Bishnoi/Khejri, Chipko 1973, Appiko 1982–83, Jungle Bachao.",
   "Link movements to later statutes and public consciousness.",
   "Note Chipko/Bahuguna and Right Livelihood Award 1987.",
   "Frame local action preceding national environmental law."],
  ["Chipko", "Appiko", "Bishnoi", "Khejri", "Jungle Bachao", "Bahuguna", "environmental movement", "forest protection", "Right Livelihood Award", "people's movements"],
  ["Chipko movement ~1973 Himalayan tree protection; Appiko 1982–83 in Western Ghats.",
   "Bishnoi community ethos includes historic sacrifice for Khejri trees.",
   "Movements shaped opinion before Water/Air/EPA statutes matured."],
  "Hug trees (Chipko) before writing Acts.",
  "Policy week opens with social history. Movements demonstrate that Indian environmentalism is not only post-Bhopal legislation. Dates and regional tags (Himalaya vs Western Ghats) are tested. Connect grassroots ethics to later NGT/PIL enforcement culture."
)

N(57,
  ["Timeline Acts: Water 1974, Air 1981 (am. 1987), EPA 1986 (am. 1991).",
   "Distinguish Act (what) vs Rules (how).",
   "List key Rules: HW 1989, BMW 1998, MSW 2000/2016, Batteries 2001, Plastic/E-waste 2011, C&D 2016.",
   "Explain CPCB/SPCB institutional role under Water Act."],
  ["Water Act 1974", "Air Act 1981", "EPA 1986", "Rules", "CPCB", "SPCB", "Hazardous Waste Rules", "MSW Rules 2016", "E-waste Rules 2011", "umbrella law"],
  ["Water 1974 → Air 1981 → EPA 1986 umbrella after Bhopal-era urgency.",
   "Act = substantive law; Rules = procedural subordinate legislation.",
   "Sectoral Rules update faster than parent Acts as new waste streams emerge."],
  "Wet Air envelops Environment (W-A-E).",
  "Law-and-rules lecture is timeline memorization gold. Water/Air/EPA purposes and institutions (boards) plus Rules ecosystem (HW, BMW, MSW, e-waste…) form checklist answers. Emphasize EPA as umbrella enabling diverse Rules."
)

N(58,
  ["Explain PIL role in Indian environmental jurisprudence.",
   "Recall M.C. Mehta line of cases (incl. education mandate link).",
   "State how judgments drive policy beyond statutes alone.",
   "Note absolute liability / polluter-pays themes in landmark holdings."],
  ["PIL", "M.C. Mehta", "Supreme Court", "landmark judgments", "polluter pays", "absolute liability", "environmental education", "judicial activism", "fundamental rights", "public interest"],
  ["Public Interest Litigation expanded access to environmental remedies.",
   "M.C. Mehta cases reshaped industrial siting, pollution control and education mandates.",
   "Judgments operationalize constitutional rights into concrete environmental duties."],
  "Courts wrote green chapters via PIL.",
  "Judgments lecture shows judiciary as policy engine. Named case families and doctrines (polluter pays, absolute liability) matter more than endless citations. Tie education mandate back to Lecture 1 framing."
)

N(59,
  ["State NGT Act 2010; natural justice; endeavor to dispose in 6 months.",
   "List benches: Principal New Delhi; Bhopal, Pune, Kolkata, Chennai.",
   "Explain NGT's specialized role vs general courts.",
   "Summarize types of orders: penalties, restoration, compliance directions."],
  ["NGT", "National Green Tribunal", "2010", "natural justice", "six months", "principal bench", "environmental adjudication", "restoration", "expert members", "appeals"],
  ["NGT established under 2010 Act; guided by principles of natural justice.",
   "Seats: New Delhi (principal) plus Bhopal, Pune, Kolkata, Chennai.",
   "Aim to dispose cases expeditiously (statutory endeavor within 6 months)."],
  "Green Tribunal 2010 — six-month sprint.",
  "NGT lecture institutionalizes speedy, expert environmental adjudication. Bench geography and natural-justice principle are standard MCQs. Orders often blend science (restoration plans) with compliance timelines—bridge to EIA conditioning."
)

N(60,
  ["Define rapid EIA purpose: predict impacts before decision.",
   "Outline steps: baseline, impact prediction, mitigation, public consult, clearance conditions.",
   "Apply to River Ib Barrage case (submergence, DEM, alternatives).",
   "Argue EIA as preventive policy tool linked to NGT/clearances."],
  ["rapid EIA", "River Ib", "barrage", "submergence", "digital elevation model", "impact prediction", "public consultation", "clearance", "mitigation measures", "case study"],
  ["EIA systematically predicts and evaluates project impacts before approval.",
   "Rapid EIA case study: River Ib Barrage (Odisha) — submergence analysis using DEM etc.",
   "Clearance conditions convert predicted mitigations into enforceable requirements."],
  "Predict, consult, condition — then build.",
  "Final lecture applies EIA to a real barrage proposal: flooding extent, alternatives and safeguards. Rapid EIA compresses study time but must still cover key impacts. Caps the course: science metrics + law + participatory decision-making for sustainable projects."
)


def week_of(lec: int) -> int:
    return (lec - 1) // 5 + 1


def build() -> dict:
    lectures = []
    for lec in range(1, 61):
        if lec not in NOTES:
            raise SystemExit(f"Missing notes for lecture {lec}")
        objectives, keywords, facts, mnemonic, summary = NOTES[lec]
        assert 3 <= len(objectives) <= 5, lec
        assert 8 <= len(keywords) <= 12, (lec, len(keywords))
        assert len(facts) == 3, lec
        assert isinstance(summary, str) and summary.count(".") >= 3, lec
        lectures.append({
            "lec": lec,
            "week": week_of(lec),
            "title": TITLES[lec],
            "objectives": objectives,
            "keywords": keywords,
            "likelyFacts": facts,
            "mnemonic": mnemonic,
            "summary": summary,
        })
    return {"lectures": lectures}


def main() -> None:
    data = build()
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    # validate round-trip
    loaded = json.loads(OUT.read_text(encoding="utf-8"))
    n = len(loaded["lectures"])
    lecs = [x["lec"] for x in loaded["lectures"]]
    assert n == 60 and lecs == list(range(1, 61))
    for item in loaded["lectures"]:
        w = item["week"]
        lec = item["lec"]
        assert w == (lec - 1) // 5 + 1
        assert 3 <= len(item["objectives"]) <= 5
        assert 8 <= len(item["keywords"]) <= 12
        assert len(item["likelyFacts"]) == 3
        assert item["mnemonic"] is None or isinstance(item["mnemonic"], str)
        assert isinstance(item["summary"], str) and len(item["summary"]) > 80
    print(f"Wrote {OUT}")
    print(f"Lecture count: {n}")
    print("JSON valid: yes")


if __name__ == "__main__":
    main()
