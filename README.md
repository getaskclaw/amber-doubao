# amber-doubao

用私有题库 **AMBER** 实测火山方舟（Volcengine Ark）豆包系模型，只公开结果，不公开题目。
English: [README.en.md](README.en.md)

## 这是什么

- 每期 `results/YYYY-Www.md`：同题、同 harness，对目标模型跑全库（23 案 / 26 卷）。
- 一期固定报告：题集规模与哈希、每案得分与通过/失败、终端终态、token 用量与时延、环境指纹、按证据纪律写的定性裁决。
- 题目、oracle、transcript、中间产物**永不公开**（见下「发布纪律」）。
- 姐妹仓：[amber-gpt](https://github.com/getaskclaw/amber-gpt)（GPT 周测）、[amber-crof](https://github.com/getaskclaw/amber-crof)、[amber-ollama](https://github.com/getaskclaw/amber-ollama)、[amber-devin](https://github.com/getaskclaw/amber-devin)、[amber-deepseek](https://github.com/getaskclaw/amber-deepseek)、[amber-commandcode](https://github.com/getaskclaw/amber-commandcode)、[amber-opencode](https://github.com/getaskclaw/amber-opencode)、[amber-workbuddy](https://github.com/getaskclaw/amber-workbuddy)、[amber-kimi](https://github.com/getaskclaw/amber-kimi)。
- AMBER 是 agentic 实战题库（施工/运维/审查/视觉/需求漂移），规范与制题工具见 [getaskclaw/amber](https://github.com/getaskclaw/amber)；考题本体私有。

## 发布纪律（红线）

1. 只发：分数与聚合、token 用量、速度、定性裁决。
2. 永不发：题目内容、oracle/判分器、transcript、考生工作区、任何能复原题面的中间产物。
3. 每期必钉：模型 ID、effort 档、日期（UTC）、harness 版本、每案内容哈希（bundle_sha）。哈希用于对照 [amber](https://github.com/getaskclaw/amber) 的公开哈希清单，自证题集未变。
4. 案号与题目结构属私有面：公开结果里案例只用稳定别名（A-xxxxxxxx，哈希派生）+ bundle 哈希作句柄；内部案号、变体名、题目描述永不出现。
5. 基调：这是社区实测，不是对厂商的攻击。数据说话，措辞克制。

## 渠道说明

本仓考的是**火山方舟 Agent Plan**（订阅套餐）车道的模型。注意该套餐的模型目录与后付费 API 不同：无版本锁定 ID，豆包 2.1-pro 级只有 `doubao-seed-evolving` 一个入口（官方公告其与当日最新版同步）。成绩归属以卷面实测的线路名为准。

## 一个方法论前提

同名模型、同 provider，两次跑也可能不同分——推理参数、负载、服务端版本都在漂；`evolving` 通道更会随官方升级换脑。所以这里的一切结论都带日期与档位。单日数字是快照，不是定律。

## 结果索引

| 期 | 内容 | 结论 |
|---|---|---|
| [2026-W38](results/2026-W38.md) | doubao-seed-evolving（≡ 2.1-pro-0915 官方同步版）@ high 全库首考 | 案级 16/23 追平已发布最佳；施工/文本/运维/漂移 97.9% 顶级，审查/视觉/前端净 −2 负资产，核验三案全部考墙零交付 |

## 免责

与火山引擎/字节跳动无任何隶属/赞助关系。分数是特定日期、特定档位的快照，不构成采购建议。
