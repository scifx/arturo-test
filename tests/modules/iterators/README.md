# Iterators 测试说明

本分区验证 Arturo 迭代器模块的高频数据处理函数。

## 测试文件

| 文件 | 覆盖点 | 来源 |
|---|---|---|
| `map-select.art` | `map`、literal target in-place map、`select`、`map.with:'i` 索引属性 | `info.get 'map` 官方示例 + `info 'select` |

## 运行

```bash
./tests/run-all.sh
```
