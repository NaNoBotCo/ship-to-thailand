THE WHOLE HOUSE, BY SEA · ย้ายบ้านข้ามทะเล

Shipping personal effects from the US to Thailand in a shared container, with Send2Thai's
prices, a cost calculator, the steps, and the Chiang Mai end strung as a Mot Dang net.

Live:   https://motdang.net/sites/ship-to-thailand/   (canonical)
        https://nanobotco.github.io/ship-to-thailand/

Words:  tools/content.py (English and Thai, same keys)
Net:    data/net.json (Mot Dang record ids) + data/hrefs.json (their motdang.net paths)

Build and check:
    python3 tools/build.py && node tools/card.mjs && python3 tools/check.py

Mot Dang copy:
    SITE_URL=https://motdang.net/sites/ship-to-thailand \
      OUT=../mot-dang/assets/sites/ship-to-thailand python3 tools/build.py
    cd ../mot-dang && python3 publish/deploy.py --only sites --yes

Send2Thai's figures were read from send2thai.com on 27 September 2026.
