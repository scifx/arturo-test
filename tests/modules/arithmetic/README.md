# arithmetic 测试说明

对应官方库模块 [Arithmetic](https://arturo-lang.io/documentation/library/arithmetic)。

网页总章有 CLI `info` 没有的导读：类型提升、原地修改、有理数 `1:2`、quantity 运算。

## 测试文件

| 文件 | 覆盖点 | 来源 |
|---|---|---|
| `official-examples-smoke.art` | 11 个函数的 `info.get` 原始示例 | 上游 runtime |
| `chapter-overview.art` | 总章 Basic Usage / Common Patterns / 文档错误对照 | 官方网页总章 + 实测 |

## 运行

```bash
./tests/run-all.sh
```
