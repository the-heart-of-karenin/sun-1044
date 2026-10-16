> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# 整除断言的全部5次幂：证明草稿

2026-10-16。使用[divisibility-brauer-reduction.md](divisibility-brauer-reduction.md)的ell_v、J及其整坐标变换。下面证明J∈Z_5[[u]]，所以v_5(R_n)>=v_5(2n+1)对所有n成立。

## 1. 特征5中央双平面的高度

模5有-324=-4、540=0，于是v=1时的六次式变成

P0=xyz*s*(s²-4xy)，s=x+y+z。

其分支曲线是四条直线x=0,y=0,z=0,s=0与光滑二次曲线s²-4xy=0。
双覆盖有以下有理双点，且没有其他奇点：

- (0:1:-1)、(1:0:-1)：各为D6。
- (1:1:0)：为A3。
- 三个坐标顶点：各为A1。

局部核验：在第一个D6点取y=1、S=s，则除去平方单位后分支为X*S*(S²-4X)。令U=X-S²/8，它变成-4S U²+S^5/16，是D6正规型；另一点由交换x,y得到。
在(1:1:0)，z=0与二次曲线以交数2相切，其他分支为单位，双覆盖为A3。
坐标顶点是两个横截分支，给A1。特征5中所有用到的2、4、8、16均可逆。

最小消解是K3曲面。18条例外曲线的根格为D6⊕D6⊕A3⊕A1³；加上拉回的直线类（与例外曲线正交、平方为2），得到秩至少19的Neron-Severi子格。

形式Brauer群的Hasse系数是beta_2 mod5。
这里约化后的beta_n与A_n(-4)=sum_j binom(n,j)^3同余，因此beta_2=10=0(mod5)；不把它误写为特征0中原beta_n的等式。
故高度不是1。若高度h有限，Artin--Mazur的斜率结果给rho<=22-2h；rho>=19强迫h=1，矛盾。因此h=∞，即此中央形式群的[5]恒为零。
这里没有把单个Hasse零值独自当成高度无穷的证据；秩19的几何输入排除了所有有限高度h>=2。

## 2. 连一阶v变形也有零5级数

取底环R=Z_5[epsilon]/(epsilon²)，v=1+epsilon。
在R/5中有P_v=(1+epsilon)P0。
因sqrt(1+epsilon)=1+epsilon/2，将w乘以这个单位即把该双平面与中央双平面的常值族同构。
所以其形式Brauer群的[5]在整个R/5上为零，包括epsilon一次项。

R没有5挠。由[divisibility-brauer-reduction.md](divisibility-brauer-reduction.md)第3节最后的形式群引理，

ell_(1+epsilon)(u)∈R[[u]]。

其常数项与epsilon系数分别是ell_1和(dell_v/dv)|_(v=1)，故两者都在Z_5[[u]]。
于是J=103ell_1+357(dell_v/dv)|_1也在Z_5[[u]]。
由整数坐标变换(A)，得到所需的全部5进整除。

## 标准输入

- 双覆盖的形式Brauer对数及本题Cech坐标：[divisibility-brauer-reduction.md](divisibility-brauer-reduction.md)第2节。
- Artin--Mazur, Formal groups arising from algebraic varieties, Ann.Sci.ENS10 (1977), 87-131，关于有限高度斜率及Picard数的结果：
  https://www.numdam.org/article/ASENS_1977_4_10_1_87_0.pdf
- 有理双点的D6、A3、A1标准正规型与消解；上面已写出本题局部识别。

这是一条新局部证明草稿，尚无外部审阅。它没有处理其他素数q>=7的高次幂。
