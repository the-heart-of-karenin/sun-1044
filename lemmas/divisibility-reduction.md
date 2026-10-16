> 辅助研究笔记。个别段落保留早期进度描述；本文的用途及后续主稿见 [阅读顺序](../docs/reading-guide.md)。

# 最后一条整除断言：等价约化及已证的局部部分

2026-10-16。完整整除断言尚未证明。本文件把它变成一个奇数分母问题，并证明其3进部分与所有素数的一阶整除。

后续更新：[divisibility-brauer-reduction.md](divisibility-brauer-reduction.md)给出固定双平面形式Brauer对数的全n等价约化；[divisibility-five-adic.md](divisibility-five-adic.md)和[divisibility-seven-seventeen.md](divisibility-seven-seventeen.md)进一步证明全部5进、7进、17进部分。以下第4节保留较早阶段的缺口描述，以[remaining-work.md](../archive/remaining-work.md)为最新状态。

令

T_n=sum_(k<n)(357k+103)2160^(n-1-k)binom(2k,k)A_k，

u_n=T_n/[n binom(2n-1,n-1)]，u_0=0。

原断言等价于所有u_n均为整数。

## 1. 一阶递推与等价奇数分母条件

由于n binom(2n-1,n-1)=n binom(2n,n)/2，直接相除得到

(2n+1)u_(n+1)=1080n u_n+(357n+103)A_n，u_1=103。

因此2进整性自动成立；尚需控制全部奇素数。

令G(z)=sum A_n z^n，U(z)=sum_(n>=1)u_n z^n，B(z)=(1-540z)^(-1/2)，

R(z)=B(z)(357zG'(z)+103G(z))=sum R_n z^n。

递推给出

(2-1080z)U'-U/z=357zG'+103G，

其原点解析解为

U(z)=z B(z)*sum_(n>=0) R_n z^n/(2n+1)。

B与1/B=sqrt(1-540z)的系数均为整数，常数项1，所以完整原整除断言等价于

2n+1 divides R_n 对所有n>=0成立，                    (D)

其中

R_n=sum_(k=0)^n (357k+103) A_k binom(2n-2k,n-k)135^(n-k)。

这一等价性没有损失任何n，包含合数与素数幂。

## 2. 3的任意次幂：已证

记s_3(n)为n的三进制数字和。展开R_n中的A_k，置d=n-k、e=k-j，于是n=d+e+j。每一项含135^d*(-324)^e及

(e+3j)!/(e!j!³)=binom(e+3j,e)*(3j)!/(j!³)。

Legendre阶乘赋值公式给出v_3((3j)!/(j!³))=s_3(j)。因此每项的3进赋值至少3d+4e+s_3(j)，而数字和次可加性给出

s_3(n)<=s_3(d)+s_3(e)+s_3(j)<=d+e+s_3(j)。

所以v_3(R_n)>=s_3(n)。若3^r|2n+1，n的最低r个三进制数字均为1，故s_3(n)>=r。这证明(D)中所要求的全部3次幂。

## 3. 所有奇素数的一阶整除：已证

对奇素数p，记h=(p-1)/2。g_t的反射Newton多面体给出内层生成函数的Lucas同余

G(z)=G_p(z)G(z^p) (modp)，G_p=sum_(k<p) A_k z^k。

同样B(z)=B_h(z)B(z^p)(modp)，B_h=sum_(k<=h)binom(2k,k)135^k z^k。

于是

R(z)=[(357theta+103)G_p(z)]B_h(z) * (GB)(z^p) (modp)。

方括号乘积的次数至多p-1+h=3h。对n=h+pm，唯一可贡献的同余类系数是h，因为h+p=3h+1超出次数。因此

$R_{h+pm}=R_h[z^m](GB)(z)\pmod p$。

若p>7，则

R_h=(-540)^h W_p (modp)，

W_p为原加权和。[weighted-ordinary-proof.md](../archive/weighted-ordinary-proof.md)证明普通分支的W_p被p整除；惰性分支虽尚未完成模p²，但P_p=P_p'=E_p=0(modp)已经给出W_p=0(modp)。因此R_h=0(modp)。

p=7按原定义W_7=14(mod49)，所以同样成立。p=5直接计算R_2=51253380，含5；p=3已由第2节覆盖。故对所有n，rad(2n+1) divides R_n。

## 4. 当前缺口

对q>=5，仍需证明q^r|R_n，只要q^r|2n+1。第3节的一阶Lucas恒等式不能自动迭代为q^r精度，除以q后尚有新的误差项。

Guo的Franel整除定理虽可用于[transverse-congruence.md](transverse-congruence.md)的一个边界常数，但它的参数(-4,-16,3,1)不能直接替换为本题(-324,2160,357,103)。本题的完整整除断言仍未证明。
