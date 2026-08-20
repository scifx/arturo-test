# 必读 — 项目记忆提示词

> 任何 agent 进入此仓库时都应先读此文件。**不要编造 API，所有代码必须经过 runtime 验证。**

## 0. Arturo 核心心智模型（必先建立）

Arturo 的思维模型只有一句话：**字典 + 指针**。

- 每个词就是一个**字典条目**（`print`、`map`、`sort`、`+` 都是）。
- `'x` 是指针（`:literal`），`var 'x` 读指针，`let 'x v` 写指针。
- `sort 'xs` = "给 sort 一个指向 xs 的指针，让它原地改我"；`sort xs` = "拷一份排完扔掉"。

### 六个元能力关键字（语言的"自举"基础设施）

没有这六个关键字，你无法靠自己搞懂 Arturo。它们分三层：

| 层 | 关键字 | 作用 | 一句话 |
|---|---|---|---|
| **查字典** | `symbols` | 字典目录 | `symbols \| keys \| print` 列出所有可用词条 |
| | `info` (+`.get`) | 查词条的契约 | `info 'x` 看签名/属性/返回值；`.get` 取元数据**字典**和**可运行的官方示例** |
| | `inspect` | 查值的运行时结构 | `inspect x` 看字典键、嵌套块、错误内容、日期字段——value 的实际样子 |
| **指针** | `var` | 解引用**读** | `var 'a` → a 的值 |
| | `let` | 解引用**写** | `let 'a v` → 把 a 绑定到 v |
| **执行** | `do` | 块从"数据"变"代码" | `do [code]` 执行惰性块 |

**工作流：** 不认识某个词 → `symbols` 找它存在 → `info '词` 看契约 → `info.get '词 | get 'example` 拿官方示例 → 改写成自己代码 → `inspect` 看值的实际结构确认。

**Agent 入仓测试**：每次进仓库先跑以下命令验证模型：

```bash
./tests/verify-mental-model.sh
```

该脚本测试 `symbols`/`info`/`info.get`/`inspect`/`var`/`let`/`do` 七个核心操作都能正常调用。见 `tests/modules/core/mental-model.art`。

## 1. 项目定位

`arturo-test` 是辅助 [`scifx/arturo-language-skill`](https://github.com/scifx/arturo-language-skill) 创建和迭代的验证仓库。它为 agent 编写 Arturo 代码积累可验证、可反馈、可复用的示例。

## 2. 核心约定

### 2.1 skill 位置
- skill 本体在 `skills/arturo-language/`（已 commit，热启动即用）。
- 更新：`git -C skills/arturo-language pull --ff-only`。
- 可执行 runtime：`skills/arturo-language/bin/arturo`（`run-all.sh` 自动探测）。
- MCP stdio server：`python3 skills/arturo-language/mcp/server.py`（3 个工具：`arturo_info`、`arturo_search`、`arturo_doc_url`）。
- CLI 查函数：`skills/arturo-language/bin/ahelp <symbol>`。

### 2.2 测试文件结构

每个 `tests/modules/<module>/` 必须包含：

| 文件 | 用途 |
|---|---|
| `README.md` | 测试说明、文件列表、覆盖范围 |
| `反馈.md` | 给上游 skill 的反馈——网页/runtime 不一致、文档缺口 |
| `经验.md` | agent 写 Arturo 的编码经验、避坑指南 |
| `*.art` | 可运行、可回归的测试（使用 `ensure.that:` 断言） |
| `官方示例.md` | 由 `tools/sync-library-examples.py` 导出的原始官方示例 |

### 2.3 全量验证标准

1. **读网页总章**：https://arturo-lang.io/documentation/library/<module>
2. **逐条跑官方示例.md 到 runtime**，每个 symbol 至少一个 `ensure.that:` 断言
3. **所有断言通过后** 才更新 `经验.md` / `反馈.md`
4. 按功能分片（如 `block-ops.art`, `dictionary-ops.art`）

### 2.4 当日报告体系

- 决策写入 `docs/YYYY-MM-DD/对话总结.md`
- 测试结果写入 `docs/YYYY-MM-DD/测试报告.md`
- 项目变更写入 `docs/YYYY-MM-DD/项目变更.md`
- 项目级变更汇总到 `CHANGELOG.md`

## 3. Arturo 编码规则（已验证）

### 3.1 语法

- 负数用 `neg N`，不要写 `-N`。
- 长链比较/计算**必须加括号**：
  ```arturo
  (size lst) = 2          ; 正确
  (jaro "one" "one") = 1.0  ; 正确
  and? (contains? s "a") ((size s) > 1)  ; 正确
  ```
- 逻辑用 `and?` / `or?` / `not?`（logic 模块）
- bitwise 用 `and` / `or` / `xor`（bitwise 模块，不带 `?`）
- 字符串拼接用 `++`，只用 `++` 接两个 `:string`；其他类型先用 `to :string`。
- 正则用 `{/\d+/}`（brace 包 slash）。

### 3.2 已发现 runtime 不一致

| 条目 | 网页写法 | runtime 实测 |
|---|---|---|
| `match` 返回值 | `"o world"`（string） | `["o world"]`（block） |
| `truncate 5` 省略号 | `"Hello..."` | `"Hello ..."`（空格在点前） |
| `` `x` `` 类型 | 可能是 `:char` | **`:unit`（quantity）**，`first "x"` 才是 `:char` |
| `pad.with:`0`` | 官方示例写 `` `0` `` | TypeError，须 `pad.with:(first "0")` |
| `suffix?` + 正则 | 文档有示例 | **不支持**，返回 false（`prefix?` 支持） |
| `escape.shell` 纯字母 | | 原样返回，只特殊字符才加引号 |

### 3.3 经验要点

- `ensure.that: "name" [expr]`——断言表达式必须求值为 `:logical`
- 测试文件以 `print "PASS <module>/<case>"` 结尾
- `match` 全家桶返回 `:block`
- `split "ab"` 返回 `[:string]` 不是 `[:char]`
- `alphabet 'es` 返回 `[:char]`
- `~"\|name\|"` 是求值插值，`render.template` 是 `<||>` 块模板引擎
- 块 `[...]` 是数据不执行；`do [...]` 才执行
- 别名 = 共享引用（`b: a`），`new a` = 独立拷贝

## 4. 运行测试

```bash
./tests/run-all.sh
```

当前全项目 51 个 `.art` 测试文件通过（0.10.1-dev+43）。

## 5. 参与规则

- 新增测试分区时必须包含 README.md / 反馈.md / 经验.md
- 不要编造 API——每个断言必须先跑 runtime 验证
- 用户当次提醒要原文或近原文写入对话总结
- 成功输出要在 `CHANGELOG.md` 更新测试文件计数