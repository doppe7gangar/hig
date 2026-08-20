# Skill Apple Design

Apple 级动效 & 设计哲学，一键导入你的 AI Agent。

6 个 Skill，覆盖从设计原则到代码审计的完整链路——帮你写出真正"活"的界面。

[English](README.md)

---

## 安装

```bash
# macOS / Linux
bash <(curl -fsSL https://raw.githubusercontent.com/neko233-com/skill-apple-design/main/scripts/install.sh)

# Windows PowerShell
irm https://raw.githubusercontent.com/neko233-com/skill-apple-design/main/scripts/install.ps1 | iex

# 手动复制
git clone https://github.com/neko233-com/skill-apple-design.git
cp -r skill-apple-design/skills/* your-project/.claude/skills/
```

安装脚本自动检测 `.claude` / `.mimocode` 平台，复制到正确位置。

---

## Skills

| Skill | 一句话 | 什么时候用 |
|-------|--------|-----------|
| **apple-design** | Apple WWDC 设计哲学 + 17 条动效原则 | 构建手势驱动 UI、弹簧动画、可中断过渡 |
| **emil-design-eng** | UI 打磨、组件设计、动画决策框架 | 设计工程师日常开发 |
| **review-animations** | 10 条铁律审查动效代码 | Code Review |
| **improve-animations** | 扫描整个代码库，生成优先级修复计划 | 项目审计 |
| **find-animation-opportunities** | 找出「该动但没动」的地方 | 需求发现 |
| **animation-vocabulary** | 动效术语反查：描述效果 → 命名 | 团队沟通对齐 |

---

## 使用

安装后在 Agent 中直接调用：

```
/apple-design        → 问 Apple 设计哲学
/review-animations   → 审查动效代码
/improve-animations  → 扫描项目生成修复计划
```

也可以单独复制需要的 skill：

```bash
cp skills/apple-design/SKILL.md your-project/.claude/skills/
```

---

## Skill 详解

### apple-design — 设计哲学

Apple WWDC 设计演讲精华，翻译成 Web 开发语言。核心要点：

- **响应延迟** — pointer-down 即反馈，不等 click
- **直接操纵** — 1:1 跟踪手指，尊重抓取偏移
- **可中断性** — 动画随时可反转（最重要的原则）
- **弹簧动画** — 用 damping + response 而非 duration
- **动量投射** — 根据释放速度预测落点
- **空间一致性** — 进出路径对称，锚定触发源
- **材质深度** — 半透明层次传递层级关系
- **字体排印** — tracking 随尺寸变化

### emil-design-eng — 设计工程

UI 打磨的完整方法论：

- **动画决策框架** — 是否该动 → 什么缓动 → 多快
- **组件构建原则** — 按钮 scale(0.97)、popover 从触发器缩放
- **性能规则** — 只动 transform 和 opacity
- **Sonner 原则** — 构建受欢迎组件的 6 条经验

### review-animations — 动效审查

10 条铁律 + 强制升级触发器：

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
    ├── install.sh
    └── install.ps1
```

---

## License

MIT
