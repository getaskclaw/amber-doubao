# 线级身份探针：doubao-seed-evolving 换皮假说终审（2026-09-17）

English: [model-identity-wire-probe-2026-09.en.md](model-identity-wire-probe-2026-09.en.md)

## 背景

AMBER W38 全库实测中，`doubao-seed-evolving`（火山方舟 Agent Plan，官方称与 Doubao-Seed-2.1-pro-0915 同版）的九轴成绩指纹与 deepseek-flash 家族高度相似（z-cos 前四近邻全部为 ds 车道）。分数相似只能证明"行为同形"，不能证明或排除"换皮"（同一模型换个名字卖）。本终审用线级探针（wire-level probes）回答这个问题。

## 方法

同一把订阅 key、同一端点（`/api/plan/v3`）、同一最小请求（`hi`），对三个模型各发一次，只看响应的"信封格式"，不看内容：

1. **模板偏移指纹**：tiny 请求的 `prompt_tokens` ≈ 该模型聊天模板的固定开销。不同模型家族的模板不同，此值稳定可复现，是模型级指纹。
2. **schema 签名**：响应 message 里有没有 `encrypted_content` 字段（火山 Seed 系加密推理签名）。
3. **别名回显**：请求模型 X，读 `response.model`——网关若偷偷改写（请求 A 实际服务 B），这里会露馅。

复现脚本：[model-identity-wire-probe-2026-09.py](model-identity-wire-probe-2026-09.py)（stdlib，key 走环境变量不落盘）。

## 结果

| 请求的 model | echo（response.model） | prompt_tokens（`hi`） | encrypted_content |
|---|---|---|---|
| doubao-seed-evolving | doubao-seed-evolving（无改写） | 47 | **有** |
| deepseek-v4.1-flash | deepseek-v4-1-flash | 31 | 无 |
| deepseek-v4-flash | deepseek-v4-flash-ga-260731 | 84 | 无 |

同一请求复跑验证稳定性：doubao 47/48，ds-v4.1 31/32（`hi`→`hello there` 各 +1 token，偏移稳定）。

## 结论

**换皮假说不成立。** 三证合一：模板指纹两两不同（47/31/84）、`encrypted_content` 仅豆包携带、回显各报真名。ark 端点上的 doubao-seed-evolving 与其 deepseek 系是不同的模型。AMBER 成绩指纹的高度相似是真实的能力谱趋同（或相近训练配方），不是贴牌。

附带发现：ark 的 `deepseek-v4-flash` 回显泄露底层构建号（ga-260731）；ds 系"尝鲜版"在套餐内偶发 429。

## 方法学教训

分数形状相似 ≠ 身份相同（similarity ≠ identity）。余弦近邻排序只能提出嫌疑；四次廉价调用（模板偏移 + schema 字段 + 回显）即可终审。先跑线级探针，再决定要不要烧全库对拍。
