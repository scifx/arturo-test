# vector-math 实战项目

用官方 `module` / `method.public` / `export` 做成可导入的数值矢量模块，再用 3D 合力 / 三角形面积做组合回归。

模块化的最小验证在 `tests/modules/core/module-export.art`；这里保留完整项目。

## 覆盖语言点

- `module`、`function`、`method.public`、`export`：模块内函数 + 对外方法。
- `\name`：模块内部互调。`import ./{vector}!`、`standalone?`：文件拆分。
- `couple`、`map`、`fold.seed:`、`every?`、`get`、`size`：逐分量运算。
- `hypot`、`sqrt`、`//`、`neg`、`abs`：模长、单位矢量和负数。
- `throw`、`throws?`、`unless`：维度不一致、零向量等错误路径。
- `write.json` / `read.json`：把计算结果做成可断言的报告。

## 文件

| 文件 | 角色 |
|---|---|
| `vector.art` | 官方 `module` 矢量库。单独运行时执行单元断言。 |
| `vector-math.art` | `import ./{vector}!` 后计算合力、单位方向和三角形面积。 |

## 运行

```bash
./tests/run-all.sh
```
