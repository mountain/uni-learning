import json
import re
from pathlib import Path
from typing import List
from urllib.parse import quote, urlparse

import requests


ROOT = Path("/Users/mingli/Khex/uni-learning")
REF_DIR = ROOT / "references"
REPORT_PATH = ROOT / "agents/collector/paper-download-report-002.json"

PAPERS = [
    {"title": "A Logical Calculus of the Ideas Immanent in Nervous Activity", "year": 1943, "hint_urls": ["https://doi.org/10.1007/BF02478259", "http://www.cse.chalmers.se/~coquand/AUTOMATA/mcp.pdf"]},
    {"title": "Cybernetics: Or Control and Communication in the Animal and the Machine", "year": 1948, "hint_urls": ["https://archive.org/download/cyberneticsorco00wien/cyberneticsorco00wien.pdf"]},
    {"title": "The Mathematical Theory of Communication", "year": 1949, "hint_urls": []},
    {"title": "Programming a Computer for Playing Chess", "year": 1950, "hint_urls": ["https://doi.org/10.1080/14786445008521796", "https://vision.unipv.it/IA1/ProgrammingaComputerforPlayingChess.pdf"]},
    {"title": "Presentation of a Maze-Solving Machine", "year": 1952, "hint_urls": ["https://archive.org/download/claudeelwoodshannoncollectedpapers/Claude_Elwood_Shannon_Collected_Papers.pdf"]},
    {"title": "Design for a Brain", "year": 1952, "hint_urls": ["https://archive.org/download/designforbrain00ashb/designforbrain00ashb.pdf"]},
    {"title": "A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence", "year": 1955, "hint_urls": ["http://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html", "http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf"]},
    {"title": "Empirical Explorations with the Logic Theory Machine", "year": 1957, "hint_urls": ["https://www.rand.org/content/dam/rand/pubs/papers/2008/P1314.pdf"]},
    {"title": "The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain", "year": 1958, "hint_urls": ["https://doi.org/10.1037/h0042519", "https://psychclassics.yorku.ca/Rosenblatt/perceptron.pdf"]},
    {"title": "Some Methods of Artificial Intelligence and Heuristic Programming", "year": 1959, "hint_urls": ["http://jmc.stanford.edu/articles/heuristic/heuristic.pdf"]},
    {"title": "Some Studies in Machine Learning Using the Game of Checkers", "year": 1959, "hint_urls": ["https://doi.org/10.1145/1457838.1457862", "https://www.cs.virginia.edu/~evans/cs655/readings/samuel.pdf"]},
    {"title": "Report on a General Problem-Solving Program", "year": 1959, "hint_urls": ["http://jmc.stanford.edu/articles/gps/gps.pdf"]},
    {"title": "Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I", "year": 1960, "hint_urls": ["https://doi.org/10.1145/367177.367199", "http://jmc.stanford.edu/articles/recursive/recursive.pdf"]},
    {"title": "Adaptive Switching Circuits", "year": 1960, "hint_urls": ["https://isl.stanford.edu/~widrow/papers/c1960adaptiveswitching.pdf"]},
    {"title": "A Machine-Oriented Logic Based on the Resolution Principle", "year": 1965, "hint_urls": ["https://doi.org/10.1145/321250.321253", "https://www.cs.utexas.edu/~mooney/cs343/resolution-refutation.pdf"]},
    {"title": "ELIZA—A Computer Program for the Study of Natural Language Communication between Man and Machine", "year": 1966, "hint_urls": ["https://doi.org/10.1145/365153.365168", "https://courses.cs.umbc.edu/undergraduate/CMSC331/resources/papers/eliza.january1966.html.pdf"]},
    {"title": "Language Identification in the Limit", "year": 1967, "hint_urls": ["https://doi.org/10.1016/S0019-9958(67)91165-5"]},
    {"title": "A Formal Basis for the Heuristic Determination of Minimum Cost Paths", "year": 1968, "hint_urls": ["https://doi.org/10.1109/TSSC.1968.300136", "https://dans.world/repository/hartFormalBasis1968/hartFormalBasis1968.pdf"]},
    {"title": "Perceptrons", "year": 1969, "hint_urls": []},
    {"title": "STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving", "year": 1971, "hint_urls": ["https://web.stanford.edu/class/cs221/2016/readings/strips.pdf", "https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/strips.pdf"]},
    {"title": "Understanding Natural Language", "year": 1972, "hint_urls": []},
    {"title": "Toward a Mathematical Theory of Inductive Inference", "year": 1975, "hint_urls": ["https://doi.org/10.1016/0001-8708(75)90027-2"]},
    {"title": "Production Rules as a Representation for a Knowledge-Based Consultation Program", "year": 1977, "hint_urls": ["https://web.stanford.edu/class/cs520/papers/shortliffe-buchanan-1975.pdf"]},
    {"title": "A Theory of the Learnable", "year": 1984, "hint_urls": ["https://doi.org/10.1145/1968.1972", "https://www.cs.cmu.edu/~avrim/Papers/valiant84.pdf"]},
    {"title": "Neural Networks and Physical Systems with Emergent Collective Computational Abilities", "year": 1982, "hint_urls": ["https://doi.org/10.1073/pnas.79.8.2554", "https://www.pnas.org/doi/pdf/10.1073/pnas.79.8.2554"]},
    {"title": "Fusion, Propagation, and Structuring in Belief Networks", "year": 1986, "hint_urls": ["https://doi.org/10.1016/0004-3702(86)90072-X", "https://www.cs.ubc.ca/~murphyk/Bayes/pearl1986.pdf"]},
    {"title": "Learning Representations by Back-Propagating Errors", "year": 1986, "hint_urls": ["https://doi.org/10.1038/323533a0", "https://www.cs.toronto.edu/~hinton/absps/naturebp.pdf"]},
    {"title": "Occam's Razor", "year": 1987, "hint_urls": ["https://doi.org/10.1016/0004-3702(87)90014-1", "https://www.cs.cmu.edu/~avrim/Papers/occam.pdf"]},
    {"title": "Learning to Predict by the Methods of Temporal Differences", "year": 1988, "hint_urls": ["https://doi.org/10.1007/BF00115009"]},
    {"title": "Computational Limitations on Learning from Examples", "year": 1988, "hint_urls": ["https://doi.org/10.1145/62212.62213", "https://dl.acm.org/doi/pdf/10.1145/62212.62213"]},
    {"title": "The Computational Complexity of Probabilistic Inference Using Bayesian Belief Networks", "year": 1990, "hint_urls": ["http://www2.stat.duke.edu/~sayan/npcomplete.pdf"]},
    {"title": "Q-Learning", "year": 1992, "hint_urls": ["https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf"]},
    {"title": "Approximating Probabilistic Inference in Bayesian Belief Networks is NP-Hard", "year": 1993, "hint_urls": ["http://www.cs.helsinki.fi/group/cosco/Teaching/Probability/2007/dagum.pdf"]},
    {"title": "Support-Vector Networks", "year": 1995, "hint_urls": ["https://doi.org/10.1007/BF00994018"]},
    {"title": "Long Short-Term Memory", "year": 1997, "hint_urls": ["https://doi.org/10.1162/neco.1997.9.8.1735"]},
    {"title": "Random Forests", "year": 2001, "hint_urls": ["https://doi.org/10.1023/A:1010933404324"]},
    {"title": "Conditional Random Fields: Probabilistic Models for Segmenting and Labeling Sequence Data", "year": 2001, "hint_urls": ["https://repository.upenn.edu/cis_papers/159/"]},
    {"title": "Latent Dirichlet Allocation", "year": 2003, "hint_urls": ["https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf"]},
    {"title": "Reducing the Dimensionality of Data with Neural Networks", "year": 2006, "hint_urls": ["https://doi.org/10.1126/science.1127647", "https://www.cs.toronto.edu/~hinton/science.pdf"]},
    {"title": "ImageNet: A Large-Scale Hierarchical Image Database", "year": 2009, "hint_urls": ["https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf"]},
]


def decade_folder(year: int) -> str:
    return f"{(year // 10) * 10}s"


def target_folder(year: int) -> Path:
    if year <= 2010:
        return REF_DIR / decade_folder(year)
    return REF_DIR / str(year)


def normalize(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def token_set(text: str):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def title_match(a: str, b: str) -> bool:
    na = normalize(a)
    nb = normalize(b)
    if na == nb:
        return True
    sa = token_set(a)
    sb = token_set(b)
    if not sa or not sb:
        return False
    overlap = len(sa & sb) / min(len(sa), len(sb))
    return overlap >= 0.6


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    s = re.sub(r"_+", "_", s)
    return s[:100] or "paper"


def find_existing_pdf_by_title(title: str):
    for f in REF_DIR.rglob("*.pdf"):
        if title_match(title, f.stem.replace("_", " ")):
            return f
    return None


def is_pdf_bytes(data: bytes) -> bool:
    return data.startswith(b"%PDF-")


def download_bytes(session: requests.Session, url: str):
    for _ in range(2):
        try:
            res = session.get(url, timeout=40, allow_redirects=True, headers={"User-Agent": "Mozilla/5.0"})
            if res.status_code >= 400:
                continue
            if is_pdf_bytes(res.content):
                return res.content
        except Exception:
            continue
    return None


def semantic_scholar_candidates(session: requests.Session, title: str):
    api = (
        "https://api.semanticscholar.org/graph/v1/paper/search?"
        f"query={quote(title)}&limit=5&fields=title,openAccessPdf,externalIds"
    )
    try:
        res = session.get(api, timeout=12)
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
        if wanted not in got and got not in wanted and not title_match(title, row.get("title") or ""):
            continue
        pdf_url = (row.get("openAccessPdf") or {}).get("url")
        if pdf_url:
            out.append(pdf_url)
        arxiv_id = (row.get("externalIds") or {}).get("ArXiv")
        if arxiv_id:
            out.append(f"https://arxiv.org/pdf/{arxiv_id}.pdf")
        doi = (row.get("externalIds") or {}).get("DOI")
        if doi:
            out.append(f"https://doi.org/{doi}")
    return out


def openalex_candidates(session: requests.Session, title: str):
    url = f"https://api.openalex.org/works?search={quote(title)}&per-page=5"
    try:
        res = session.get(url, timeout=12)
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
        if wanted not in got and got not in wanted and not title_match(title, row.get("display_name") or ""):
            continue
        open_access = row.get("open_access") or {}
        oa_url = open_access.get("oa_url")
        if oa_url:
            out.append(oa_url)
        best = row.get("best_oa_location") or {}
        pdf_url = best.get("pdf_url")
        if pdf_url:
            out.append(pdf_url)
        primary = row.get("primary_location") or {}
        p2 = primary.get("pdf_url")
        if p2:
            out.append(p2)
        doi = row.get("doi")
        if doi:
            out.append(doi)
    return out


def extract_doi(text: str):
    m = re.search(r"(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)", text)
    return m.group(1) if m else None


def doi_candidates(session: requests.Session, hint_urls):
    out = []
    for url in hint_urls or []:
        doi = extract_doi(url)
        if not doi:
            continue
        try:
            s2 = session.get(
                f"https://api.semanticscholar.org/graph/v1/paper/DOI:{quote(doi)}?fields=title,openAccessPdf,externalIds",
                timeout=12,
            )
            if s2.ok:
                js = s2.json()
                pdf_url = (js.get("openAccessPdf") or {}).get("url")
                if pdf_url:
                    out.append(pdf_url)
                arxiv_id = (js.get("externalIds") or {}).get("ArXiv")
                if arxiv_id:
                    out.append(f"https://arxiv.org/pdf/{arxiv_id}.pdf")
        except Exception:
            pass
        try:
            oa = session.get(f"https://api.openalex.org/works/https://doi.org/{doi}", timeout=12)
            if oa.ok:
                j2 = oa.json()
                oa_url = (j2.get("open_access") or {}).get("oa_url")
                if oa_url:
                    out.append(oa_url)
                p1 = (j2.get("best_oa_location") or {}).get("pdf_url")
                if p1:
                    out.append(p1)
                p2 = (j2.get("primary_location") or {}).get("pdf_url")
                if p2:
                    out.append(p2)
        except Exception:
            pass
    return out


def html_embedded_pdf_candidates(session: requests.Session, hint_urls):
    out = []
    for url in hint_urls or []:
        if url.lower().endswith(".pdf"):
            continue
        try:
            r = session.get(url, timeout=12, allow_redirects=True)
            if not r.ok:
                continue
            ct = (r.headers.get("content-type") or "").lower()
            if "html" not in ct:
                continue
            html = r.text
            for p in re.findall(r'https?://[^"\']+?\.pdf(?:\?[^"\']*)?', html):
                out.append(p)
            parsed = urlparse(r.url)
            for p in re.findall(r'["\'](/[^"\']+?\.pdf(?:\?[^"\']*)?)["\']', html):
                out.append(f"{parsed.scheme}://{parsed.netloc}{p}")
        except Exception:
            pass
    return out


def unique(urls):
    seen = set()
    out = []
    for u in urls:
        if not u:
            continue
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
    if out_file.exists() and is_pdf_bytes(out_file.read_bytes()[:5]):
        return {"title": title, "status": "exists", "path": str(out_file)}
    existing = find_existing_pdf_by_title(title)
    if existing:
        return {"title": title, "status": "exists", "path": str(existing)}
    candidates: List[str] = []
    candidates.extend(paper.get("hint_urls") or [])
    candidates.extend(doi_candidates(session, paper.get("hint_urls") or []))
    candidates.extend(html_embedded_pdf_candidates(session, paper.get("hint_urls") or []))
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
        file = target_folder(p["year"]) / f"{slugify(p['title'])}.pdf"
        if not file.exists():
            existing = find_existing_pdf_by_title(p["title"])
            if existing:
                continue
            failed.append({"title": p["title"], "reason": "missing-file"})
            continue
        if not is_pdf_bytes(file.read_bytes()[:5]):
            failed.append({"title": p["title"], "reason": "invalid-pdf"})
    return failed


def main():
    papers = PAPERS[:40]
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
    REPORT_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
