import re

now = "2026-11-06 13:55:13 +0000"

faqs_data = {
    "_posts/2022-11-24-how-to-choose-a-set-of-lawn-bowls.md": [
        {
            "question": "What size lawn bowls should I buy?",
            "answer": "Choose the largest size you can comfortably hold and control throughout a full delivery swing without straining your fingers or dropping the bowl early. If your thumbs and middle fingers overlap when wrapping your hands around the bowl, you can handle that size comfortably."
        },
        {
            "question": "Should beginners buy narrow-bias or mid-bias bowls?",
            "answer": "Mid-bias bowls (such as the Taylor Ace or Drakes Pride Professional) are the best choice for beginners. They provide a predictable, forgiving arc that works on both outdoor grass and indoor rinks, making line control much easier to learn than narrow-bias models."
        },
        {
            "question": "Is it better to buy new or second-hand lawn bowls?",
            "answer": "Second-hand bowls from reputable brands like Taylor, Henselite, Aero, or Drakes Pride are ideal for your first set because they cost significantly less and retain resale value. Ensure any second-hand set has a valid World Bowls stamp and matching serial numbers on all four bowls."
        },
        {
            "question": "What is the difference between gripped and non-gripped lawn bowls?",
            "answer": "Gripped bowls feature recessed indentations or dimple patterns along the running surface to enhance finger traction, especially in wet weather or for bowlers with smaller hands. Non-gripped bowls have smooth running surfaces preferred by bowlers with larger hands or a cradle delivery."
        }
    ],
    "_posts/2019-04-09-best-lawn-bowls-for-beginners.md": [
        {
            "question": "Which model of lawn bowls is best for a beginner?",
            "answer": "The Taylor Ace and Drakes Pride Professional are widely considered the two best models for beginner lawn bowlers. Both feature a predictable mid-bias trajectory, forgiving draw curves, and versatile performance across both indoor surfaces and outdoor greens."
        },
        {
            "question": "Should a new bowler choose heavy or medium weight bowls?",
            "answer": "Almost all modern lawn bowlers, including beginners, should choose Heavy weight bowls. Heavy bowls resist wind deflection better, stay steadier on uneven grass, and track more consistently down the green."
        },
        {
            "question": "How much should a beginner spend on their first set of bowls?",
            "answer": "A new set of four bowls from leading brands costs between £350 and £450. However, a quality second-hand set in good condition with a valid World Bowls stamp typically costs between £100 and £200, representing exceptional value for new club members."
        }
    ],
    "_posts/2018-01-12-best-rated-bowls-for-leads.md": [
        {
            "question": "Why do leads prefer narrow-to-mid bias bowls?",
            "answer": "Leads bowl when the rink is open and free of obstacles, meaning their primary job is drawing repeatedly to within inches of the jack. Narrow-to-mid bias bowls have a tighter, flatter finish that minimises ditch drift and allows tight line discipline."
        },
        {
            "question": "Which lawn bowl is best for leads on indoor carpet vs outdoor grass?",
            "answer": "On fast indoor carpet and artificial greens (14+ seconds), ultra-narrow models like the Taylor Vector VS or Drakes Pride D-Tec excel. On standard UK outdoor grass (11–13 seconds), a mid-narrow bowl like the Drakes Pride Professional or Aero Quantum provides better clearance."
        },
        {
            "question": "Do leads need gripped bowls?",
            "answer": "Yes, many leads choose deep-grooved grips (like Taylor's Progrip or Aero's Z-Scoop) to maintain identical fingertip placement end after end, which is critical for consistent draw weight control."
        }
    ],
    "_posts/2022-04-01-best-lawn-bowls-for-skips.md": [
        {
            "question": "Why do skips generally prefer wider-bias lawn bowls?",
            "answer": "Skips bowl last when the head is congested with short woods and blockers. Wider-bias models (like the Taylor International or Aero Sonic) allow skips to swing around short bowls and still reach the jack, while holding line under added weight for trail and conversion shots."
        },
        {
            "question": "Can a skip use narrow-bias bowls?",
            "answer": "Narrow-bias bowls make it difficult for skips to draw around blockers on slower outdoor greens. However, on true indoor carpet (15–17 seconds) or exceptionally fast summer greens, experienced skips often succeed with mid-narrow models like the Taylor Ace."
        },
        {
            "question": "Which bowl is best for driving and weighted shots?",
            "answer": "Bowls with a strong shoulder that hold their trajectory under pace—such as the Henselite Tiger and Taylor Ace—are favoured for running shots and drives because they do not whip unexpectedly across the rink when delivered with firm weight."
        }
    ],
    "_posts/2019-07-25-best-lawn-bowls-for-fast-greens.md": [
        {
            "question": "What is considered a fast lawn bowls green?",
            "answer": "Greens with timings of 15 seconds or higher (measured by the time in seconds a bowl takes from release to come to rest over 27 metres) are considered fast. Speeds above 16–17 seconds are common on indoor needlefelt carpets and Australian bentgrass greens."
        },
        {
            "question": "Why do you need narrow-bias bowls on fast greens?",
            "answer": "Because fast greens take so long to slow the bowl down, the bias has much more time to bite, causing wide-bias bowls to bend excessively. A narrow-bias model allows you to stay within your rink boundaries without having to take extreme amounts of green."
        },
        {
            "question": "Which lawn bowls are best for fast outdoor turf and indoor rinks?",
            "answer": "The Aero GrooVe, Taylor Vector VS, and Taylor Lazer are the premier narrow-line models for fast outdoor greens and indoor clubs. They hold their line cleanly and deliver a steady, flat finish at the head."
        }
    ]
}

for path, faqs in faqs_data.items():
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    yaml_lines = ["faqs:"]
    for item in faqs:
        q = item["question"].replace('"', '\\"')
        a = item["answer"].replace('"', '\\"')
        yaml_lines.append(f'  - question: "{q}"')
        yaml_lines.append(f'    answer: "{a}"')
    faqs_str = "\n".join(yaml_lines) + "\n"

    parts = content.split("---", 2)
    if len(parts) >= 3:
        fm = parts[1]
        fm = re.sub(r"faqs:.*?(?=\n\S|\n---)", "", fm, flags=re.DOTALL).rstrip()
        if "last_modified_at:" in fm:
            fm = re.sub(r"last_modified_at:\s*[^\n]+", f"last_modified_at: {now}", fm)
        else:
            fm += f"\nlast_modified_at: {now}"
        fm += "\n" + faqs_str
        new_content = "---" + fm + "---" + parts[2]
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Added faqs to {path}")

