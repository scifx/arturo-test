# 项目变更记录

本文件记录 `arturo-test` 仓库层面的结构变化。更细的当日过程、测试结果和经验沉淀放在 `docs/<date>/`。

## 2026-08-19

### 新增

- 建立以 Arturo 官方 library module 为核心的测试组织方式：`tests/modules/<module>/`。
- 补齐 26 个官方模块目录，每个目录包含 `README.md`、`反馈.md`、`经验.md`、`官方示例.md`。
- 新增 `tests/official-library/`，验证官方 library metadata/example 覆盖。
- 新增 `tests/projects/` 与首个实战项目 `word-frequency/`。
- 新增 `tools/sync-library-examples.py`、`examples/library/`（从已准备好的 skill/runtime 导出官方示例；不自动联网）。
- 新增当日报告：`docs/2026-08-19/`。
- 新增实战项目 `tests/projects/vector-math/`：
  - `ops.art`：自包含 helper
  - `vector.art`：官方 `module.with` + `init` 里 `this\ops: import.lean ./{ops}!`
  - `vector-math.art`：合力 / 三角形面积场景
- 新增官方分区模块小测试：
  - `tests/modules/core/module-export.art`
  - `tests/modules/core/module-scope-import.art`
  - `tests/modules/core/module-helpers.art`
- 按官方网页 library **总章**（CLI `info` 没有的导读）新增 `chapter-overview.art`：
  - `arithmetic` `numbers` `bitwise` `comparison` `logic` `statistics`
  - `sets` `colors` `dates` `paths` `crypto` `strings` `types`
  - `files` `system` `reflection` `iterators` `collections` `core`
  - `exceptions` `io` `quantities`
- Collections 全量：`block-ops.art`、`dictionary-ops.art`。

### 验证

- 从上游 skill/runtime 导出 521 个 symbol 的 904 段官方示例；`info.get` 覆盖 520/521（gap：`window`）。
- 10 个模块的官方原始示例可整模块回归（`official-examples-smoke.art`）。
- `./tests/run-all.sh` 当前跑通 **48** 个 `.art` 测试文件（`arturo 0.10.1-dev+43`）。

### 约定调整

- 不 vendor、不在测试时自动 clone/fetch 上游 skill。
- 用户当次提醒写入当天 `docs/YYYY-MM-DD/对话总结.md`。
- 模块小测试放 `tests/modules/<官方模块>/`，实战项目放 `tests/projects/`，项目经验浓缩回官方分区。
- 抽 skill 前要读网页总章，不能只靠 `info.get`。
- 源码负数写 `neg 6`，不要写 `-6`；长链加括号。
- bitwise `and` ≠ logic `and?`（`and? 42 8` 为 Type Error）。
- 模块内互调写 `this\name`（`\name` 是简写）；对外入口用 `method.public`。

## 2026-08-20

### Strings 全量验证（同 collections 级别）

- **`tests/modules/strings/`** 从 2 个测试文件扩展到 **5 个**，新增：
  - `chapter-overview.art`（升级）：覆盖网页总章全部要点——`++`、大小写、谓词、match/replace、wordwrap/truncate/pad、split/join/slice、`~`/render.template
  - `case-and-predicates.art`（新增）：全部大小写函数（upper/lower/capitalize + mutate） + 全部谓词（upper?/lower?/ascii?/numeric?/whitespace?/prefix?/suffix?/contains?/match?），含 char 参数和 unicode 用例
  - `regex.art`（新增）：match 全部 7 种变体 + match?.in + replace 全部变体
  - `ops.art`（新增）：strip/pad/truncate/wordwrap/escape/indent/outdent/translate/alphabet/jaro/levenshtein/join/split/slice/render.template
  - `text-and-regex.art`（保留原 curated 文件）
- 全部 ~100 条断言通过当前 runtime（0.10.1-dev+43），strings 测试文件 5 个，全项目从 48 增至 **51**。
- 更新 `README.md`、`经验.md`、`反馈.md` 涵盖全量实测发现。

### 新发现的 runtime 差异

| 发现 | 细节 |
|---|---|
| `suffix?` 不支持 regex | 文档有 `{/\w/}` 示例但 runtime 返回 false（`prefix?` 正常支持） |
| `` `x` `` 为 `:unit` | `` `0` `` 不可用于 `pad.with`；须 `first "0"` 转 `:char` |
| `escape.shell` 行为 | 纯字母串原样返回，仅在含特殊字符时加单引号 |
| `truncate` 空格 | 默认 truncate 省略号前有一个空格，`.preserve` 模式才无空格 |
| 运算符优先级 | `size lst = 2` 解析为 `size (lst = 2)`，必须写 `(size lst) = 2`；同模式适用于 `jaro`/`levenshtein` 等 |

### 新增项目记忆与 MCP 集成文件

- `AGENTS.md`（新增）：项目级 agent 记忆提示词，汇总所有约定、编码规则、经验差异、测试方法，供后续 agent 进入项目时自动读取。
- `mcp.json`（新增）：项目级 MCP server 注册，遵循 `agent-plugins.org` 标准，注册 `arturo-help`（本地 stdio）和 `exa`（远程 HTTP）两个 MCP 服务器。
- `skills/arturo-language/`：已按 README 约定放置 skill 本体到 `skills/` 目录（gitignored），`run-all.sh` 可自动探测。
