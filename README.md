# Java 面试题库 & 面试宝典

> 本仓库收录了 Java 后端开发相关的面试题，涵盖多个知名企业的真实面试经历。同时包含基于 Docsify 构建的在线文档站点，支持搜索、侧边栏导航等功能。

**在线访问**: [https://hello-github-ui.github.io/exams/](https://hello-github-ui.github.io/exams/)

---

## 目录

- [面试题内容概览](#面试题内容概览)
- [在线文档站点](#在线文档站点)
  - [站点内容统计](#站点内容统计)
  - [目录结构](#站点目录结构)
- [PDF 转 Markdown 教程](#pdf-转-markdown-教程)
  - [技术选型](#技术选型)
  - [转换步骤](#转换步骤)
  - [图片处理](#图片处理)
  - [目录归类策略](#目录归类策略)
  - [注意事项](#注意事项)
- [如何编辑已有的 Markdown 文件](#如何编辑已有的-markdown-文件)
- [如何新增 Markdown 文件](#如何新增-markdown-文件)
- [如何更新侧边栏导航](#如何更新侧边栏导航)
- [本地预览与调试](#本地预览与调试)
- [部署指南](#部署指南)
  - [GitHub Pages](#github-pages)
  - [Vercel](#vercel)

---

## 面试题内容概览

| 文件 | 来源 | 备注 |
|------|------|------|
| [JAVA核心知识点整理](content/java-core/index.md) | PDF 整理 | 30 个章节，含全量版与转换报告 |
| [BOSS直聘后端开发面试.md](BOSS直聘后端开发面试.md) | BOSS直聘 | 含详细答案 |
| [招商证券Java笔试题及答案.md](招商证券Java笔试题及答案.md) | 招商证券 | 含详细答案 |
| [招商银行Java后端面试.md](招商银行Java后端面试.md) | 招商银行 | 含详细答案 |

### BOSS直聘后端开发面试

涵盖以下主题：
- 线程池（热更新、核心参数、拒绝策略）
- Spring 自动装配原理
- MySQL（存储引擎、日志、数据一致性）
- Redis（数据类型、分布式锁、缓存穿透）
- gRPC 与微服务

### 招商证券 Java 笔试题

涵盖以下主题：
- Java 基础（基本数据类型、多态、异常、GC、volatile）
- Java 编程题（回文串、单例模式、链表反转、二叉树遍历）
- 数据结构与算法（二叉搜索树、快速排序、哈希表、动态规划）

### 招商银行 Java 后端面试

涵盖以下主题：
- Redis（数据类型、缓存穿透/击穿/雪崩）
- MySQL（存储引擎、B+树、三范式）
- Spring（请求处理流程、Bean 生命周期）
- 并发（线程池、ConcurrentHashMap）
- 系统设计（一致性哈希、服务交互方案）

---

## 在线文档站点

`docs/` 目录是一个基于 [Docsify](https://docsify.js.org/) 构建的静态文档站点，包含从 PDF 转换而来的 428 篇 Markdown 文档和 14,000+ 张图片。

### 站点内容统计

| 指标 | 数值 |
|------|------|
| Markdown 文件 | 428 篇 |
| 提取图片 | 14,122 张 |
| 分类目录 | 32 个 |
| 转换工具 | PyMuPDF (fitz) |

### 目录结构

```
docs/                            ← 站点根目录（部署此目录）
├── index.html                   ← Docsify 入口（站点核心）
├── index.md                     ← 首页
├── _sidebar.md                  ← 侧边栏导航配置
├── .nojekyll                    ← GitHub Pages 兼容
├── assets/
│   ├── docsify/                 ← Docsify 本地资源（CSS/JS/插件）
│   └── images/                  ← 从 PDF 提取的图片
├── algorithm/                   ← 代码随想录算法（6 篇）
├── big-interview-3rd/           ← 第3版互联网大厂面试题（155 篇）
├── company-questions/           ← 各大公司面试题库（32 篇）
├── interview-questions/         ← 笔试面试真题（57 篇）
├── java-interview-core/         ← Java面试突击核心讲（3 篇）
├── java3y/                      ← Java3y 系列（15 篇）
├── javaguide/                   ← JavaGuide 系列（34 篇）
├── javainterview/               ← JavaInterview 参考（42 篇）
├── note/                        ← Note 面试题分类（80 篇）
└── root-pdfs/                   ← 独立面试资料（4 篇）
```

---

## PDF 转 Markdown 教程

本项目使用 **PyMuPDF (fitz)** 将 PDF 面试题批量转换为 Markdown 格式，并自动整理目录层级和归类。

### 技术选型

| 方案 | 优点 | 缺点 | 选择理由 |
|------|------|------|----------|
| **PyMuPDF (fitz)** | 速度快、中文支持好、可提取图片 | 复杂排版还原度一般 | 首选：速度和中文友好度最佳 |
| pdfplumber | 表格提取优秀 | 速度慢，不支持图片提取 | 不适合大规模处理 |
| pdfminer.six | 布局分析强 | 速度极慢 | 408 个文件不可接受 |
| OCR (paddleocr) | 扫描件效果好 | 极慢、资源占用高 | 仅作为备选方案 |

### 转换步骤

#### 1. 安装依赖

```bash
pip install pymupdf
```

#### 2. 准备转换脚本

核心转换逻辑如下（完整脚本见仓库 `scripts/` 目录）：

```python
import fitz  # PyMuPDF
import os
import re
import hashlib
from pathlib import Path

SOURCE_DIR = "./Java_Interview_Book"    # PDF 源目录
OUTPUT_DIR = "./docs"                    # Markdown 输出目录
IMAGES_DIR = "./docs/assets/images"      # 图片输出目录

def convert_pdf_to_markdown(pdf_path, output_md_path, images_dir):
    pdf_stem = Path(pdf_path).stem
    doc = fitz.open(pdf_path)
    md_lines = []

    # YAML 前置元数据
    md_lines.append("---")
    md_lines.append(f"title: {pdf_stem}")
    md_lines.append(f"source: {os.path.relpath(pdf_path, SOURCE_DIR)}")
    md_lines.append(f"pages: {doc.page_count}")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append(f"# {pdf_stem}")
    md_lines.append("")

    for page_num in range(doc.page_count):
        page = doc[page_num]

        # 提取文本
        text = page.get_text("text").strip()
        text = re.sub(r'\n{3,}', '\n\n', text)

        if text:
            if page_num > 0:
                md_lines.append("\n---\n")
            md_lines.append(text)

        # 提取图片
        image_list = page.get_images(full=True)
        for img_idx, img in enumerate(image_list):
            xref = img[0]
            base_image = page.parent.extract_image(xref)
            img_bytes = base_image["image"]
            img_ext = base_image["ext"]

            # 生成唯一文件名（MD5 去重）
            img_hash = hashlib.md5(img_bytes).hexdigest()[:8]
            img_filename = f"{pdf_stem}_p{page_num+1}_{img_idx+1}_{img_hash}.{img_ext}"
            img_path = os.path.join(images_dir, img_filename)

            if not os.path.exists(img_path):
                with open(img_path, "wb") as f:
                    f.write(img_bytes)

            # Markdown 图片引用
            md_lines.append(f"\n![{pdf_stem} 第{page_num+1}页插图](../assets/images/{img_filename})")

    doc.close()

    # 写入 Markdown 文件
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    return True
```

#### 3. 批量转换

```bash
python3 convert_pdfs.py
```

脚本会自动：
- 遍历 `Java_Interview_Book/` 下所有 PDF 文件
- 按目录结构和文件名关键词自动归类
- 提取文本和图片
- 生成带 YAML 元数据的 Markdown 文件
- 生成 `_sidebar.md` 侧边栏导航
- 生成 `index.md` 首页

### 图片处理

PDF 中的图片采用以下流程处理：

1. **检测**：`page.get_images(full=True)` 获取所有图片引用
2. **提取**：`page.parent.extract_image(xref)` 获取图片二进制数据
3. **去重**：通过 MD5 hash 避免重复存储
4. **保存**：命名规则 `{pdf名}_p{页码}_{序号}_{hash}.{ext}`
5. **引用**：Markdown 中插入 `![描述](../assets/images/{文件名})`

### 目录归类策略

采用**两层归类**策略：

**第一层：按来源目录映射**

| 源目录 | 目标分类 |
|--------|----------|
| 1658页《Java面试突击核心讲》 | `java-interview-core/` |
| Java3y | `java3y/`（细分 interview/ebooks/mindmaps） |
| JavaGuide | `javaguide/`（细分 java-basics/jvm/framework/...） |
| Note | `note/`（细分 java-basics/jvm/concurrency/...） |
| 代码随想录算法PDF | `algorithm/` |
| 各大公司面试题库 | `company-questions/` |
| 笔试面试真题 | `interview-questions/` |
| 第3版互联网大厂面试题 | `big-interview-3rd/` |

**第二层：按文件名关键词细化**

对于内容杂乱的目录（如 Note），通过文件名关键词实现自动子分类：

```python
if "jvm" in filename → note/jvm/
if "spring" in filename → note/framework/
if "mysql" or "redis" in filename → note/database/
if "kafka" or "rabbitmq" in filename → note/middleware/
```

### 注意事项

1. **复杂排版还原度**：PyMuPDF 按阅读顺序提取文本，对于多栏布局、表格等复杂排版，文本顺序可能出现错乱
2. **扫描件 PDF**：部分 PDF 为扫描件（纯图片无文字层），PyMuPDF 无法直接提取文本，需配合 OCR
3. **字体编码**：部分 PDF 使用非标准字体编码，提取的文本可能出现字符显示异常
4. **图片位置**：Markdown 中图片会按提取顺序顺次展示，无法还原原始排版位置
5. **增量转换**：已转换的文件会自动跳过，新增 PDF 追加即可

---

## 如何编辑已有的 Markdown 文件

### 方法一：直接在 GitHub 网页编辑（推荐新手）

1. 打开仓库 `https://github.com/hello-github-ui/exams`
2. 进入 `docs/` 目录，找到要编辑的 `.md` 文件
3. 点击文件，然后点击右上角的铅笔图标 ✏️
4. 在线编辑 Markdown 内容
5. 编辑完成后点击 **Commit changes**
6. 等待 1-2 分钟，GitHub Pages 自动更新

### 方法二：本地编辑（推荐）

```bash
# 1. 克隆仓库
git clone https://github.com/hello-github-ui/exams.git
cd exams

# 2. 用你喜欢的编辑器打开 docs/ 目录下的 .md 文件
#    推荐：VS Code、Typora、Obsidian
code docs/note/java-basics/Java基础面试题_91道.md

# 3. 编辑保存后，提交并推送
git add docs/
git commit -m "update: 更新Java基础面试题内容"
git push origin master
```

### 方法三：使用 TRAE 直接编辑

在 TRAE 中打开项目，直接在文件树中找到 `docs/` 目录下的 `.md` 文件进行编辑，完成后提交推送即可。

---

## 如何新增 Markdown 文件

### 步骤 1：确定分类目录

根据你的内容主题，选择合适的分类目录：

| 内容主题 | 放置目录 |
|----------|----------|
| Java 基础、集合、异常 | `docs/note/java-basics/` |
| JVM、内存模型、GC | `docs/note/jvm/` |
| 多线程、并发编程 | `docs/note/concurrency/` |
| Spring / MyBatis / Tomcat | `docs/note/framework/` |
| MySQL / Redis / MongoDB | `docs/note/database/` |
| Kafka / RabbitMQ / RocketMQ | `docs/note/middleware/` |
| Dubbo / Zookeeper / 分布式 | `docs/note/distributed/` |
| Linux / Nginx / Git | `docs/note/devops/` |
| 设计模式 / 算法 / 网络 | `docs/note/other/` |
| 算法专题 | `docs/algorithm/` |
| 大厂面试题 | `docs/big-interview-3rd/` |
| 企业面试真题 | `docs/interview-questions/company/` |
| 公司题库 | `docs/company-questions/bank-368/` |

### 步骤 2：创建 Markdown 文件

在对应目录下创建 `.md` 文件，文件名使用中文或英文均可：

```bash
# 示例：新增一篇 Redis 面试题
cat > docs/note/database/Redis集群面试题.md << 'EOF'
---
title: Redis集群面试题
source: 手动编写
created_at: 2026-06-23
---

# Redis集群面试题

## 1. Redis Cluster 是什么？

Redis Cluster 是 Redis 的分布式解决方案...

## 2. Redis Cluster 的数据分片机制？

...
EOF
```

### 步骤 3：更新侧边栏导航

编辑 `docs/_sidebar.md`，在对应分类下添加新链接：

```markdown
* **🗄 Note - 数据库**
  * [Redis面试题_70道](note/database/Redis面试题_70道.md)
  * [Redis集群面试题](note/database/Redis集群面试题.md)    ← 新增这一行
```

### 步骤 4：提交推送

```bash
git add docs/
git commit -m "add: 新增Redis集群面试题"
git push origin master
```

等待 1-2 分钟，GitHub Pages 自动更新，新文档即可在线访问。

### 文件命名规范

- 推荐使用中文文件名（方便识别）：`Redis集群面试题.md`
- 特殊字符会被自动替换：`()` → `_`，`：` → `-`，空格 → `_`
- 避免使用 `/ \ : * ? " < > |` 等系统保留字符

---

## 如何更新侧边栏导航

侧边栏配置文件为 `docs/_sidebar.md`，格式如下：

```markdown
<!-- Java 面试宝典 - 侧边栏导航 -->

* [🏠 首页](/)

* **📂 分类名称**
  * [文档标题](相对路径/文件名.md)
  * [文档标题](相对路径/文件名.md)
```

**注意事项**：
- 所有路径都是相对于 `docs/` 目录的
- 分类名称用 `**粗体**` 包裹
- 文档链接使用 Markdown 标准链接格式 `[标题](路径)`
- 修改后需提交推送才能生效

---

## 本地预览与调试

在推送前，可以在本地预览站点效果：

```bash
# 方法一：Python 内置 HTTP 服务器
cd docs
python3 -m http.server 8080
# 然后打开 http://localhost:8080/

# 方法二：Docsify 官方 CLI（需要 Node.js）
npx docsify serve docs
# 然后打开 http://localhost:3000
```

---

## 部署指南

### GitHub Pages

1. 代码推送到 `master` 分支后自动部署
2. 访问地址：`https://hello-github-ui.github.io/exams/`
3. 如需重新配置：仓库 Settings → Pages → Branch: `master`，目录: `/docs`

### Vercel

1. 登录 [Vercel Dashboard](https://vercel.com/dashboard)
2. 点击 **Add New Project** → Import `hello-github-ui/exams`
3. 配置：
   - **Framework Preset**: Other
   - **Root Directory**: `docs`
   - **Build Command**: *(留空)*
4. 点击 **Deploy**

---

## 贡献

欢迎提交 Issue 或 Pull Request 补充更多面试题。具体步骤：

1. Fork 本仓库
2. 创建分支：`git checkout -b feature/new-content`
3. 在 `docs/` 对应目录下新增或编辑 `.md` 文件
4. 更新 `docs/_sidebar.md` 添加导航链接
5. 提交并推送：`git push origin feature/new-content`
6. 创建 Pull Request
