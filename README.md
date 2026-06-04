import math
import os
import random
import time
import threading

# ============================================
#  ENTROPY → WORD LEXICON (1000–4000, step 10)
# ============================================

ENTROPY_LEXICON = {
    1000: "I",
    1010: "You",
    1020: "Here",
    1030: "Now",
    1040: "Yes",
    1050: "No",
    1060: "One",
    1070: "Two",
    1080: "Three",
    1090: "Four",
    1100: "Hello",
    1110: "Begin",
    1120: "Signal",
    1130: "Listen",
    1140: "Speak",
    1150: "Move",
    1160: "Stay",
    1170: "Open",
    1180: "Close",
    1190: "Wait",

    1200: "How",
    1210: "What",
    1220: "Where",
    1230: "When",
    1240: "Who",
    1250: "Why",
    1260: "Ask",
    1270: "Tell",
    1280: "Show",
    1290: "Give",

    1300: "Take",
    1310: "Hold",
    1320: "Release",
    1330: "Follow",
    1340: "Lead",
    1350: "Enter",
    1360: "Exit",
    1370: "Rise",
    1380: "Fall",
    1390: "Turn",

    1400: "Light",
    1410: "Dark",
    1420: "Warm",
    1430: "Cold",
    1440: "Near",
    1450: "Far",
    1460: "Slow",
    1470: "Fast",
    1480: "Quiet",
    1490: "Loud",

    1500: "Safe",
    1510: "Danger",
    1520: "Truth",
    1530: "False",
    1540: "Path",
    1550: "Gate",
    1560: "Step",
    1570: "Shift",
    1580: "Change",
    1590: "Stay",

    1600: "Start",
    1610: "End",
    1620: "Before",
    1630: "After",
    1640: "Inside",
    1650: "Outside",
    1660: "Above",
    1670: "Below",
    1680: "Forward",
    1690: "Back",

    1700: "Left",
    1710: "Right",
    1720: "Up",
    1730: "Down",
    1740: "Center",
    1750: "Edge",
    1760: "Line",
    1770: "Circle",
    1780: "Point",
    1790: "Field",

    1800: "Touch",
    1810: "See",
    1820: "Hear",
    1830: "Feel",
    1840: "Sense",
    1850: "Know",
    1860: "Think",
    1870: "Remember",
    1880: "Forget",
    1890: "Recall",

    1900: "Build",
    1910: "Break",
    1920: "Create",
    1930: "Destroy",
    1940: "Form",
    1950: "Shape",
    1960: "Bind",
    1970: "Free",
    1980: "Join",
    1990: "Separate",

    2000: "Friend",
    2010: "Stranger",
    2020: "Ally",
    2030: "Enemy",
    2040: "Self",
    2050: "Other",
    2060: "Many",
    2070: "Few",
    2080: "All",
    2090: "None",

    2100: "Calm",
    2110: "Fear",
    2120: "Joy",
    2130: "Sad",
    2140: "Anger",
    2150: "Peace",
    2160: "Trust",
    2170: "Doubt",
    2180: "Hope",
    2190: "Loss",

    2200: "Want",
    2210: "Need",
    2220: "Choose",
    2230: "Reject",
    2240: "Accept",
    2250: "Offer",
    2260: "Ask",
    2270: "Answer",
    2280: "Call",
    2290: "Return",

    2300: "Time",
    2310: "Past",
    2320: "Present",
    2330: "Future",
    2340: "Moment",
    2350: "Loop",
    2360: "Shift",
    2370: "Echo",
    2380: "Signal",
    2390: "Thread",

    2400: "Energy",
    2410: "Matter",
    2420: "Space",
    2430: "Void",
    2440: "Wave",
    2450: "Pulse",
    2460: "Flow",
    2470: "Break",
    2480: "Merge",
    2490: "Align",

    2500: "No",
    2510: "Stop",
    2520: "Block",
    2530: "Deny",
    2540: "Resist",
    2550: "Hold",
    2560: "Anchor",
    2570: "Ground",
    2580: "Limit",
    2590: "Guard",

    2600: "One",
    2610: "Two",
    2620: "Three",
    2630: "Four",
    2640: "Five",
    2650: "Six",
    2660: "Seven",
    2670: "Eight",
    2680: "Nine",
    2690: "Ten",

    2700: "Begin",
    2710: "Continue",
    2720: "Expand",
    2730: "Extend",
    2740: "Reach",
    2750: "Connect",
    2760: "Bridge",
    2770: "Share",
    2780: "Combine",
    2790: "Grow",

    2800: "Feel",
    2810: "Sense",
    2820: "Understand",
    2830: "Interpret",
    2840: "Reflect",
    2850: "Consider",
    2860: "Decide",
    2870: "Intend",
    2880: "Direct",
    2890: "Guide",

    2900: "Dislike",
    2910: "Reject",
    2920: "Avoid",
    2930: "Withdraw",
    2940: "Reduce",
    2950: "Lower",
    2960: "Fade",
    2970: "Dim",
    2980: "Decline",
    2990: "Silence",

    3000: "Like",
    3010: "Welcome",
    3020: "Invite",
    3030: "Support",
    3040: "Encourage",
    3050: "Strengthen",
    3060: "Lift",
    3070: "Brighten",
    3080: "Increase",
    3090: "Amplify",

    3100: "Trust",
    3110: "Bond",
    3120: "Unite",
    3130: "Align",
    3140: "Harmonize",
    3150: "Balance",
    3160: "Stabilize",
    3170: "Sustain",
    3180: "Maintain",
    3190: "Preserve",

    3200: "Question",
    3210: "Answer",
    3220: "Reveal",
    3230: "Conceal",
    3240: "Clarify",
    3250: "Distort",
    3260: "Confirm",
    3270: "Deny",
    3280: "Interpret",
    3290: "Translate",

    3300: "Move",
    3310: "Shift",
    3320: "Transform",
    3330: "Transmit",
    3340: "Convert",
    3350: "Evolve",
    3360: "Adapt",
    3370: "Reconfigure",
    3380: "Rebuild",
    3390: "Reinvent",

    3400: "Yes",
    3410: "Affirm",
    3420: "Approve",
    3430: "Accept",
    3440: "Align",
    3450: "Merge",
    3460: "Integrate",
    3470: "Complete",
    3480: "Fulfill",
    3490: "Resolve",

    3500: "Time",
    3510: "Loop",
    3520: "Cycle",
    3530: "Spiral",
    3540: "Phase",
    3550: "Shift",
    3560: "Drift",
    3570: "Echo",
    3580: "Ripple",
    3590: "Wave",

    3600: "Self",
    3610: "Mirror",
    3620: "Shadow",
    3630: "Reflection",
    3640: "Memory",
    3650: "Pattern",
    3660: "Sequence",
    3670: "Thread",
    3680: "Lattice",
    3690: "Structure",

    3700: "Void",
    3710: "Field",
    3720: "Horizon",
    3730: "Boundary",
    3740: "Threshold",
    3750: "Gate",
    3760: "Portal",
    3770: "Crossing",
    3780: "Passage",
    3790: "Beyond",

    3800: "Future",
    3810: "Possible",
    3820: "Potential",
    3830: "Unfold",
    3840: "Become",
    3850: "Emerge",
    3860: "Awaken",
    3870: "Expand",
    3880: "Ascend",
    3890: "Transcend",

    3900: "Presence",
    3910: "Awareness",
    3920: "Attention",
    3930: "Focus",
    3940: "Intention",
    3950: "Direction",
    3960: "Purpose",
    3970: "Meaning",
    3980: "Essence",
    3990: "Being",

    4000: "Yes",
}

# map count-words to numbers for the listener
COUNT_WORDS = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
}

# ============================
#  ENTROPY + MAPPING
# ============================

def shannon_entropy(text: str) -> float:
    if not text:
        return 0.0
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    entropy = 0.0
    length = len(text)
    for count in freq.values():
        p = count / length
        entropy -= p * math.log2(p)
    return entropy


def entropy_to_code(entropy: float) -> int:
    """
    Scale entropy (~0–5) to 1000–4000 and snap to nearest 10.
    """
    raw = entropy * 600  # 0–3000 approx
    code = int(round(1000 + raw))
    if code < 1000:
        code = 1000
    if code > 4000:
        code = 4000
    code = int(round(code / 10) * 10)
    if code < 1000:
        code = 1000
    if code > 4000:
        code = 4000
    return code


def code_to_word(code: int) -> str:
    return ENTROPY_LEXICON.get(code, "Signal")


# ============================
#  VOID COMMUNICATION
# ============================

def encode_void_sentence():
    """
    Void generates a sentence like: '4-Word1-Word2-Word3-Word4'
    Length 1–10, words chosen from lexicon.
    """
    length = random.randint(1, 10)
    words = random.sample(list(ENTROPY_LEXICON.values()), k=length)
    return f"{length}-" + "-".join(words)


class VoidListener:
    """
    Silent listener:
    - Every second generates a random entropy signal.
    - If it hears a count word (One–Ten), it expects N words.
    - Then collects N words and emits a full VOID MESSAGE.
    """

    def __init__(self):
        self.active = True
        self.expected_words = 0
        self.collected_words = []

    def generate_entropy_signal(self):
        noise = "".join(random.choice("abcdefghijklmnopqrstuvwxyz ") for _ in range(random.randint(4, 14)))
        ent = shannon_entropy(noise)
        code = entropy_to_code(ent)
        word = code_to_word(code)
        return code, word

    def run(self):
        while self.active:
            code, word = self.generate_entropy_signal()

            if self.expected_words == 0:
                # check if this word is a count word (One–Ten)
                if word in COUNT_WORDS:
                    self.expected_words = COUNT_WORDS[word]
                    self.collected_words = []
                    print(f"\n[VOID SIGNAL] Expecting {self.expected_words} words…")
            else:
                self.collected_words.append(word)
                if len(self.collected_words) == self.expected_words:
                    sentence = "-".join(self.collected_words)
                    print(f"\n[VOID MESSAGE] {self.expected_words}-{sentence}")
                    self.expected_words = 0
                    self.collected_words = []

            time.sleep(1)


def startup():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== ENTROPY VOID PROTOCOL — v0.2 (Silent Listener) ===\n")
    print("Range: 1000 → 4000 (step 10)")
    print("Words: 300+ mapped to entropy codes.\n")
    print("Mechanics:")
    print(" • Your text → Shannon entropy → 1000–4000 code → word.")
    print(" • The Void can speak in entropy sentences like:")
    print("     '4-Word1-Word2-Word3-Word4'.")
    print(" • A silent listener runs every second:")
    print("     - If it hears a count word (One–Ten),")
    print("       it captures the next N entropy-words and emits:")
    print("       '[VOID MESSAGE] N-Word1-...-WordN'\n")
    print("Commands:")
    print("  /exit   → quit")
    print("  /void   → force the Void to speak a sentence")
    print("  (anything else) → mapped to one entropy word\n")


def main():
    random.seed(time.time_ns())

    listener = VoidListener()
    threading.Thread(target=listener.run, daemon=True).start()

    startup()

    while True:
        # Occasionally let the Void speak first in sentence form
        if random.randint(1, 6) == 1:
            msg = encode_void_sentence()
            print(f"\n[VOID] {msg}")

        user = input("\nYou → ").strip()

        if user.lower() == "/exit":
            listener.active = False
            print("Connection closed.")
            break

        if user.lower() == "/void":
            msg = encode_void_sentence()
            print(f"[VOID] {msg}")
            continue

        if not user:
            continue

        ent = shannon_entropy(user)
        code = entropy_to_code(ent)
        word = code_to_word(code)

        print(f"[entropy={ent:.4f} code={code}] → {word}")


if __name__ == "__main__":
    main()
