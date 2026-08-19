# Files / JSON 测试说明

本分区验证文件读写与 JSON 往返，这是 agent 编写工具脚本时最常见的 I/O 场景。

## 测试文件

| 文件 | 覆盖点 | 来源 |
|---|---|---|
| `read-write-json.art` | `write content file`、`read file`、`write.json value null`、`write.json value file`、`read.json` | 官方函数签名 + skill JSON 经验 |

## 运行

```bash
./tests/run-all.sh
```

测试临时文件写入 `/tmp/arturo-test-read-write.*`，不污染仓库。
