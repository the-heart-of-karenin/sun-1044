# 计算附件

这里保存研究中使用的程序。它们辅助核对公式或产生有界的探索数据，不是整套证明的形式化验证器，也不验证所引用的算术几何定理。

整理时没有重新执行这些程序；历史运行记录在各笔记及 `review/` 中。路径调整只为使程序能从仓库根目录启动。默认参数沿用研究时的范围，没有加入批量运行入口、自动扫描或后台任务。

## 环境与运行

此前环境为 Python 3.14.3、SymPy 1.14.0、mpmath 1.3.0。建议使用独立 Python 环境，再在仓库根目录执行：

```sh
python -m pip install -r requirements.txt
python scripts/nl-certificate.py
```

每次只运行所需的附件。文件名保留了研究时的命名；`certificate` 表示代数计算附件，不表示 Lean、Coq 等系统中的形式化证明。

## 代数计算

| 文件 | 用途 |
| --- | --- |
| [ode-certificate.py](ode-certificate.py) | 四阶微分方程的算子恒等式 |
| [product-certificate.py](product-certificate.py) | 两个二阶解的乘积分解 |
| [nl-certificate.py](nl-certificate.py) | 参数曲线上的导数关系及对称平方约化 |
| [modular7-certificate.py](modular7-certificate.py) | 七次模方程的构造与有界系数比较 |
| [cm-certificate.py](cm-certificate.py) | 复乘选根与模方程导数 |
| [generic-product-certificate.py](generic-product-certificate.py) | 一般参数下的四阶算子与二次不变量 |
| [curve-isotropy-certificate.py](curve-isotropy-certificate.py) | 全参数曲线上的二次型关系 |
| [isotropy-certificate.py](isotropy-certificate.py) | 早期固定点二次型比较；后来有全曲线版本 |
| [weighted-wronskian-certificate.py](weighted-wronskian-certificate.py) | 七次对应的矩阵、导数与常数 |
| [divisibility-brauer-certificate.py](divisibility-brauer-certificate.py) | 奇坐标变换及特殊素数的局部代数 |
| [divisibility-tate-certificate.py](divisibility-tate-certificate.py) | 除子类论证中的向量系数与 Jacobian |
| [divisibility-inert-certificate.py](divisibility-inert-certificate.py) | 双平面模型、截面与判别式；另含固定素数的少量系数例子 |

`modular7-certificate.py` 会写入或覆盖 [data/modular7-polynomial.txt](../data/modular7-polynomial.txt)。另外两份使用该多项式的附件直接读取仓库已有的数据，无需先运行生成程序。

模方程附件的有限展开应与主稿的先验极点界一起理解。对于坐标变换等无限形式恒等式，有界系数检查本身不能代替正文的一般推导。

## 公共计算模块

| 文件 | 用途 |
| --- | --- |
| [bivariate-period.py](bivariate-period.py) | 双变量周期偏微分方程的行向量 |
| [period-operator.py](period-operator.py) | 归一化四阶算子的系数 |

## 有限探索与例子

| 文件 | 范围与用途 |
| --- | --- |
| [short-ode-check.py](short-ode-check.py) | 有界线性代数，用于最初发现微分方程 |
| [nl-series.py](nl-series.py) | 参数曲线上有限个级数系数的探索 |
| [frobenius-probe.py](frobenius-probe.py) | 固定小素数和有界 $q$ 展开中的 Frobenius 比较 |
| [prime-power-probe.py](prime-power-probe.py) | 固定素数幂的系数探索；输出含一条后来未成立的候选公式，不能当作结论 |
| [second-section.py](second-section.py) | 有界截面 Ansatz 的探索，不证明其他截面不存在 |
| [verify-short.py](verify-short.py) | 九个分支例子及模 $p$ 系数例子 |
| [inert-exception-certificate.py](inert-exception-certificate.py) | 早期论证中两个例外素数的有限检查 |

有限例子保留是为了说明研究过程。它们既不覆盖全部素数，也不是主稿正确性的独立证据。
