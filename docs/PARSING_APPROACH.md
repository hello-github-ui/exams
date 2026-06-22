# PDF 解析与转换思路文档

> 本文档详细说明 Java_Interview_Book 项目中 PDF 文档解析为 Markdown 的整体思路、技术选型及实施方法。

---

## 1. 项目背景

**Java_Interview_Book** 是一个收录了大量 Java 面试资料的仓库，包含 **408 个 PDF 文件**（约 2.1GB），内容涵盖：

- Java 基础、JVM、多线程/并发编程
- Spring 全家桶、MyBatis 等主流框架
- MySQL、Redis、MongoDB 等数据库
- Kafka、RabbitMQ、RocketMQ 等消息中间件
- 分布式系统、微服务架构
- LeetCode 算法、设计模式
- 各大互联网公司（阿里、腾讯、字节、美团等）面试真题
- 计算机基础（网络、操作系统）

原始资料以 PDF 格式为主，无法直接用于 Web 展示，因此需要将其转换为 Markdown 格式并组织为静态站点。

---

## 2. 技术选型

### 2.1 PDF 解析引擎：PyMuPDF (fitz)

| 方案 | 优点 | 缺点 | 选择理由 |
|------|------|------|----------|
| **PyMuPDF (fitz)** | ⚡ 速度快、中文支持好、可提取图片、轻量 | 复杂排版还原度一般 | ✅ 首选：速度和中文友好度最佳 |
| pdfplumber | 表格提取优秀 | 速度慢，不支持图片提取 | ❌ 不适合大规模处理 |
| pdfminer.six | 布局分析强 | 速度极慢 | ❌ 408 个文件不可接受 |
| OCR (paddleocr) | 扫描件效果好 | 极慢、资源占用高 | ❌ 仅作为备选方案 |

### 2.2 站点框架：Docsify

| 方案 | 优点 | 缺点 | 选择理由 |
|------|------|------|----------|
| **Docsify** | 无需构建、纯前端、轻量快速 | SEO 需额外配置 | ✅ 最适合大量 Markdown 的直接展示 |
| VitePress | 构建快、SEO 好 | 需要 Node.js 构建 | 可选替代方案 |
| Docusaurus | 功能丰富 | 配置复杂 | 对当前项目过重 |

---

## 3. 解析架构

```
┌─────────────────────────────────────────────────────────────┐
│                     Java_Interview_Book                       │
│  (408个PDF, ~2.1GB, 分布在12个目录)                          │
└──────────────┬──────────────────────────────┬──────────────┘
               │                              │
               ▼                              ▼
    ┌──────────────────┐          ┌──────────────────────┐
    │ 目录归类引擎      │          │   PyMuPDF 解析引擎   │
    │                   │          │                      │
    │ • 按源目录映射    │          │  • 文本提取(get_text)│
    │ • 按文件名关键词  │          │  • 图片提取(extract) │
    │ • 子分类细化      │          │  • 元数据提取        │
    └────────┬─────────┘          └──────────┬───────────┘
             │                               │
             └──────────┬────────────────────┘
                        ▼
            ┌──────────────────────┐
            │   Markdown 生成器     │
            │                      │
            │  • YAML Front Matter │
            │  • 正文 + 图片引用   │
            │  • 页面分隔          │
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │    docs/ 输出目录     │
            │                      │
            │  • 18+ 分类子目录    │
            │  • assets/images/    │
            │  • _sidebar.md      │
            │  • index.md         │
            └──────────────────────┘
```

### 3.1 目录归类策略

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

对于内容杂乱的目录（如 Note、JavaGuide），通过文件名关键词实现自动子分类：

```python
# 示例：关键词匹配规则
if "jvm" in filename → note/jvm/
if "spring" in filename → note/framework/
if "mysql" or "redis" in filename → note/database/
if "kafka" or "rabbitmq" in filename → note/middleware/
```

### 3.2 图片处理策略

PDF 中的图片采用以下流程处理：

1. **检测**：对每页调用 `page.get_images(full=True)` 获取所有图片引用
2. **提取**：`page.parent.extract_image(xref)` 获取图片二进制数据
3. **保存**：命名规则 `{pdf名}_p{页码}_{序号}_{hash}.{ext}`
4. **引用**：在 Markdown 中插入 `![描述](../assets/images/{文件名})`

> **为什么要 hash 去重？**
> 同一个图片可能在 PDF 中被多次引用（如重复的 Logo），通过 MD5 hash 可以避免重复存储。

---

## 4. 文件格式规范

### 4.1 Markdown 输出格式

每个转换后的 Markdown 文件包含：

```markdown
---
title: Java基础面试题(35题)
source: 各大公司面试题库/面试题库（368题）/01、Java基础(35题).pdf
pages: 8
converted_at: 2026-06-22
---

# Java基础面试题(35题)

[正文内容...]

![插图](../assets/images/java基础_p1_1_a1b2c3d4.png)
```

### 4.2 文件名处理

PDF 源文件名可能包含特殊字符，统一做以下处理：

```
"01、Java基础(35题).pdf" → "01、Java基础(35题).md"
"第三版：Dubbo 19 道.pdf" → "第三版-Dubbo_19_道.md"
```

---

## 5. 后期部署架构

```
┌───────────────────────────────────────────────────────┐
│                   用户访问                              │
└─────────────────┬─────────────────────────────────────┘
                  │
        ┌─────────┴──────────┐
        │                    │
   GitHub Pages         Vercel
  (docs/目录直接部署)    (更快的 CDN)
        │                    │
        └─────────┬──────────┘
                  ▼
         ┌──────────────────┐
         │   docsify CDN     │
         │ (index.html 入口) │
         └──────────────────┘
                  │
         ┌────────┴────────┐
         ▼                 ▼
    _sidebar.md        *.md 文档
  (导航)              (内容页面)
         │                 │
         └────────┬────────┘
                  ▼
          ┌──────────────┐
          │  搜索插件      │
          │(full-text)    │
          └──────────────┘
```

---

## 6. 实施步骤

| 步骤 | 操作 | 产出 |
|------|------|------|
| 1 | 安装 PyMuPDF | `pip install pymupdf` |
| 2 | 编写转换脚本 | `convert_pdfs.py` |
| 3 | 运行批量转换 | 408 个 PDF → 对应 Markdown |
| 4 | 生成导航文件 | `_sidebar.md` 自动生成 |
| 5 | 部署配置 | `index.html` (Docsify 入口) |
| 6 | 推送 GitHub | GitHub Pages 自动部署 |
| 7 | (可选) 导入 Vercel | Vercel 加速部署 |

---

## 7. 注意事项与局限

### 7.1 已知局限

1. **复杂排版还原度**：PyMuPDF 按阅读顺序提取文本，对于多栏布局、表格等复杂排版，文本顺序可能出现错乱
2. **扫描件 PDF**：部分 PDF 为扫描件（纯图片无文字层），PyMuPDF 无法直接提取文本，需配合 OCR
3. **字体编码**：部分 PDF 使用非标准字体编码，提取的文本可能出现字符显示异常
4. **图片位置**：Markdown 中图片会按提取顺序顺次展示，无法还原原始排版位置

### 7.2 改进方向

- **OCR 支持**：集成 PaddleOCR 或 Tesseract 处理扫描件
- **排版优化**：使用 pdfplumber 辅助表格提取
- **增量更新**：支持只转换新增/变更的 PDF
- **断点续传**：记录转换进度，中断后可恢复

---

## 8. 目录结构总览

```
docs/
├── index.html              # Docsify 入口（站点启动文件）
├── index.md                # 首页
├── _sidebar.md             # 侧边栏导航（自动生成）
├── README.md               # GitHub 首页
├── assets/
│   └── images/             # 全部提取的图片
├── java-interview-core/    # 1658页面试突击核心讲
├── javaguide/              # JavaGuide 系列
│   ├── java-basics/        # Java 基础
│   ├── jvm/                # JVM
│   ├── framework/          # 框架
│   ├── interview-guide/    # 面试突击版
│   ├── computer-basics/    # 计算机基础
│   ├── leetcode/           # LeetCode
│   └── learning-roadmap/   # 学习路线
├── note/                   # Note 面试题分类
│   ├── java-basics/        # Java 基础
│   ├── jvm/                # JVM
│   ├── concurrency/        # 多线程/并发
│   ├── framework/          # 框架
│   ├── database/           # 数据库
│   ├── middleware/         # 消息中间件
│   ├── distributed/        # 分布式
│   ├── devops/             # DevOps
│   └── data-engineer/      # 大数据/ES
├── java3y/                 # Java3y 系列
│   ├── interview/          # 对线面试官
│   ├── ebooks/             # 电子书
│   └── mindmaps/           # 思维导图
├── interview-questions/    # 笔试面试真题
│   ├── company/            # 企业真题
│   ├── by-topic/           # 按知识点
│   └── exam-packs/         # 笔试题套餐
├── company-questions/      # 各大公司题库
│   ├── bank-219/           # 219问
│   └── bank-368/           # 368题
├── algorithm/              # 代码随想录算法
└── big-interview-3rd/      # 第3版大厂面试题
```