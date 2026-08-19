# 项目变更记录

本文件记录 `arturo-test` 仓库层面的结构变化。更细的当日过程、测试结果和经验沉淀放在 `docs/<date>/`。

## 2026-08-19

### 新增

- 建立以 Arturo 官方 library module 为核心的测试组织方式：`tests/modules/<module>/`。
- 补齐 26 个官方模块目录，每个目录包含：
  - `README.md`
  - `反馈.md`
  - `经验.md`
  - `官方示例.md`
- 新增 `tests/official-library/`，用于验证官方 library metadata/example 覆盖情况。
- 新增 `tests/projects/`，用于沉淀实战项目级可验证示例。
- 新增 `tools/sync-library-examples.py`，从已准备好的上游 skill/runtime 批量导出官方 `info.get` 示例。
- 新增 `examples/library/`，作为官方示例 Markdown 集中索引副本。
- 新增首个实战项目：`tests/projects/word-frequency/`。
- 新增当日报告目录：`docs/2026-08-19/`。

### 验证

- 从上游 skill/runtime 导出 521 个 library symbol 的 904 段官方示例。
- `info.get` metadata/example 覆盖验证：520/521 个 symbol 通过。
- 已知 gap：`window` 在 index 中，但当前 bundled runtime 无法 `info.get 'window`。
- 已将 10 个可整模块原样运行的官方示例模块纳入默认回归：
  - `arithmetic`
  - `bitwise`
  - `colors`
  - `comparison`
  - `crypto`
  - `dates`
  - `paths`
  - `quantities`
  - `sets`
  - `statistics`
- `./tests/run-all.sh` 当前跑通 18 个 `.art` 测试文件。

### 约定调整

- 不 vendor 上游 skill。
- 不在测试运行时自动 clone/fetch 上游 skill。
- 使用者按需手动准备或更新 `scifx/arturo-language-skill`，再通过 `ARTURO_SKILL_DIR` 或 `ARTURO_BIN` 指定 runtime。
