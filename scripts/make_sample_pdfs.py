"""Generate the five FICTIONAL ShopEase policy PDFs used by the RAG component.
Content lives in scripts/policy_content.py. Replace the PDFs with your own documents any time:
just drop PDFs into docs/ (the index rebuilds automatically)."""
import sys
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer

sys.path.insert(0, str(Path(__file__).parent))
from policy_content import DOCS, META  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "docs"


def build(fname, title, policy_id, sections):
    ss = getSampleStyleSheet()
    body = ParagraphStyle("b", parent=ss["BodyText"], fontSize=10.5, leading=14.5, spaceAfter=6)
    bullet = ParagraphStyle("bl", parent=body, leftIndent=18, bulletIndent=6, spaceAfter=3)
    meta = ParagraphStyle("m", parent=ss["Italic"], fontSize=8.5, textColor="#555555", spaceAfter=10)
    story = [Paragraph(title, ss["Title"]), Paragraph(f"{policy_id}  |  {META}", meta)]
    for head, blocks in sections:
        part = [Paragraph(head, ss["Heading2"])]
        for b in blocks:
            if isinstance(b, list):
                part += [Paragraph(x, bullet, bulletText="\u2022") for x in b]
                part.append(Spacer(1, 4))
            else:
                part.append(Paragraph(b, body))
        story.append(KeepTogether(part[:2]))  # keep heading with first paragraph
        story += part[2:]

    def footer(canvas, doc):
        canvas.setFont("Helvetica", 8)
        canvas.drawCentredString(A4[0] / 2, 1.1 * cm, f"{title}  -  page {doc.page}")

    SimpleDocTemplate(str(OUT / fname), pagesize=A4, title=title, author="ShopEase (fictional)",
                      leftMargin=2.2 * cm, rightMargin=2.2 * cm, topMargin=2 * cm, bottomMargin=2 * cm
                      ).build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.pdf"):
        old.unlink()
    for fname, (title, pid, sections) in DOCS.items():
        build(fname, title, pid, sections)
        print("wrote", OUT / fname)
