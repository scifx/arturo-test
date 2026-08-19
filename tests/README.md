# Arturo 可验证示例测试

本目录用于把 Arturo 语言 skill 的知识转化为可运行测试。测试优先从官方 `info` / `info.get` 示例、官方模块函数签名和已验证经验出发。

## 重要约定：不自动获取 skill

上游 `scifx/arturo-language-skill` 会经常更新，因此本仓库不提交 skill 副本；同时为了避免每次测试都联网、耗时、浪费资源，测试运行器也**不会自动 fetch/clone**。

使用者需要自己按需准备或更新 skill：

```bash
git clone https://github.com/scifx/arturo-language-skill.git /tmp/arturo-language-skill
# 后续需要更新时：
git -C /tmp/arturo-language-skill pull --ff-only
```

## 运行

如果 runtime 在默认位置 `/tmp/arturo-language-skill/bin/arturo` 或 `skills/arturo-language/bin/arturo`：

```bash
./tests/run-all.sh
```

也可以显式指定：

```bash
ARTURO_SKILL_DIR=/tmp/arturo-language-skill ./tests/run-all.sh
ARTURO_BIN=/tmp/arturo-language-skill/bin/arturo ./tests/run-all.sh
```

## 分区原则

`tests/modules/` 参照 Arturo library module 分区。每个分区都有：

- `README.md`：覆盖范围、测试文件说明。
- `反馈.md`：对 skill 或官方文档的反馈材料。
- `经验.md`：agent 写 Arturo 时应复用的经验。
- `*.art`：可执行、可回归的示例。

`tests/projects/` 放实战项目级示例，同样要求每个项目文件夹有 `README.md`、`反馈.md`、`经验.md`。
