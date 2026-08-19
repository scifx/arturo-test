# vector-math 实战项目

官方 `module` 包装的数值矢量包：`ops.art` 是子模块，`vector.art` 相当于 Python 的 `__init__.py`。

模块化的最小验证在 `tests/modules/core/module-export.art` 和 `module-scope-import.art`。

## 覆盖语言点

- `module.with`、`init`、`this\name`、`import.lean`：包入口把外部函数挂到模块上。
- `method.public`、`export`、`import ./{vector}!`、`standalone?`：对外 API 和文件拆分。
- `couple`、`map`、`fold.seed:`、`hypot`、`//`、`throw`、JSON 报告。

## 文件

| 文件 | 角色 |
|---|---|
| `ops.art` | 外部 helper 函数（lean 子模块，互不点名）。 |
| `vector.art` | `init` 里 `this\ops: import.lean ./{ops}!`，公开方法走 `this\ops\...` / `this\vecAdd`。 |
| `vector-math.art` | 导入该包，计算合力、单位方向和三角形面积。 |

## 运行

```bash
./tests/run-all.sh
```
