# 部署指南：GitHub Pages + Vercel

> 将 Java 面试宝典静态站点部署到 GitHub Pages 和 Vercel 的完整步骤。

---

## 1. 前提条件

- ✅ 已完成 PDF → Markdown 转换（`docs/` 目录已生成）
- ✅ GitHub 账户（用于托管仓库）
- ✅ Vercel 账户（可选，用于加速访问）

---

## 2. 目录结构确认

部署前请确认 `docs/` 目录结构完整：

```
docs/
├── index.html              # Docsify 入口（站点核心）
├── index.md                # 首页
├── _sidebar.md             # 侧边栏导航
├── README.md               # GitHub 首页展示
├── .nojekyll               # [重要] 禁止 GitHub Pages 使用 Jekyll
├── PARSING_APPROACH.md     # 解析思路文档
├── DEPLOYMENT_GUIDE.md     # [本文档]
├── assets/
│   └── images/             # 提取的图片资源
├── java-interview-core/
├── javaguide/
├── note/
├── java3y/
├── interview-questions/
├── company-questions/
├── algorithm/
├── big-interview-3rd/
└── root-pdfs/
```

> **关键文件**: `.nojekyll` 文件必须存在，否则 GitHub Pages 会忽略 `_sidebar.md`（以下划线开头的文件）。

---

## 3. 部署到 GitHub Pages

### 3.1 初始化 Git 仓库

```bash
# 在项目根目录执行
cd /Users/qiyue/code/exams

# 初始化仓库
git init

# 添加文件（使用 .gitignore 排除大文件和临时文件）
git add docs/ .gitignore
git commit -m "init: Java面试宝典站点 - PDF转Markdown站点"
```

### 3.2 推送到 GitHub

```bash
# 创建 GitHub 仓库后
git remote add origin https://github.com/<your-username>/java-interview-book.git
git branch -M main
git push -u origin main
```

### 3.3 配置 GitHub Pages

> **方法一：通过仓库设置页面（推荐）**

1. 打开仓库 → **Settings** → **Pages**
2. **Source**: 选择 `Deploy from a branch`
3. **Branch**: 选择 `main`，目录选择 `/docs`
4. 点击 **Save**

> **方法二：通过 GitHub Actions（自动化构建）**

创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Pages
        uses: actions/configure-pages@v4
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: 'docs'
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 3.4 访问地址

部署完成后，你的站点将在以下地址可用：

```
https://<your-username>.github.io/java-interview-book/
```

---

## 4. 部署到 Vercel（可选，推荐）

Vercel 提供更快的全球 CDN 和自动 HTTPS，适合国内用户访问。

### 4.1 导入项目

1. 打开 [Vercel Dashboard](https://vercel.com/dashboard)
2. 点击 **Import Project** → **Import Git Repository**
3. 选择你刚推送的 GitHub 仓库

### 4.2 配置项目

| 配置项 | 值 |
|--------|-----|
| Framework Preset | **Other** |
| Root Directory | `docs/` |
| Build Command | _(留空，Docsify 无需构建)_ |
| Output Directory | _(留空)_ |
| Install Command | _(留空)_ |

### 4.3 环境变量（可选）

无需额外环境变量。

### 4.4 部署

点击 **Deploy**，等待部署完成（通常只需 1-2 分钟）。

### 4.5 自定义域名

可在 Vercel 项目设置中添加自定义域名：

```
Settings → Domains → 添加你的域名
```

### 4.6 访问地址

```
https://java-interview-book.vercel.app/
```

---

## 5. 双平台部署对比

| 特性 | GitHub Pages | Vercel |
|------|-------------|--------|
| **部署方式** | 推送即部署 | 自动监听 Git |
| **中国大陆访问** | ❌ 不稳定 | ✅ 较快 |
| **自定义域名** | ✅ 支持 | ✅ 支持 |
| **HTTPS** | ✅ 自动 | ✅ 自动 |
| **构建步骤** | ❌ 无需 | ❌ 无需 |
| **CDN** | Fastly | Vercel Edge Network |
| **配额** | 1GB / 月 100GB | 免费版 100GB |

> **建议**: 同时部署到两个平台，GitHub Pages 作为主站，Vercel 作为境内加速镜像。

---

## 6. 推荐 .gitignore 配置

```gitignore
# Python 临时文件
__pycache__/
*.py[cod]
*.egg-info/

# 系统文件
.DS_Store
Thumbs.db

# 原始 PDF 源文件（如果不需要追踪）
# Java_Interview_Book/

# 临时工作目录
.trae-cn/

# IDE
.vscode/
.idea/
```

---

## 7. 维护与更新

### 7.1 新增 PDF 后的更新流程

```bash
# 1. 重新运行转换脚本（会自动跳过已转换的文件）
python3 convert_pdfs.py

# 2. 查看变更
git status
git diff

# 3. 提交并推送
git add docs/
git commit -m "update: 新增XX面试题资料"
git push
```

### 7.2 全量重新转换

```bash
# 删除已转换文件，重新运行
rm -rf docs/
python3 convert_pdfs.py
```

### 7.3 监控转换状态

转换报告保存在 `docs/conversion_report.json`，包含每个文件的转换状态、页数、图片数等信息。

---

## 8. 故障排除

### 8.1 GitHub Pages 不显示内容

```
检查点：
✅ `.nojekyll` 文件存在吗？
✅ 仓库 Settings → Pages 配置正确吗？
✅ `index.html` 在 docs/ 目录下吗？
✅ GitHub Actions 部署成功了吗？
```

### 8.2 Docsify 侧边栏不显示

```
检查点：
✅ `_sidebar.md` 文件存在且内容正确吗？
✅ `loadSidebar: true` 在 index.html 中配置了吗？
✅ 文件编码是 UTF-8 吗？
```

### 8.3 图片显示异常

```markdown
# 检查 Markdown 中的图片路径是否正确
# 格式应为: ![描述](../assets/images/文件名)

# 确认 assets/images/ 目录存在且有图片文件
```

### 8.4 页面加载慢

```html
<!-- 将 Docsify CDN 替换为国内镜像 -->
<!-- 原版 -->
<script src="//cdn.jsdelivr.net/npm/docsify@5/lib/docsify.min.js"></script>

<!-- 国内镜像 -->
<script src="//cdn.bootcss.com/docsify/5.0.0/docsify.min.js"></script>
```