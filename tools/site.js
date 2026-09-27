// site.js — the hero net, the cost calculator, and the hours line.
(() => {
  const cfg = JSON.parse(document.getElementById("cfg").textContent);
  const T = cfg.t;
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- the net: Thailand on the left, the US on the right, the Pacific between.
     Every jewel is painted with the previous frame of the whole canvas, so each one holds
     the net, which holds the jewels, which hold the net. ---------- */
  const cv = document.getElementById("net");
  if (cv) {
    const ctx = cv.getContext("2d");
    const prev = document.createElement("canvas");
    const pctx = prev.getContext("2d");
    const P = cfg.ports;
    const named = [
      { k: "cm", x: 0.1, y: 0.2, r: 15, home: 1 }, { k: "lcb", x: 0.15, y: 0.44, r: 10 },
      { k: "sea", x: 0.86, y: 0.12, r: 10 }, { k: "or", x: 0.84, y: 0.22, r: 9 },
      { k: "sf", x: 0.855, y: 0.34, r: 10 }, { k: "la", x: 0.885, y: 0.45, r: 12 },
      { k: "sd", x: 0.9, y: 0.53, r: 8 }, { k: "lv", x: 0.95, y: 0.39, r: 8 }, { k: "hi", x: 0.62, y: 0.47, r: 9 },
    ];
    // sea jewels on a loose lattice; a fixed seed keeps the net the same on every visit
    let seed = 7;
    const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
    const J = named.map((n) => ({ ...n }));
    const COLS = 7, ROWS = 4;
    const grid = [];
    for (let c = 0; c < COLS; c++) for (let r = 0; r < ROWS; r++) {
      const j = { x: 0.24 + c * 0.075 + (rnd() - 0.5) * 0.03, y: 0.1 + r * 0.14 + (rnd() - 0.5) * 0.04 + (c % 2) * 0.05, r: 4 + rnd() * 4 };
      grid.push(J.length); J.push(j);
    }
    const E = [];
    const idx = (c, r) => grid[c * ROWS + r];
    for (let c = 0; c < COLS; c++) for (let r = 0; r < ROWS; r++) {
      if (c + 1 < COLS) E.push([idx(c, r), idx(c + 1, r)]);
      if (r + 1 < ROWS) E.push([idx(c, r), idx(c, r + 1)]);
      if (c + 1 < COLS && r + 1 < ROWS && (c + r) % 2 === 0) E.push([idx(c, r), idx(c + 1, r + 1)]);
    }
    const K = Object.fromEntries(named.map((n, i) => [n.k, i]));
    E.push([K.cm, K.lcb]);
    for (let r = 0; r < ROWS; r++) E.push([K.lcb, idx(0, r)]);
    E.push([K.cm, idx(0, 0)]);
    for (const k of ["sea", "or", "sf", "la", "sd"]) {
      let best = 0, bd = 9;
      for (let r = 0; r < ROWS; r++) { const j = J[idx(COLS - 1, r)], d = Math.abs(j.y - J[K[k]].y); if (d < bd) { bd = d; best = r; } }
      E.push([K[k], idx(COLS - 1, best)]);
    }
    E.push([K.lv, K.la], [K.lv, K.sf], [K.sea, K.or], [K.or, K.sf], [K.sf, K.la], [K.la, K.sd]);
    let hiBest = [0, 9]; grid.forEach((g) => { const d = Math.hypot(J[g].x - J[K.hi].x, J[g].y - J[K.hi].y); if (d < hiBest[1]) hiBest = [g, d]; });
    E.push([K.hi, hiBest[0]], [K.hi, K.la]);
    const adj = J.map(() => []);
    E.forEach(([a, b]) => { adj[a].push(b); adj[b].push(a); });

    // boxes walk the net from a US jewel to Chiang Mai along the shortest string path
    const path = (from) => {
      const q = [from], seen = { [from]: -1 };
      while (q.length) { const v = q.shift(); if (v === K.cm) break; for (const w of adj[v]) if (!(w in seen)) { seen[w] = v; q.push(w); } }
      const out = []; for (let v = K.cm; v !== -1; v = seen[v]) out.unshift(v); return out;
    };
    const US = ["sea", "or", "sf", "la", "sd", "lv", "hi"];
    const boxes = [];
    const spawn = () => { const p = path(K[US[Math.floor(Math.random() * US.length)]]); boxes.push({ p, t: 0, v: 0.35 + Math.random() * 0.25 }); };

    let W = 0, H = 0, dpr = 1;
    const size = () => {
      dpr = Math.min(2, devicePixelRatio || 1);
      W = cv.clientWidth; H = cv.clientHeight;
      cv.width = prev.width = Math.round(W * dpr); cv.height = prev.height = Math.round(H * dpr);
    };
    size(); addEventListener("resize", size);
    const X = (j) => j.x * W, Y = (j) => j.y * H * (W < 600 ? 1.4 : 0.8) + H * 0.06;
    const scale = () => Math.max(0.7, Math.min(1.25, W / 900));

    const waves = [];
    const glow = (i, now) => {
      let g = 0;
      for (const w of waves) {
        const d = Math.hypot(X(J[i]) - w.x, Y(J[i]) - w.y), front = (now - w.t) * 0.5;
        g += Math.max(0, 1 - Math.abs(d - front) / 60) * Math.max(0, 1 - (now - w.t) / 2600);
      }
      return Math.min(1, g);
    };

    const frame = (now) => {
      if (cv.clientWidth !== W || cv.clientHeight !== H) size();
      if (!W || !H) return;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const g = ctx.createRadialGradient(W * 0.3, H * 0.2, 10, W * 0.5, H * 0.5, Math.max(W, H));
      g.addColorStop(0, "#15395a"); g.addColorStop(1, "#0a1a2c");
      ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
      // land: two soft shores
      for (const [cx, rx] of [[0, 0.2], [W, 0.16]]) {
        const sg = ctx.createRadialGradient(cx, H * 0.3, 0, cx, H * 0.3, W * rx);
        sg.addColorStop(0, "rgba(232,176,74,.10)"); sg.addColorStop(1, "rgba(232,176,74,0)");
        ctx.fillStyle = sg; ctx.fillRect(0, 0, W, H);
      }
      // strings
      for (const [a, b] of E) {
        const ga = (glow(a, now) + glow(b, now)) / 2;
        ctx.strokeStyle = `rgba(232,176,74,${0.28 + ga * 0.6})`; ctx.lineWidth = 1 + ga * 1.5;
        ctx.beginPath(); ctx.moveTo(X(J[a]), Y(J[a])); ctx.lineTo(X(J[b]), Y(J[b])); ctx.stroke();
      }
      // boxes
      const s = scale();
      for (const b of boxes) {
        const seg = Math.min(b.p.length - 2, Math.floor(b.t)), f = b.t - seg;
        const A = J[b.p[seg]], B = J[b.p[seg + 1]];
        const x = X(A) + (X(B) - X(A)) * f, y = Y(A) + (Y(B) - Y(A)) * f;
        ctx.fillStyle = "#c89b5a"; ctx.strokeStyle = "#7a5424"; ctx.lineWidth = 1;
        ctx.fillRect(x - 4 * s, y - 4 * s, 8 * s, 8 * s); ctx.strokeRect(x - 4 * s, y - 4 * s, 8 * s, 8 * s);
        ctx.beginPath(); ctx.moveTo(x - 4 * s, y); ctx.lineTo(x + 4 * s, y); ctx.stroke();
      }
      // jewels: each one shows the last frame of the whole net
      J.forEach((j, i) => {
        const r = j.r * s * (1 + glow(i, now) * 0.35), x = X(j), y = Y(j);
        ctx.save(); ctx.beginPath(); ctx.arc(x, y, r, 0, 7); ctx.clip();
        ctx.drawImage(prev, x - r, y - r, r * 2, r * 2);
        const sh = ctx.createRadialGradient(x - r * 0.35, y - r * 0.4, r * 0.1, x, y, r);
        const hue = [42, 190, 330, 150][i % 4];
        sh.addColorStop(0, "rgba(255,250,235,.85)"); sh.addColorStop(0.35, `hsla(${hue},80%,70%,.28)`); sh.addColorStop(1, `hsla(${hue},70%,25%,.55)`);
        ctx.fillStyle = sh; ctx.fillRect(x - r, y - r, r * 2, r * 2);
        ctx.restore();
        ctx.strokeStyle = j.home ? "#e0503f" : "rgba(255,217,138,.9)"; ctx.lineWidth = j.home ? 2.5 : 1.2;
        ctx.beginPath(); ctx.arc(x, y, r, 0, 7); ctx.stroke();
      });
      // names
      ctx.font = `600 ${Math.round(12 * s)}px Prompt, Sarabun, sans-serif`; ctx.textBaseline = "middle";
      named.forEach((n) => {
        const x = X(J[K[n.k]]), y = Y(J[K[n.k]]), left = n.x > 0.5;
        ctx.textAlign = left ? "right" : "left";
        ctx.fillStyle = n.home ? "#ffd98a" : "rgba(246,236,214,.85)";
        ctx.fillText(P[n.k], x + (left ? -1 : 1) * (n.r * s + 6), y);
      });
      pctx.setTransform(1, 0, 0, 1, 0, 0); pctx.drawImage(cv, 0, 0);
    };

    let last = 0, acc = 0;
    const loop = (now) => {
      const dt = Math.min(0.05, (now - (last || now)) / 1000); last = now;
      acc += dt; if (acc > 1.1 && boxes.length < 9) { acc = 0; spawn(); }
      for (const b of boxes) b.t += dt * b.v;
      for (let i = boxes.length - 1; i >= 0; i--) if (boxes[i].t >= boxes[i].p.length - 1) {
        const h = J[K.cm]; waves.push({ x: X(h), y: Y(h), t: now }); boxes.splice(i, 1);
      }
      while (waves.length && now - waves[0].t > 2600) waves.shift();
      frame(now);
      if (!document.hidden) requestAnimationFrame(loop); else last = 0;
    };
    document.addEventListener("visibilitychange", () => { if (!document.hidden && !still) requestAnimationFrame(loop); });
    cv.addEventListener("click", (e) => {
      const rc = cv.getBoundingClientRect(), x = e.clientX - rc.left, y = e.clientY - rc.top;
      waves.push({ x, y, t: performance.now() });
      if (still) { frame(performance.now() + 400); }
    });
    if (still) { for (let i = 0; i < 4; i++) frame(0); } else { for (let i = 0; i < 3; i++) spawn(); requestAnimationFrame(loop); }
    window.__net = { J, E, boxes };
  }

  /* ---------- cost ---------- */
  const $ = (id) => document.getElementById(id);
  const money = (n) => "$" + Math.round(n).toLocaleString("en-US");
  const BOX = 4.5, PAL = (40 * 48 * 44) / 1728, CONT = 1170;
  const calc = () => {
    const boxes = Math.max(0, Math.min(2000, +$("boxes").value || 0));
    const cuft = Math.max(0, Math.min(5000, +$("cuft").value || 0));
    const allow = $("allow").checked;
    const v = boxes * BOX + cuft;
    const row = $("boxrow");
    const nb = Math.min(120, boxes), nf = Math.min(60, Math.round(cuft / BOX));
    row.innerHTML = "<i></i>".repeat(nb) + '<i class="f"></i>'.repeat(nf);
    $("total").innerHTML = `${T.c_total}: <b>${v.toLocaleString("en-US", { maximumFractionDigits: 1 })} ${T.c_cuft}</b>`;
    const pallets = Math.max(1, Math.ceil(v / PAL));
    const R = [
      { k: "SQ", $: Math.max(70, v) * 10.9, sub: v < 70 ? `${T.c_min}: 70 ${T.c_cuft}` : `${v.toFixed(0)} × $10.90` },
      { k: "SB", $: pallets * 700, sub: `${pallets} ${T.c_pallets}` },
      { k: "SW", $: Math.max(300, v) * 8.9, sub: !allow ? T.c_noallow : v < 300 ? `${T.c_min}: 300 ${T.c_cuft}` : `${v.toFixed(0)} × $8.90`, off: !allow },
      { k: "SC", $: 7900, sub: v > CONT ? T.c_over : `≈ ${CONT.toLocaleString("en-US")} ${T.c_cuft}`, off: v > CONT },
    ];
    const live = R.filter((r) => !r.off && v > 0);
    const best = live.length ? live.reduce((a, b) => (b.$ < a.$ ? b : a)) : null;
    $("routes").innerHTML = R.map((r) => `<li class="${r === best ? "best" : ""}${r.off ? " off" : ""}"><span>${T.c_routes[r.k]}<span class="sub">${r.sub}</span></span>` +
      `<span><span class="amt">${money(r.$)}</span>${r === best ? `<span class="tag">${T.c_best}</span>` : ""}</span></li>`).join("");
  };
  if ($("boxes")) { ["boxes", "cuft", "allow"].forEach((id) => $(id).addEventListener("input", calc)); calc(); }

  /* ---------- their hours, 9:00–20:00 Los Angeles, shown in Chiang Mai time ---------- */
  const hrs = $("hours");
  if (hrs) {
    try {
      const off = (tz, d) => { const p = new Date(d.toLocaleString("en-US", { timeZone: tz })); return (p - new Date(d.toLocaleString("en-US", { timeZone: "UTC" }))) / 60000; };
      const now = new Date(), la = off("America/Los_Angeles", now), bkk = 420;
      const fmt = (h) => { const m = ((h * 60 - la + bkk) % 1440 + 1440) % 1440; return `${String(Math.floor(m / 60)).padStart(2, "0")}:${String(m % 60).padStart(2, "0")}`; };
      hrs.textContent = T.hours_now.replace("{a}", fmt(9)).replace("{b}", fmt(20));
    } catch (e) { /* the fixed line above still stands */ }
  }
})();
