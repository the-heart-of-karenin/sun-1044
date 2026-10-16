> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# Laurent多项式模型与Dwork路线

2026-10-15，第二题继续研究。以下常数项恒等式已直接证明；尚未推出九分支超同余。

## 1. A_n(t)的Laurent多项式表达式

记s=1+x+y，并置

g_t(x,y)=s^3/(xy)+t s。

则有恒等式

A_n(t)=CT_{x,y} g_t(x,y)^n。

证明：按g_t^n中t的次数展开。t^(n-k)项为

binom(n,k) CT s^(n+2k)/(xy)^k
=binom(n,k)(n+2k)!/(k!^2 n!)
=(n+2k)!/((n-k)!k!^3)，

正好是定义中的系数。因此不必借助有理坐标换元或轮廓积分来证明。

## 2. 完整系数及截断和

令

Lambda_t(x,y,w)=(w+2+w^(-1))*g_t(x,y)。

由于CT_w(w+2+w^(-1))^n=binom(2n,n)，有

binom(2n,n) A_n(t)=CT Lambda_t^n，

F_t(z)=CT 1/(1-z Lambda_t)。

所以原S_p是这个三变量Laurent多项式周期的p项截断。

## 3. Newton多面体

g_t的Newton多边形为顶点(-1,-1)、(2,-1)、(-1,2)的三角形。t s的支集位于其中，不改变顶点；边界为x=-1、y=-1、x+y=1。整数严格内点仅有(0,0)。

Lambda_t的Newton多面体是该三角形与[-1,1]的直积，面方程均可写成整系数线性式=1，故为反射多面体，唯一内部格点为原点。

这使一般Dwork同余可适用，但一般定理只给通常精度。尤其不能把F_p(z_0)模p²等于复乘Frobenius值当成已获证明的推论。

## 4. 文献适用性核查

1. Beukers, Supercongruences using modular forms, arXiv:2403.03301v3，Assumption(II)要求权2模形式的唯一零点阶数r<=1。当前30级Z的零点阶数为3/2（局部坐标计普通消失阶数3，对应阶2椭圆点），不满足条件。不能直接套用Theorem1.15/1.16。
   https://arxiv.org/html/2403.03301v3
2. Beukers–Vlasenko, Dwork crystals III, arXiv:2105.14841v3，Introduction及Conjecture7.5明确区分Cartier操作的高精度结论和截断周期和的高精度结论，后者不是一般定理。本文Lambda还不是文中只由顶点组成、对顶点传递作用的完全对称族。
   https://arxiv.org/html/2105.14841v3
3. Yu Fu, p-adic Rigidity and Supercongruences at Rank Two Attractors, arXiv:2609.36045，结论主要是顶点展开系数行列式同余，不是本题S_p的截断和公式。即使验证复乘与典范提升，也还须单独证明截断和对应。
   https://arxiv.org/html/2609.36045

## 5. 已排除的简单截断替代

沿第一题曲线有H(r)=(1-r)/(1+r) Z(-r/(2(1+r)))。该无限级数恒等式不能直接给出原n<p截断与Z的X^n、n<p截断相等。

短时例子：p=11时原S_11=113 (mod121)，而直接Z截断在X=-1/10处为28 (mod121)，甚至模11也不同。这不是原猜想的反例，只是否定这种不保截断方式的替代。

当前优先目标：找到对原Laurent周期的截断保留模p²精度的有限变换，或建立适用的Cartier/模形式比较公式。
