#!/usr/bin/env python3
"""Convert the Java core interview PDF into Markdown content files."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PDF = Path("/Users/qiyue/code/Java_Interview_Book/JAVA核心知识点整理（283页，超级详细）.pdf")
OUT_DIR = ROOT / "content" / "java-core"
CHAPTER_DIR = OUT_DIR / "chapters"
REPORT = OUT_DIR / "extraction-report.md"


@dataclass(frozen=True)
class OutlineItem:
    title: str
    page: int
    depth: int


HEADER_RE = re.compile(r"^\s*13/04/2018\s+Page\s+\d+\s+of\s+\d+\s*$")
TOC_DOTS_RE = re.compile(r"\s*\.{5,}\s*(\d+)\s*$")
SPACED_ASCII_RE = re.compile(r"(?<=[A-Za-z])\s+(?=[A-Za-z])")
NUMBERED_HEADING_RE = re.compile(r"^(\d+(?:\.\d+)+\.?|\d+\.)\s+(.+)$")


def normalize_title(title: str) -> str:
    title = unicodedata.normalize("NFKC", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title


def slugify(title: str, fallback: str) -> str:
    title = normalize_title(title)
    title = re.sub(r"^\d+(?:\.\d+)*\.?\s*", "", title).strip()
    mapping = {
        "目录": "toc",
        "JVM": "jvm",
        "JAVA集合": "java-collections",
        "JAVA多线程并发": "java-concurrency",
        "JAVA基础": "java-basics",
        "Spring 原理": "spring",
        "微服务": "microservices",
        "Netty 与RPC": "netty-rpc",
        "网络": "network",
        "日志": "logging",
        "Zookeeper": "zookeeper",
        "Kafka": "kafka",
        "RabbitMQ": "rabbitmq",
        "Hbase": "hbase",
        "MongoDB": "mongodb",
        "Cassandra": "cassandra",
        "设计模式": "design-patterns",
        "负载均衡": "load-balancing",
        "数据库": "database",
        "一致性算法": "consensus",
        "JAVA算法": "java-algorithms",
        "数据结构": "data-structures",
        "加密算法": "cryptography",
        "分布式缓存": "distributed-cache",
        "Hadoop": "hadoop",
        "Spark": "spark",
        "Storm": "storm",
        "YARN": "yarn",
        "机器学习": "machine-learning",
        "云计算": "cloud-computing",
    }
    return mapping.get(title, fallback)


def flatten_outline(reader: PdfReader) -> list[OutlineItem]:
    items: list[OutlineItem] = []

    def walk(nodes: list, depth: int) -> None:
        for node in nodes:
            if isinstance(node, list):
                walk(node, depth + 1)
                continue
            title = normalize_title(getattr(node, "title", str(node)))
            try:
                page = reader.get_destination_page_number(node) + 1
            except Exception:
                page = 1
            items.append(OutlineItem(title=title, page=page, depth=depth))

    walk(reader.outline, 0)
    return items


def clean_line(line: str) -> str:
    line = unicodedata.normalize("NFKC", line).replace("\x00", "")
    line = line.replace("\u3000", " ").strip()
    line = TOC_DOTS_RE.sub(r"  \1", line)
    line = re.sub(r"[ \t]+", " ", line)
    return line


def page_text(reader: PdfReader, page_no: int) -> str:
    raw = reader.pages[page_no - 1].extract_text() or ""
    lines: list[str] = []
    for raw_line in raw.splitlines():
        line = clean_line(raw_line)
        if not line or HEADER_RE.match(line):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def heading_level(line: str) -> int | None:
    match = NUMBERED_HEADING_RE.match(line)
    if not match:
        return None
    number = match.group(1).rstrip(".")
    parts = [part for part in number.split(".") if part]
    if not parts:
        return None
    return min(len(parts) + 1, 6)


def markdownize_text(text: str, chapter_title: str | None = None) -> str:
    out: list[str] = []
    previous_blank = True
    in_fence = False

    for line in text.splitlines():
        line = clean_line(line)
        if not line:
            if not previous_blank:
                out.append("")
            previous_blank = True
            continue

        level = heading_level(line)
        if level:
            if chapter_title and normalize_title(line) == normalize_title(chapter_title):
                level = 1
            if out and out[-1] != "":
                out.append("")
            out.append(f"{'#' * level} {line}")
            previous_blank = False
            continue

        if line.startswith(("public ", "private ", "protected ", "class ", "interface ", "@Override")):
            if not in_fence:
                if out and out[-1] != "":
                    out.append("")
                out.append("```java")
                in_fence = True
            out.append(line)
            previous_blank = False
            continue

        if in_fence and not line.startswith(("public ", "private ", "protected ", "class ", "interface ", "@", "}", "{", "//")):
            out.append("```")
            in_fence = False

        out.append(line)
        previous_blank = False

    if in_fence:
        out.append("```")
    return "\n".join(out).strip() + "\n"


def build_page_markdown(reader: PdfReader) -> list[str]:
    pages = []
    for page_no in range(1, len(reader.pages) + 1):
        text = page_text(reader, page_no)
        pages.append(f"<!-- page: {page_no} -->\n\n{text}".strip())
    return pages


def write_index(chapters: list[tuple[OutlineItem, Path, int, int]], total_pages: int) -> None:
    rows = ["| 章节 | 页码范围 | Markdown |", "|---|---:|---|"]
    for item, path, start, end in chapters:
        rel = path.relative_to(OUT_DIR).as_posix()
        rows.append(f"| {item.title} | {start}-{end} | [{path.name}]({rel}) |")

    content = f"""# JAVA核心知识点整理

来源 PDF：`{SOURCE_PDF.name}`

本目录面向静态站点和 Notion 迁移整理：

- `chapters/`：按 PDF 一级书签拆分的章节 Markdown。
- `full.md`：按页保留的全量 Markdown，包含 `<!-- page: N -->` 页码标记，便于回查原 PDF。
- `extraction-report.md`：转换范围、页码和注意事项。

PDF 共 {total_pages} 页。

## 章节

{chr(10).join(rows)}
"""
    (OUT_DIR / "index.md").write_text(content, encoding="utf-8")


def write_report(outline: list[OutlineItem], chapters: list[tuple[OutlineItem, Path, int, int]], total_pages: int) -> None:
    outline_rows = ["| 层级 | 标题 | 起始页 |", "|---:|---|---:|"]
    for item in outline:
        outline_rows.append(f"| {item.depth + 1} | {'　' * item.depth}{item.title} | {item.page} |")

    chapter_rows = ["| 文件 | 来源页码 |", "|---|---:|"]
    for _, path, start, end in chapters:
        chapter_rows.append(f"| `{path.relative_to(ROOT).as_posix()}` | {start}-{end} |")

    content = f"""# PDF 转换报告

- 源文件：`{SOURCE_PDF}`
- 输出目录：`{OUT_DIR}`
- PDF 页数：{total_pages}
- 处理方式：使用 PDF 内置书签拆分一级章节；正文按页抽取文字，移除固定页眉页码。
- 可追溯性：`full.md` 保留 `<!-- page: N -->` 页码标记，章节文件按原 PDF 页码范围拆分。

## 注意事项

- 本 PDF 是文字版，未使用 OCR。
- PDF 中图片、复杂表格和原始版式不会被完全还原为 Markdown 视觉效果；正文文本已完整抽取到 `full.md`。
- 章节文件用于阅读和静态站点展示；如需逐字核对，以 `full.md` 的页码标记对照原 PDF。

## 生成文件

{chr(10).join(chapter_rows)}

## PDF 书签目录

{chr(10).join(outline_rows)}
"""
    REPORT.write_text(content, encoding="utf-8")


def main() -> None:
    reader = PdfReader(str(SOURCE_PDF))
    outline = flatten_outline(reader)
    top_level = [item for item in outline if item.depth == 0]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CHAPTER_DIR.mkdir(parents=True, exist_ok=True)

    pages = build_page_markdown(reader)
    full_body = "\n\n".join(markdownize_text(page) for page in pages)
    (OUT_DIR / "full.md").write_text(f"# JAVA核心知识点整理（全量版）\n\n{full_body}", encoding="utf-8")

    chapters: list[tuple[OutlineItem, Path, int, int]] = []
    for idx, item in enumerate(top_level):
        start = item.page
        end = (top_level[idx + 1].page - 1) if idx + 1 < len(top_level) else len(reader.pages)
        fallback = f"chapter-{idx + 1:02d}"
        filename = f"{idx + 1:02d}-{slugify(item.title, fallback)}.md"
        path = CHAPTER_DIR / filename
        raw = "\n\n".join(pages[start - 1 : end])
        body = markdownize_text(raw, item.title)
        path.write_text(body, encoding="utf-8")
        chapters.append((item, path, start, end))

    write_index(chapters, len(reader.pages))
    write_report(outline, chapters, len(reader.pages))

    print(f"Wrote {OUT_DIR}")
    print(f"Chapters: {len(chapters)}")
    print(f"Pages: {len(reader.pages)}")


if __name__ == "__main__":
    main()
