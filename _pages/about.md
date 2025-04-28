---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
# 🙋🏼About Me
Hello! I am Pinglu Zhang (张平路), a master's student at the &nbsp;<img src='./images/uestc.jpg' style='height: 1.5em;'>&nbsp; [Institute of Fundamental and Frontier Sciences (IFFS)](https://www.iffs.uestc.edu.cn/), [University of Electronic Science and Technology of China (UESTC)](https://www.uestc.edu.cn) (电子科技大学，基础与前沿研究院), majoring in Computer Science and Technology. 

I am also part of a joint training program (联合培养) at the &nbsp;<img src='./images/zgc.jpg' style='height: 1.6em;'>&nbsp; [Zhongguancun Academy](http://bjzgca.bjedu.cn)(北京中关村学院).

I am conducting research on [Sequence Alignment](http://lab.malab.cn/~cjt/MSA/) at the [Malab](http://123.57.240.48/forum.php?mod=viewthread&tid=8672) laboratory under the supervision of [Prof. Quan Zou](http://lab.malab.cn/~zq/) (邹权教授). My work focuses on developing multiple sequence alignment for large-scale data, mulitiple genome alignment, centromere region alignment, and related topics <a href='https://scholar.google.com/citations?user=T70BtHMAAAAJ&hl'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>. 

Researchers interested in collaboration are welcome to contact me at [pingluzhang@outlook.com](mailto:pingluzhang@outlook.com).


# 🔥 News
- *2025.02.07*: &nbsp;🎉🎉 New article has been accepted by Genome Research!
- *2024.12.30*: &nbsp;🎉🎉 I have been offered a joint PhD position at [UESTC](https://www.uestc.edu.cn/) and [Zhongguancun Academy](http://bjzgca.bjedu.cn).
- *2024.09.08*: &nbsp;🎉🎉 New Homepage was released! 

# 📝 Publications 
## Selected Publication

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">Genome Research 2025</div>
      <img src='images/RaMA.svg' alt="sym" width="90%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[Fast sequence alignment for centromere with RaMA](https://doi.org/10.1101/gr.279763.124)

**Pinglu Zhang**, Yanming Wei, Qinzhong Tian, Quan Zou, Yansu Wang\*

**Genome Research, 2025, 中科院1区, nature index journal, IF2024=6.24.** 

[**Paper**](https://github.com/metaphysicser/metaphysicser.github.io/blob/main/paper/RaMA.pdf)&nbsp;&nbsp;[**Code**](https://github.com/metaphysicser/RaMA)&nbsp;&nbsp;<strong><span class='show_paper_citations' data='T70BtHMAAAAJ:qjMakFHDy7sC'></span></strong>

- RaMA is a novel sequence alignment tool designed for centromeric regions, leveraging rare matches as anchors and a 2-piece affine gap cost to capture genetic evolution accurately.
- RaMA utilizes parallel computing and the wavefront algorithm, achieving up to 13.66 times faster processing and using only 11% of UniAligner's memory.
- Additionally, RaMA introduces two innovative methods for defining reliable alignment regions, which further refine the accuracy of centromeric alignment statistics and provide more robust insights into genetic variations.
- Downstream analysis of simulated data and HOR arrays demonstrates RaMA's superior accuracy in capturing true HOR structures and defining reliable alignment regions.

</div>
</div>


<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">Bioinformatics 2024</div>
      <img src='images/FMAlign2.png' alt="sym" width="90%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[FMAlign2: a novel fast multiple nucleotide sequence alignment method for ultralong datasets](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btae014/7515251)

**Pinglu Zhang**, Huan Liu, Yanming Wei, Yixiao Zhai, Qinzhong Tian, Quan Zou\*

**Bioinformatics, 2024, 中科院3区, CCF-B, IF2024=4.4.** 

[**Paper**](https://github.com/metaphysicser/metaphysicser.github.io/blob/main/paper/FMAlign2.pdf)&nbsp;&nbsp;[**Code**](https://github.com/malabz/FMAlign2)&nbsp;&nbsp;<strong><span class='show_paper_citations' data='T70BtHMAAAAJ:u-x6o8ySG0sC'></span></strong>

- FMAlign2 is an improved MSA method that uses a suffix array and vertical division strategy to align ultralong sequences in parallel. 
- FMAlign2 reduces processing time while maintaining accuracy, handling sequences up to billions in length efficiently.

</div>
</div>

## Other Publications

- [PS-mixer: A polar-vector and strength-vector mixer model for multimodal sentiment analysis](https://www.sciencedirect.com/science/article/pii/S0306457322003302), H Lin<sup>†</sup>, **P Zhang**<sup>†</sup>, J Ling, Z Yang\*, LK Lee, W Liu. Information Processing & Management, 2023, 中科院1区, CCF-B, IF2023=8.6.&nbsp;&nbsp;[**Paper**](https://github.com/metaphysicser/metaphysicser.github.io/blob/main/paper/PS-Mixer.pdf)&nbsp;&nbsp;[**Code**](https://github.com/metaphysicser/PS-Mixer)&nbsp;&nbsp;<strong><span class='show_paper_citations' data='T70BtHMAAAAJ:u5HHmVD_uO8C'></span></strong>

- [Chimera: Ultrafast and Memory-efficient Database Construction for High-Accuracy Taxonomic Classification in the Age of Expanding Genomic Data](https://www.biorxiv.org/content/10.1101/2025.03.26.645388v1.abstract), Q Tian<sup>†</sup>, **P Zhang**<sup>†</sup>, Y Wei, Q Zou, Y Wang\*, X Luo\*. bioRxiv, 2025.&nbsp;&nbsp;[**Paper**](https://github.com/metaphysicser/metaphysicser.github.io/blob/main/paper/Chimera.pdf)&nbsp;&nbsp;[**Code**](https://github.com/LoadStar822/Chimera)&nbsp;&nbsp;<strong><span class='show_paper_citations' data='T70BtHMAAAAJ:IjCSPb-OGe4C'></span></strong>

- [HAlign-4: A New Strategy for Rapidly Aligning Millions of Sequences](https://doi.org/10.1093/bioinformatics/btae718), T Zhou, **P Zhang**,  Q Zou\*, W Han\*. Bioinformatics, 2024, 中科院3区, CCF-B, IF2024=4.4.&nbsp;&nbsp;[**Paper**](https://github.com/metaphysicser/metaphysicser.github.io/blob/main/paper/HAlign4.pdf)&nbsp;&nbsp;[**Code**](https://github.com/metaphysicser/HAlign-4)&nbsp;&nbsp;<strong><span class='show_paper_citations' data='T70BtHMAAAAJ:2osOgNQ5qMEC'></span></strong>

- [TPMA: A two pointers meta-alignment tool to ensemble different multiple nucleic acid sequence alignments](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011988), Y Zhai, J Chao, Y Wang, **P Zhang**, F Tang\*, Q Zou\*. PLOS Computational Biology, 2024, 中科院2区, CCF-B, IF2024=3.8.&nbsp;&nbsp;[**Paper**](https://github.com/metaphysicser/metaphysicser.github.io/blob/main/paper/TPMA.pdf)&nbsp;&nbsp;[**Code**](https://github.com/malabz/TPMA)&nbsp;&nbsp;<strong><span class='show_paper_citations' data='T70BtHMAAAAJ:d1gkVwhDpl0C'></span></strong>

- [Application and Comparison of Machine Learning and Database-Based Methods in Taxonomic Classification of High-Throughput Sequencing Data](https://academic.oup.com/gbe/article-abstract/16/5/evae102/7674165), Q Tian, **P Zhang**, Y Zhai, Y Wang\*, Q Zou\*. Genome Biology and Evolution, 2024, 中科院2区, IF2024=3.2.&nbsp;&nbsp;[**Paper**](https://github.com/metaphysicser/metaphysicser.github.io/blob/main/paper/sequence%20classification%20survey.pdf)&nbsp;&nbsp;[**Code**](http://lab.malab.cn/~tqz/project/taxonomic/)&nbsp;&nbsp;<strong><span class='show_paper_citations' data='T70BtHMAAAAJ:9yKSN-GCB0IC'></span></strong>

- [TCM@MPXV: A Resource for Treating Monkeypox Patients in Traditional Chinese Medicine](https://www.eurekaselect.com/article/142054), Xin Zhang, Feiran Zhou, **Pinglu Zhang**, Quan Zou\* and Ying Zhang\*. Current Bioinformatics, 2024, 中科院3区, IF2024=2.4.&nbsp;&nbsp;[**Paper**](https://github.com/metaphysicser/metaphysicser.github.io/blob/main/paper/TCM.pdf)&nbsp;&nbsp;<strong><span class='show_paper_citations' data='T70BtHMAAAAJ:UeHWp8X0CEIC'></span></strong>

# 🎖 Honors and Awards
- *2023.09* The First Prize (Ranked 1st Overall) in the CBC Data Challenge (CBC数据挑战赛全国一等奖).
- *2025.03* 电子科技大学优秀研究生和学术青苗.

# 📖 Educations
- *2023.09 - (now)*: Master, [Institute of Fundamental and Frontier Sciences (IFFS)](https://www.iffs.uestc.edu.cn/), [University of Electronic Science and Technology of China (UESTC)](https://www.uestc.edu.cn) (电子科技大学，基础与前沿研究院). &nbsp;<img src='./images/uestc.jpg' style='height: 1.5em;'>&nbsp;

- *2025.03 - (now)*: Master (Joint Program), [Zhongguancun Academy](http://bjzgca.bjedu.cn)(北京中关村学院).<img src='./images/zgc.jpg' style='height: 1.6em;'>&nbsp; 

- *2024.06 - 2025.03*: Master (Joint Program), [Yangtze Delta Region Institute (Quzhou)](http://ydri.uestc.edu.cn), [University of Electronic Science and Technology of China (UESTC)](https://www.uestc.edu.cn) (电子科技大学，长三角研究院). &nbsp;<img src='./images/uestc.jpg' style='height: 1.5em;'>&nbsp; 

- *2019.09 - 2023.06*: Bachelor, [School of Computer Science](http://cs.gdut.edu.cn), [Guangdong University of Technology (GDUT)](http://www.gdut.edu.cn) (广东工业大学，计算机学院). &nbsp;<img src='./images/gdut.png' style='height: 4em;'>&nbsp;


