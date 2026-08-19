# Official Library 示例验证

本分区从 Arturo 官方 library / 上游 skill runtime 的 `info.get` 出发，验证“默认示例”是否可被发现和沉淀。

## 测试文件

| 文件 | 作用 |
|---|---|
| `library-metadata-coverage.art` | 对上游 skill `references/library-index.csv` 中的符号生成 `info.get 'symbol` 检查，确认 metadata 与 example 字段可用。|

## 当前验证结果

- library index：521 个 symbol。
- `info.get` metadata/example 可用：520 个 symbol。
- 已知 gap：`window` 在 index 中，但当前 bundled runtime 无法 `info.get 'window`。
- 已导出官方示例：904 段。
- 已整模块原样跑通的官方示例模块：`arithmetic`、`bitwise`、`colors`、`comparison`、`crypto`、`dates`、`paths`、`quantities`、`sets`、`statistics`。

## 运行

先按仓库根 README 手动准备上游 skill，然后：

```bash
./tests/run-all.sh
```

## 默认示例文本

每个官方模块目录都有：

```text
tests/modules/<module>/官方示例.md
```

集中索引副本位于：

```text
examples/library/
```

生成方式见 `tools/sync-library-examples.py`。该工具不联网、不拉取 skill，只读取已经准备好的 runtime 与 `library-index.csv`。
