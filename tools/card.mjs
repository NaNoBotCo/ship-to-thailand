// card.mjs — docs/card.jpg, the 1200×630 share card, photographed from the hero by headless Chrome.
//   node tools/card.mjs
import { spawn } from "node:child_process";
import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const PAGE = new URL("../docs/index.html", import.meta.url).href;
const OUT = fileURLToPath(new URL("../docs/card.jpg", import.meta.url));
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
await send("Page.navigate", { url: PAGE });
await sleep(1200);
await ev(`document.querySelector('.lang').style.display='none';document.querySelector('.hint').style.display='none';
  document.getElementById('net').style.height='630px';document.getElementById('net').style.minHeight='630px';
  document.querySelector('.hero-in').style.paddingBottom='44px';
  document.querySelector('.hero h1').style.fontSize='64px';document.querySelector('.lede').style.fontSize='26px';
  document.querySelector('.lede').style.maxWidth='860px';document.querySelector('.kicker').style.fontSize='20px';
  document.querySelector('.hero-in .wrap').style.maxWidth='1080px';1`);
await sleep(4000);
const s = await send("Page.captureScreenshot", { format: "jpeg", quality: 88, clip: { x: 0, y: 0, width: 1200, height: 630, scale: 1 } });
writeFileSync(OUT, Buffer.from(s.result.data, "base64"));
console.log("card", OUT);
chrome.kill();
process.exit(0);
