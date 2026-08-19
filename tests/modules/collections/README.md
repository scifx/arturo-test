# Collections 测试说明

本分区验证 block 与 dictionary 的常见写法，优先覆盖 agent 生成 Arturo 时高频使用的数据结构操作。

## 测试文件

| 文件 | 覆盖点 | 来源 |
|---|---|---|
| `dictionary-and-mutation.art` | `sort 'xs` 就地排序、`append 'xs` 就地追加、`loop`、动态 key 的 `key?`/`get`/`set` | 官方函数签名 + skill 指针模型 |

## 运行

```bash
./tests/run-all.sh
```
