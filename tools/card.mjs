// card.mjs — docs/card.jpg (English) and docs/card-th.jpg (Thai), the 1200×630 share cards,
// photographed from the hero by headless Chrome, with this copy's address at the foot.
//   node tools/card.mjs
import { spawn } from "node:child_process";
import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const JOBS = [["../docs/index.html", "../docs/card.jpg"], ["../docs/th/index.html", "../docs/card-th.jpg"]];
const ADDRESS = "nanobotco.github.io/ship-to-thailand";
const port = 9300 + Math.floor(Math.random() * 400);
const chrome = spawn(CHROME, ["--headless=new", `--remote-debugging-port=${port}`, "--no-first-run",
  "--allow-file-access-from-files", "--user-data-dir=/tmp/ship-card-" + port, "about:blank"], { stdio: "ignore" });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let ws;
for (let i = 0; i < 50; i++) {
  try { const l = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
    const t = l.find((x) => x.type === "page"); if (t) { ws = new WebSocket(t.webSocketDebuggerUrl); break; } } catch {}
  await sleep(200);
}
await new Promise((r) => ws.addEventListener("open", r));
let id = 0; const wait = {};
ws.addEventListener("message", (e) => { const m = JSON.parse(e.data); if (m.id && wait[m.id]) { wait[m.id](m); delete wait[m.id]; } });
const send = (method, params = {}) => new Promise((r) => { const i = ++id; wait[i] = r; ws.send(JSON.stringify({ id: i, method, params })); });
const ev = async (expr) => (await send("Runtime.evaluate", { expression: expr, returnByValue: true, awaitPromise: true })).result?.result?.value;

await send("Emulation.setDeviceMetricsOverride", { width: 1200, height: 630, deviceScaleFactor: 1, mobile: false });
for (const [page, card] of JOBS) {
  await send("Page.navigate", { url: new URL(page, import.meta.url).href });
  await sleep(1200);
  await ev(`document.querySelector('.lang').style.display='none';document.querySelector('.hint').style.display='none';
    document.getElementById('net').style.height='630px';document.getElementById('net').style.minHeight='630px';
    document.querySelector('.hero-in').style.paddingBottom='84px';
    document.querySelector('.hero h1').style.fontSize='64px';document.querySelector('.lede').style.fontSize='26px';
    document.querySelector('.lede').style.maxWidth='860px';document.querySelector('.kicker').style.fontSize='20px';
    document.querySelector('.hero-in .wrap').style.maxWidth='1080px';
    var a=document.createElement('div');a.textContent='${ADDRESS}';
    a.style.cssText='position:fixed;left:0;right:0;bottom:0;height:56px;padding:0 40px;display:flex;align-items:center;background:#0b1d30;color:#ffd98a;font:600 26px ui-monospace,Menlo,monospace;z-index:99999';
    document.body.appendChild(a);1`);
  await sleep(4000);
  const s = await send("Page.captureScreenshot", { format: "jpeg", quality: 88, clip: { x: 0, y: 0, width: 1200, height: 630, scale: 1 } });
  const out = fileURLToPath(new URL(card, import.meta.url));
  writeFileSync(out, Buffer.from(s.result.data, "base64"));
  console.log("card", out);
}
chrome.kill();
process.exit(0);
