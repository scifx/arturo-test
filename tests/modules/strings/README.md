# strings 测试说明

对应 [Strings](https://arturo-lang.io/documentation/library/strings)。  
全量验证参照 collections 同级别标准：网页总章 + 官方示例逐条跑 runtime。

| 文件 | 覆盖 |
|---|---|
| `chapter-overview.art` | 网页总章：`++`、大小写、前后缀、strip、match/replace、wordwrap/truncate/pad、split/join/slice、`~`/render.template |
| `case-and-predicates.art` | 全部大小写函数 + 全部谓词：upper/lower/capitalize, upper?/lower?/ascii?/numeric?/whitespace?/prefix?/suffix?/contains?/match? |
| `regex.art` | match 全家桶（exact/regex/once/count/capture/named/bounds/in） + replace 全部变体 + match? |
| `ops.art` | 其它所有：strip/pad/truncate/wordwrap/escape/indent/outdent/translate/alphabet/jaro/levenshtein/join/split/slice/render.template |
| `text-and-regex.art` | curated 场景 |

```bash
./tests/run-all.sh
```