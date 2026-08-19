# collections 测试说明

对应 [Collections](https://arturo-lang.io/documentation/library/collections)。  
数组（block）和字典都在这一章，必须分开测透。

| 文件 | 覆盖 |
|---|---|
| `chapter-overview.art` | 总章：`++`、下标、contains?/key?、range |
| `dictionary-and-mutation.art` | sort/append 原地改、词频 get/set |
| `block-ops.art` | 别名/`new`、couple、chop/drop/take/pop、split/slice、rotate |
| `dictionary-ops.art` | 动态键、extend 拷贝、dictionary.with、嵌套 select |

```bash
./tests/run-all.sh
```
