# Apple Design Skills

Apple 级动效 & 设计哲学，一键导入你的 AI Agent。

---

## 一键安装

```bash
# macOS / Linux
bash <(curl -fsSL https://raw.githubusercontent.com/neko233-com/skill-apple-design/main/scripts/install.sh)

# Windows PowerShell
irm https://raw.githubusercontent.com/neko233-com/skill-apple-design/main/scripts/install.ps1 | iex

# 或者手动复制
git clone https://github.com/neko233-com/skill-apple-design.git
cp -r skill-apple-design/skills/* your-project/.claude/skills/
```

安装脚本会自动检测你的 Agent 平台（`.claude` / `.mimocode`），把 skills 复制到正确位置。

---

## 包含的 Skills

| Skill | 用途 | 适合谁 |
|-------|------|--------|
| **apple-design** | Apple WWDC 设计哲学 + 17 条动效原则 | 所有人 |
| **emil-design-eng** | UI 打磨、组件设计、动画决策框架 | 设计工程师 |
| **review-animations** | 审查动效代码，10 条铁律打分 | Code Review |
| **improve-animations** | 扫描整个代码库，生成优先级修复计划 | 代码审计 |
| **find-animation-opportunities** | 找出「该动但没动」的地方 | 需求发现 |
| **animation-vocabulary** | 动效术语反查：描述效果 → 命名 | 沟通对齐 |

---

## 快速上手

### 1. 先装 skill

```bash
# 进入你的项目目录
cd your-project

# 一键安装
bash ../skill-apple-design/scripts/install.sh
```

### 2. 在 AI Agent 中使用

安装后，skill 会出现在你的 Agent 的可用列表中：

```
/apple-design        → 问 Apple 设计相关问题
/review-animations   → 让 AI 审查你的动效代码
/improve-animations  → 让 AI 扫描整个项目并生成修复计划
```

### 3. 单独使用某个 skill

每个 skill 都是独立的 Markdown 文件，可以直接复制你需要的：

```bash
# 只要 apple-design
cp skills/apple-design/SKILL.md your-project/.claude/skills/
```

---

## Skill 详解

### apple-design — Apple 设计哲学

Apple WWDC 设计演讲精华，翻译成 Web 开发语言。涵盖：

- **响应延迟**：pointer-down 即反馈，不等 click
- **直接操纵**：1:1 跟踪手指，尊重抓取偏移
- **可中断性**：最重要原则——动画随时可反转
- **弹簧动画**：用 damping + response 而非 duration
- **动量投射**：根据释放速度预测落点
- **空间一致性**：进出路径对称，锚定触发源
- **材质深度**：半透明层次传递层级关系
- **字体排印**：tracking 随尺寸变化，大字收紧小字放松

### emil-design-eng — 设计工程实践

设计工程哲学，包含：

- **动画决策框架**：是否该动 → 什么缓动 → 多快
- **组件构建原则**：按钮 scale(0.97)、popover 从触发器缩放
- **性能规则**：只动 transform 和 opacity、Framer Motion 硬件加速陷阱
- **Sonner 原则**：构建受欢迎组件的 6 条经验

### review-animations — 动效审查

10 条铁律 + 强制升级触发器 + 分级修复优先级：

1. 动效必须有理由
2. 高频操作不加动效
3. 用 ease-out，不用 ease-in
4. UI 动画 < 300ms
5. popover 从触发器缩放
6. 可中断
7. 只用 GPU 属性
8. 支持 reduced-motion
9. 进入慢、退出快
10. 风格统一

### improve-animations — 代码库审计

4 阶段工作流：侦察 → 并行审计 → 筛选 → 写计划

生成 `plans/` 目录下的自包含修复计划，任何 agent 都能执行。

### find-animation-opportunities — 发现机会

4 道门槛过滤：频率 → 目的 → 速度 → 功能。大部分候选会被拒绝，只留高确信度机会。

### animation-vocabulary — 术语词典

把模糊描述翻译成精确术语：

- "那个弹出框从按钮长出来" → **Origin-aware animation**
- "iOS 滚动拉过头弹回来" → **Rubber-banding**
- "一个形状变成另一个" → **Morph**

---

## 项目结构

```
skill-apple-design/
├── README.md
├── LICENSE
├── skills/
│   ├── apple-design/SKILL.md
│   ├── emil-design-eng/SKILL.md
│   ├── review-animations/
│   │   ├── SKILL.md
│   │   └── STANDARDS.md
│   ├── improve-animations/
│   │   ├── SKILL.md
│   │   ├── AUDIT.md
│   │   └── PLAN-TEMPLATE.md
│   ├── find-animation-opportunities/SKILL.md
│   └── animation-vocabulary/SKILL.md
└── scripts/
    ├── install.sh       # macOS/Linux 一键安装
    └── install.ps1      # Windows PowerShell 一键安装
```

---

## License

MIT
