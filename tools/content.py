"""content.py — every word on the page, English and Thai, keyed the same.

Send2Thai's figures are from their own pages, read 2026-09-27:
  send2thai.com/service-personal.aspx · faq.aspx · service-insurance.aspx ·
  service-pickup-charge.aspx · service-consolidate.aspx · index.aspx
"""

READ = {"en": "27 September 2026", "th": "27 กันยายน 2569"}

# code, price shown, $ figure for the calculator (None = not in it)
RATES = [
    ("SX", {"en": "from $30 a box", "th": "เริ่ม $30 ต่อกล่อง"}),
    ("SM", {"en": "from $30 a box", "th": "เริ่ม $30 ต่อกล่อง"}),
    ("SQ", {"en": "$10.90 per cu ft", "th": "$10.90 ต่อลูกบาศก์ฟุต"}),
    ("SB", {"en": "$700 a pallet", "th": "$700 ต่อพาเลท"}),
    ("SW", {"en": "$8.90 per cu ft", "th": "$8.90 ต่อลูกบาศก์ฟุต"}),
    ("SC", {"en": "$7,900", "th": "$7,900"}),
    ("AF", {"en": "$12.50 per kg", "th": "$12.50 ต่อกิโลกรัม"}),
]

T = {
"en": {
    "lang": "en",
    "title": "The Whole House, by Sea",
    "desc": ("Shipping personal effects from the US to Thailand in a shared container: Send2Thai's "
             "prices, a cost calculator, the steps, and the Chiang Mai end."),
    "other": "ภาษาไทย",
    "kicker": "US → Thailand · personal effects · by sea",
    "h1": "The whole house, by sea",
    "lede": ("A Mot Dang reader shipped an entire house from the United States to Thailand with "
             "<b>Send2Thai</b> for <b>$2,000</b>."),
    "hint": "Tap a jewel. Each one holds the whole net.",
    "jump": [("#ltc", "Shared container"), ("#prices", "Prices"), ("#cost", "Cost"), ("#steps", "Steps"),
             ("#chiang-mai", "Chiang Mai"), ("#contact", "Contact")],

    "ltc_h": "Shared container",
    "ltc": [
        ("<b>LTC — less than a container.</b> Your boxes ride in a shipping container with other "
         "people's, and you pay for the space they take. Freight offices call it <b>LCL</b>, "
         "less-than-container load."),
        ("The other way is a container to yourself — <b>FCL</b>, full container load. Send2Thai sells "
         "both: boxes, pallets and cubic feet in a shared container, or a 20-foot container for one house."),
        ("Their sea rates are <b>door to door, all in</b>: pickup or drop-off in the US, export, the "
         "voyage, import, Thai customs clearance, and delivery to the door in Thailand. They also deliver "
         "to Laos, Myanmar and Cambodia."),
    ],

    "prices_h": "Prices",
    "prices_note": "Personal effects, from Send2Thai's own price page, read {read}. Codes are theirs.",
    "rate_rows": {
        "SX": ("X-Box", "Send2Thai's own boxes, sold at their branches. Priced by the box, papers and delivery included."),
        "SM": ("Moving box", "Home Depot or Lowe's boxes in the sizes they list. Priced by the box."),
        "SQ": ("Cubic foot", "Your own boxes, any number. 70 cu ft minimum ($763). No weight limit."),
        "SB": ("Pallet", "One pallet box, 40 × 48 × 44 inches, no weight limit."),
        "SW": ("Furniture", "Furniture, fridges and other large things, under the move-home allowance. "
                            "300 cu ft minimum ($2,670). Wooden crating and pickup within 20 miles included."),
        "SC": ("Whole house", "A 20-foot container to yourself: furniture and household, tax clearance "
                              "included, weight not counted. Their menu calls it the 26′ Truck."),
        "AF": ("Air", "By plane, to the door. Import tax not included."),
    },
    "th_code": "Code", "th_what": "Service", "th_price": "Price",

    "two_h": "What $2,000 buys",
    "two": [
        ("<b>183 cubic feet</b> at the cubic-foot rate: $2,000 ÷ $10.90.",),
        ("<b>About 40 moving boxes</b> of 24 × 18 × 18 inches. One box is 7,776 cubic inches ÷ 1,728 = "
         "4.5 cu ft; 183 ÷ 4.5 = 40.7.",),
        ("<b>Nearly three pallets.</b> A pallet box is 40 × 48 × 44 = 84,480 cubic inches = 48.9 cu ft, "
         "for $700 — $14.32 a cubic foot. Three cost $2,100.",),
        ("<b>A quarter of a container.</b> A 20-foot container holds about 1,170 cu ft inside; $7,900 for "
         "the lot is $6.75 a cubic foot, the cheapest rate on the page once it is full.",),
    ],

    "cost_h": "Cost",
    "cost_intro": ("Count your boxes and your big things. The page prices every sea route from the rates "
                   "above and marks the cheapest."),
    "f_boxes": "Moving boxes, 24 × 18 × 18 in",
    "f_cuft": "Furniture and big things, cubic feet",
    "f_cuft_help": "Movers' rule of thumb: a three-seat sofa 35–50 cu ft, a fridge 30–45, a queen bed with frame about 60.",
    "f_allow": "The move-home allowance applies to me (ask Send2Thai)",
    "c_total": "Total",
    "c_cuft": "cu ft",
    "c_routes": {
        "SQ": "Cubic foot (SQ)",
        "SB": "Pallets (SB)",
        "SW": "Furniture (SW)",
        "SC": "Whole container (SC)",
    },
    "c_pallets": "pallets, if it packs tight",
    "c_min": "minimum charge",
    "c_over": "more than one container holds",
    "c_noallow": "needs the move-home allowance",
    "c_best": "cheapest",
    "c_note": ("Estimates from the listed rates. Send2Thai measures the boxes and sends the invoice; "
               "their <a href=\"https://send2thai.com/calculate.aspx\">calculator</a> has the zone prices."),

    "steps_h": "Steps",
    "steps": [
        ("Join", "Register at send2thai.com for a member number. Membership costs nothing; Premium is $10 a year."),
        ("Pack", "Standard boxes, 24 × 18 × 18 inches, at most 32 kg each so one person can lift them. "
                 "X-Boxes are for sale at every branch."),
        ("Label", "Enter each box's size and weight on their site, pay the invoice, and print the Ship ID "
                  "label. No printer: write the Ship ID on the box."),
        ("Hand over", "Drop the boxes at a branch or drop point, or book a pickup."),
        ("Sail", "The shared container goes by sea. Send2Thai clears Thai customs."),
        ("Open the door", "The boxes arrive at your door in Thailand."),
    ],
    "pickup_h": "Pickup",
    "pickup": [
        "Los Angeles: free on the 2nd and 4th Saturday of the month, shipments over $95, within 30 miles.",
        "Oregon: free on Mondays, shipments over $125, within 45 miles.",
        "Further out: $4 a mile up to 50 miles, $3.50 to 100, $3 to 150.",
        "Boxes wait at the front door, packed and ready to lift. Tip the driver at least $5.",
    ],

    "cover_h": "Cover",
    "cover": [
        "Loss is covered up to $95, or ฿3,000, a shipment, at no charge.",
        "More cover costs 5% of the value you declare.",
        "Their policy pays for loss, not for damage. Pack for a sea voyage.",
    ],

    "customs_h": "Customs",
    "customs": [
        ("Send2Thai's furniture rate is sold for people using <b>สิทธิ์ย้ายกลับไทย</b> — the move-home "
         "allowance, a customs exemption for used household goods when someone moves to Thailand. Ask "
         "them whether your passport and visa qualify before you pack."),
        ("Thai customs for the north sits in Chiang Mai: the Region 3 office and the airport customs "
         "house, both in the net below."),
    ],

    "cm_h": "Chiang Mai",
    "cm_lede": ("Mot Dang strings the places a move touches into one net. Open any of them on Mot Dang "
                "and it shows all the others."),
    "cm_more": "Indra's Net, drawn",
    "cm_disclose": "The people who publish Mot Dang also run Chiang Mai Visa Desk.",

    "contact_h": "Contact",
    "contact_rows": [
        ("Phone", '<a href="tel:+13233369595">+1 323-336-9595</a>'),
        ("LINE", '<a href="https://lin.ee/5XcOTxh">@sendtothai</a>'),
        ("Email", '<a href="mailto:info@send2thai.com">info@send2thai.com</a>'),
        ("Web", '<a href="https://send2thai.com/">send2thai.com</a>'),
        ("Facebook", '<a href="https://www.facebook.com/Send2Thai/">Send2Thai</a>'),
    ],
    "hours": "Their hours line: 9:00–20:00, Los Angeles time.",
    "hours_now": "That is {a}–{b} in Chiang Mai today.",
    "branches_h": "Branches",
    "branches": [
        ("Los Angeles", "5301 W Sunset Blvd, Thai Town", "+1 323-336-9595"),
        ("Oregon", "Portland area", "+1 503-946-5666"),
        ("Seattle", "1108 Industry Dr, Tukwila", "+1 206-569-4630"),
        ("Las Vegas", "Self-service, 24 hours", ""),
        ("Hawaii", "Self-service, 24 hours", ""),
        ("San Francisco · San Diego", "Drop points", ""),
    ],

    "src_h": "Sources",
    "src": [
        ("https://send2thai.com/service-personal.aspx", "Send2Thai: personal effects"),
        ("https://send2thai.com/faq.aspx", "Send2Thai: questions"),
        ("https://send2thai.com/service-pickup-charge.aspx", "Send2Thai: pickup"),
        ("https://send2thai.com/service-insurance.aspx", "Send2Thai: insurance"),
        ("https://send2thai.com/", "Send2Thai: home"),
        ("https://en.wikipedia.org/wiki/Intermodal_container", "Wikipedia: intermodal container (20-ft volume)"),
        ("https://www.customs.go.th/", "Thai Customs Department"),
    ],
    "src_read": "Send2Thai's pages read {read}. Their prices change; theirs is the price that counts.",
    "foot": 'On <a href="https://motdang.net/">Mot Dang · มดแดง</a>',
},

"th": {
    "lang": "th",
    "title": "ย้ายบ้านข้ามทะเล",
    "desc": ("ส่งของใช้ส่วนตัวจากอเมริกากลับไทยแบบรวมตู้ ราคาของ Send2Thai เครื่องคิดค่าส่ง ขั้นตอน "
             "และปลายทางที่เชียงใหม่"),
    "other": "English",
    "kicker": "อเมริกา → ไทย · ของใช้ส่วนตัว · ทางเรือ",
    "h1": "ย้ายบ้านข้ามทะเล",
    "lede": ("ผู้อ่านมดแดงคนหนึ่งส่งของทั้งบ้านจากอเมริกากลับไทยกับ <b>Send2Thai</b> "
             "ค่าส่ง <b>$2,000</b>"),
    "hint": "แตะอัญมณีดู ทุกเม็ดสะท้อนตาข่ายทั้งผืน",
    "jump": [("#ltc", "รวมตู้"), ("#prices", "ราคา"), ("#cost", "ค่าส่ง"), ("#steps", "ขั้นตอน"),
             ("#chiang-mai", "เชียงใหม่"), ("#contact", "ติดต่อ")],

    "ltc_h": "รวมตู้",
    "ltc": [
        ("<b>ส่งแบบไม่เต็มตู้ (LTC หรือ LCL)</b> กล่องของเราไปในตู้คอนเทนเนอร์ใบเดียวกับของคนอื่น "
         "จ่ายเท่าที่ของเรากินที่"),
        ("อีกแบบคือเหมาตู้ทั้งใบ (FCL) Send2Thai มีทั้งสองแบบ ส่งเป็นกล่อง เป็นพาเลท "
         "หรือคิดเป็นลูกบาศก์ฟุตในตู้รวม หรือเหมาตู้ 20 ฟุตทั้งบ้าน"),
        ("ราคาทางเรือของเขาเป็นแบบ<b>ถึงหน้าบ้าน รวมทุกอย่าง</b> ตั้งแต่รับของหรือเอาของไปส่งที่อเมริกา "
         "ส่งออก ขนข้ามทะเล นำเข้า เคลียร์ศุลกากรไทย จนถึงหน้าประตูบ้านที่ไทย "
         "ส่งไปลาว พม่า และกัมพูชาได้ด้วย"),
    ],

    "prices_h": "ราคา",
    "prices_note": "ของใช้ส่วนตัว จากหน้าราคาของ Send2Thai เอง อ่านเมื่อ {read} รหัสบริการเป็นของเขา",
    "rate_rows": {
        "SX": ("กล่อง X-Box", "กล่องของ Send2Thai ซื้อได้ที่สาขา คิดเป็นกล่อง รวมค่าเอกสารและค่าส่งถึงบ้านแล้ว"),
        "SM": ("กล่องย้ายบ้าน", "กล่องของ Home Depot หรือ Lowe's ตามขนาดที่เขากำหนด คิดเป็นกล่อง"),
        "SQ": ("คิดเป็นลูกบาศก์ฟุต", "กล่องของเราเอง กี่กล่องก็ได้ ขั้นต่ำ 70 ลูกบาศก์ฟุต ($763) ไม่จำกัดน้ำหนัก"),
        "SB": ("พาเลท", "กล่องพาเลทใบใหญ่ 40 × 48 × 44 นิ้ว ไม่จำกัดน้ำหนัก"),
        "SW": ("เฟอร์นิเจอร์", "เฟอร์นิเจอร์ ตู้เย็น ของชิ้นใหญ่ แบบใช้สิทธิ์ย้ายกลับไทย ขั้นต่ำ 300 ลูกบาศก์ฟุต "
                               "($2,670) รวมค่าตีลังไม้ และรับของถึงบ้านในระยะ 20 ไมล์"),
        "SC": ("ทั้งบ้าน", "เหมาตู้ 20 ฟุต เฟอร์นิเจอร์และของใช้ทั้งบ้าน รวมเคลียร์ภาษี ไม่คิดน้ำหนัก "
                           "ในเมนูของเขาเรียกว่า 26′ Truck"),
        "AF": ("ทางเครื่องบิน", "ส่งถึงหน้าบ้าน ไม่รวมภาษีนำเข้า"),
    },
    "th_code": "รหัส", "th_what": "บริการ", "th_price": "ราคา",

    "two_h": "$2,000 ได้แค่ไหน",
    "two": [
        ("<b>183 ลูกบาศก์ฟุต</b> ถ้าคิดเป็นลูกบาศก์ฟุต: $2,000 ÷ $10.90",),
        ("<b>ราว 40 กล่อง</b> ขนาด 24 × 18 × 18 นิ้ว กล่องหนึ่ง 7,776 ลูกบาศก์นิ้ว ÷ 1,728 = "
         "4.5 ลูกบาศก์ฟุต · 183 ÷ 4.5 = 40.7",),
        ("<b>เกือบสามพาเลท</b> กล่องพาเลท 40 × 48 × 44 = 84,480 ลูกบาศก์นิ้ว = 48.9 ลูกบาศก์ฟุต "
         "ราคา $700 ตกลูกบาศก์ฟุตละ $14.32 สามพาเลท $2,100",),
        ("<b>หนึ่งในสี่ตู้</b> ตู้ 20 ฟุตจุข้างในราว 1,170 ลูกบาศก์ฟุต เหมา $7,900 ตกลูกบาศก์ฟุตละ $6.75 "
         "ถูกที่สุดในหน้านี้ ถ้าใส่เต็มตู้",),
    ],

    "cost_h": "ค่าส่ง",
    "cost_intro": "นับกล่อง นับของชิ้นใหญ่ หน้านี้คิดค่าส่งทางเรือทุกแบบจากราคาข้างบน แล้วบอกว่าแบบไหนถูกที่สุด",
    "f_boxes": "กล่องย้ายบ้าน 24 × 18 × 18 นิ้ว",
    "f_cuft": "เฟอร์นิเจอร์และของชิ้นใหญ่ (ลูกบาศก์ฟุต)",
    "f_cuft_help": "ตัวเลขคร่าว ๆ ของคนขนย้าย: โซฟาสามที่นั่ง 35–50 ลูกบาศก์ฟุต ตู้เย็น 30–45 เตียงควีนพร้อมโครงราว 60",
    "f_allow": "ฉันใช้สิทธิ์ย้ายกลับไทยได้ (ถาม Send2Thai)",
    "c_total": "รวม",
    "c_cuft": "ลูกบาศก์ฟุต",
    "c_routes": {
        "SQ": "คิดเป็นลูกบาศก์ฟุต (SQ)",
        "SB": "พาเลท (SB)",
        "SW": "เฟอร์นิเจอร์ (SW)",
        "SC": "เหมาตู้ (SC)",
    },
    "c_pallets": "พาเลท ถ้าจัดของแน่น",
    "c_min": "คิดขั้นต่ำ",
    "c_over": "เกินตู้เดียว",
    "c_noallow": "ต้องใช้สิทธิ์ย้ายกลับไทย",
    "c_best": "ถูกที่สุด",
    "c_note": ("เป็นตัวเลขประมาณจากราคาที่ประกาศ Send2Thai วัดกล่องจริงแล้วออกใบแจ้งหนี้ "
               "<a href=\"https://send2thai.com/calculate.aspx\">เครื่องคิดค่าส่งของเขา</a>มีราคาตามโซน"),

    "steps_h": "ขั้นตอน",
    "steps": [
        ("สมัคร", "ลงทะเบียนที่ send2thai.com รับเลขสมาชิก ไม่มีค่าสมัคร สมาชิก Premium ปีละ $10"),
        ("แพ็ก", "ใช้กล่องขนาดมาตรฐาน 24 × 18 × 18 นิ้ว กล่องละไม่เกิน 32 กก. ให้คนเดียวยกไหว "
                 "กล่อง X-Box มีขายทุกสาขา"),
        ("ติดป้าย", "กรอกขนาดและน้ำหนักแต่ละกล่องในเว็บเขา จ่ายเงิน แล้วพิมพ์ป้าย Ship ID "
                    "ไม่มีเครื่องพิมพ์ เขียน Ship ID ข้างกล่องก็ได้"),
        ("ส่งของ", "เอากล่องไปส่งที่สาขาหรือจุดรับของ หรือนัดให้มารับที่บ้าน"),
        ("ลงเรือ", "ตู้รวมไปทางเรือ Send2Thai เคลียร์ศุลกากรไทยให้"),
        ("เปิดประตู", "กล่องมาถึงหน้าบ้านที่เมืองไทย"),
    ],
    "pickup_h": "รับของถึงบ้าน",
    "pickup": [
        "ลอสแอนเจลิส: ฟรีทุกวันเสาร์ที่สองและสี่ของเดือน ค่าส่งเกิน $95 ในระยะ 30 ไมล์",
        "ออริกอน: ฟรีทุกวันจันทร์ ค่าส่งเกิน $125 ในระยะ 45 ไมล์",
        "ไกลกว่านั้น: ไมล์ละ $4 ถึง 50 ไมล์ · $3.50 ถึง 100 · $3 ถึง 150",
        "วางกล่องไว้หน้าบ้าน แพ็กเสร็จพร้อมยก ให้ทิปคนขับอย่างน้อย $5",
    ],

    "cover_h": "ประกัน",
    "cover": [
        "ของหายได้ชดเชยไม่เกิน $95 หรือ 3,000 บาทต่อการส่งหนึ่งครั้ง ไม่เสียเงินเพิ่ม",
        "อยากได้ความคุ้มครองเพิ่ม จ่าย 5% ของมูลค่าที่แจ้ง",
        "ประกันของเขาจ่ายเมื่อของหาย ไม่จ่ายเมื่อของเสียหาย แพ็กให้ทนการเดินทางทางทะเล",
    ],

    "customs_h": "ศุลกากร",
    "customs": [
        ("ราคาเฟอร์นิเจอร์ของ Send2Thai ขายสำหรับคนที่ใช้<b>สิทธิ์ย้ายกลับไทย</b> "
         "คือการยกเว้นอากรของใช้ในบ้านที่ใช้แล้ว เมื่อย้ายมาอยู่เมืองไทย "
         "ถาม Send2Thai ก่อนแพ็กว่าหนังสือเดินทางและวีซ่าของเราใช้สิทธิ์นี้ได้ไหม"),
        ("ศุลกากรของภาคเหนืออยู่ที่เชียงใหม่ ทั้งสำนักงานศุลกากรภาคที่ 3 และด่านศุลกากรท่าอากาศยาน "
         "อยู่ในตาข่ายข้างล่างนี้"),
    ],

    "cm_h": "เชียงใหม่",
    "cm_lede": ("มดแดงร้อยที่ที่การย้ายบ้านไปแตะเข้าเป็นตาข่ายผืนเดียว "
                "เปิดหน้าไหนในมดแดง ก็เห็นที่อื่นทั้งหมด"),
    "cm_more": "ตาข่ายพระอินทร์ (ภาษาอังกฤษ)",
    "cm_disclose": "คนที่ทำมดแดงเปิด Chiang Mai Visa Desk ด้วย",

    "contact_h": "ติดต่อ",
    "contact_rows": [
        ("โทร", '<a href="tel:+13233369595">+1 323-336-9595</a>'),
        ("LINE", '<a href="https://lin.ee/5XcOTxh">@sendtothai</a>'),
        ("อีเมล", '<a href="mailto:info@send2thai.com">info@send2thai.com</a>'),
        ("เว็บ", '<a href="https://send2thai.com/">send2thai.com</a>'),
        ("เฟซบุ๊ก", '<a href="https://www.facebook.com/Send2Thai/">Send2Thai</a>'),
    ],
    "hours": "เวลาทำการที่เขาประกาศ: 9:00–20:00 ตามเวลาลอสแอนเจลิส",
    "hours_now": "วันนี้ตรงกับ {a}–{b} เวลาเชียงใหม่",
    "branches_h": "สาขา",
    "branches": [
        ("ลอสแอนเจลิส", "5301 W Sunset Blvd ไทยทาวน์", "+1 323-336-9595"),
        ("ออริกอน", "ย่านพอร์ตแลนด์", "+1 503-946-5666"),
        ("ซีแอตเทิล", "1108 Industry Dr, Tukwila", "+1 206-569-4630"),
        ("ลาสเวกัส", "บริการตัวเอง 24 ชั่วโมง", ""),
        ("ฮาวาย", "บริการตัวเอง 24 ชั่วโมง", ""),
        ("ซานฟรานซิสโก · ซานดิเอโก", "จุดรับของ", ""),
    ],

    "src_h": "ที่มา",
    "src": [
        ("https://send2thai.com/service-personal.aspx", "Send2Thai: ส่งของใช้ส่วนตัวกลับไทย"),
        ("https://send2thai.com/faq.aspx", "Send2Thai: คำถามที่พบบ่อย"),
        ("https://send2thai.com/service-pickup-charge.aspx", "Send2Thai: รับสินค้าที่บ้าน"),
        ("https://send2thai.com/service-insurance.aspx", "Send2Thai: ประกันสินค้า"),
        ("https://send2thai.com/", "Send2Thai: หน้าหลัก"),
        ("https://en.wikipedia.org/wiki/Intermodal_container", "Wikipedia: ตู้คอนเทนเนอร์ (ปริมาตรตู้ 20 ฟุต)"),
        ("https://www.customs.go.th/", "กรมศุลกากร"),
    ],
    "src_read": "อ่านหน้าเว็บ Send2Thai เมื่อ {read} ราคาเปลี่ยนได้ ราคาที่ใช้จริงคือราคาของเขา",
    "foot": 'อยู่บน <a href="https://motdang.net/">มดแดง · Mot Dang</a>',
},
}
