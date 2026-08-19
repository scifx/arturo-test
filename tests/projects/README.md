# 实战项目测试

本目录用于放置比单个官方函数更接近真实 agent 任务的小项目。项目仍然必须可运行、可断言、可回归。

## 组织约定

每个项目文件夹都包含：

- `README.md`：项目目标、运行方式、覆盖语言点。
- `反馈.md`：项目暴露出的 skill 文档需求或运行时问题。
- `经验.md`：可复用的 Arturo 项目组织经验。
- `*.art`：项目代码或项目级测试。

## 当前项目

| 项目 | 说明 |
|---|---|
| `word-frequency/` | 从文本生成词频 dictionary 与 JSON 输出，覆盖 strings + collections + files 的组合用法。|
| `vector-math/` | 官方 `module` 数值矢量库：加减、点积、叉积、模长、单位矢量，并用 3D 合力 / 三角形面积做组合回归。模块化经验浓缩在 `tests/modules/core/经验.md`。|
