# arturo-test

这个仓库用于辅助 `arturo-language` skill 的创建、验证和迭代：为 agent 编写 Arturo 代码积累**可运行、可回归、可反馈**的示例。

重要约定：上游 skill 会频繁更新，**本仓库不 vendor / 不提交 skill 内容，也不在测试运行时自动拉取 skill**。需要测试时，使用者自己按需拉取或更新 [`scifx/arturo-language-skill`](https://github.com/scifx/arturo-language-skill)，然后把本仓库测试指向其中的 Arturo runtime。

## 目标

1. 按 Arturo 官方库模块分区积累示例代码。
2. 每个测试分区同时维护：
   - `README.md`：测试说明、覆盖函数、运行方式。
   - `反馈.md`：给 skill 上游沉淀的问题、文档缺口、可改进点。
   - `经验.md`：已验证的 Arturo 写法、坑点、agent 编码规则。
3. 所有 `.art` 文件都应可被本仓库的运行器验证，避免“看起来像 Arturo”的不可执行代码。
4. 除模块级官方示例外，维护 `tests/projects/` 实战项目示例，验证多模块组合用法。

## 仓库主干结构

```text
CHANGELOG.md                       # 项目级变更记录
docs/
  README.md
  2026-08-19/                      # 按日期记录项目变更、测试报告、对话总结
tools/
  sync-library-examples.py         # 从已准备好的 skill/runtime 导出官方 library 示例；不自动联网
tests/
  run-all.sh                       # 运行所有 Arturo 测试；不自动联网获取 skill
  README.md
  反馈.md
  经验.md
  official-library/                # 全库 metadata/example coverage 验证
  modules/                         # 参照 Arturo library module 分区，目录已补齐并填充 官方示例.md
  projects/                        # 实战项目级可验证示例
examples/
  library/                         # 官方示例集中索引副本
```

## 准备上游 skill

任选一种方式，手动准备一次即可。

### 放在 `/tmp`

```bash
git clone https://github.com/scifx/arturo-language-skill.git /tmp/arturo-language-skill
# 需要更新时手动执行：
git -C /tmp/arturo-language-skill pull --ff-only
```

### 放在仓库内的忽略目录

```bash
mkdir -p skills
git clone https://github.com/scifx/arturo-language-skill.git skills/arturo-language
# skills/ 已被 .gitignore 忽略，不会提交。
```

## 快速验证

如果 skill 在 `/tmp/arturo-language-skill` 或 `skills/arturo-language`，直接运行：

```bash
./tests/run-all.sh
```

也可以显式指定：

```bash
ARTURO_SKILL_DIR=/tmp/arturo-language-skill ./tests/run-all.sh
# 或
ARTURO_BIN=/tmp/arturo-language-skill/bin/arturo ./tests/run-all.sh
```

## 查询与同步官方函数示例

单个函数查询：

```bash
/tmp/arturo-language-skill/bin/ahelp map
/tmp/arturo-language-skill/bin/arturo --no-color -e "info.get 'map | get 'example | print"
```

如果你把 skill 放在 `skills/arturo-language`，则对应改成：

```bash
skills/arturo-language/bin/ahelp map
```

批量把当前 skill/runtime 的官方 library 示例同步到各模块文件夹：

```bash
ARTURO_BIN=/tmp/arturo-language-skill/bin/arturo \
LIBRARY_INDEX=/tmp/arturo-language-skill/references/library-index.csv \
python3 tools/sync-library-examples.py
```

该工具不 clone、不 fetch，只读取你已经准备好的 skill。当前已导出 521 个 symbol 的 904 段官方示例到：

```text
tests/modules/<module>/官方示例.md
examples/library/<module>.md
```

其中已实测可以整模块直接运行的官方原始示例，会额外生成：

```text
tests/modules/<module>/official-examples-smoke.art
```

## 新增测试分区约定

新增一个测试文件夹时，请至少包含：

```text
tests/modules/<module-name>/
  README.md
  反馈.md
  经验.md
  <verified-example>.art
```

`.art` 文件建议使用 `ensure.that:` 写可读断言，并以 `PASS <module>/<case>` 作为成功输出。

## 实战项目约定

实战项目放在：

```text
tests/projects/<project-name>/
  README.md
  反馈.md
  经验.md
  <project>.art
```

项目示例应覆盖多模块组合场景，例如文本处理 + dictionary + JSON、本地 `import` 模块 + 数值计算、HTTP + JSON、CLI + 文件等。

## 变更记录与当日报告

项目级变更写入：

```text
CHANGELOG.md
```

较大的结构调整、批量验证、上游反馈和与用户讨论形成的新约定，按日期写入：

```text
docs/YYYY-MM-DD/
  README.md
  项目变更.md
  测试报告.md
  对话总结.md
```

当前报告：[`docs/2026-08-19/`](./docs/2026-08-19/)。
