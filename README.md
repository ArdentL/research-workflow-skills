# Research Workflow Skills

[English](README.en.md) · [安装](docs/installation.md) · [完整示例](examples/paper-to-proposal/README.md) · [MIT](LICENSE)

**面向 Codex / Claude Code 的科研工作流 Skills：论文全文阅读、研究 Proposal、独立评审与关键科研决策。**

AI agent skills for **paper reading**, **research proposals**, **independent review**, and **evidence-based research decisions**.

这套 skill 来自 ArdentL 的实际科研协作流程，重点解决两件事：让研究方案能够追溯到论文原文，让关键决定能够追溯到证据、预算和明确负责人。可以逐个安装，也可以组合使用；无需采用整套论文工作台。

| Skill | 适用任务 | 主要产物 |
| --- | --- | --- |
| [paper-to-proposal](skills/paper-to-proposal/SKILL.md) | 论文收集后的全文阅读、近邻机制对比、研究方案与独立元评审 | 全文覆盖表、实际模型回执、原文证据、Proposal、评审与修订 |
| [research-decision-review](skills/research-decision-review/SKILL.md) | 创新性边界、核心结论、协议改变、扩量或研究方向取舍 | 紧凑证据包、审查原文、事实核查、明确决定与执行记录 |

首版提供工作说明、模板、合成示例和安装工具。模型通道、PDF 工具和子 agent 由使用者现有客户端提供；这里没有自动调用模型的后台服务。角色可配置，没有写死厂商、模型版本或私人路径。

## 快速安装

需要 Python 3.10+；克隆仓库需要 Git，也可从 Releases 下载源码 ZIP。安装和检查仅使用 Python 标准库。

```powershell
git clone https://github.com/ArdentL/research-workflow-skills.git
cd research-workflow-skills
python scripts/validate_bundle.py
python scripts/install.py --client codex --all --dry-run
python scripts/install.py --client codex --all
```

Claude Code 使用 `--client claude`。只安装论文流程可使用 `--skill paper-to-proposal`；也支持指定项目级安装目录。安装器默认不覆盖已有 skill，不修改全局指令或模型配置，不调用模型。见[安装与卸载](docs/installation.md)。

## 使用示例

在支持显式 skill 调用的 Codex 会话中：

```text
用 $paper-to-proposal 处理我提供的论文。
沿用项目已批准的模型通道和预算，独立读全文，比较近邻机制，
形成最小可证伪实验，再交给不继承讨论历史的新评审。
保留实际覆盖、回执、原始评审和逐项修订。

用 $research-decision-review 审查是否扩大实验规模。
先核已有结果，整理一页证据包；审查者和费用上限沿用项目配置。
```

其他兼容客户端也可以通过自然语言要求读取对应 `SKILL.md`。每个 skill 独立可用，不会强制串行调用另一个。

## 工作流保留哪些证据

1. **全文覆盖**：实际获得哪些原文、正文与附录读到哪里、哪些图表无法可靠抽取。下载、助手阅读、用户已读分别记录。
2. **真实模型调用**：实际 provider、模型身份、通道、输入范围、输出和调用回执。同模型分身不计为多个模型。
3. **机制差异**：对照最近邻到底共享什么、改变什么，哪些控制实验能区分新机制与额外信息或计算。
4. **可证伪 Proposal**：具体问题、最小实验、强基线与简单替换、统计单位、主指标、资源和停止条件。
5. **独立评审**：新上下文只接收 Proposal、原文和必要工具说明；原始意见、反证、答复与未解决项都保留。
6. **关键决策**：主力负责执行与核验，重要节点集中审查；建议、审查意见、实际批准与执行结果分别记录。

只有一个模型或缺少独立评审能力时，可以交付明确标记的草案；未完成的步骤保持待完成。论文流程本身不会授权实验、训练、额外花费或公开发布。

## 完整示例与成熟度

[合成端到端示例](examples/paper-to-proposal/README.md) 展示一个存在机制重合、忽略附录反例的 Proposal，如何经过评审后改成明确的最小验证。所有演示阅读和评审都标为合成记录，未冒充真实模型调用或科研结果。

v0.1.0 是首次公开工作流包。自动检查覆盖 UTF-8、相对引用、安装冲突和示例来源哈希；另有受限任务的独立行为试用。这些检查没有测量科研产出提升。详见[验证记录](docs/validation.md)。

## 文档与贡献

- [证据、模型、预算与权限约定](docs/workflow-contract.md)
- [来源与许可说明](PROVENANCE.md)
- [贡献指南](CONTRIBUTING.md) · [安全与隐私](SECURITY.md)
- [更新记录](CHANGELOG.md) · [引用元数据](CITATION.cff)

代码、skill、模板及合成示例采用 [MIT](LICENSE)。不包含第三方 skill 文本、真实论文 PDF、模型权重、私有研究记录或账户凭据。
