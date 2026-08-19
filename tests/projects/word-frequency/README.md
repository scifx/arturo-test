# word-frequency 实战项目

这是第一个实战项目示例：从一段文本生成词频 dictionary，并输出 JSON。

## 覆盖语言点

- `lower`、`replace`、`split.words`：文本清洗与切分。
- `loop`、`key?`、`get`、`set`：动态 dictionary 计数。
- `write.json value null`、`read.json`：JSON 字符串往返。
- `ensure.that:`：项目级可验证断言。

## 运行

```bash
./tests/run-all.sh
```

或单独运行：

```bash
ARTURO_BIN=/tmp/arturo-language-skill/bin/arturo ./tests/run-all.sh
```
