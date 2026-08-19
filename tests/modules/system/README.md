# system 测试说明

本分区对应 Arturo 官方库模块：`system`。

## 当前状态

- 已建立分区骨架，等待从上游 skill 的 `info.get` 官方示例与实战代码中补充可验证用例。
- 新增 `.art` 文件时，请在文件头部标明覆盖的官方函数，并使用 `ensure.that:` 写断言。

## 建议流程

先按仓库根 README 手动准备或更新上游 skill，然后查询本模块相关函数：

```bash
/tmp/arturo-language-skill/bin/ahelp -s system
./tests/run-all.sh
```

如果 skill 放在其他位置，请用 `ARTURO_SKILL_DIR=...` 或 `ARTURO_BIN=...` 指定。
