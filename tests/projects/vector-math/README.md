# vector-math 实战项目

第二个实战项目：实现一个可导入的数值矢量模块，并用 3D 合力 / 三角形面积场景做回归。

## 覆盖语言点

- `function`、`;; description`、`info.get`：用户函数文档与查字典。
- `import ./{vector}!`、`standalone?`：本地模块拆分和主程序守卫。
- `couple`、`map`、`fold.seed:`、`every?`、`get`、`size`：逐分量运算。
- `hypot`、`sqrt`、`//`、`neg`、`abs`：模长、单位矢量和负数。
- `throw`、`throws?`、`unless`：维度不一致、零向量等错误路径。
- `write.json` / `read.json`：把计算结果做成可断言的报告。

## 文件

| 文件 | 角色 |
|---|---|
| `vector.art` | 可导入矢量库。单独运行时执行单元断言。 |
| `vector-math.art` | 导入该库，计算合力、单位方向和三角形面积。 |

## 运行

```bash
./tests/run-all.sh
```

或单独运行：

```bash
ARTURO_BIN=/tmp/arturo-language-skill/bin/arturo \
  /tmp/arturo-language-skill/bin/arturo --no-color tests/projects/vector-math/vector.art

ARTURO_BIN=/tmp/arturo-language-skill/bin/arturo \
  /tmp/arturo-language-skill/bin/arturo --no-color tests/projects/vector-math/vector-math.art
```
