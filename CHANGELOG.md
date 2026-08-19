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
