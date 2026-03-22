import json
import re
from pathlib import Path
from urllib.parse import quote

import requests


ROOT = Path("/Users/mingli/Khex/uni-learning")
PAPER_LIST = ROOT / "agents/collector/001-paper-list.md"
REF_DIR = ROOT / "references"


def decade_folder(year: int) -> str:
    return f"{(year // 10) * 10}s"


def target_folder(year: int) -> Path:
    if year <= 2010:
        return REF_DIR / decade_folder(year)
    return REF_DIR / str(year)


def normalize(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    s = re.sub(r"_+", "_", s)
    return s[:100] or "paper"


def parse_paper_list():
    content = PAPER_LIST.read_text(encoding="utf-8")
    footnotes = {int(n): u for n, u in re.findall(r"^\[(\d+)\]:\s+(\S+)", content, re.M)}
    papers = []
    for line in content.splitlines():
        if not line.startswith("|"):
            continue
        if "主题" in line or "---" in line:
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 6:
            continue
        title = cols[1].strip("* ").strip()
        year_text = cols[3]
        source_text = cols[5]
        if not title:
            continue
        year_match = re.search(r"(19\d{2}|20\d{2})", year_text)
        if not year_match:
            continue
        year = int(year_match.group(1))
        ref_match = re.search(r"\[(\d+)\]", source_text)
        ref_url = footnotes.get(int(ref_match.group(1))) if ref_match else None
        papers.append({"title": title, "year": year, "ref_url": ref_url})
    return papers


def existing_title_keys():
    keys = set()
    for file in REF_DIR.rglob("*.pdf"):
        keys.add(normalize(file.stem))
    return keys


def is_pdf_bytes(data: bytes) -> bool:
    return data.startswith(b"%PDF-")


def download_bytes(session: requests.Session, url: str):
    try:
        res = session.get(url, timeout=20, allow_redirects=True)
        if res.status_code >= 400:
            return None
        if is_pdf_bytes(res.content):
            return res.content
        return None
    except Exception:
        return None


def semantic_scholar_candidates(session: requests.Session, title: str):
    api = (
        "https://api.semanticscholar.org/graph/v1/paper/search?"
        f"query={quote(title)}&limit=5&fields=title,openAccessPdf,externalIds"
    )
    try:
        res = session.get(api, timeout=10)
        if not res.ok:
            return []
        data = res.json().get("data", [])
    except Exception:
        return []
    wanted = normalize(title)
    out = []
    for row in data:
        got = normalize(row.get("title") or "")
        if not got:
            continue
        if wanted not in got and got not in wanted:
            continue
        pdf_url = (row.get("openAccessPdf") or {}).get("url")
        if pdf_url:
            out.append(pdf_url)
        arxiv_id = (row.get("externalIds") or {}).get("ArXiv")
        if arxiv_id:
            out.append(f"https://arxiv.org/pdf/{arxiv_id}.pdf")
    return out


def openalex_candidates(session: requests.Session, title: str):
    url = f"https://api.openalex.org/works?search={quote(title)}&per-page=5"
    try:
        res = session.get(url, timeout=10)
        if not res.ok:
            return []
        results = res.json().get("results", [])
    except Exception:
        return []
    wanted = normalize(title)
    out = []
    for row in results:
        got = normalize(row.get("display_name") or "")
        if not got:
            continue
        if wanted not in got and got not in wanted:
            continue
        primary = row.get("primary_location") or {}
        pdf_url = primary.get("pdf_url")
        if pdf_url:
            out.append(pdf_url)
        best = row.get("best_oa_location") or {}
        pdf_url2 = best.get("pdf_url")
        if pdf_url2:
            out.append(pdf_url2)
    return out


def source_candidates(ref_url: str):
    if not ref_url:
        return []
    out = [ref_url]
    arxiv_abs = re.search(r"arxiv\.gg/abs/([^?]+)", ref_url)
    if arxiv_abs:
        out.append(f"https://arxiv.org/pdf/{arxiv_abs.group(1)}.pdf")
    arxiv_org = re.search(r"arxiv\.org/(?:abs|pdf)/([^?]+)", ref_url)
    if arxiv_org:
        aid = arxiv_org.group(1).replace(".pdf", "")
        out.append(f"https://arxiv.org/pdf/{aid}.pdf")
    iclr = re.search(r"proceedings\.iclr\.cc/.+/hash/([^/]+)-Abstract-Conference\.html", ref_url)
    if iclr:
        h = iclr.group(1)
        y = re.search(r"/paper/(?:files/)?paper/(\d{4})/", ref_url)
        if y:
            out.append(f"https://proceedings.iclr.cc/paper_files/paper/{y.group(1)}/file/{h}-Paper-Conference.pdf")
    pmlr = re.search(r"proceedings\.mlr\.press/v(\d+)/([^.]+)\.html", ref_url)
    if pmlr:
        out.append(f"https://proceedings.mlr.press/v{pmlr.group(1)}/{pmlr.group(2)}.pdf")
    if "nips.cc/virtual/2021/36555" in ref_url:
        out.append("https://arxiv.org/pdf/2111.02358.pdf")
    if "openai.com/index/language-models-are-few-shot-learners" in ref_url:
        out.append("https://arxiv.org/pdf/2005.14165.pdf")
    if "journal.hep.com.cn/fcs/EN/10.1007/s11704-024-40231-1" in ref_url:
        out.append("https://arxiv.org/pdf/2308.11432.pdf")
    if "fugumt.com/fugumt/paper_check/2411.01992v2" in ref_url:
        out.append("https://arxiv.org/pdf/2411.01992.pdf")
    if "catalyzex.com/author/Clayton%20Sanford" in ref_url:
        out.append("https://arxiv.org/pdf/2501.02984.pdf")
    if "jessetnroberts.com/publications/How-Powerful-are-Decoder-Only-Transformer-Neural-Models" in ref_url:
        out.append("https://arxiv.org/pdf/2406.12181.pdf")
    if "catalyzex.com/author/Joshua%20Brul%C3%A9" in ref_url:
        out.append("https://arxiv.org/pdf/1603.06125.pdf")
    if "dblp.org/rec/journals/corr/abs-2410-16531" in ref_url:
        out.append("https://arxiv.org/pdf/2410.16531.pdf")
    return out


def unique(urls):
    seen = set()
    out = []
    for u in urls:
        if not u:
            continue
        u = u.replace("http://", "https://")
        if u in seen:
            continue
        seen.add(u)
        out.append(u)
    return out


def save_paper(session: requests.Session, paper):
    title = paper["title"]
    year = paper["year"]
    folder = target_folder(year)
    folder.mkdir(parents=True, exist_ok=True)
    out_file = folder / f"{slugify(title)}.pdf"
    if out_file.exists():
        if is_pdf_bytes(out_file.read_bytes()[:5]):
            return {"title": title, "status": "exists", "path": str(out_file)}
    candidates = []
    candidates.extend(source_candidates(paper.get("ref_url")))
    candidates.extend(semantic_scholar_candidates(session, title))
    candidates.extend(openalex_candidates(session, title))
    for url in unique(candidates):
        data = download_bytes(session, url)
        if data:
            out_file.write_bytes(data)
            return {"title": title, "status": "downloaded", "path": str(out_file), "url": url}
    return {"title": title, "status": "failed"}


def clean_html():
    for h in REF_DIR.rglob("*.html"):
        h.unlink()


def verify_manifest(papers):
    failed = []
    for p in papers:
        year = p["year"]
        file = target_folder(year) / f"{slugify(p['title'])}.pdf"
        if not file.exists():
            failed.append({"title": p["title"], "reason": "missing-file"})
            continue
        head = file.read_bytes()[:5]
        if not is_pdf_bytes(head):
            failed.append({"title": p["title"], "reason": "invalid-pdf"})
    return failed


def main():
    papers = parse_paper_list()
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})
    results = []
    for i, paper in enumerate(papers, 1):
        print(f"[{i}/{len(papers)}] {paper['title']}", flush=True)
        results.append(save_paper(session, paper))
    clean_html()
    failed_verify = verify_manifest(papers)
    summary = {
        "total": len(papers),
        "downloaded": len([r for r in results if r["status"] == "downloaded"]),
        "exists": len([r for r in results if r["status"] == "exists"]),
        "failed_download": [r["title"] for r in results if r["status"] == "failed"],
        "failed_verify": failed_verify,
    }
    out = ROOT / "agents/collector/paper-download-report.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
