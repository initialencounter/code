import random
import docx
from docx import shared
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
ast = '''adsorbent 吸附剂
adsorption 吸附 
affinity chromatography 亲和色谱法
aliquot (一)份 
alkalinity 碱度 
alumina 氧化铝 
ambient temperature 室温 
ammonium thiocyanate 硫氰酸铵 
药物分析英语词汇
analytical quality control(AQC)分析质量控制
Abbe refractometer 阿贝折射仪 
anhydrous substance 干燥品 absorbance 吸收度 
anionic surfactant titration 
阴离子表面活性剂滴定法
absorbance ratio 吸收度比值 
absorption 吸收
antibiotics-microbial test 抗生素微生物检定法
absorption curve 吸收曲线 
absorption spectrum 吸收光谱 
antioxidant 抗氧剂 
absorptivity 吸收系数 
appendix 附录 accuracy 准确度 application of sample 点样 acid-dye colorimetry 酸性染料比色法area normalization method 面积归一化法
acidimetry 酸量法 argentimetry 银量法 acid-insoluble ash 酸不溶性灰分 arsenic 砷 acidity 酸度 arsenic stain 砷斑 activity 活度 ascending development 上行展开
additive 添加剂 
ash-free filter paper 无灰滤纸(定量滤纸)
additivity 加和性 
adjusted retention time 调整保留时间assay 含量测定 
assay tolerance 含量限度 bromate titration 溴酸盐滴定法atmospheric pressure ionization(API) 大气压离子化bromimetry 溴量法 
bromocresol green 溴甲酚绿 attenuation 衰减 
bromocresol purple 溴甲酚紫 back extraction 反萃取 
bromophenol blue 溴酚蓝 back titration 回滴法 
bromothymol blue 溴麝香草酚蓝 bacterial endotoxins test 细菌内毒素检查法
bulk drug, pharmaceutical product 原料药
band absorption 谱带吸收 
buret 滴定管 baseline correction 基线校正 
by-product 副产物 baseline drift 基线漂移 
calibration curve 校正曲线 batch, lot 批 
calomel electrode 甘汞电极 batch(lot) number 批号 
calorimetry 量热分析 Benttendorff method 白田道夫(检砷)法
capacity factor 容量因子 
capillary zone electrophoresis (CZE) 毛细管区带电泳between day (day to day, inter-day) precision 日间精密
度 
capillary gas chromatography 毛细管气相色谱法between run (inter-run) precision 批间精密度
carrier gas 载气 biotransformation 生物转化 
cation-exchange resin 阳离子交换树脂bioavailability test 生物利用度试验
ceri(o)metry 铈量法 bioequivalence test 生物等效试验
characteristics, description 性状 biopharmaceutical analysis 体内药物分析，生物药物分析
check valve 单向阀 
chemical shift 化学位移 blank test 空白试验 
chelate compound 鳌合物 boiling range 沸程 
chemically bonded phase 化学键合相British Pharmacopeia (BP) 英国药典 
chemical equivalent 化学当量 coefficient of distribution 分配系数
Chinese Pharmacopeia (ChP) 中国药典
coefficient of variation 变异系数 
color change interval (指示剂)变色范围Chinese material medicine 中成药
Chinese materia medica 中药学 color reaction 显色反应 Chinese materia medica preparation 中药制剂colorimetric analysis 比色分析 
colorimetry 比色法 Chinese Pharmaceutical Association (CPA) 中国药学会
column capacity 柱容量 
column dead volume 柱死体积 chiral 手性的 
column efficiency 柱效 chiral stationary phase (CSP) 手性固定相
column interstitial volume 柱隙体积
chiral separation 手性分离 
column outlet pressure 柱出口压 chirality 手性
column temperature 柱温 chiral carbon atom 手性碳原子 
column pressure 柱压 chromatogram 色谱图 
column volume 柱体积 chromatography 色谱法 
column overload 柱超载 chromatographic column 色谱柱 
column switching 柱切换 chromatographic condition 色谱条件
committee of drug evaluation 药品审评委员会
chromatographic data processor 色谱数据处理机
comparative test 比较试验 chromatographic work station 色谱工作站
completeness of solution 溶液的澄清度
clarity 澄清度 
compound medicines 复方药 clathrate, inclusion compound 包合物
computer-aided pharmaceutical analysis 计算机辅助药 
物分析 clearance 清除率 
concentration-time curve 浓度,时间曲线
clinical pharmacy 临床药学 
confidence interval 置信区间 deflection point 拐点
confidence level 置信水平 degassing 脱气 confidence limit 置信限 deionized water 去离子水 congealing point 凝点 deliquescence 潮解 congo red 刚果红(指示剂) depressor substances test 降压物质检查法
content uniformity 装量差异 
derivative spectrophotometry 导数分光光度法
controlled trial 对照试验 
correlation coefficient 相关系数 derivatization 衍生化 contrast test 对照试验 descending development 下行展开
counter ion 反离子(平衡离子) 
desiccant 干燥剂 cresol red 甲酚红(指示剂) 
detection 检查 crucible 坩埚 
detector 检测器
crude drug 生药 
developer, developing reagent 展开剂crystal violet 结晶紫(指示剂) 
cuvette, cell 比色池 developing chamber 展开室 cyanide 氰化物 deviation 偏差 cyclodextrin 环糊精 dextrose 右旋糖，葡萄糖 cylinder, graduate cylinder, measuring cylinder 量筒diastereoisomer 非对映异构体 
diazotization 重氮化 cylinder-plate assay 管碟测定法 
2,6-dichlorindophenol titration 2,6-二氯靛酚滴定法daughter ion (质谱)子离子 
dead space 死体积 differential scanning calorimetry (DSC) 差示扫描热量法
dead-stop titration 永停滴定法 
differential spectrophotometry 差示分光光度法dead time 死时间 
decolorization 脱色 differential thermal analysis (DTA) 差示热分析
decomposition point 分解点 
differentiating solvent 区分性溶剂 deflection 偏差 
diffusion 扩散 electrophoresis 电泳
digestion 消化 electrospray interface 电喷雾接口
diphastic titration 双相滴定 
electromigration injection 电迁移进样
disintegration test 崩解试验 
dispersion 分散度 elimination 消除 dissolubility 溶解度 eluate 洗脱液 dissolution test 溶出度检查 elution 洗脱 distilling range 馏程 emission spectrochemical analysis 发射光谱分析
distribution chromatography 分配色谱
enantiomer 对映体 distribution coefficient 分配系数 end absorption 末端吸收 dose 剂量 end point correction 终点校正 drug control institutions 药检机构 endogenous substances 内源性物质
drug quality control 药品质量控制 
enzyme immunoassay(EIA) 酶免疫分析drug release 药物释放度 
drug standard 药品标准 enzyme drug 酶类药物 drying to constant weight 干燥至恒重enzyme induction 酶诱导 
enzyme inhibition 酶抑制 dual wavelength spectrophotometry 双波长分光光度法
eosin sodium 曙红钠(指示剂) duplicate test 重复试验 epimer 差向异构体 effective constituent 有效成分 equilibrium constant 平衡常数 effective plate number 有效板数 equivalence point 等当点 efficiency of column 柱效 error in volumetric analysis 容量分析误差
electron capture detector 电子捕获检测器
excitation spectrum 激发光谱 electron impact ionization 电子轰击离子化exclusion chromatography 排阻色谱法
expiration date 失效期 fluorescence polarization immunoassay(FPIA) 
external standard method 外标法 
荧光偏振免疫分析 extract 提取物 
fluorescent agent 荧光剂 extraction gravimetry 提取重量法 
fluorescence spectrophotometry 荧光分光光度法
extraction titration 提取容量法 
extrapolated method 外插法，外推法fluorescence detection 荧光检测器
factor 系数，因数，因子 fluorimetyr 荧光分析法 feature 特征 foreign odor 异臭 Fehling’s reaction 费林反应 foreign pigment 有色杂质 field disorption ionization 场解吸离子化formulary 处方集 
fraction 馏分 field ionization 场致离子化 
freezing test 结冻试验
filter 过滤，滤光片 
funnel 漏斗 filtration 过滤 
fused peaks, overlapped peaks 重叠峰
fineness of the particles 颗粒细度
fused silica 熔融石英 flame ionization detector(FID) 火焰离子化检测器
gas chromatography(GC) 气相色谱法
flame emission spectrum 火焰发射光谱
gas-liquid chromatography(GLC) 气液色谱法
flask 烧瓶 
gas purifier 气体净化器 flow cell 流通池 
gel filtration chromatography 凝胶过滤色谱法
flow injection analysis 流动注射分析
gel permeation chromatography 凝胶渗透色谱法
flow rate 流速 
fluorescamine 荧胺 general identification test 一般鉴别试验
fluorescence immunoassay(FIA) 荧光免疫分析
general notices (药典)凡例 
general requirements (药典)通则 hydrophilicity 亲水性
hydrophobicity 疏水性 good clinical practices(GCP) 药品临床管理规范
hydroscopic 吸湿的 
hydroxyl value 羟值 good laboratory practices(GLP) 药品实验室管理规范
hyperchromic effect 浓色效应 good manufacturing practices(GMP) 药品生产质量管理
hypochromic effect 淡色效应 规范 
identification 鉴别 good supply practices(GSP) 药品供应管理规范
ignition to constant weight 灼烧至恒重
gradient elution 梯度洗脱 
immobile phase 固定相 grating 光栅 
immunoassay 免疫测定 gravimetric method 重量法 
impurity 杂质 Gutzeit test 古蔡(检砷)法 
inactivation 失活 half peak width 半峰宽
index 索引 [halide] disk method, wafer method, pellet method 压片
法 
indicator 指示剂 head-space concentrating injector 顶空浓缩进样器
indicator electrode 指示电极 
inhibitor 抑制剂 heavy metal 重金属 
injecting septum 进样隔膜胶垫 heat conductivity 热导率 
injection valve 进样阀 height equivalent to a theoretical plate 理论塔板高度
instrumental analysis 仪器分析 height of an effective plate 有效塔板高度insulin assay 胰岛素生物检定法 
integrator 积分仪 high-performance liquid chromatography (HPLC) 高效液
相色谱法 intercept 截距 high-performance thin-layer chromatography (HPTLC) interface 接口 高效薄层色谱法 
interference filter 干涉滤光片 hydrate 水合物 
intermediate 中间体 hydrolysis 水解 
internal standard substance 内标物质Kjeldahl method for nitrogen 凯氏定氮法
international unit(IU) 国际单位 Kober reagent 科伯试剂 in vitro 体外Kovats retention index 科瓦茨保留指数 
in vivo 体内 
labelled amount 标示量 iodide 碘化物 
leading peak 前延峰 iodoform reaction 碘仿反应 
least square method 最小二乘法 iodometry 碘量法 
leveling effect 均化效应 ion-exchange cellulose 离子交换纤维素
licensed pharmacist 执业药师 ion pair chromatography 离子对色谱limit control 限量控制 
limit of detection(LOD) 检测限 ion suppression 离子抑制 
limit of quantitation(LOQ) 定量限 
ionic strength 离子强度
limit test (杂质)限度(或限量)试验
ion-pairing agent 离子对试剂 
ionization 电离，离子化 limutus amebocyte lysate(LAL) 鲎试验
ionization region 离子化区 
linearity and range 线性及范围 irreversible indicator 不可逆指示剂
linearity scanning 线性扫描 irreversible potential 不可逆电位liquid chromatograph/mass spectrometer (LC/MS) 液质 
联用仪 
isoabsorptive point 等吸收点 
litmus paper 石蕊试纸 isocratic elution 等溶剂组成洗脱 
loss on drying 干燥失重 isoelectric point 等电点 
low pressure gradient pump 低压梯度泵
isoosmotic solution 等渗溶液 
isotherm 等温线 luminescence 发光 Karl Fischer titration 卡尔?费歇尔滴定lyophilization 冷冻干燥 
main constituent 主成分 kinematic viscosity 运动黏度 
make-up gas 尾吹气 
maltol reaction 麦牙酚试验 microsyringe 微量注射器
Marquis test 马奎斯试验 migration time 迁移时间 mass analyzer detector 质量分析检测器millipore filtration 微孔过滤 
minimum fill 最低装量 mass spectrometric analysis 质谱分析
mobile phase 流动相 
modifier 改性剂，调节剂 mass spectrum 质谱图 
molecular formula 分子式 mean deviation 平均偏差 
monitor 检测，监测 measuring flask, volumetric flask 量瓶
monochromator 单色器 measuring pipet(te) 刻度吸量管 
monographs 正文 medicinal herb 草药 
mortar 研钵 melting point 熔点 
moving belt interface 传送带接口 
melting range 熔距
multidimensional detection 多维检测
metabolite 代谢物 
multiple linear regression 多元线性回归metastable ion 亚稳离子 
methyl orange 甲基橙 
multivariate calibration 多元校正 methyl red 甲基红 
natural product 天然产物 micellar chromatography 胶束色谱法
Nessler glasses(tube) 奈斯勒比色管
micellar electrokinetic capillary chromatography(MECC, 
Nessler’s reagent 碱性碘化汞钾试液MEKC) 胶束电动毛细管色谱法 
micelle 胶束 
neutralization 中和 microanalysis 微量分析 
nitrogen content 总氮量 microcrystal 微晶 
nonaqueous acid-base titration 非水酸碱滴定
microdialysis 微透析 
micropacked column 微型填充柱 nonprescription drug, over the counter drugs (OTC drugs) 
非处方药 microsome 微粒体 
nonproprietary name, generic name 非专有名
nonspecific impurity 一般杂质 orthogonal test 正交试验
non-volatile matter 不挥发物 orthophenanthroline 邻二氮菲 normal phase 正相 outlier 可疑数据，逸出值 normalization 归一化法 overtones 倍频峰，泛频峰 notice 凡例 oxidation-reduction titration 氧化还原滴定
nujol mull method 石蜡糊法 
oxygen flask combustion 氧瓶燃烧
octadecylsilane chemically bonded silica 十八烷基硅烷
键合硅胶 
packed column 填充柱 octylsilane 辛(烷)基硅烷 
packing material 色谱柱填料 odorless 无臭 
palladium ion colorimetry 钯离子比色法
official name 法定名 
official specifications 法定标准 parallel analysis 平行分析 official test 法定试验 parent ion 母离子
on-column detector 柱上检测器 particulate matter 不溶性微粒 on-column injection 柱头进样 partition coefficient 分配系数 on-line degasser 在线脱气设备 parts per million (ppm) 百万分之几
on the dried basis 按干燥品计 
pattern recognition 模式识别 opalescence 乳浊 
peak symmetry 峰不对称性 open tubular column 开管色谱柱 
peak valley 峰谷 optical activity 光学活性 
peak width at half height 半峰宽 optical isomerism 旋光异构 
percent transmittance 透光百分率optical purity 光学纯度 
optimization function 优化函数 pH indicator absorbance ratio method pH指示剂吸光度
比值法 
organic volatile impurities 有机挥发性杂质
pharmaceutical analysis 药物分析
orthogonal function spectrophotometry 正交函数分光光
度法 pharmacopeia 药典 
pharmacy 药学 prescription drug 处方药
phenolphthalein 酚酞 pretreatment 预处理 photodiode array detector(DAD) 光电二极管阵列检测器primary standard 基准物质 
principal component analysis 主成分分析
photometer 光度计 
pipeclay triangle 泥三角programmed temperature gas chromatography 程序升温 
气相色谱法 pipet(te) 吸移管，精密量取 
prototype drug 原型药物 planar chromatography 平板色谱法
provisions for new drug approval 新药审批办法
plate storage rack 薄层板贮箱 
purification 纯化 polarimeter 旋光计 
purity 纯度 polarimetry 旋光测定法 
pyrogen 热原 polarity 极性 
pycnometric method 比重瓶法polyacrylamide gel 聚丙酰胺凝胶 
quality control(QC) 质量控制 polydextran gel 葡聚糖凝胶 
quality evaluation 质量评价 polystyrene gel 聚苯乙烯凝胶 
quality standard 质量标准 polystyrene film 聚苯乙烯薄膜 
quantitative determination 定量测定 
porous polymer beads 高分子多孔小球
quantitative analysis 定量分析 post-column derivatization 柱后衍生化
quasi-molecular ion 准分子离子 potentiometer 电位计 racemization 消旋化 potentiometric titration 电位滴定法radioimmunoassay 放射免疫分析法
precipitation form 沉淀形式 random sampling 随机抽样 precision 精密度rational use of drug 合理用药 pre-column derivatization 柱前衍生化readily carbonizable substance 易炭化物
preparation 制剂 reagent sprayer 试剂喷雾器 
recovery 回收率 safety 安全性
reference electrode 参比电极 Sakaguchi test 坂口试验 refractive index 折光指数 salt bridge 盐桥 related substance 有关物质 salting out 盐析 relative density 相对密度 sample applicator 点样器 relative intensity 相对强度 sample application 点样 repeatability 重复性 sample on-line pretreatment 试样在线预处理
replicate determination 平行测定 
sampling 取样 reproducibility 重现性 
saponification value 皂化值 residual basic hydrolysis method 剩余碱水解法
saturated calomel electrode(SCE) 饱和甘汞电极
residual liquid junction potential 残余液接电位
selectivity 选择性 residual titration 剩余滴定 separatory funnel 分液漏斗 residue on ignition 炽灼残渣 shoulder peak 肩峰 resolution 分辨率，分离度signal to noise ratio 信噪比 response time 响应时间 significant difference 显著性差异 retention 保留 significant figure 有效数字 reversed phase chromatography 反相色谱法significant level 显著性水平 
significant testing 显著性检验 reverse osmosis 反渗透 
silanophilic interaction 亲硅羟基作用
rider peak 驼峰 
rinse 清洗，淋洗 silica gel 硅胶 robustness 可靠性，稳定性 silver chloride electrode 氯化银电极
routine analysis 常规分析 
similarity 相似性 round 修约(数字) 
simultaneous equations method 解线性方程组法
ruggedness 耐用性 
size exclusion chromatography(SEC) 空间排阻色谱法 standard deviation 标准差
standardization 标定 sodium dodecylsulfate, SDS 十二烷基硫酸钠
standard operating procedure(SOP) 标准操作规程
sodium hexanesulfonate 己烷磺酸钠
standard substance 标准品 
stationary phase coating 固定相涂布sodium taurocholate 牛璜胆酸钠 
sodium tetraphenylborate 四苯硼钠
starch indicator 淀粉指示剂 
statistical error 统计误差 sodium thiosulphate 硫代硫酸钠 
sterility test 无菌试验 solid-phase extraction 固相萃取 
stirring bar 搅拌棒 solubility 溶解度 
stock solution 储备液 solvent front 溶剂前沿 
stoichiometric point 化学计量点 solvophobic interaction 疏溶剂作用
storage 贮藏 specific absorbance 吸收系数 
stray light 杂散光 specification 规格 
substituent 取代基 specificity 专属性 
substrate 底物 specific rotation 比旋度 
sulfate 硫酸盐 specific weight 比重 
sulphated ash 硫酸盐灰分 spiked 加入标准的 
supercritical fluid chromatography(SFC) 超临界流体色谱
法 split injection 分流进样 
support 载体(担体) splitless injection 无分流进样 
suspension 悬浊液 spray reagent (平板色谱中的)显色剂
swelling degree 膨胀度 spreader 铺板机 
symmetry factor 对称因子 stability 稳定性 
syringe pump 注射泵 standard color solution 标准比色液
systematic error 系统误差 
system model 系统模型 thymol 百里酚(麝香草酚)(指示剂)
system suitability 系统适用性 
thymolphthalein 百里酚酞(麝香草酚酞)(指示剂)
tablet 片剂 
tailing factor 拖尾因子 thymolsulfonphthalein ( thymol blue) 百里酚蓝(麝香草酚
蓝)(指示剂) tailing peak 拖尾峰 
titer, titre 滴定度 tailing-suppressing reagent 扫尾剂
time-resolved fluoroimmunoassay 时间分辨荧光免疫法
test of hypothesis 假设检验 
titrant 滴定剂 test solution(TS) 试液 
titration error 滴定误差 tetrazolium colorimetry 四氮唑比色法
titrimetric analysis 滴定分析法 therapeutic drug monitoring(TDM) 治疗药物监测tolerance 容许限 
toluene distillation method 甲苯蒸馏法
thermal analysis 热分析法
thermal conductivity detector 热导检测器toluidine blue 甲苯胺蓝(指示剂)
thermocouple detector 热电偶检测器total ash 总灰分 
total quality control(TQC) 全面质量控制
thermogravimetric analysis(TGA) 热重分析法
traditional drugs 传统药 thermospray interface 热喷雾接口
traditional Chinese medicine 中药
The United States Pharmacopoeia(USP) 美国药典
transfer pipet 移液管 The Pharmacopoeia of Japan(JP) 日本药局方turbidance 混浊 
turbidimetric assay 浊度测定法 thin layer chromatography(TLC) 薄层色谱法
turbidimetry 比浊法 
turbidity 浊度 thiochrome reaction 硫色素反应 
ultracentrifugation 超速离心 three-dimensional chromatogram 三维色谱图
ultrasonic mixer 超生混合器 
ultraviolet irradiation 紫外线照射 xylenol orange 二甲酚橙(指示剂)
undue toxicity 异常毒性 
zigzag scanning 锯齿扫描 uniform design 均匀设计 
zone electrophoresis 区带电泳 uniformity of dosage units 含量均匀度
zwitterions 两性离子 uniformity of volume 装量均匀性(装量差异)zymolysis 酶解作用 
uniformity of weight 重量均匀性(片重差异)
validity 可靠性 
variance 方差 
versus …对…，…与…的关系曲线
viscosity 粘度 
volatile oil determination apparatus 挥发油测定器
volatilization 挥发法 
volumetric analysis 容量分析 
volumetric solution(VS) 滴定液 
vortex mixer 涡旋混合器 
watch glass 表面皿 
wave length 波长 
wave number 波数 
weighing bottle 称量瓶 
weighing form 称量形式 
weights 砝码 
well-closed container 密闭容器 
xylene cyanol blue FF 二甲苯蓝FF(指示剂)
'''
ast =ast.replace('\n','')
lst = []
stt=''
def isChinese(word):
    if '\u4e00'<=word<='\u9fff':
            return True
    return False
for i in range(len(ast)-1):
    if isChinese(ast[i]):
        lst.append(i)
lstt = []
for j in range(len(lst)-3):
    if lst[j+1]-lst[j]==1:
        pass
    else:
        lstt.append(lst[j])
lsttt = []
for k in range(0,len(lstt)-1):
    strr = ast[lstt[k]:lstt[k+1]+1][1:]
    if len(strr)>1 and '(' not in strr and ')' not in strr and ',' not in strr and '，' not in strr:
        lsttt.append(strr)
random.shuffle(lsttt)
dox = docx.Document()
for l in lsttt:
    dox.add_paragraph(l)
dox.save('/Users/mac/Documents/大学文档/药物分析/专业术语.docx')
print(lsttt)