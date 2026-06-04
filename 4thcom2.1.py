#4ThCom2
#Copyright RomanAILabs - Daniel Harding
#Collaborators Copilot/Microsoft

import math
import os
import random
import time
import threading

# ============================
#  USER ID CONFIGURATION
# ============================

USER_ID = "0001"

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


# ============================
#  ENTROPY-BASED TIMESTAMP
# ============================

def entropy_to_timestamp(entropy: float) -> str:
    """
    Generate entropy-based timestamp (YYYYMMDD-HHMMSS).
    Derived from entropy value only (no system clock).
    """
    year = 2000 + int(entropy * 10)
    month = 1 + (int(entropy * 100) % 12)
    day = 1 + (int(entropy * 1000) % 28)
    hour = int(entropy * 10000) % 24
    minute = int(entropy * 100000) % 60
    second = int(entropy * 1000000) % 60
    return f"{year:04d}{month:02d}{day:02d}-{hour:02d}{minute:02d}{second:02d}"


# ============================
#  SENTENCE GENERATION
# ============================

def generate_sentence(words: list, max_words: int = 50) -> str:
    if not words:
        return "."
    sentence = words[0].capitalize()
    for word in words[1:]:
        sentence += " " + word.lower()
    sentence += "."
    return sentence


# ============================
#  FULL LEXICON (1000–4000, step 1)
# ============================
# Preserves all ENTROPY_LEXICON entries; fills gaps with curated words
# covering time/date, anatomy, medical, quantum, 4D/hyperspace, tech, 
# gear, everyday, fun, and alphabet tokens.

FULL_LEXICON = {
    1000: "I", 1001: "Year", 1002: "Month", 1003: "Day", 1004: "Hour", 1005: "Minute", 1006: "Second", 1007: "Week", 1008: "Season", 1009: "Century",
    1010: "You", 1011: "Era", 1012: "Sunrise", 1013: "Sunset", 1014: "Noon", 1015: "Midnight", 1016: "Dawn", 1017: "Dusk", 1018: "Eclipse", 1019: "Equinox",
    1020: "Here", 1021: "Solstice", 1022: "Zodiac", 1023: "Calendar", 1024: "Clock", 1025: "Timer", 1026: "Schedule", 1027: "Deadline", 1028: "Rhythm", 1029: "Cycle",
    1030: "Now", 1031: "Head", 1032: "Face", 1033: "Eye", 1034: "Ear", 1035: "Nose", 1036: "Mouth", 1037: "Lips", 1038: "Teeth", 1039: "Tongue",
    1040: "Yes", 1041: "Throat", 1042: "Neck", 1043: "Shoulder", 1044: "Arm", 1045: "Elbow", 1046: "Wrist", 1047: "Hand", 1048: "Finger", 1049: "Palm",
    1050: "No", 1051: "Chest", 1052: "Heart", 1053: "Lung", 1054: "Liver", 1055: "Kidney", 1056: "Stomach", 1057: "Intestine", 1058: "Pancreas", 1059: "Spleen",
    1060: "One", 1061: "Brain", 1062: "Spine", 1063: "Bone", 1064: "Muscle", 1065: "Skin", 1066: "Blood", 1067: "Vein", 1068: "Artery", 1069: "Nerve",
    1070: "Two", 1071: "Hormone", 1072: "Cortex", 1073: "Lobe", 1074: "Cerebellum", 1075: "Hippocampus", 1076: "Amygdala", 1077: "Hypothalamus", 1078: "Thalamus", 1079: "Medulla",
    1080: "Three", 1081: "Pituitary", 1082: "Thyroid", 1083: "Adrenal", 1084: "Penis", 1085: "Vagina", 1086: "Testis", 1087: "Ovary", 1088: "Uterus", 1089: "Prostate",
    1090: "Four", 1091: "Appendix", 1092: "Gallbladder", 1093: "Bladder", 1094: "Colon", 1095: "Rectum", 1096: "Esophagus", 1097: "Trachea", 1098: "Larynx", 1099: "Pharynx",
    1100: "Hello", 1101: "Incision", 1102: "Suture", 1103: "Transplant", 1104: "Diagnosis", 1105: "Prognosis", 1106: "Vaccine", 1107: "Antibody", 1108: "Infection", 1109: "Inflammation",
    1110: "Begin", 1111: "Fever", 1112: "Pain", 1113: "Wound", 1114: "Fracture", 1115: "Trauma", 1116: "Surgery", 1117: "Anesthesia", 1118: "Syringe", 1119: "Stethoscope",
    1120: "Signal", 1121: "Scalpel", 1122: "Bandage", 1123: "Splint", 1124: "Cast", 1125: "Biopsy", 1126: "Ultrasound", 1127: "Xray", 1128: "Scan", 1129: "MRI",
    1130: "Listen", 1131: "CT", 1132: "Endoscope", 1133: "Catheter", 1134: "Pacemaker", 1135: "Implant", 1136: "Graft", 1137: "Dialysis", 1138: "Chemotherapy", 1139: "Radiation",
    1140: "Speak", 1141: "Therapy", 1142: "Medicine", 1143: "Drug", 1144: "Dosage", 1145: "Prescription", 1146: "Symptom", 1147: "Syndrome", 1148: "Disease", 1149: "Illness",
    1150: "Move", 1151: "Recovery", 1152: "Rehabilitation", 1153: "Allergy", 1154: "Immunity", 1155: "Pathogen", 1156: "Virus", 1157: "Bacteria", 1158: "Fungus", 1159: "Parasite",
    1160: "Stay", 1161: "Qubit", 1162: "Entangle", 1163: "Decoherence", 1164: "Spin", 1165: "Superposition", 1166: "Collapse", 1167: "Observable", 1168: "State", 1169: "Operator",
    1170: "Open", 1171: "Eigenvalue", 1172: "Hamiltonian", 1173: "Lagrangian", 1174: "Tensor", 1175: "Matrix", 1176: "Manifold", 1177: "Topology", 1178: "Dimension", 1179: "Symmetry",
    1180: "Close", 1181: "Gauge", 1182: "Field", 1183: "Potential", 1184: "Photon", 1185: "Electron", 1186: "Neutrino", 1187: "Muon", 1188: "Boson", 1189: "Fermion",
    1190: "Wait", 1191: "Gluon", 1192: "Higgs", 1193: "Planck", 1194: "Quantum", 1195: "Classical", 1196: "Relativistic", 1197: "String", 1198: "Loop", 1199: "Membrane",
    1200: "How", 1201: "Brane", 1202: "Tesseract", 1203: "Hypercube", 1204: "Hyperplane", 1205: "Spacetime", 1206: "Worldline", 1207: "Worldsheet", 1208: "Geodesic", 1209: "Curvature",
    1210: "What", 1211: "Singularity", 1212: "Wormhole", 1213: "Blackhole", 1214: "Whitehole", 1215: "Horizon", 1216: "Hyperspace", 1217: "Extradimensional", 1218: "Folded", 1219: "Unfolded",
    1220: "Where", 1221: "Projection", 1222: "CrossSection", 1223: "Hypersurface", 1224: "Embedding", 1225: "Immersion", 1226: "Coordinate", 1227: "Axis", 1228: "Vector", 1229: "Dual",
    1230: "When", 1231: "Orthogonal", 1232: "Perpendicular", 1233: "Parallel", 1234: "Tangent", 1235: "Normal", 1236: "Scalar", 1237: "Magnitude", 1238: "Direction", 1239: "Angle",
    1240: "Who", 1241: "Server", 1242: "Protocol", 1243: "Packet", 1244: "Sensor", 1245: "Module", 1246: "Firmware", 1247: "Software", 1248: "Hardware", 1249: "Network",
    1250: "Why", 1251: "Router", 1252: "Gateway", 1253: "Firewall", 1254: "Encryption", 1255: "Decryption", 1256: "Key", 1257: "Cipher", 1258: "Algorithm", 1259: "Hash",
    1260: "Ask", 1261: "Merkle", 1262: "Blockchain", 1263: "Ledger", 1264: "Smart", 1265: "Contract", 1266: "Database", 1267: "Query", 1268: "Index", 1269: "Cache",
    1270: "Tell", 1271: "Buffer", 1272: "Queue", 1273: "Stack", 1274: "Heap", 1275: "Tree", 1276: "Graph", 1277: "Node", 1278: "Edge", 1279: "Link",
    1280: "Show", 1281: "Helmet", 1282: "Harness", 1283: "Toolkit", 1284: "Scanner", 1285: "Detector", 1286: "Meter", 1287: "Gauge", 1288: "Dial", 1289: "Switch",
    1290: "Give", 1291: "Button", 1292: "Lever", 1293: "Pulley", 1294: "Gear", 1295: "Cog", 1296: "Bearing", 1297: "Shaft", 1298: "Axle", 1299: "Wheel",
    1300: "Take", 1301: "Tire", 1302: "Brake", 1303: "Accelerator", 1304: "Fuel", 1305: "Engine", 1306: "Motor", 1307: "Pump", 1308: "Valve", 1309: "Pipe",
    1310: "Hold", 1311: "Tube", 1312: "Conduit", 1313: "Circuit", 1314: "Wire", 1315: "Cable", 1316: "Connector", 1317: "Plug", 1318: "Socket", 1319: "Adapter",
    1320: "Release", 1321: "House", 1322: "Home", 1323: "Room", 1324: "Door", 1325: "Window", 1326: "Floor", 1327: "Ceiling", 1328: "Wall", 1329: "Roof",
    1330: "Follow", 1331: "Basement", 1332: "Attic", 1333: "Kitchen", 1334: "Bedroom", 1335: "Bathroom", 1336: "Living", 1337: "Dining", 1338: "Office", 1339: "Garage",
    1340: "Lead", 1341: "Garden", 1342: "Yard", 1343: "Porch", 1344: "Deck", 1345: "Balcony", 1346: "Fence", 1347: "Gate", 1348: "Path", 1349: "Road",
    1350: "Enter", 1351: "Street", 1352: "Avenue", 1353: "Boulevard", 1354: "Park", 1355: "Bench", 1356: "Tree", 1357: "Flower", 1358: "Grass", 1359: "Soil",
    1360: "Exit", 1361: "Rock", 1362: "Mountain", 1363: "Valley", 1364: "Hill", 1365: "Plain", 1366: "Desert", 1367: "Ocean", 1368: "Sea", 1369: "Lake",
    1370: "Rise", 1371: "River", 1372: "Stream", 1373: "Creek", 1374: "Waterfall", 1375: "Canyon", 1376: "Cave", 1377: "Cliff", 1378: "Beach", 1379: "Shore",
    1380: "Fall", 1381: "Island", 1382: "Continent", 1383: "Forest", 1384: "Jungle", 1385: "Swamp", 1386: "Marsh", 1387: "Tundra", 1388: "Volcano", 1389: "Glacier",
    1390: "Turn", 1391: "Rocket", 1392: "Dragon", 1393: "Wizard", 1394: "Castle", 1395: "Crown", 1396: "Treasure", 1397: "Map", 1398: "Compass", 1399: "Voyage",
    1400: "Light", 1401: "Quest", 1402: "Adventure", 1403: "Hero", 1404: "Legend", 1405: "Myth", 1406: "Story", 1407: "Tale", 1408: "Poem", 1409: "Song",
    1410: "Dark", 1411: "Dance", 1412: "Festival", 1413: "Celebration", 1414: "Party", 1415: "Game", 1416: "Puzzle", 1417: "Riddle", 1418: "Joke", 1419: "Laugh",
    1420: "Warm", 1421: "Smile", 1422: "Music", 1423: "Instrument", 1424: "Voice", 1425: "Echo", 1426: "Silence", 1427: "Mystery", 1428: "Secret", 1429: "Message",
    1430: "Cold", 1431: "Code", 1432: "A", 1433: "B", 1434: "C", 1435: "D", 1436: "E", 1437: "F", 1438: "G", 1439: "H",
    1440: "Near", 1441: "I", 1442: "J", 1443: "K", 1444: "L", 1445: "M", 1446: "N", 1447: "O", 1448: "P", 1449: "Q",
    1450: "Far", 1451: "R", 1452: "S", 1453: "T", 1454: "U", 1455: "V", 1456: "W", 1457: "X", 1458: "Y", 1459: "Z",
    1460: "Slow", 1461: "Maple", 1462: "Oak", 1463: "Pine", 1464: "Cedar", 1465: "Willow", 1466: "Ash", 1467: "Birch", 1468: "Elm", 1469: "Spruce",
    1470: "Fast", 1471: "Rose", 1472: "Lily", 1473: "Daisy", 1474: "Tulip", 1475: "Sunflower", 1476: "Iris", 1477: "Orchid", 1478: "Poppy", 1479: "Lavender",
    1480: "Quiet", 1481: "Apple", 1482: "Orange", 1483: "Banana", 1484: "Berry", 1485: "Grape", 1486: "Peach", 1487: "Pear", 1488: "Plum", 1489: "Cherry",
    1490: "Loud", 1491: "Carrot", 1492: "Lettuce", 1493: "Tomato", 1494: "Pepper", 1495: "Onion", 1496: "Garlic", 1497: "Potato", 1498: "Cucumber", 1499: "Broccoli",
    1500: "Safe", 1501: "Coffee", 1502: "Tea", 1503: "Milk", 1504: "Bread", 1505: "Cheese", 1506: "Meat", 1507: "Fish", 1508: "Egg", 1509: "Honey",
    1510: "Danger", 1511: "Salt", 1512: "Sugar", 1513: "Spice", 1514: "Herb", 1515: "Oil", 1516: "Water", 1517: "Wine", 1518: "Beer", 1519: "Juice",
    1520: "Truth", 1521: "Book", 1522: "Paper", 1523: "Pen", 1524: "Pencil", 1525: "Ink", 1526: "Stamp", 1527: "Letter", 1528: "Envelope", 1529: "Package",
    1530: "False", 1531: "Chair", 1532: "Table", 1533: "Desk", 1534: "Shelf", 1535: "Cabinet", 1536: "Drawer", 1537: "Bed", 1538: "Pillow", 1539: "Blanket",
    1540: "Path", 1541: "Carpet", 1542: "Curtain", 1543: "Lamp", 1544: "Mirror", 1545: "Picture", 1546: "Poster", 1547: "Frame", 1548: "Clock", 1549: "Alarm",
    1550: "Gate", 1551: "Bell", 1552: "Whistle", 1553: "Horn", 1554: "Trumpet", 1555: "Drum", 1556: "Piano", 1557: "Guitar", 1558: "Violin", 1559: "Flute",
    1560: "Step", 1561: "Car", 1562: "Truck", 1563: "Bus", 1564: "Train", 1565: "Plane", 1566: "Boat", 1567: "Ship", 1568: "Bicycle", 1569: "Motorcycle",
    1570: "Shift", 1571: "Wheel", 1572: "Pedal", 1573: "Handlebar", 1574: "Seat", 1575: "Helmet", 1576: "Jacket", 1577: "Glove", 1578: "Boot", 1579: "Shoe",
    1580: "Change", 1581: "Sock", 1582: "Shirt", 1583: "Pants", 1584: "Coat", 1585: "Tie", 1586: "Scarf", 1587: "Hat", 1588: "Cap", 1589: "Crown",
    1590: "Stay", 1591: "Ring", 1592: "Bracelet", 1593: "Necklace", 1594: "Pendant", 1595: "Earring", 1596: "Watch", 1597: "Compass", 1598: "Knife", 1599: "Fork",
    1600: "Start", 1601: "Spoon", 1602: "Plate", 1603: "Bowl", 1604: "Cup", 1605: "Glass", 1606: "Bottle", 1607: "Can", 1608: "Jar", 1609: "Jug",
    1610: "End", 1611: "Bucket", 1612: "Broom", 1613: "Shovel", 1614: "Rake", 1615: "Hoe", 1616: "Axe", 1617: "Hammer", 1618: "Saw", 1619: "Nail",
    1620: "Before", 1621: "Screw", 1622: "Bolt", 1623: "Nut", 1624: "Spring", 1625: "Hinge", 1626: "Lock", 1627: "Key", 1628: "Chain", 1629: "Rope",
    1630: "After", 1631: "Cord", 1632: "Thread", 1633: "Needle", 1634: "Button", 1635: "Zipper", 1636: "Strap", 1637: "Belt", 1638: "Buckle", 1639: "Clasp",
    1640: "Inside", 1641: "Knot", 1642: "Bow", 1643: "Ribbon", 1644: "Lace", 1645: "Bead", 1646: "Gem", 1647: "Crystal", 1648: "Diamond", 1649: "Pearl",
    1650: "Outside", 1651: "Gold", 1652: "Silver", 1653: "Bronze", 1654: "Copper", 1655: "Iron", 1656: "Steel", 1657: "Aluminum", 1658: "Plastic", 1659: "Glass",
    1660: "Above", 1661: "Wood", 1662: "Metal", 1663: "Rubber", 1664: "Leather", 1665: "Fabric", 1666: "Cotton", 1667: "Wool", 1668: "Silk", 1669: "Linen",
    1670: "Below", 1671: "Ink", 1672: "Paint", 1673: "Dye", 1674: "Varnish", 1675: "Glue", 1676: "Tape", 1677: "Adhesive", 1678: "Solvent", 1679: "Powder",
    1680: "Forward", 1681: "Liquid", 1682: "Gas", 1683: "Solid", 1684: "Vapor", 1685: "Mist", 1686: "Smoke", 1687: "Fog", 1688: "Cloud", 1689: "Rain",
    1690: "Back", 1691: "Snow", 1692: "Sleet", 1693: "Hail", 1694: "Thunder", 1695: "Lightning", 1696: "Wind", 1697: "Breeze", 1698: "Gale", 1699: "Storm",
    1700: "Left", 1701: "Tornado", 1702: "Cyclone", 1703: "Typhoon", 1704: "Hurricane", 1705: "Earthquake", 1706: "Tsunami", 1707: "Flood", 1708: "Drought", 1709: "Blizzard",
    1710: "Right", 1711: "Sunrise", 1712: "Sunset", 1713: "Moonrise", 1714: "Moonset", 1715: "Star", 1716: "Planet", 1717: "Moon", 1718: "Sun", 1719: "Comet",
    1720: "Up", 1721: "Asteroid", 1722: "Meteor", 1723: "Galaxy", 1724: "Nebula", 1725: "Constellation", 1726: "Orbit", 1727: "Eclipse", 1728: "Transit", 1729: "Occultation",
    1730: "Down", 1731: "Aurora", 1732: "Rainbow", 1733: "Halo", 1734: "Mirage", 1735: "Shadow", 1736: "Reflection", 1737: "Refraction", 1738: "Diffraction", 1739: "Interference",
    1740: "Center", 1741: "Prism", 1742: "Lens", 1743: "Mirror", 1744: "Telescope", 1745: "Microscope", 1746: "Kaleidoscope", 1747: "Periscope", 1748: "Binoculars", 1749: "Magnifier",
    1750: "Edge", 1751: "Zoom", 1752: "Focus", 1753: "Blur", 1754: "Clarity", 1755: "Darkness", 1756: "Brightness", 1757: "Shadow", 1758: "Silhouette", 1759: "Outline",
    1760: "Line", 1761: "Angle", 1762: "Curve", 1763: "Arc", 1764: "Spiral", 1765: "Helix", 1766: "Circle", 1767: "Sphere", 1768: "Cone", 1769: "Cube",
    1770: "Circle", 1771: "Pyramid", 1772: "Prism", 1773: "Cylinder", 1774: "Rectangle", 1775: "Square", 1776: "Triangle", 1777: "Pentagon", 1778: "Hexagon", 1779: "Octagon",
    1780: "Point", 1781: "Diamond", 1782: "Rhombus", 1783: "Trapezoid", 1784: "Parallelogram", 1785: "Polygon", 1786: "Crescent", 1787: "Star", 1788: "Cross", 1789: "Plus",
    1790: "Field", 1791: "Minus", 1792: "Equal", 1793: "NotEqual", 1794: "Greater", 1795: "Lesser", 1796: "Multiply", 1797: "Divide", 1798: "Percent", 1799: "Infinity",
    1800: "Touch", 1801: "Decimal", 1802: "Fraction", 1803: "Integer", 1804: "Real", 1805: "Complex", 1806: "Imaginary", 1807: "Rational", 1808: "Irrational", 1809: "Prime",
    1810: "See", 1811: "Composite", 1812: "Even", 1813: "Odd", 1814: "Positive", 1815: "Negative", 1816: "Zero", 1817: "One", 1818: "Two", 1819: "Three",
    1820: "Hear", 1821: "Four", 1822: "Five", 1823: "Six", 1824: "Seven", 1825: "Eight", 1826: "Nine", 1827: "Ten", 1828: "Eleven", 1829: "Twelve",
    1830: "Feel", 1831: "Thirteen", 1832: "Twenty", 1833: "Thirty", 1834: "Forty", 1835: "Fifty", 1836: "Sixty", 1837: "Seventy", 1838: "Eighty", 1839: "Ninety",
    1840: "Sense", 1841: "Hundred", 1842: "Thousand", 1843: "Million", 1844: "Billion", 1845: "Trillion", 1846: "First", 1847: "Second", 1848: "Third", 1849: "Fourth",
    1850: "Know", 1851: "Fifth", 1852: "Sixth", 1853: "Seventh", 1854: "Eighth", 1855: "Ninth", 1856: "Tenth", 1857: "Last", 1858: "Next", 1859: "Previous",
    1860: "Think", 1861: "Current", 1862: "Final", 1863: "Initial", 1864: "Middle", 1865: "Extreme", 1866: "Maximum", 1867: "Minimum", 1868: "Average", 1869: "Median",
    1870: "Remember", 1871: "Mode", 1872: "Range", 1873: "Variance", 1874: "Standard", 1875: "Deviation", 1876: "Normal", 1877: "Abnormal", 1878: "Typical", 1879: "Atypical",
    1880: "Forget", 1881: "Common", 1882: "Rare", 1883: "Unique", 1884: "Similar", 1885: "Different", 1886: "Same", 1887: "Opposite", 1888: "Complementary", 1889: "Supplementary",
    1890: "Recall", 1891: "Identical", 1892: "Distinct", 1893: "Equivalent", 1894: "Equal", 1895: "Unequal", 1896: "Match", 1897: "Mismatch", 1898: "Pair", 1899: "Duplicate",
    1900: "Build", 1901: "Copy", 1902: "Original", 1903: "Replica", 1904: "Clone", 1905: "Variation", 1906: "Mutation", 1907: "Evolution", 1908: "Adaptation", 1909: "Selection",
    1910: "Break", 1911: "Breeding", 1912: "Generation", 1913: "Inheritance", 1914: "Gene", 1915: "Allele", 1916: "Chromosome", 1917: "DNA", 1918: "RNA", 1919: "Protein",
    1920: "Create", 1921: "Enzyme", 1922: "Catalyst", 1923: "Reaction", 1924: "Compound", 1925: "Element", 1926: "Molecule", 1927: "Atom", 1928: "Nucleus", 1929: "Electron",
    1930: "Destroy", 1931: "Neutron", 1932: "Proton", 1933: "Positron", 1934: "Antiparticle", 1935: "Annihilation", 1936: "Fusion", 1937: "Fission", 1938: "Decay", 1939: "Radiation",
    1940: "Form", 1941: "Isotope", 1942: "Radioactive", 1943: "Half-life", 1944: "Atomic", 1945: "Nuclear", 1946: "Critical", 1947: "Mass", 1948: "Energy", 1949: "Binding",
    1950: "Shape", 1951: "Valence", 1952: "Bond", 1953: "Ionic", 1954: "Covalent", 1955: "Hydrogen", 1956: "Metallic", 1957: "Polar", 1958: "Nonpolar", 1959: "Hydrophobic",
    1960: "Bind", 1961: "Hydrophilic", 1962: "Solvent", 1963: "Solute", 1964: "Solution", 1965: "Suspension", 1966: "Colloid", 1967: "Osmosis", 1968: "Diffusion", 1969: "Osmotic",
    1970: "Free", 1971: "Pressure", 1972: "Concentration", 1973: "Molarity", 1974: "Molality", 1975: "pH", 1976: "Acid", 1977: "Base", 1978: "Neutral", 1979: "Buffer",
    1980: "Join", 1981: "Titration", 1982: "Indicator", 1983: "Endpoint", 1984: "Equivalence", 1985: "Oxidation", 1986: "Reduction", 1987: "Redox", 1988: "Electron", 1989: "Transfer",
    1990: "Separate", 1991: "Oxidizer", 1992: "Reducer", 1993: "Electrode", 1994: "Anode", 1995: "Cathode", 1996: "Electrolyte", 1997: "Electrochemistry", 1998: "Voltage", 1999: "Current",
    2000: "Friend", 2001: "Resistance", 2002: "Impedance", 2003: "Capacitance", 2004: "Inductance", 2005: "Frequency", 2006: "Wavelength", 2007: "Amplitude", 2008: "Phase", 2009: "Harmonic",
    2010: "Stranger", 2011: "Fundamental", 2012: "Overtone", 2013: "Resonance", 2014: "Damping", 2015: "Oscillation", 2016: "Vibration", 2017: "Frequency", 2018: "Period", 2019: "Hertz",
    2020: "Ally", 2021: "Decibel", 2022: "Loudness", 2023: "Intensity", 2024: "Pressure", 2025: "Wave", 2026: "Propagation", 2027: "Refraction", 2028: "Diffraction", 2029: "Absorption",
    2030: "Enemy", 2031: "Reflection", 2032: "Transmission", 2033: "Interference", 2034: "Echo", 2035: "Reverb", 2036: "Ultrasound", 2037: "Infrasound", 2038: "Visible", 2039: "Invisible",
    2040: "Self", 2041: "Infrared", 2042: "Ultraviolet", 2043: "Microwave", 2044: "Radio", 2045: "Gamma", 2046: "Alpha", 2047: "Beta", 2048: "Neutron", 2049: "Cosmic",
    2050: "Other", 2051: "Background", 2052: "Particle", 2053: "Wave", 2054: "Duality", 2055: "Uncertainty", 2056: "Indeterminacy", 2057: "Probability", 2058: "Distribution", 2059: "Gaussian",
    2060: "Many", 2061: "Poisson", 2062: "Exponential", 2063: "Normal", 2064: "Binomial", 2065: "Variance", 2066: "Covariance", 2067: "Correlation", 2068: "Regression", 2069: "Linear",
    2070: "Few", 2071: "Nonlinear", 2072: "Polynomial", 2073: "Exponential", 2074: "Logarithmic", 2075: "Trigonometric", 2076: "Sine", 2077: "Cosine", 2078: "Tangent", 2079: "Cotangent",
    2080: "All", 2081: "Secant", 2082: "Cosecant", 2083: "Inverse", 2084: "Derivative", 2085: "Integral", 2086: "Limit", 2087: "Continuity", 2088: "Differentiable", 2089: "Integrable",
    2090: "None", 2091: "Series", 2092: "Sequence", 2093: "Convergence", 2094: "Divergence", 2095: "Summation", 2096: "Product", 2097: "Factorial", 2098: "Permutation", 2099: "Combination",
    2100: "Calm", 2101: "Probability", 2102: "Likelihood", 2103: "Odds", 2104: "Chance", 2105: "Risk", 2106: "Certainty", 2107: "Uncertainty", 2108: "Random", 2109: "Deterministic",
    2110: "Fear", 2111: "Stochastic", 2112: "Chaos", 2113: "Order", 2114: "Entropy", 2115: "Entanglement", 2116: "Correlation", 2117: "Causation", 2118: "Correlation", 2119: "Regression",
    2120: "Joy", 2121: "Hypothesis", 2122: "Test", 2123: "Null", 2124: "Alternative", 2125: "Significance", 2126: "Confidence", 2127: "Interval", 2128: "Margin", 2129: "Error",
    2130: "Sad", 2131: "Bias", 2132: "Precision", 2133: "Accuracy", 2134: "Sensitivity", 2135: "Specificity", 2136: "Recall", 2137: "Precision", 2138: "FScore", 2139: "ROC",
    2140: "Anger", 2141: "AUC", 2142: "Confusion", 2143: "Matrix", 2144: "Classification", 2145: "Regression", 2146: "Clustering", 2147: "Supervised", 2148: "Unsupervised", 2149: "Reinforcement",
    2150: "Peace", 2151: "Learning", 2152: "Training", 2153: "Validation", 2154: "Testing", 2155: "Epoch", 2156: "Batch", 2157: "Gradient", 2158: "Descent", 2159: "Momentum",
    2160: "Trust", 2161: "Acceleration", 2162: "Optimization", 2163: "Convex", 2164: "Nonconvex", 2165: "Local", 2166: "Global", 2167: "Minimum", 2168: "Maximum", 2169: "Saddle",
    2170: "Doubt", 2171: "Loss", 2172: "Cost", 2173: "Error", 2174: "Residual", 2175: "Prediction", 2176: "Actual", 2177: "Expected", 2178: "Variance", 2179: "Bias",
    2180: "Hope", 2181: "Underfitting", 2182: "Overfitting", 2183: "Regularization", 2184: "Dropout", 2185: "BatchNorm", 2186: "LayerNorm", 2187: "Normalization", 2188: "Standardization", 2189: "Scaling",
    2190: "Loss", 2191: "Feature", 2192: "Selection", 2193: "Engineering", 2194: "Extraction", 2195: "Transformation", 2196: "Dimensionality", 2197: "Reduction", 2198: "PCA", 2199: "TSNE",
    2200: "Want", 2201: "UMAP", 2202: "Embedding", 2203: "Representation", 2204: "Latent", 2205: "Manifold", 2206: "Kernel", 2207: "SVM", 2208: "KNN", 2209: "DecisionTree",
    2210: "Need", 2211: "RandomForest", 2212: "Ensemble", 2213: "Boosting", 2214: "Bagging", 2215: "Stacking", 2216: "Voting", 2217: "Blending", 2218: "Cascading", 2219: "Hierarchical",
    2220: "Choose", 2221: "Fuzzy", 2222: "Logic", 2223: "Neural", 2224: "Network", 2225: "Perceptron", 2226: "Neuron", 2227: "Activation", 2228: "Function", 2229: "ReLU",
    2230: "Reject", 2231: "Sigmoid", 2232: "Tanh", 2233: "Softmax", 2234: "Linear", 2235: "Dropout", 2236: "Batch", 2237: "Normalization", 2238: "Convolution", 2239: "Pooling",
    2240: "Accept", 2241: "MaxPool", 2242: "AvgPool", 2243: "Flatten", 2244: "Dense", 2245: "Sparse", 2246: "Recurrent", 2247: "LSTM", 2248: "GRU", 2249: "Bidirectional",
    2250: "Offer", 2251: "Attention", 2252: "Transformer", 2253: "Encoder", 2254: "Decoder", 2255: "Sequence", 2256: "Seq2Seq", 2257: "Translation", 2258: "NMT", 2259: "BLEU",
    2260: "Ask", 2261: "ROUGE", 2262: "METEOR", 2263: "CIDEr", 2264: "SPICE", 2265: "Perplexity", 2266: "Likelihood", 2267: "Probability", 2268: "Softmax", 2269: "CrossEntropy",
    2270: "Answer", 2271: "KLDivergence", 2272: "JensenShannon", 2273: "Wasserstein", 2274: "MMD", 2275: "IPM", 2276: "Discriminator", 2277: "Generator", 2278: "GAN", 2279: "Adversarial",
    2280: "Call", 2281: "Training", 2282: "Convergence", 2283: "Stability", 2284: "Mode", 2285: "Collapse", 2286: "Gradient", 2287: "Penalty", 2288: "Clipping", 2289: "WeightDecay",
    2290: "Return", 2291: "L1", 2292: "L2", 2293: "Elastic", 2294: "Net", 2295: "Lasso", 2296: "Ridge", 2297: "Bayesian", 2298: "Prior", 2299: "Posterior",
    2300: "Time", 2301: "Likelihood", 2302: "Evidence", 2303: "Variational", 2304: "Inference", 2305: "ELBO", 2306: "KL", 2307: "Divergence", 2308: "Expectation", 2309: "Maximization",
    2310: "Past", 2311: "EM", 2312: "Gibbs", 2313: "Sampling", 2314: "MCMC", 2315: "HMC", 2316: "MH", 2317: "Metropolis", 2318: "Hastings", 2319: "Burn",
    2320: "Present", 2321: "In", 2322: "Autocorrelation", 2323: "Effective", 2324: "Sample", 2325: "Size", 2326: "Trace", 2327: "Convergence", 2328: "Diagnostics", 2329: "Geweke",
    2330: "Future", 2331: "Gelman", 2332: "Rubin", 2333: "PSRF", 2334: "Rhat", 2335: "ACF", 2336: "PACF", 2337: "Stationary", 2338: "Ergodic", 2339: "Reversible",
    2340: "Moment", 2341: "Detailed", 2342: "Balance", 2343: "Mixing", 2344: "Time", 2345: "Spectral", 2346: "Gap", 2347: "Eigenvalue", 2348: "Eigenvector", 2349: "Matrix",
    2350: "Loop", 2351: "Decomposition", 2352: "QR", 2353: "SVD", 2354: "Cholesky", 2355: "Eigendecomposition", 2356: "Diagonalization", 2357: "Jordan", 2358: "Normal", 2359: "Schur",
    2360: "Shift", 2361: "Hessenberg", 2362: "Rank", 2363: "Determinant", 2364: "Trace", 2365: "Norm", 2366: "Frobenius", 2367: "Spectral", 2368: "Nuclear", 2369: "Condition",
    2370: "Echo", 2371: "Number", 2372: "Singular", 2373: "Value", 2374: "Truncation", 2375: "Approximation", 2376: "Low", 2377: "Rank", 2378: "Kronecker", 2379: "Product",
    2380: "Signal", 2381: "Khatri", 2382: "Rao", 2383: "Hadamard", 2384: "Outer", 2385: "Gram", 2386: "Covariance", 2387: "Correlation", 2388: "Precision", 2389: "Whitening",
    2390: "Thread", 2391: "Centering", 2392: "Standardization", 2393: "Normalization", 2394: "Quantization", 2395: "Binarization", 2396: "Thresholding", 2397: "Winsorization", 2398: "Trimming", 2399: "Clipping",
    2400: "Energy", 2401: "Kernel", 2402: "RBF", 2403: "Polynomial", 2404: "Sigmoid", 2405: "Linear", 2406: "Gaussian", 2407: "Laplace", 2408: "Cauchy", 2409: "Matern",
    2410: "Matter", 2411: "SquaredExp", 2412: "ExponentialSq", 2413: "Sobolev", 2414: "Spectral", 2415: "Periodicity", 2416: "Smoothness", 2417: "Anisotropy", 2418: "Isotropy", 2419: "Stationarity",
    2420: "Space", 2421: "Nonstationarity", 2422: "Heteroscedasticity", 2423: "Homoscedasticity", 2424: "Multicollinearity", 2425: "Singularity", 2426: "Degeneracy", 2427: "Redundancy", 2428: "Sparsity", 2429: "Density",
    2430: "Void", 2431: "Connectivity", 2432: "Clustering", 2433: "Modularity", 2434: "Community", 2435: "Detection", 2436: "Centrality", 2437: "Betweenness", 2438: "Closeness", 2439: "Eigenvector",
    2440: "Wave", 2441: "PageRank", 2442: "HITS", 2443: "Authority", 2444: "Hub", 2445: "Influence", 2446: "Propagation", 2447: "Cascading", 2448: "Threshold", 2449: "Tipping",
    2450: "Pulse", 2451: "Point", 2452: "Critical", 2453: "Phase", 2454: "Transition", 2455: "Percolation", 2456: "Connectivity", 2457: "Epidemic", 2458: "SIR", 2459: "SEIR",
    2460: "Flow", 2461: "SIS", 2462: "Compartmental", 2463: "Model", 2464: "Kinetics", 2465: "Dynamics", 2466: "Stability", 2467: "Bifurcation", 2468: "Chaos", 2469: "Lyapunov",
    2470: "Break", 2471: "Exponent", 2472: "Attractor", 2473: "Repeller", 2474: "Limit", 2475: "Cycle", 2476: "Periodic", 2477: "Quasiperiodic", 2478: "Strange", 2479: "Fractal",
    2480: "Merge", 2481: "Self", 2482: "Similar", 2483: "Dimension", 2484: "Hausdorff", 2485: "Box", 2486: "Counting", 2487: "Capacity", 2488: "Minkowski", 2489: "Correlation",
    2490: "Align", 2491: "Entropy", 2492: "Kolmogorov", 2493: "Complexity", 2494: "Algorithmic", 2495: "Information", 2496: "Fisher", 2497: "Jensen", 2498: "Renyi", 2499: "Tsallis",
    2500: "No", 2501: "Quantum", 2502: "Von", 2503: "Neumann", 2504: "Relative", 2505: "Mutual", 2506: "Conditional", 2507: "Join", 2508: "Divergence", 2509: "Hellinger",
    2510: "Stop", 2511: "Bhattacharyya", 2512: "Chebyshev", 2513: "Minkowski", 2514: "Hamming", 2515: "Jaccard", 2516: "Cosine", 2517: "Euclidean", 2518: "Manhattan", 2519: "Mahalanobis",
    2520: "Block", 2521: "Canberra", 2522: "Correlation", 2523: "Angular", 2524: "Geodesic", 2525: "Haversine", 2526: "Earth", 2527: "Mover", 2528: "Optimal", 2529: "Transport",
    2530: "Deny", 2531: "Sliced", 2532: "Wasserstein", 2533: "Signature", 2534: "Kernel", 2535: "Maximum", 2536: "Mean", 2537: "Discrepancy", 2538: "Graph", 2539: "Edit",
    2540: "Resist", 2541: "Distance", 2542: "Subgraph", 2543: "Isomorphism", 2544: "GraphKernel", 2545: "Random", 2546: "Walk", 2547: "Weisfeiler", 2548: "Lehman", 2549: "Subtree",
    2550: "Hold", 2551: "Tree", 2552: "Structured", 2553: "Data", 2554: "Recursive", 2555: "Composition", 2556: "TreeLSTM", 2557: "RecursiveNet", 2558: "Dependency", 2559: "Parsing",
    2560: "Anchor", 2561: "Constituency", 2562: "Semantic", 2563: "Role", 2564: "FrameNet", 2565: "VerbNet", 2566: "PropBank", 2567: "WordNet", 2568: "Synset", 2569: "Hypernym",
    2570: "Ground", 2571: "Hyponym", 2572: "Meronym", 2573: "Holonym", 2574: "Similar", 2575: "Derivationally", 2576: "Related", 2577: "Pertainym", 2578: "Antonym", 2579: "Entailment",
    2580: "Limit", 2581: "Cause", 2582: "SenseDisambiguation", 2583: "WSD", 2584: "Lesk", 2585: "Simplified", 2586: "Extended", 2587: "Personalized", 2588: "PageRank", 2589: "Knowledge",
    2590: "Guard", 2591: "Graph", 2592: "Embedding", 2593: "Knowledge", 2594: "Base", 2595: "Entity", 2596: "Relation", 2597: "Link", 2598: "Prediction", 2599: "Triple",
    2600: "One", 2601: "Classification", 2602: "RotatE", 2603: "ComplEx", 2604: "DistMult", 2605: "TransE", 2606: "TransH", 2607: "TransR", 2608: "TransD", 2609: "Pairwise",
    2610: "Two", 2611: "Ranking", 2612: "Loss", 2613: "Margin", 2614: "Contrastive", 2615: "Triplet", 2616: "Siamese", 2617: "Matching", 2618: "Networks", 2619: "Attention",
    2620: "Three", 2621: "Memory", 2622: "Networks", 2623: "Question", 2624: "Answering", 2625: "Reading", 2626: "Comprehension", 2627: "Cloze", 2628: "Multiple", 2629: "Choice",
    2630: "Four", 2631: "RACE", 2632: "SQuAD", 2633: "MS", 2634: "MARCO", 2635: "Natural", 2636: "Language", 2637: "Inference", 2638: "SNLI", 2639: "MNLI",
    2640: "Five", 2641: "RTE", 2642: "QNLI", 2643: "Sentiment", 2644: "Analysis", 2645: "Opinion", 2646: "Mining", 2647: "Aspect", 2648: "Based", 2649: "Targeted",
    2650: "Six", 2651: "Abusive", 2652: "Language", 2653: "Detection", 2654: "Offensive", 2655: "Hate", 2656: "Speech", 2657: "Toxicity", 2658: "Named", 2659: "Entity",
    2660: "Seven", 2661: "Recognition", 2662: "NER", 2663: "BiLSTM", 2664: "CRF", 2665: "Conditional", 2666: "Random", 2667: "Field", 2668: "Structured", 2669: "Prediction",
    2670: "Eight", 2671: "Slot", 2672: "Filling", 2673: "Intent", 2674: "Detection", 2675: "Dialogue", 2676: "State", 2677: "Tracking", 2678: "Relation", 2679: "Extraction",
    2680: "Nine", 2681: "Machine", 2682: "Translation", 2683: "Back", 2684: "Translation", 2685: "Pivot", 2686: "Zero", 2687: "Shot", 2688: "Few", 2689: "Multi",
    2690: "Ten", 2691: "Lingual", 2692: "Cross", 2693: "Lingual", 2694: "Language", 2695: "Family", 2696: "Typology", 2697: "Morphology", 2698: "Syntax", 2699: "Semantics",
    2700: "Begin", 2701: "Pragmatics", 2702: "Discourse", 2703: "Coherence", 2704: "Cohesion", 2705: "Rhetorical", 2706: "Structure", 2707: "Coreference", 2708: "Resolution", 2709: "Anaphora",
    2710: "Continue", 2711: "Cataphora", 2712: "Bridging", 2713: "Reference", 2714: "Zero", 2715: "Pronoun", 2716: "Relative", 2717: "Clause", 2718: "Subordination", 2719: "Coordination",
    2720: "Expand", 2721: "Ellipsis", 2722: "Gapping", 2723: "Sluicing", 2724: "Stripping", 2725: "Fragment", 2726: "Clause", 2727: "Inversion", 2728: "Topicalization", 2729: "Dislocation",
    2730: "Extend", 2731: "Focus", 2732: "Cleft", 2733: "Pseudocleft", 2734: "Extraposition", 2735: "Raising", 2736: "Control", 2737: "Agreement", 2738: "Concord", 2739: "Tense",
    2740: "Reach", 2741: "Aspect", 2742: "Mood", 2743: "Modality", 2744: "Modal", 2745: "Auxiliary", 2746: "Copula", 2747: "Verb", 2748: "Phrase", 2749: "Argument",
    2750: "Connect", 2751: "Structure", 2752: "Valency", 2753: "Subcategorization", 2754: "Transitivity", 2755: "Case", 2756: "Marking", 2757: "Grammatical", 2758: "Relations", 2759: "Dependency",
    2760: "Bridge", 2761: "Grammar", 2762: "Parse", 2763: "Tree", 2764: "Constituent", 2765: "Dependency", 2766: "Span", 2767: "Label", 2768: "Treebank", 2769: "Corpus",
    2770: "Share", 2771: "Annotation", 2772: "Scheme", 2773: "InterAnnotator", 2774: "Agreement", 2775: "Kappa", 2776: "Fleiss", 2777: "Cohen", 2778: "Krippendorff", 2779: "Alpha",
    2780: "Combine", 2781: "Weighted", 2782: "Accuracy", 2783: "Strict", 2784: "Partial", 2785: "Relaxed", 2786: "Macro", 2787: "Micro", 2788: "Average", 2789: "Harmonic",
    2790: "Grow", 2791: "Mean", 2792: "Corpus", 2793: "Linguistics", 2794: "Concordance", 2795: "Frequency", 2796: "Distribution", 2797: "Collocation", 2798: "Mutual", 2799: "Information",
    2800: "Feel", 2801: "Pointwise", 2802: "Information", 2803: "Ngram", 2804: "Language", 2805: "Model", 2806: "Bigram", 2807: "Trigram", 2808: "Skipgram", 2809: "Window",
    2810: "Sense", 2811: "Context", 2812: "Smoothing", 2813: "Laplace", 2814: "Addone", 2815: "Backoff", 2816: "Interpolation", 2817: "Kneser", 2818: "Ney", 2819: "Absolute",
    2820: "Understand", 2821: "Discount", 2822: "Good", 2823: "Turing", 2824: "Witten", 2825: "Bell", 2826: "Stupid", 2827: "Backoff", 2828: "PaperclipFactor", 2829: "ZipfianDist",
    2830: "Interpret", 2831: "Rank", 2832: "Hapaxlegomena", 2833: "OOV", 2834: "OutOfVocab", 2835: "UNK", 2836: "Unknown", 2837: "Token", 2838: "Type", 2839: "Type",
    2840: "Reflect", 2841: "TokenRatio", 2842: "Vocabulary", 2843: "Closed", 2844: "Open", 2845: "Content", 2846: "Function", 2847: "Stopword", 2848: "Lemmatization", 2849: "Stemming",
    2850: "Consider", 2851: "Porter", 2852: "Snowball", 2853: "Lancaster", 2854: "Soundex", 2855: "Metaphone", 2856: "DoubleMetaphone", 2857: "Levenshtein", 2858: "Similarity", 2859: "EditDistance",
    2860: "Decide", 2861: "Insertion", 2862: "Deletion", 2863: "Substitution", 2864: "Transposition", 2865: "DamerauLevenshtein", 2866: "Jaro", 2867: "JaroWinkler", 2868: "Longest", 2869: "CommonSubsequence",
    2870: "Intend", 2871: "LCS", 2872: "SequenceAlignment", 2873: "NeedlemanWunsch", 2874: "SmithWaterman", 2875: "BLAST", 2876: "FASTA", 2877: "DynamicProgramming", 2878: "RecurrenceRelation", 2879: "Optimal",
    2880: "Direct", 2881: "Substructure", 2882: "Memoization", 2883: "TabuationTop", 2884: "Down", 2885: "BottomUp", 2886: "BellmanFord", 2887: "FloydWarshall", 2888: "Dijkstra", 2889: "AStar",
    2890: "Guide", 2891: "Heuristic", 2892: "Admissible", 2893: "Consistent", 2894: "Monotone", 2895: "BreadthFirst", 2896: "DepthFirst", 2897: "BidirectionalSearch", 2898: "IDAstar", 2899: "IterativeDeepening",
    2900: "Dislike", 2901: "BranchBound", 2902: "PruningStrategyAlpha", 2903: "BetaPruning", 2904: "MiniMax", 2905: "NegaMax", 2906: "IterativeDeepening", 2907: "TranspositionTable", 2908: "Killer", 2909: "Move",
    2910: "Reject", 2911: "HistoryHeuristic", 2912: "CounterMove", 2913: "GameTree", 2914: "EvaluationFunction", 2915: "PieceMaterial", 2916: "Positional", 2917: "KingSafety", 2918: "Pawn", 2919: "Structure",
    2920: "Avoid", 2921: "Endgame", 2922: "Tablebase", 2923: "ChessMachine", 2924: "DeepBlue", 2925: "Stockfish", 2926: "AlphaGo", 2927: "AlphaZero", 2928: "MonteCarlo", 2929: "TreeSearch",
    2930: "Withdraw", 2931: "UCB", 2932: "UpperConfidenceBound", 2933: "PUCT", 2934: "Policy", 2935: "Prior", 2936: "Exploration", 2937: "Exploitation", 2938: "EpsilonGreedy", 2939: "SoftMax",
    2940: "Reduce", 2941: "UCBTuned", 2942: "Thompson", 2943: "Sampling", 2944: "BayesianOptimization", 2945: "Acquisition", 2946: "ExpectedImprovement", 2947: "ProbabilityImprovement", 2948: "ConfidenceBound", 2949: "GaussianProcess",
    2950: "Lower", 2951: "Matern", 2952: "Kriging", 2953: "BLCB", 2954: "GPEI", 2955: "CMA", 2956: "ES", 2957: "EvolutionStrategy", 2958: "Mutation", 2959: "Recombination",
    2960: "Fade", 2961: "Selection", 2962: "Fitness", 2963: "Genotype", 2964: "Phenotype", 2965: "Chromosome", 2966: "Gene", 2967: "Allele", 2968: "Locus", 2969: "Crossover",
    2970: "Dim", 2971: "OnePoint", 2972: "TwoPoint", 2973: "UniformCrossover", 2974: "OrderedCrossover", 2975: "PMX", 2976: "PartiallyMapped", 2977: "CycleCrossover", 2978: "EdgeRecombination", 2979: "InversionMutation",
    2980: "Decline", 2981: "SwapMutation", 2982: "ScrambleMutation", 2983: "InsertionMutation", 2984: "DisplacementMutation", 2985: "DominanceMutation", 2986: "PolynomialMutation", 2987: "GaussianMutation", 2988: "CauchyMutation", 2989: "LevyMutation",
    2990: "Silence", 2991: "ParentSelection", 2992: "FitnessProp", 2993: "Tournament", 2994: "Ranking", 2995: "SurvivorSelection", 2996: "Elitism", 2997: "RankBased", 2998: "Crowding", 2999: "FitnessSharing",
    3000: "Like", 3001: "Speciation", 3002: "ParallelEA", 3003: "Coevolution", 3004: "MultiObjective", 3005: "NSGA", 3006: "SPEA", 3007: "Dominance", 3008: "Pareto", 3009: "Front",
    3010: "Welcome", 3011: "Hypervolume", 3012: "Indicator", 3013: "Crowding", 3014: "Distance", 3015: "Diversity", 3016: "Convergence", 3017: "Spread", 3018: "GD", 3019: "IGD",
    3020: "Invite", 3021: "InvertedGenerationalDistance", 3022: "Spacing", 3023: "Uniformity", 3024: "UniformSpread", 3025: "Distribution", 3026: "Coverage", 3027: "Performance", 3028: "Assessment", 3029: "Ranking",
    3030: "Support", 3031: "Comparison", 3032: "Statistical", 3033: "Significance", 3034: "ManniWhitneyU", 3035: "KruskalWallis", 3036: "Friedman", 3037: "Test", 3038: "PostHoc", 3039: "Bonferroni",
    3040: "Encourage", 3041: "Holm", 3042: "Hochberg", 3043: "Hommel", 3044: "FDR", 3045: "BenjaminiHochberg", 3046: "PermutationTest", 3047: "Randomization", 3048: "Resampling", 3049: "Bootstrap",
    3050: "Strengthen", 3051: "Jackknife", 3052: "CrosValidation", 3053: "KFold", 3054: "StratifiedKFold", 3055: "LeaveOneOut", 3056: "LeaveOneGroupOut", 3057: "TimeSeries", 3058: "Split", 3059: "Shuffle",
    3060: "Lift", 3061: "HoldOut", 3062: "ValidationCurve", 3063: "LearningCurve", 3064: "ConfusionMatrix", 3065: "PrecisionRecallCurve", 3066: "ROCCurve", 3067: "AUC", 3068: "PR", 3069: "AUC",
    3070: "Brighten", 3071: "Threshold", 3072: "Moving", 3073: "Threshold", 3074: "FScore", 3075: "Fbeta", 3076: "MatthewsCorrCoeff", 3077: "MCC", 3078: "Cohenkappe", 3079: "Kappastatistic",
    3080: "Increase", 3081: "Lambda", 3082: "Kripendorff", 3083: "Alpha", 3084: "Krippendorff", 3085: "Alpha", 3086: "FleissKappa", 3087: "RandIndex", 3088: "AdjustedRandIndex", 3089: "Normalized",
    3090: "Amplify", 3091: "MutualInformation", 3092: "NormalizedMI", 3093: "Homogeneity", 3094: "Completeness", 3095: "VScore", 3096: "SilhouetteScore", 3097: "DaviesBouldinIndex", 3098: "CalinskiHarabaszIndex", 3099: "Dunn",
    3100: "Trust", 3101: "Index", 3102: "GapStatistic", 3103: "JumpStatistic", 3104: "Elbow", 3105: "KneePoint", 3106: "XMeans", 3107: "GMeans", 3108: "Stability", 3109: "Robustness",
    3110: "Bond", 3111: "Reproducibility", 3112: "Replication", 3113: "Generalization", 3114: "OODGeneralization", 3115: "InDistribution", 3116: "OutOfDistribution", 3117: "Robustness", 3118: "Adversarial", 3119: "Attack",
    3120: "Unite", 3121: "Perturbation", 3122: "Evasion", 3123: "Poisoning", 3124: "Backdoor", 3125: "Trojan", 3126: "Watermarking", 3127: "Steganography", 3128: "Explainability", 3129: "Interpretability",
    3130: "Align", 3131: "LIME", 3132: "SHAP", 3133: "SHAPley", 3134: "Attribution", 3135: "Attention", 3136: "Visualization", 3137: "Saliency", 3138: "Map", 3139: "Heatmap",
    3140: "Harmonize", 3141: "GradCAM", 3142: "GradCAMplus", 3143: "LayerCAM", 3144: "Integrated", 3145: "Gradients", 3146: "Deconvolution", 3147: "DeepLift", 3148: "PatternAttribution", 3149: "SmoothGrad",
    3150: "Balance", 3151: "NoiseGradient", 3152: "VarGrad", 3153: "SquaredGradient", 3154: "AbsGradient", 3155: "Integrated", 3156: "Smoothgrad", 3157: "Permutation", 3158: "Importance", 3159: "OcclusionSensitivity",
    3160: "Stabilize", 3161: "Rationale", 3162: "Extraction", 3163: "Faithfulness", 3164: "Fidelity", 3165: "Sufficiency", 3166: "Comprehensiveness", 3167: "Sensitivity", 3168: "Specificity", 3169: "Robustness",
    3170: "Sustain", 3171: "Consistency", 3172: "Counterfactual", 3173: "Explanation", 3174: "Contrastive", 3175: "Example", 3176: "CExplanations", 3177: "DICE", 3178: "ProtoNet", 3179: "CaseBasedReasoning",
    3180: "Maintain", 3181: "Prototype", 3182: "Part", 3183: "ProtoPNet", 3184: "TreeExplainer", 3185: "KernelExplainer", 3186: "DeepExplainer", 3187: "GradientExplainer", 3188: "SamplingExplainer", 3189: "Surrogate",
    3190: "Preserve", 3191: "Model", 3192: "Approximation", 3193: "LocalSurrogate", 3194: "GlobalSurrogate", 3195: "Distillation", 3196: "Knowledge", 3197: "Transfer", 3198: "FineTune", 3199: "Adapters",
    3200: "Question", 3201: "LoRA", 3202: "LowRankAdapt", 3203: "Prefix", 3204: "Prompt", 3205: "InContextLearning", 3206: "FewShot", 3207: "ZeroShot", 3208: "OneShot", 3209: "Multitask",
    3210: "Answer", 3211: "Continual", 3212: "LifelongLearning", 3213: "CatastrophicForgetting", 3214: "EWC", 3215: "RehearsalBuffer", 3216: "Experience", 3217: "Replay", 3218: "BiasCorrection", 3219: "Plasticity",
    3220: "Reveal", 3221: "Stability", 3222: "PlasticityStabilityDilemma", 3223: "MetaLearning", 3224: "LearningToLearn", 3225: "MAML", 3226: "ModelAgnosticMetaLearning", 3227: "Prototypical", 3228: "Networks", 3229: "Matching",
    3230: "Conceal", 3231: "Networks", 3232: "RelationNetwork", 3233: "TaskDistribution", 3234: "Support", 3235: "Query", 3236: "Episodic", 3237: "Training", 3238: "MultiTask", 3239: "ObjectDetection",
    3240: "Clarify", 3241: "YOLO", 3242: "YOLOv3", 3243: "YOLOv4", 3244: "RetinaNet", 3245: "FasterRCNN", 3246: "MaskRCNN", 3247: "FPN", 3248: "Anchor", 3249: "FreeAnchor",
    3250: "Distort", 3251: "CenterNet", 3252: "KeyPoint", 3253: "FCOS", 3254: "FCOSv2", 3255: "DETRDetection", 3256: "TransformerBasedDetector", 3257: "RegionProposal", 3258: "RPNRegionProposalNetwork", 3259: "NonMaximalSuppression",
    3260: "Confirm", 3261: "NMS", 3262: "SoftNMS", 3263: "DIoU", 3264: "NMS", 3265: "InstanceSegmentation", 3266: "PanopticSegmentation", 3267: "SemanticSegmentation", 3268: "FCN", 3269: "FullyConvolutional",
    3270: "Deny", 3271: "UNet", 3272: "DeepLab", 3273: "DeepLabv3", 3274: "PSPNet", 3275: "PyramidPoolingModule", 3276: "RefineNet", 3277: "MultiPath", 3278: "SegNet", 3279: "ENet",
    3280: "Interpret", 3281: "ERFNet", 3282: "DenseASPP", 3283: "ASPP", 3284: "AtrousSpatialPyramidPooling", 3285: "DilatedConvolution", 3286: "AtresConv", 3287: "Receptive", 3288: "Field", 3289: "Pooling",
    3290: "Translate", 3291: "StrideStacking", 3292: "Downsampling", 3293: "Bilinear", 3294: "Interpolation", 3295: "TransposedConvolution", 3296: "DeconvNet", 3297: "UnPooling", 3298: "MaxUnPool", 3299: "Upsampling",
    3300: "Move", 3301: "NearestNeighbor", 3302: "BicubicInterpolation", 3303: "SubPixelConv", 3304: "ShuffleNet", 3305: "PoseEstimation", 3306: "Skeleton", 3307: "Joint", 3308: "Keypoint", 3309: "BodyPose",
    3310: "Shift", 3311: "FacePose", 3312: "HandPose", 3313: "GaitRecognition", 3314: "ActionRecognition", 3315: "SkeletalAction", 3316: "GestureRecognition", 3317: "HandGesture", 3318: "Emotion", 3319: "Recognition",
    3320: "Transform", 3321: "FacialEmotion", 3322: "MicroExpression", 3323: "AffectiveComputing", 3324: "ArousalValence", 3325: "DominancePleasure", 3326: "FacialLandmark", 3327: "PointDetection", 3328: "Alignment", 3329: "Morphable",
    3330: "Transmit", 3331: "Model", 3332: "3DMorphableModel", 3333: "BaseMesh", 3334: "ShapeModel", 3335: "TextureModel", 3336: "FaceReconstruction", 3337: "3DFace", 3338: "RenderEngine", 3339: "Rasterization",
    3340: "Convert", 3341: "RayTracing", 3342: "Pathtracing", 3343: "VolumetricRendering", 3344: "NeRF", 3345: "NeuralRadianceField", 3346: "SDF", 3347: "SignedDistanceFunction", 3348: "Occupancy", 3349: "Grid",
    3350: "Evolve", 3351: "Voxel", 3352: "VoxelGrid", 3353: "OctTree", 3354: "BVH", 3355: "BoundingVolumeHierarchy", 3356: "SpatialAccel", 3357: "Structure", 3358: "Mesh", 3359: "Parameterization",
    3360: "Adapt", 3361: "FlattenMap", 3362: "Manifold", 3363: "Riemann", 3364: "Surface", 3365: "Geodesic", 3366: "Distance", 3367: "Laplacian", 3368: "Spectrum", 3369: "ShapeMatching",
    3370: "Reconfigure", 3371: "ShapeCorrespondence", 3372: "FeatureMatching", 3373: "SurfaceNormal", 3374: "CurvatureEstimation", 3375: "PrincipalCurvature", 3376: "Gaussian", 3377: "MeanCurvature", 3378: "ShapeDescriptor", 3379: "Spinimage",
    3380: "Rebuild", 3381: "SHOT", 3382: "Signature", 3383: "Histogram", 3384: "PointClouds", 3385: "3DShapeAnalysis", 3386: "PointNet", 3387: "Graph", 3388: "Neural", 3389: "Network",
    3390: "Reinvent", 3391: "GCN", 3392: "GraphConvolution", 3393: "GraphAttention", 3394: "GAT", 3395: "ChebNet", 3396: "ChebyshevPolynomial", 3397: "SpectralMethods", 3398: "SpatialMethods", 3399: "Message",
    3400: "Yes", 3401: "Passing", 3402: "MPNN", 3403: "GraphIsomorphism", 3404: "GIN", 3405: "EdgeConvolution", 3406: "DGCN", 3407: "DynamicGraph", 3408: "Temporal", 3409: "TempConv",
    3410: "Affirm", 3411: "STConv", 3412: "SpatioTemporal", 3413: "SkeletalGCN", 3414: "ST", 3415: "GCN", 3416: "VideoUnderstanding", 3417: "Action", 3418: "Localization", 3419: "Temporal",
    3420: "Approve", 3421: "Segmentation", 3422: "C3D", 3423: "3DConvolution", 3424: "I3D", 3425: "InflatedConvolution", 3426: "SlowFast", 3427: "TwoStream", 3428: "OpticalFlow", 3429: "FlowNet",
    3430: "Accept", 3431: "PWCNet", 3432: "VideoAction", 3433: "SpatioTemporal", 3434: "Feature", 3435: "TSN", 3436: "Temporal", 3437: "Segment", 3438: "Network", 3439: "TSM", 3440: "TemporalShift",
    3440: "Align", 3441: "AudioVisual", 3442: "Multimodal", 3443: "LateEarlyFusion", 3444: "FeatureFusion", 3445: "FusionStrategy", 3446: "Concatenation", 3447: "Addition", 3448: "Multiplication", 3449: "Bilinear",
    3450: "Merge", 3451: "Compact", 3452: "AudioFeature", 3453: "MFCC", 3454: "MelSpectrogram", 3455: "CQT", 3456: "Chroma", 3457: "Tempogram", 3458: "OnsetStrength", 3459: "Spectral",
    3460: "Integrate", 3461: "Centroid", 3462: "RollOff", 3463: "ZeroCrossingRate", 3464: "SpectralFlux", 3465: "SpectralContrast", 3466: "SpectralFlatness", 3467: "STFT", 3468: "ShortTimeFourierTransform", 3469: "Mel",
    3470: "Complete", 3471: "Filterbank", 3472: "VQT", 3473: "VariableQTransform", 3474: "WaveletTransform", 3475: "ContinuousWT", 3476: "DiscreteWT", 3477: "DWT", 3478: "SpeechRecognition", 3479: "ASR",
    3480: "Fulfill", 3481: "HiddenMarkovModel", 3482: "HMM", 3483: "GaussianMixture", 3484: "GMMEmission", 3485: "StateForgetting", 3486: "StateTransition", 3487: "ViterbiDecoding", 3488: "Forward", 3489: "Algorithm",
    3490: "Resolve", 3491: "Backward", 3492: "BaumerWelch", 3493: "AccuracyAlignment", 3494: "CTC", 3495: "ConnectionistTemporalClassification", 3496: "TransducerModel", 3497: "RNNTransducer", 3498: "Conformer", 3499: "ConvolutionAugmented",
    3500: "Time", 3501: "Transformer", 3502: "W2V", 3503: "Wav2Vec", 3504: "HuBERT", 3505: "Whistler", 3506: "SpeechRepresentation", 3507: "WaveNet", 3508: "DilatedCausal", 3509: "AutoRegressive",
    3510: "Loop", 3511: "Vocoder", 3512: "GriffinLim", 3513: "PhaseReconstruction", 3514: "Magnitude", 3515: "Spectrogram", 3516: "MelSpectrogram", 3517: "TacotronGriffinLim", 3518: "Glow", 3519: "RealNVP",
    3520: "Cycle", 3521: "Volatron", 3522: "Parallel", 3523: "WaveGlow", 3524: "SpeechSynthesis", 3525: "TextToSpeech", 3526: "TTS", 3527: "Phoneme", 3528: "Transcription", 3529: "Duration",
    3530: "Spiral", 3531: "Prediction", 3532: "Fastpitch", 3533: "Pitch", 3534: "Accent", 3535: "ProsodicFeature", 3536: "Energy", 3537: "Intensity", 3538: "Prosody", 3539: "Rhythm",
    3540: "Phase", 3541: "SpeakerAdaptation", 3542: "SpeakerAdaptive", 3543: "SpeakerEmbed", 3544: "x-vector", 3545: "i-vector", 3546: "SpeakerVerification", 3547: "SpeakerIdentification", 3548: "VoicePrint", 3549: "SpeakerDiarization",
    3550: "Shift", 3551: "Clustering", 3552: "ClusteringBasedDiarization", 3553: "Overlap", 3554: "DetectionOverlapDetection", 3555: "EndToEnd", 3556: "Target", 3557: "Speaker", 3558: "Extraction", 3559: "BeamForming",
    3560: "Drift", 3561: "MVDRBeamformer", 3562: "GEVBeamformer", 3563: "Null", 3564: "Steering", 3565: "Delay", 3566: "Sum", 3567: "MicrophoneArray", 3568: "LinearArray", 3569: "CircularArray",
    3570: "Echo", 3571: "SphericArray", 3572: "AcousticScene", 3573: "EnvironmentalSound", 3574: "SoundEventDetection", 3575: "SED", 3576: "WeaklySupervised", 3577: "MultiInstance", 3578: "Learning", 3579: "SoundSeparation",
    3580: "Ripple", 3581: "SourceSeparation", 3582: "Masking", 3583: "TFMask", 3584: "MagnitudeMask", 3585: "PhaseSensitiveMask", 3586: "IRM", 3587: "IdealRatioMask", 3588: "MMSE", 3589: "MinMeanSquareError",
    3590: "Wave", 3591: "PSMPhaseSensitive", 3592: "NMF", 3593: "NonNegativeMatrixFactorization", 3594: "MultiLayerNMF", 3595: "DictLearning", 3596: "SparseCoding", 3597: "VQ", 3598: "VectorQuantization", 3599: "VQNMF",
    3600: "Self", 3601: "CNMF", 3602: "ConvolutiveNMF", 3603: "DenoisingAutoencoder", 3604: "DAE", 3605: "Denoising", 3606: "DenoisingScore", 3607: "MatchingNetwork", 3608: "Diffusion", 3609: "ProbabilisticModel",
    3610: "Mirror", 3611: "DiffusionModel", 3612: "DDPM", 3613: "DenoisingDiffusion", 3614: "ProbabilisticModel", 3615: "ScoreMatching", 3616: "EnergyBasedModel", 3617: "Boltzmann", 3618: "Machine", 3619: "RBM",
    3620: "Shadow", 3621: "DeepBoltzmann", 3622: "DBM", 3623: "ContrastiveDivergence", 3624: "CD", 3625: "PersistentContrastive", 3626: "PCD", 3627: "FastWeights", 3628: "Auxiliary", 3629: "Variable",
    3630: "Reflection", 3631: "TemperingVariationMC", 3632: "ParallelTempering", 3633: "ReplicaExchange", 3634: "MCMC", 3635: "MonteCarloMarkovChain", 3636: "MH", 3637: "MetropolisHastings", 3638: "Gibbs", 3639: "Slice",
    3640: "Memory", 3641: "SamplerAdaptiveSlice", 3642: "Hamiltonian", 3643: "Dynamics", 3644: "Leapfrog", 3645: "Integrator", 3646: "SymplecticIntegrator", 3647: "MassMatrix", 3648: "Riemannian", 3649: "Geometry",
    3650: "Pattern", 3651: "ManifoldMCMC", 3652: "NUTSNoUturnSamplerABC", 3653: "ApproximateBayesianComputation", 3654: "LikelihoodFree", 3655: "Inference", 3656: "PseudoMarginal", 3657: "Particle", 3658: "Filter", 3659: "BootstrapFilter",
    3660: "Sequence", 3661: "SequentialImportanceResampling", 3662: "SIRParticleFilter", 3663: "AuxiliaryParticleFilter", 3664: "APFUnscented", 3665: "KalmanFilter", 3666: "UKF", 3667: "ExtendedKalmanFilter", 3668: "EKF", 3669: "OptimalSmoothing",
    3670: "Thread", 3671: "Rauch", 3672: "TippettSeyear", 3673: "RTS", 3674: "Smoother", 3675: "KalmanSmoother", 3676: "FixedLagSmoother", 3677: "FixedIntervalSmoother", 3678: "twofiltersmoothersystem", 3679: "StateSpaceModel",
    3680: "Lattice", 3681: "Temporal", 3682: "DynamicalSystem", 3683: "ARIMA", 3684: "AutoregressiveIntegrated", 3685: "MA", 3686: "SARIMA", 3687: "ARIMAX", 3688: "Vector", 3689: "Autoregression",
    3690: "Structure", 3691: "VAR", 3692: "VARMA", 3693: "VECM", 3694: "VectorErrorCorrection", 3695: "Cointegration", 3696: "Johansen", 3697: "Test", 3698: "GrangerCausality", 3699: "CausalityTest",
    3700: "Void", 3701: "Exogeneity", 3702: "WeakExogeneity", 3703: "StrongExogeneity", 3704: "PreterminedVariable", 3705: "InstrumentalVariable", 3706: "IV", 3707: "TwoStageLeastSquares", 3708: "2SLS", 3709: "SystemGMM",
    3710: "Field", 3711: "DynamicPanelData", 3712: "Arellano", 3713: "Bond", 3714: "Blundell", 3715: "Bond", 3716: "Difference", 3717: "GMM", 3718: "System", 3719: "GMM", 3720: "HansenTest",
    3720: "Horizon", 3721: "SpecificationTest", 3722: "Sargan", 3723: "TestOverIdentification", 3724: "CrossSectional", 3725: "FE", 3726: "FixedEffect", 3727: "RE", 3728: "RandomEffect", 3729: "Hausman",
    3730: "Boundary", 3731: "TestChoiceModel", 3732: "BinaryChoice", 3733: "Logit", 3734: "Probit", 3735: "Tobit", 3736: "CensoredRegression", 3737: "SelectionBias", 3738: "Heckman", 3739: "TwoStep",
    3740: "Threshold", 3741: "Correction", 3742: "InverseMillsRatio", 3743: "GeneralizedLinearModel", 3744: "GLM", 3745: "ExponentialFamily", 3746: "LinkFunction", 3747: "QuasiLikelihood", 3748: "GEE", 3749: "GeneralizedEstEquation",
    3750: "Gate", 3751: "WorkingCorrelation", 3752: "Exchangeable", 3753: "Autoregressive", 3754: "Unstructured", 3755: "IndependenceWorking", 3756: "HeirarchicalGeneralizedLinearModel", 3757: "HGLM", 3758: "RandomSlope", 3759: "RandomIntercept",
    3760: "Portal", 3761: "MixedEffectModel", 3762: "BestLinearUnbiasedPredictor", 3763: "BLUP", 3764: "ConditionalMode", 3765: "Multilevel", 3766: "Hierarchical", 3767: "Nesting", 3768: "Crossing", 3769: "CrossClassified",
    3770: "Crossing", 3771: "Design", 3772: "Orthogonal", 3773: "BalancedDesign", 3774: "IncompleteBlockDesign", 3775: "BIBD", 3776: "ResolvableDesign", 3777: "LargeBlockDesign", 3778: "Latin", 3779: "Square",
    3780: "Passage", 3781: "GracoLatinSquare", 3782: "Youden", 3783: "Square", 3784: "StimuluusResponseExperiment", 3785: "CyclicDesign", 3786: "AlternatingDesign", 3787: "CrossoverDesign", 3788: "Carryover", 3789: "Effect",
    3790: "Beyond", 3791: "Period", 3792: "Treatment", 3793: "Randomization", 3794: "Blocking", 3795: "Stratification", 3796: "Matching", 3797: "Adjustment", 3798: "CovariatAdjustment", 3799: "ANCOVAAnalysisCovariance",
    3800: "Future", 3801: "MancvaMultivariateANCOVA", 3802: "Manova", 3803: "MultivariateAnalysisVariance", 3804: "CanonicalCorrelation", 3805: "CCA", 3806: "LinearDiscriminantAnalysis", 3807: "LDA", 3808: "QDA", 3809: "QuadraticDiscriminantAnalysis",
    3810: "Possible", 3811: "RobustStatistics", 3812: "BreakdownPoint", 3813: "InfluenceFunction", 3814: "M", 3815: "Estimator", 3816: "S", 3817: "Estimator", 3818: "MM", 3819: "Estimator",
    3820: "Potential", 3821: "Winsorization", 3822: "Trimming", 3823: "Jackknife", 3824: "MedianAbsoluteDeviation", 3825: "MAD", 3826: "InterquartileRange", 3827: "IQR", 3828: "BoxPlot", 3829: "WhiskerPlot",
    3830: "Unfold", 3831: "OutlierDetection", 3832: "IsolationForest", 3833: "LocalOutlierFactor", 3834: "LOF", 3835: "OneClassSVM", 3836: "OCSVM", 3837: "EllipticEnvelope", 3838: "RobustCovariance", 3839: "EmpiricalCovariance",
    3840: "Become", 3841: "LedoitWolf", 3842: "ShrinkageEstimator", 3843: "GraphicalLasso", 3844: "SparsePrecision", 3845: "Estimation", 3846: "StructuralEquationModel", 3847: "SEM", 3848: "PathAnalysis", 3849: "LatentVariable",
    3850: "Emerge", 3851: "Factor", 3852: "Analysis", 3853: "PrincipalComponentAnalysis", 3854: "PCA", 3855: "FactorAnalysis", 3856: "FA", 3857: "ProbabilisticPCA", 3858: "PPCA", 3859: "VBEMAlgorithm",
    3860: "Awaken", 3861: "VariationalBayesian", 3862: "Inference", 3863: "InfiniteGaussianMixture", 3864: "DirichletProcessMixture", 3865: "DPM", 3866: "ChineseRestaurantProcess", 3867: "CRP", 3868: "IndianBuffetProcess", 3869: "IBP",
    3870: "Expand", 3871: "BetaBernoulliProcess", 3872: "LatentDirichletAllocation", 3873: "LDA", 3874: "TopicModel", 3875: "HierarchicalDirichletProcess", 3876: "HDP", 3877: "PachinkoAllocation", 3878: "PAM", 3879: "TopicHierarchy",
    3880: "Ascend", 3881: "CorrelatedTopicModel", 3882: "CTM", 3883: "DynamicTopicModel", 3884: "DTM", 3885: "TemporalTopicModel", 3886: "FacetedTopicModel", 3887: "SyntacticTopicModel", 3888: "STM", 3889: "StructuralTopicModel",
    3890: "Transcend", 3891: "SparseTopicModel", 3892: "OnlineVBEM", 3893: "StreamingInference", 3894: "OnlineLearning", 3895: "Incremental", 3896: "Learning", 3897: "ConceptDrift", 3898: "NonStationaryEnvironment", 3899: "AdaptiveUnderstanding",
    3900: "Presence", 3901: "ActivationFunction", 3902: "SigmoidFunction", 3903: "TanhFunction", 3904: "ReLU", 3905: "Leaky", 3906: "ReLU", 3907: "ELU", 3908: "SELU", 3909: "Swish",
    3910: "Awareness", 3911: "Mish", 3912: "HardSwish", 3913: "HardSigmoid", 3914: "HardTanh", 3915: "LogSigmoid", 3916: "LogSoftmax", 3917: "GLU", 3918: "GatedLinearUnit", 3919: "Bilinear",
    3920: "Attention", 3921: "ScaledDotProductAttention", 3922: "MultiHeadAttention", 3923: "AttentionHead", 3924: "QueryKeyValue", 3925: "QKV", 3926: "SelfAttention", 3927: "CrossAttention", 3928: "Additive", 3929: "Attention",
    3930: "Focus", 3931: "Bahdanau", 3932: "Location", 3933: "BasedAttention", 3934: "RelativePositionalEncoding", 3935: "RotaryPositionalEmbedding", 3936: "RoPE", 3937: "ALiBi", 3938: "AttentionWithLinearBias", 3939: "Flash",
    3940: "Intention", 3941: "Attention", 3942: "Efficient", 3943: "Attention", 3944: "LineartransformerComplexityReduction", 3945: "LinearAttention", 3946: "PerformerFRQA", 3947: "Feature", 3948: "RankingQueryAttention", 3949: "Linformer",
    3950: "Direction", 3951: "Transformer", 3952: "BigBirdSparseAttention", 3953: "SpaceAttenion", 3954: "EarthMoverDistance", 3955: "EMD", 3956: "LongformerLocalGlobal", 3957: "LongformerAttention", 3958: "AlternatingChunkAttention", 3959: "Reformer",
    3960: "Purpose", 3961: "LocalSensitiveHashing", 3962: "LSH", 3963: "MultiHashFunctions", 3964: "ReformerAttention", 3965: "LucidrainsMesh", 3966: "TensorProduct", 3967: "TensorNetworkAttention", 3968: "CompressiveTransformer", 3969: "MemoryCompression",
    3970: "Meaning", 3971: "Recurrence", 3972: "TransformerXL", 3973: "RelativePositionBias", 3974: "RecurrenceMemory", 3975: "SegmentLevelRecurrence", 3976: "TransformerXLRecurrence", 3977: "Compressive", 3978: "Compression", 3979: "Pattern",
    3980: "Essence", 3981: "Retrieval", 3982: "RetrievalAugmented", 3983: "Generation", 3984: "RAG", 3985: "REALM", 3986: "FiD", 3987: "FusionInDecoder", 3988: "PervasiveAttention", 3989: "VariationalInference",
    3990: "Being", 3991: "VARTransformer", 3992: "IterativeRefinement", 3993: "SmoothingRefinement", 3994: "MinimalEdditing", 3995: "LaTeX", 3996: "Edit", 3997: "EditOperation", 3998: "Insertion", 3999: "Deletion",
    4000: "Yes",
}


def code_to_word(code: int) -> str:
    return FULL_LEXICON.get(code, "Signal")


# ============================
#  VOID COMMUNICATION
# ============================

def format_com(sender_id: str, word_count: int, message: str, timestamp: str) -> str:
    return f"({sender_id}) - ({word_count}) - ({message}) - (entropy-time: {timestamp})"


def calculate_message_cost(word_count: int) -> float:
    return 0.0


class EPAddress:
    """
    EP (Entropy Protocol) Address parser.
    Supports formats:
    - "EEEE.PPPP"           (entropy.protocol)
    - "EEEE.PPPP.YYYYMMDD"  (entropy.protocol.date)
    """

    def __init__(self, address: str):
        """Parse an EP address string."""
        self.raw = address
        self.entropy = None
        self.protocol = None
        self.date = None
        self._parse()

    def _parse(self):
        """Parse the address into components."""
        parts = self.raw.split(".")
        
        if len(parts) < 2:
            raise ValueError(f"Invalid EP address: {self.raw} (need at least EEEE.PPPP)")
        
        try:
            self.entropy = int(parts[0])
            self.protocol = int(parts[1])
        except ValueError:
            raise ValueError(f"Invalid EP address: entropy and protocol must be integers")
        
        if len(parts) >= 3:
            try:
                self.date = int(parts[2])
                if not (10000000 <= self.date <= 99999999):
                    raise ValueError(f"Date must be in YYYYMMDD format (8 digits)")
            except ValueError:
                raise ValueError(f"Invalid date: {parts[2]} (must be YYYYMMDD integer)")
        
        if len(parts) > 3:
            raise ValueError(f"Too many components in EP address: {self.raw}")

    def __repr__(self):
        if self.date:
            return f"EPAddress({self.entropy}.{self.protocol}.{self.date})"
        return f"EPAddress({self.entropy}.{self.protocol})"

    def to_string(self):
        """Render the address as a string."""
        if self.date:
            return f"{self.entropy}.{self.protocol}.{self.date}"
        return f"{self.entropy}.{self.protocol}"


def startup():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== 4thCom by RomanAILabs — v0.4 (Professional COM Protocol) ===\n")
    print("Range: 1000 → 4000 (step 1, full coverage)")
    print("Format: (SENDER) - (WORD_COUNT) - (MESSAGE) - (entropy-time: TIMESTAMP)\n")
    print("Mechanics:")
    print(" • Your text → Shannon entropy → Entropy-based response")
    print(" • All messages follow professional COM format")
    print(" • Entropy timestamps (NO system clock)\n")
    print("Commands:")
    print("  /exit   → quit")
    print("  /status → system status")
    print("  (anything else) → entropy-mapped COM response\n")


def main():
    random.seed(time.time_ns())
    startup()

    while True:
        if random.randint(1, 8) == 1:
            word_count = random.randint(5, 50)
            words = random.sample(list(FULL_LEXICON.values()), k=min(word_count, len(FULL_LEXICON)))
            sentence = generate_sentence(words)
            ent = shannon_entropy(sentence)
            timestamp = entropy_to_timestamp(ent)
            endpoint_id = random.randint(1, 9999)
            print(format_com(f"EP-{endpoint_id:04d}", len(words), sentence, timestamp))

        user = input("\nYou → ").strip()

        if user.lower() == "/exit":
            print("Connection closed.")
            break

        if user.lower() == "/status":
            print(format_com("SYS", 1, "Status operational", entropy_to_timestamp(random.random() * 5)))
            continue

        if not user:
            continue

        ent = shannon_entropy(user)
        code = entropy_to_code(ent)
        word = code_to_word(code)
        timestamp = entropy_to_timestamp(ent)

        print(format_com(USER_ID, 1, word, timestamp))


if __name__ == "__main__":
    main()
