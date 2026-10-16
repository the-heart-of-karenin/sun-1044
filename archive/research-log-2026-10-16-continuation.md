> 历史记录。文中的进度判断和待办反映写作时的状态；当前状态见 [项目说明](../README.md)。

# 2026-10-16 续研记录

## 最新续研：完整整除证明草稿

后续已将本记录末尾的高次幂断点闭合。主稿[divisibility-proof.md](../proofs/divisibility-proof.md)，自审[divisibility-audit.md](../review/divisibility-audit.md)；仍无外部同行审阅。

1. 两个显式截面高度1/3、5/2且互相正交，实际给判别式60的秩19子格。惰性约化的Artin不变量因而只能为1。
2. 利用van der Geer--Katsura的全m高阶Hasse水平性，超特殊K3的任意光滑一阶变形在形式Brauer群上具有零p级数，补足全部惰性素数幂。没有只由首个Hasse导数为零作结论。
3. 原加权Gauss--Manin组合在秩3模周期中的坐标为(90,45,33)/pi，位于有理Hodge(1,1)线；加上另一个已识别的除子线，得到整个组合是代数除子类。
4. 普通高度1形式群的整同构给q=lambda ell+I，I整；已核对Nygaard--Ogus相对比较的现代精确文本Inoue arXiv2108.11227 Theorem3.1及其Hodge交换图，另核对Langer--Zink2019式(85)。除子类与单位根线正交，故103+357lambda严格为零，控制全部普通素数幂。
5. 新两份精确证书各约0.1--0.2秒；只选p=23、37的两个幂以及p=11的三个幂作旁证，无搜索、后台或定时工作。

以下记录此前一轮的进展及当时断点，保留供追溯。

## 本轮形成的新证明草稿

1. **完整加权超同余**：[weighted-wronskian-proof.md](../proofs/weighted-wronskian-proof.md)。
   核心是从有限二次不变量构造在超奇异点正则的平方根，再与固定7次模对应作Wronskian。
   普通与惰性点的平方根符号由同一个模p关系决定；惰性点必须先求导，符号多一个负号。
   自审见[weighted-wronskian-audit.md](../review/weighted-wronskian-audit.md)，精确CM证书约0.37秒。p=7直接七项分别为 $[5,17,46,37,14,28,14]\pmod{49}$，和为14。

2. **整除断言的新全n约化**：[divisibility-brauer-reduction.md](../lemmas/divisibility-brauer-reduction.md)。
   定义beta_n=CT(g-540)^n，原断言等价于(2n+1)|(151beta_n+192780beta_(n-1))。
   它也等价于固定双平面形式Brauer对数的准对数J为整系数。
   两个坐标变换t/sqrt(1-540t²)及其逆都为整数级数，故这是真正的全n等价，不只适用于素数。

3. **全部5次幂**：[divisibility-five-adic.md](../lemmas/divisibility-five-adic.md)。
   特征5的四直线加一二次曲线模型有2D6+A3+3A1，给Picard秩至少19；Hasse为0排除高度1，因此形式群高度无穷。
   一阶v变形模5只是平方单位扭曲，故该一阶变形的形式群也有零5级数，整对数引理同时控制对数及参数导数。

4. **全部7次幂、17次幂**：[divisibility-seven-seventeen.md](../lemmas/divisibility-seven-seventeen.md)。
   特征0中央曲面有两个独立非挠截面，Picard数至少19。模7、17时只有可同时消解的A5、A1点，专化仍有秩至少19；Hasse为0，所以中央形式群高度无穷。
   对具有整对数的形式群，任意准对数至多留下一个p分母；357含7和17，故这两处的全部高次幂也能消掉。

这些稿件完成了本轮自查，尚未接受外部同行审阅。完整整除断言仍未证明。

## 未成功或未证明的路线，避免下轮重复

- [prime-power-probe.py](../scripts/prime-power-probe.py)只检查8个选定的(p,r)，约0.003秒。所有要求的素数幂整除都吻合，但把R_(p^r-1)/2 /p^r模p写成54*(15/p)^r+49*(-1/p)^r的简单猜测不成立；p=11,r=2给7，而该式给4。该猜测原本就没有从一阶加权同余得到证明，不能用于后续推导。
- [second-section.py](../scripts/second-section.py)对X为q二次多项式的两种常数项作有限符号消元。常数项-1没有非退化二次解；常数项c-1仅恢复已知截面。不能把这个计算写成证明额外CM截面不存在，也不需要为此启动更高次数的大规模搜索。
- Chisholm--Deines--Long--Nebe--Swisher的2013年论文Proposition16提供CM形式群思路，但其超几何有限比较不直接等于本题。新加权证明没有假装已经建立那个比较。
- Babei等arXiv2408.08844的当前v3（2025-03-12）主定理编号为1.3，附录为7；较早笔记中的1.4/8属于旧编号，已在[remaining-work.md](remaining-work.md)更正。
- 将复数7次模对应提升为J的p整形式群反对称关系，仍是一个真正缺口。[divisibility-brauer-reduction.md](../lemmas/divisibility-brauer-reduction.md)第3节给出一旦有该关系就能证明整性的初等引理，但没有把关系本身当成已证。

## 最明确的剩余任务

对p不属于{2,3,5,7,17}，控制J的全部p进分母，等价于控制所有满足p^r|(2n+1)的n中的p^r整除。
已有每个p的一阶整除；不能除以p后无条件再次套用同一个Lucas关系。
目前可以沿形式Brauer准对数、CM对应或代数循环方向继续；需要一个可引用并核对假设的整性比较，或本题的具体构造。

全部计算均为前台短时运算，没有后台任务、定时工作或大规模搜索。
