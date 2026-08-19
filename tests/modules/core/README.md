# Core 测试说明

本分区验证 Arturo 核心心智模型与 agent 写代码最常用的元能力。

## 测试文件

| 文件 | 覆盖点 | 来源 |
|---|---|---|
| `official-info-pointer-do.art` | `info.get` 元数据、官方 example 字段、`'literal` / `var` / `let` 指针模型、`do` 执行块 | skill 的核心查字典流程与官方 runtime 元数据 |
| `attribute-default-helper.art` | 属性栈、`attr`、`??`、`function.inline`、placeholder 默认参数模式 | `arturo-language-skill` 中 issue #2136 经验 |
| `module-export.art` | `module`、内部 `function`、`method.public`、`export`、`this\name` | 官方 `module`/`export` + 矢量项目 |
| `module-helpers.art` | 给 scope-import 用的外部函数 | 包结构里的 submodule |
| `module-scope-import.art` | `module.with`、`init`、`import.lean`、`this\helpers\bang` | 对标 Python `__init__.py` |

## 运行

```bash
../../run-all.sh
# 或从仓库根目录：
./tests/run-all.sh
```
