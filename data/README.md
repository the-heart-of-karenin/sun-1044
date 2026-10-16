# 模方程数据

[modular7-polynomial.txt](modular7-polynomial.txt) 以 SymPy 可读的表达式保存二元整系数多项式 $P(T,U)$。其变量对应级数主稿中的 $T(\tau)$ 与 $T(7\tau)$。

生成程序为 [modular7-certificate.py](../scripts/modular7-certificate.py)。它运行时会覆盖这一文本；[cm-certificate.py](../scripts/cm-certificate.py) 和 [weighted-wronskian-certificate.py](../scripts/weighted-wronskian-certificate.py) 读取它。

多项式作为模方程的依据包括程序中的整数展开和 [级数主稿](../proofs/proof-series.md) 中的极点界论证，不能只凭若干系数吻合认定。
