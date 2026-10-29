#!/usr/bin/env python3
"""
Enhances the top 20 lawn bowls reviews and head-to-head comparisons with:
1. Structured "Quick Verdict" summary capsules (for AI citation & user TL;DR)
2. Markdown specification and comparison tables
3. Rich frontmatter meta descriptions
4. Current last_modified_at timestamps
5. Accessible image alt text
"""

import os
import re

POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "_posts")
MODIFIED_TIMESTAMP = "2026-10-29 15:45:00 +0000"

REVIEWS_DATA = {
    "2019-06-20-taylor-ace-review.md": {
        "description": "Comprehensive Taylor Ace lawn bowls review: bias profile analysis, grip options, indoor vs outdoor performance, and pros & cons for club bowlers.",
        "alt": "Taylor Ace lawn bowl in maroon on grass green",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Taylor Ace Lawn Bowls</h3>
  <p class="mb-2"><strong>The Taylor Ace is the UK's benchmark all-round lawn bowl.</strong> Featuring a predictable mid-to-wide trajectory and a smooth, hook-free finish, it performs reliably on outdoor grass greens (12–15 seconds) and handles wider indoor lines with equal consistency.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Club bowlers seeking one versatile set for all rink positions (Lead, Second, Third, or Skip).</li>
    <li><strong>Bias Profile:</strong> Mid-to-Wide Bias with a clean, forgiving draw arc.</li>
    <li><strong>Surface Suitability:</strong> Outdoor Grass (Medium/Slow) and Indoor Rinks.</li>
    <li><strong>Overall Score:</strong> 9.4 / 10 &mdash; Recommended Buy</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Mid Bias (Wider arc than Vector VS, narrower than Lignoid) |
| **Running Surface** | Outdoor grass greens, indoor carpet rinks |
| **Ideal Positions** | All positions (Lead to Skip) |
| **Available Sizes** | 00 to 5 |
| **Available Weights** | Medium, Heavy, Extra Heavy |
| **Grip Options** | Progrip (deep dimple), Half-Pipe, Plain non-gripped |
| **Price Guide** | £380 – £420 (New) / £150 – £250 (Second-hand) |
"""
    },
    "2019-06-02-drakes-pride-professional-review.md": {
        "description": "In-depth Drakes Pride Professional review: trajectory analysis, grip variations, running surface versatility, and expert verdict.",
        "alt": "Drakes Pride Professional lawn bowl set on green",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Drakes Pride Professional</h3>
  <p class="mb-2"><strong>The Drakes Pride Professional is the UK's traditional benchmark mid-bias bowl.</strong> It offers an exceptionally smooth, continuous draw arc without a sharp late hook, making it ideal for players who want complete control over their line on outdoor grass greens.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Traditional draw bowlers and club players looking for predictable grass performance.</li>
    <li><strong>Bias Profile:</strong> True Mid Bias with an even, continuous curve.</li>
    <li><strong>Surface Suitability:</strong> Outdoor Grass Greens (11–15 seconds) and standard indoor greens.</li>
    <li><strong>Overall Score:</strong> 9.3 / 10 &mdash; Recommended Buy</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Mid Bias (Classic continuous arc) |
| **Running Surface** | Outdoor grass greens (11–15s), indoor rinks |
| **Ideal Positions** | All positions (Lead, Second, Third, Skip) |
| **Available Sizes** | 0000 to 5 |
| **Available Weights** | Medium, Heavy, Extra Heavy |
| **Grip Options** | Traditional 30-dimple, Plain non-gripped |
| **Price Guide** | £370 – £410 (New) |
"""
    },
    "2023-03-07-henselite-tiger-ii-lawn-bowls-review.md": {
        "description": "Henselite Tiger II lawn bowls review: bias line analysis, Ergo Extreme grip test, indoor vs fast outdoor suitability, and expert ratings.",
        "alt": "Henselite Tiger II lawn bowls with Ergo Extreme grip",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Henselite Tiger II</h3>
  <p class="mb-2"><strong>The Henselite Tiger II is a precision narrow-to-mid line bowl engineered for faster playing surfaces.</strong> It features a tighter holding line through the head and finishes with a controlled, subtle draw, making it a weapon on indoor carpets and quick summer outdoor greens.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Indoor players, Leads, Seconds, and singles competitors on quick surfaces.</li>
    <li><strong>Bias Profile:</strong> Narrow-to-Mid Bias with a tight, controlled finish.</li>
    <li><strong>Surface Suitability:</strong> Fast Grass, Synthetics, and Indoor Carpets.</li>
    <li><strong>Overall Score:</strong> 9.2 / 10 &mdash; Top Indoor/Fast Surface Pick</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Narrow-to-Mid Bias (Tighter than Tiger and Tiger Pro) |
| **Running Surface** | Indoor carpets, synthetic greens, fast grass |
| **Ideal Positions** | Lead, Second, Indoor Singles Specialists |
| **Available Sizes** | 00 to 5 |
| **Available Weights** | Medium, Heavy |
| **Grip Options** | Ergo Extreme channel grip, Diamond grip |
| **Price Guide** | £390 – £430 (New) |
"""
    },
    "2018-01-12-taylor-vector-vs-review.md": {
        "description": "Taylor Vector VS lawn bowls review: narrow bias profile, indoor performance, suitability for leads, and comprehensive buyers guide.",
        "alt": "Taylor Vector VS lawn bowls set on indoor carpet rink",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Taylor Vector VS</h3>
  <p class="mb-2"><strong>The Taylor Vector VS is Taylor's premier narrow-line bowl.</strong> Specifically engineered for fast outdoor surfaces and indoor carpet rinks, it draws narrow and holds its line under pressure, allowing front-end players to draw consistently close to the ditch or jack.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Front-end bowlers (Leads and Seconds) and dedicated indoor specialists.</li>
    <li><strong>Bias Profile:</strong> Narrow Bias with a slight, gentle hook at the end of trajectory.</li>
    <li><strong>Surface Suitability:</strong> Fast Outdoor Grass, Synthetic Greens, Indoor Rinks.</li>
    <li><strong>Overall Score:</strong> 9.1 / 10 &mdash; Recommended for Leads</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Narrow Bias (Straighter than Taylor Ace) |
| **Running Surface** | Fast grass (14s+), synthetic surfaces, indoor carpets |
| **Ideal Positions** | Lead, Second, Indoor Singles |
| **Available Sizes** | 00 to 5 |
| **Available Weights** | Medium, Heavy |
| **Grip Options** | Progrip, Half-Pipe, Plain |
| **Price Guide** | £380 – £410 (New) |
"""
    },
    "2020-09-12-aero-groove-lawn-bowls-review.md": {
        "description": "Aero Groove lawn bowls review: robotic precision manufacturing, mid-bias trajectory, Z-Scoop grip evaluation, and performance score.",
        "alt": "Aero Groove lawn bowls set with Z-Scoop grip",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Aero Groove Lawn Bowls</h3>
  <p class="mb-2"><strong>The Aero Groove is an ultra-precise mid-bias bowl manufactured with robotic lathe precision.</strong> It delivers an exceptionally smooth, gradual arc that holds line in gusty wind, making it one of the most consistent all-round bowls in the Aero lineup.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Precision players who want identical trajectories on forehand and backhand.</li>
    <li><strong>Bias Profile:</strong> Mid Bias with smooth, predictable arc.</li>
    <li><strong>Surface Suitability:</strong> Medium to fast outdoor greens (12–16s) and all indoor surfaces.</li>
    <li><strong>Overall Score:</strong> 9.5 / 10 &mdash; Premium All-Rounder</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Mid Bias (Between Aero Sonic and Aero Quantum) |
| **Manufacturing** | 100% Robot Lathe Ground |
| **Running Surface** | Outdoor grass (12–16s), artificial turf, indoor rinks |
| **Ideal Positions** | Lead, Second, Third, Skip |
| **Available Sizes** | 00 to 5 |
| **Available Weights** | Medium, Heavy |
| **Grip Options** | Z-Scoop, Denticulated, Plain rings |
| **Price Guide** | £410 – £460 (New) |
"""
    },
    "2021-05-18-aero-quantum-review.md": {
        "description": "Aero Quantum lawn bowls review: wide bias profile for slow grass greens, heavy surface performance, and buyers guide.",
        "alt": "Aero Quantum lawn bowls set on heavy grass green",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Aero Quantum Lawn Bowls</h3>
  <p class="mb-2"><strong>The Aero Quantum is Aero's widest bias model, engineered specifically for heavy, slow outdoor grass greens.</strong> When early-season grass greens run under 12 seconds, the Quantum swings cleanly around short bowls without getting pulled straight.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Outdoor club bowlers on slow grass greens, and Skips needing wide drawing lines.</li>
    <li><strong>Bias Profile:</strong> Wide Bias with a pronounced, dependable swing.</li>
    <li><strong>Surface Suitability:</strong> Slow to medium outdoor grass greens (10–13 seconds).</li>
    <li><strong>Overall Score:</strong> 9.0 / 10 &mdash; Best for Heavy Grass</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Wide Bias (Widest model in Aero range) |
| **Running Surface** | Slow outdoor grass (10–13 seconds) |
| **Ideal Positions** | Third, Skip, Singles Players on Slow Greens |
| **Available Sizes** | 00 to 5 |
| **Available Weights** | Medium, Heavy |
| **Grip Options** | Z-Scoop, Denticulated |
| **Price Guide** | £420 – £470 (New) |
"""
    },
    "2018-01-12-drakes-pride-d-tec-review.md": {
        "description": "Drakes Pride D-Tec lawn bowls review: narrow bias profile, indoor specialist analysis, and direct comparisons.",
        "alt": "Drakes Pride D-Tec lawn bowl on indoor carpet",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Drakes Pride D-Tec</h3>
  <p class="mb-2"><strong>The Drakes Pride D-Tec is an ultra-narrow line bowl tailored specifically for indoor rinks and lightning-fast greens.</strong> It offers an exceptionally direct line with minimal bend, making it easy to navigate tight rinks and draw directly onto the jack.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Indoor singles competitors, Leads, and fast-paced surface bowlers.</li>
    <li><strong>Bias Profile:</strong> Narrow Bias (Drakes Pride's straightest running bowl).</li>
    <li><strong>Surface Suitability:</strong> Indoor Carpet Rinks and Fast Synthetics (15s+).</li>
    <li><strong>Overall Score:</strong> 8.9 / 10 &mdash; Dedicated Indoor Choice</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Narrow Bias (Straighter than Professional and XP) |
| **Running Surface** | Indoor carpets, fast synthetic greens |
| **Ideal Positions** | Lead, Second, Indoor Singles Specialists |
| **Available Sizes** | 0000 to 5 |
| **Available Weights** | Medium, Heavy |
| **Grip Options** | Standard dimple grip, Plain |
| **Price Guide** | £370 – £410 (New) |
"""
    },
    "2023-04-22-taylor-lignoid-lawn-bowls-review.md": {
        "description": "Taylor Lignoid lawn bowls review: wide bias profile, holding line on slow grass greens, second-hand affordability, and verdict.",
        "alt": "Taylor Lignoid lawn bowl in maroon showing wide bias profile",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Taylor Lignoid Lawn Bowls</h3>
  <p class="mb-2"><strong>The Taylor Lignoid is an unsung hero of outdoor bowling: a classic wide-bias workhorse.</strong> Offering the widest draw in the Taylor lineup, the Lignoid provides generous swing to clear short bowls and hold line on slow, uneven grass greens.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Bowlers on slow grass greens (10–12s), Skips, and budget-conscious players buying second-hand.</li>
    <li><strong>Bias Profile:</strong> Full Wide Bias with a deep sweeping trajectory.</li>
    <li><strong>Surface Suitability:</strong> Heavy, slow, and holding outdoor grass greens.</li>
    <li><strong>Overall Score:</strong> 8.8 / 10 &mdash; Best Budget Wide Bowl</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Wide Bias (Taylor's widest model) |
| **Running Surface** | Heavy and slow outdoor grass (10–12 seconds) |
| **Ideal Positions** | Skip, Third, Club Roll-ups |
| **Available Sizes** | 00 to 5 |
| **Available Weights** | Medium, Heavy |
| **Grip Options** | Progrip, Plain non-gripped |
| **Price Guide** | £380 (New) / £80 – £150 (Second-hand) |
"""
    },
    "2020-09-01-taylor-blaze-lawn-bowls-review.md": {
        "description": "Taylor Blaze lawn bowls review: mid-narrow bias line, fast surface performance, and comparison to Ace and Vector VS.",
        "alt": "Taylor Blaze lawn bowls in two-tone colour on green",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Taylor Blaze Lawn Bowls</h3>
  <p class="mb-2"><strong>The Taylor Blaze fills the sweet spot between the narrow Vector VS and the all-round Ace.</strong> It provides a slender, mid-to-narrow line with a controlled finish, offering exceptional accuracy on fast summer greens and indoor surfaces.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Bowlers looking for slightly less swing than an Ace without going to a pure narrow bowl.</li>
    <li><strong>Bias Profile:</strong> Mid-to-Narrow Bias with a clean holding arc.</li>
    <li><strong>Surface Suitability:</strong> Fast Grass, Synthetics, and Indoor Rinks.</li>
    <li><strong>Overall Score:</strong> 9.2 / 10 &mdash; Versatile Fast-Surface Pick</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Mid-to-Narrow (Between Vector VS and Ace) |
| **Running Surface** | Fast grass (13–16s), artificial greens, indoor rinks |
| **Ideal Positions** | Lead, Second, Third |
| **Available Sizes** | 00 to 5 |
| **Available Weights** | Medium, Heavy |
| **Grip Options** | Premier grip, Half-Pipe, Plain |
| **Price Guide** | £380 – £420 (New) |
"""
    },
    "2023-03-22-aero-sonic-lawn-bowl-review.md": {
        "description": "Aero Sonic lawn bowl review: mid-to-wide trajectory test, wind stability, and head-to-head comparison with Groove and Quantum.",
        "alt": "Aero Sonic lawn bowls set on outdoor green",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Aero Sonic Lawn Bowls</h3>
  <p class="mb-2"><strong>The Aero Sonic is an outdoor specialist bowl designed for typical UK grass surfaces.</strong> Positioned between the Groove and Quantum, it provides ample draw to navigate around short bowls while holding its line against gusty crosswinds.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Outdoor bowlers seeking reliable draw on standard club greens (11–14s).</li>
    <li><strong>Bias Profile:</strong> Mid-to-Wide Bias with wind-resistant trajectory.</li>
    <li><strong>Surface Suitability:</strong> Outdoor Grass Greens (11–14 seconds).</li>
    <li><strong>Overall Score:</strong> 9.3 / 10 &mdash; Top Outdoor Performer</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Mid-to-Wide Bias (Wider than Groove, narrower than Quantum) |
| **Running Surface** | Outdoor grass greens (11–14 seconds) |
| **Ideal Positions** | Lead, Second, Third, Skip |
| **Available Sizes** | 00 to 5 |
| **Available Weights** | Medium, Heavy |
| **Grip Options** | Z-Scoop, Denticulated |
| **Price Guide** | £420 – £470 (New) |
"""
    },
    "2020-08-06-drakes-pride-xp-lawn-bowls-review.md": {
        "description": "Drakes Pride XP lawn bowls review: wide bias profile, heavy grass performance, Skip suitability, and verdict.",
        "alt": "Drakes Pride XP lawn bowls on green",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Drakes Pride XP Lawn Bowls</h3>
  <p class="mb-2"><strong>The Drakes Pride XP is the widest-bias model in the Drakes Pride collection.</strong> Engineered with a bold, swinging trajectory, it is the weapon of choice for outdoor Skips needing to clear blocking bowls and draw cleanly to ditch jacks on slow greens.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Outdoor Skips, back-end players, and slow-running grass greens (10–13s).</li>
    <li><strong>Bias Profile:</strong> Wide Bias with a pronounced, smooth curve.</li>
    <li><strong>Surface Suitability:</strong> Slow to medium outdoor grass greens.</li>
    <li><strong>Overall Score:</strong> 9.0 / 10 &mdash; Recommended for Outdoor Skips</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Wide Bias (Wider than Drakes Pride Professional) |
| **Running Surface** | Slow outdoor grass (10–13 seconds) |
| **Ideal Positions** | Third, Skip |
| **Available Sizes** | 0000 to 5 |
| **Available Weights** | Medium, Heavy |
| **Grip Options** | Standard dimple grip, Plain |
| **Price Guide** | £380 – £420 (New) |
"""
    },
    "2019-05-16-drakes-pride-pro-50-review.md": {
        "description": "Drakes Pride Pro-50 lawn bowls review: channel grip evaluation, wet weather handling, and comparison to the classic Professional.",
        "alt": "Drakes Pride Pro-50 lawn bowl showing channel grip pattern",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Drakes Pride Pro-50</h3>
  <p class="mb-2"><strong>The Pro-50 takes Drakes Pride's proven Professional bias and adds an ergonomic channel grip.</strong> The deeper channel grooves deliver exceptional hand feel and slip resistance, particularly in wet, damp, or cold playing conditions.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Bowlers who love the Professional trajectory but want extra finger traction and grip security.</li>
    <li><strong>Bias Profile:</strong> True Mid Bias identical to Drakes Pride Professional.</li>
    <li><strong>Surface Suitability:</strong> Outdoor grass greens and indoor surfaces.</li>
    <li><strong>Overall Score:</strong> 9.4 / 10 &mdash; Best Grip Option</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Mid Bias (Same as Professional) |
| **Special Feature** | Deep Channel Grip for maximum finger purchase |
| **Running Surface** | Outdoor grass greens (11–15s), indoor rinks |
| **Ideal Positions** | All positions (Lead to Skip) |
| **Available Sizes** | 0000 to 5 |
| **Available Weights** | Medium, Heavy |
| **Grip Options** | Pro-50 Channel Grip |
| **Price Guide** | £380 – £420 (New) |
"""
    },
    "2023-03-07-henselite-tiger-lawn-bowls-review.md": {
        "description": "Henselite Tiger lawn bowls review: classic mid-bias draw, outdoor green adaptability, and comparison with Tiger II and Tiger Pro.",
        "alt": "Henselite Tiger lawn bowls on grass rink",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Henselite Tiger Lawn Bowls</h3>
  <p class="mb-2"><strong>The Henselite Tiger is the foundation of the modern Henselite range.</strong> Offering a full, traditional mid-bias arc, it is wider than the Tiger II and well suited for outdoor grass greens where a confident, forgiving draw is required.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Outdoor club bowlers in all positions looking for a classic, forgiving draw curve.</li>
    <li><strong>Bias Profile:</strong> Mid Bias with smooth, consistent trajectory.</li>
    <li><strong>Surface Suitability:</strong> Outdoor grass greens (11–14 seconds).</li>
    <li><strong>Overall Score:</strong> 9.1 / 10 &mdash; Reliable Outdoor Standard</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Mid Bias (Wider than Tiger II and Tiger Pro) |
| **Running Surface** | Outdoor grass greens (11–14s) |
| **Ideal Positions** | All positions (Lead to Skip) |
| **Available Sizes** | 00 to 5 |
| **Available Weights** | Medium, Heavy |
| **Grip Options** | Ergo Extreme, Diamond grip |
| **Price Guide** | £390 – £430 (New) |
"""
    },
    "2023-03-07-henselite-tiger-tx-lawn-bowls-review.md": {
        "description": "Henselite Tiger TX lawn bowls review: ultra-narrow line analysis, indoor carpet testing, and suitability for leads.",
        "alt": "Henselite Tiger TX lawn bowls on indoor carpet rink",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Henselite Tiger TX</h3>
  <p class="mb-2"><strong>The Henselite Tiger TX is Henselite's narrowest bowl for the UK indoor circuit.</strong> Designed with an ultra-direct line and a flat finish, it allows front-end players to draw directly onto the jack without taking wide ice or interfering with adjacent rinks.</p>
  <ul class="mb-0 pl-3">
    <li><strong>Best For:</strong> Indoor Leads, Seconds, and singles competitors bowling on fast carpet surfaces.</li>
    <li><strong>Bias Profile:</strong> Ultra-Narrow Bias (Henselite's straightest bowl).</li>
    <li><strong>Surface Suitability:</strong> Fast Indoor Carpets and rapid synthetic greens.</li>
    <li><strong>Overall Score:</strong> 9.0 / 10 &mdash; Top Indoor Front-End Pick</li>
  </ul>
</div>

### Model Specifications

| Feature | Specification |
| :--- | :--- |
| **Bias Profile** | Ultra-Narrow Bias (Straighter than Tiger II) |
| **Running Surface** | Indoor carpet rinks, fast artificial greens |
| **Ideal Positions** | Lead, Second, Indoor Singles |
| **Available Sizes** | 00 to 5 |
| **Available Weights** | Medium, Heavy |
| **Grip Options** | Ergo Extreme grip |
| **Price Guide** | £390 – £430 (New) |
"""
    },
    "2020-08-28-drakes-pride-professional-vs-taylor-ace.md": {
        "description": "Drakes Pride Professional vs Taylor Ace head-to-head comparison: bias arc differences, grip choices, surface versatility, and verdict.",
        "alt": "Drakes Pride Professional vs Taylor Ace comparison",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Drakes Pride Professional vs Taylor Ace</h3>
  <ul class="mb-0 pl-3">
    <li><strong>Taylor Ace:</strong> Features a slightly wider arc with a gentle hook finish. Offers superior versatility for outdoor skips and wide indoor lines.</li>
    <li><strong>Drakes Pride Professional:</strong> Delivers a continuous, perfectly even curve with zero late hook. Favoured by traditional draw bowlers and front-end players.</li>
    <li><strong>The Recommendation:</strong> Choose the <strong>Taylor Ace</strong> if you want extra draw around short bowls; choose the <strong>Professional</strong> if you prefer an even, predictable arc that never kicks at the finish.</li>
  </ul>
</div>

### Side-by-Side Comparison

| Feature / Specification | Taylor Ace | Drakes Pride Professional |
| :--- | :--- | :--- |
| **Bias Rating** | Mid Bias (Slightly wider finish) | Mid Bias (Continuous, even curve) |
| **Best Playing Surfaces** | Outdoor Grass (12–15s) & Indoor | Outdoor Grass (11–15s) & Indoor |
| **Best Position** | All positions (Lead to Skip) | All positions (Lead to Skip) |
| **Grip Options** | Progrip, Half-Pipe, Plain | 30-Dimple, Plain |
| **Size Range** | Size 00 to 5 | Size 0000 to 5 |
| **Price Bracket** | £380 – £420 | £370 – £410 |
"""
    },
    "2023-02-24-taylor-ace-vs-henselite-tiger-ii-which-is-best.md": {
        "description": "Taylor Ace vs Henselite Tiger II lawn bowls comparison: bias profile differences, outdoor vs indoor suitability, grips, and verdict.",
        "alt": "Taylor Ace vs Henselite Tiger II lawn bowls comparison",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Taylor Ace vs Henselite Tiger II</h3>
  <ul class="mb-0 pl-3">
    <li><strong>Taylor Ace:</strong> Mid-to-wide bias with a steady, predictable finish. The ultimate all-rounder for outdoor grass greens (12–15s) across all team positions.</li>
    <li><strong>Henselite Tiger II:</strong> Narrow-to-mid line with a tight, holding finish. Excels on fast outdoor surfaces, artificial turf, and indoor carpets.</li>
    <li><strong>The Recommendation:</strong> Choose the <strong>Taylor Ace</strong> for outdoor club grass versatility; choose the <strong>Tiger II</strong> if you play primarily indoors or on slick summer greens.</li>
  </ul>
</div>

### Side-by-Side Comparison

| Feature / Specification | Taylor Ace | Henselite Tiger II |
| :--- | :--- | :--- |
| **Bias Rating** | Mid Bias (Wider drawing arc) | Narrow-to-Mid Bias (Straighter line) |
| **Primary Surface** | Outdoor Grass (Slow to Medium-Fast) | Fast Grass, Synthetic & Indoor Rinks |
| **Best Team Position** | All positions (Lead to Skip) | Lead, Second, Singles Draw Bowlers |
| **Grip Options** | Progrip, Half-Pipe, Plain | Ergo Extreme, Diamond Grip |
| **Size Range** | Size 00 to 5 (Medium, Heavy, X-Heavy) | Size 00 to 5 (Medium, Heavy) |
| **Price Bracket** | £380 – £420 | £390 – £430 |
"""
    },
    "2023-03-19-taylor-vector-vs-vs-taylor-ace-which-is-best.md": {
        "description": "Taylor Vector VS vs Taylor Ace: side-by-side comparison of bias width, position suitability, green speeds, and buyer recommendations.",
        "alt": "Taylor Vector VS vs Taylor Ace comparison",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Taylor Vector VS vs Taylor Ace</h3>
  <ul class="mb-0 pl-3">
    <li><strong>Taylor Vector VS:</strong> Noticeably narrower trajectory. Designed specifically for fast outdoor greens (14s+) and indoor carpet rinks.</li>
    <li><strong>Taylor Ace:</strong> Wider arc with more swing into the head. The better all-round choice for club grass greens running 12–14 seconds.</li>
    <li><strong>The Recommendation:</strong> Choose the <strong>Vector VS</strong> if you are a Lead/Second or play predominantly indoors; choose the <strong>Ace</strong> if you play all positions on grass.</li>
  </ul>
</div>

### Side-by-Side Comparison

| Feature / Specification | Taylor Vector VS | Taylor Ace |
| :--- | :--- | :--- |
| **Bias Rating** | Narrow Bias | Mid Bias (Wider drawing line) |
| **Primary Surface** | Fast Grass (14s+) & Indoor Carpets | Outdoor Grass (12–15s) & Indoor |
| **Best Position** | Lead, Second, Indoor Singles | Lead, Second, Third, Skip |
| **Grip Options** | Progrip, Half-Pipe, Plain | Progrip, Half-Pipe, Plain |
| **Size Range** | Size 00 to 5 | Size 00 to 5 |
| **Price Bracket** | £380 – £410 | £380 – £420 |
"""
    },
    "2023-03-22-taylor-ace-vs-aero-groove-which-is-best.md": {
        "description": "Taylor Ace vs Aero Groove lawn bowls comparison: traditional Scottish craftsmanship vs robotic lathe precision, bias lines, and verdict.",
        "alt": "Taylor Ace vs Aero Groove lawn bowls comparison",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Taylor Ace vs Aero Groove</h3>
  <ul class="mb-0 pl-3">
    <li><strong>Taylor Ace:</strong> Proven mid-bias classic with deep Progrip dimple feel and forgiving draw weight. Exceptional on traditional UK club greens.</li>
    <li><strong>Aero Groove:</strong> 100% robot-lathe precision with exact track symmetry between forehand and backhand, featuring the ergonomic Z-Scoop grip.</li>
    <li><strong>The Recommendation:</strong> Choose the <strong>Taylor Ace</strong> for classic British feel and wider availability; choose the <strong>Aero Groove</strong> for supreme manufacturing consistency and grip precision.</li>
  </ul>
</div>

### Side-by-Side Comparison

| Feature / Specification | Taylor Ace | Aero Groove |
| :--- | :--- | :--- |
| **Bias Rating** | Mid Bias (Traditional Scottish arc) | Mid Bias (Robotic trajectory arc) |
| **Primary Surface** | Outdoor Grass (12–15s) & Indoor | Outdoor Grass (12–16s) & Indoor |
| **Best Position** | All positions (Lead to Skip) | All positions (Lead to Skip) |
| **Grip Options** | Progrip, Half-Pipe, Plain | Z-Scoop, Denticulated, Plain rings |
| **Size Range** | Size 00 to 5 | Size 00 to 5 |
| **Price Bracket** | £380 – £420 | £410 – £460 |
"""
    },
    "2023-03-20-taylor-ace-vs-aero-quantum-which-is-best.md": {
        "description": "Taylor Ace vs Aero Quantum comparison: mid bias vs wide bias, green speed suitability, and tactical recommendations.",
        "alt": "Taylor Ace vs Aero Quantum comparison",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Taylor Ace vs Aero Quantum</h3>
  <ul class="mb-0 pl-3">
    <li><strong>Taylor Ace:</strong> Versatile mid bias suited for a broad range of speeds (12–15 seconds) and playable across indoor and outdoor surfaces.</li>
    <li><strong>Aero Quantum:</strong> Dedicated wide bias designed specifically for heavy, holding outdoor greens (10–12 seconds).</li>
    <li><strong>The Recommendation:</strong> Choose the <strong>Taylor Ace</strong> for an all-round set you can play anywhere; choose the <strong>Aero Quantum</strong> if your club green is notoriously heavy, wet, or slow.</li>
  </ul>
</div>

### Side-by-Side Comparison

| Feature / Specification | Taylor Ace | Aero Quantum |
| :--- | :--- | :--- |
| **Bias Rating** | Mid Bias | Wide Bias (Significantly wider arc) |
| **Primary Surface** | All-round (12–15s grass + indoor) | Slow/Heavy Grass (10–12s) |
| **Best Position** | Lead to Skip | Third, Skip |
| **Grip Options** | Progrip, Half-Pipe, Plain | Z-Scoop, Denticulated |
| **Size Range** | Size 00 to 5 | Size 00 to 5 |
| **Price Bracket** | £380 – £420 | £420 – £470 |
"""
    },
    "2023-03-06-drakes-pride-d-tec-vs-drakes-pride-xp-which-is-best.md": {
        "description": "Drakes Pride D-Tec vs Drakes Pride XP: narrow bias indoor specialist vs wide bias outdoor heavyweight comparison and verdict.",
        "alt": "Drakes Pride D-Tec vs Drakes Pride XP comparison",
        "verdict_html": """<div class="alert alert-success border-success my-4 p-3 rounded">
  <h3 class="h5 font-weight-bold text-success mb-2"><i class="fas fa-check-circle mr-1"></i> Quick Verdict: Drakes Pride D-Tec vs Drakes Pride XP</h3>
  <ul class="mb-0 pl-3">
    <li><strong>Drakes Pride D-Tec:</strong> Ultra-narrow trajectory designed exclusively for rapid indoor carpets and fast artificial greens.</li>
    <li><strong>Drakes Pride XP:</strong> Wide-drawing outdoor heavyweight with a bold swinging arc to navigate around head obstacles on slow grass.</li>
    <li><strong>The Recommendation:</strong> Two opposite ends of the spectrum: choose the <strong>D-Tec</strong> for dedicated indoor competition; choose the <strong>XP</strong> for slow outdoor grass greens.</li>
  </ul>
</div>

### Side-by-Side Comparison

| Feature / Specification | Drakes Pride D-Tec | Drakes Pride XP |
| :--- | :--- | :--- |
| **Bias Rating** | Ultra-Narrow Bias | Wide Bias |
| **Primary Surface** | Fast Indoor Carpets (15s+) | Slow Outdoor Grass (10–13s) |
| **Best Position** | Lead, Second, Indoor Singles | Third, Skip |
| **Grip Options** | Standard dimple, Plain | Standard dimple, Plain |
| **Size Range** | Size 0000 to 5 | Size 0000 to 5 |
| **Price Bracket** | £370 – £410 | £380 – £420 |
"""
    }
}

def enhance_post(filename, data):
    filepath = os.path.join(POSTS_DIR, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}: file not found")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update frontmatter description & last_modified_at
    if 'description: ""' in content:
        content = content.replace('description: ""', f'description: "{data["description"]}"\nlast_modified_at: {MODIFIED_TIMESTAMP}')
    elif 'description:' in content:
        content = re.sub(r'description:\s*["\x27]?[^"\x27\n]*["\x27]?', f'description: "{data["description"]}"', content)
        if 'last_modified_at:' not in content:
            content = content.replace('description:', f'last_modified_at: {MODIFIED_TIMESTAMP}\ndescription:')

    # 2. Fix empty alt on featured image
    # Replace alt="" on featured image tag
    content = re.sub(r'(<img[^>]+src=[\x27"][^\x27"]+[\x27"][^>]+)alt=[\x27"][\x27"]', rf'\1alt="{data["alt"]}"', content, count=1)

    # 3. Inject verdict_html if not already present
    if "Quick Verdict:" not in content:
        # Inject right after the first wp:image or figure block, or after first paragraph
        match = re.search(r'(</figure>\s*<!-- /wp:image -->|</figure>)', content)
        if match:
            pos = match.end()
            content = content[:pos] + "\n\n" + data["verdict_html"] + content[pos:]
        else:
            # Fallback: after frontmatter
            fm_end = content.find("---", 4)
            if fm_end != -1:
                content = content[:fm_end+3] + "\n\n" + data["verdict_html"] + content[fm_end+3:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Enhanced {filename}")
    return True

if __name__ == "__main__":
    count = 0
    for fname, data in REVIEWS_DATA.items():
        if enhance_post(fname, data):
            count += 1
    print(f"\nSuccessfully enhanced {count} top reviews with Quick Verdicts and spec tables!")
