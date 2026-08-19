# numbers 测试说明

对应官方库模块 [Numbers](https://arturo-lang.io/documentation/library/numbers)。

网页总章有 CLI 没有的导读：常数（`epsilon` = e）、复数模/幅角、数论、三角。

## 测试文件

| 文件 | 覆盖点 | 来源 |
|---|---|---|
| `chapter-overview.art` | 总章常数 / 对数取整 / hypot / angle / 数论 / sin(pi/6) | 官方网页总章 + 实测 |

`info.get` 原始示例尚未整模块 smoke（部分函数、输出过大或 `angle` 历史 gap）。以 curated 章节测试为准。

## 运行

```bash
./tests/run-all.sh
```
