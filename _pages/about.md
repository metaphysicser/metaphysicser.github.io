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

<script>
  async function loadCitationData() {
  try {
    const response = await fetch('https://github.com/metaphysicser/metaphysicser.github.io/raw/google-scholar-stats/gs_data.json'); // 替换为你的 GitHub Pages URL

    if (!response.ok) {
      throw new Error("Failed to load JSON data");
    }

    const data = await response.json();
    const publications = data.publications;

    // 遍历每篇文章的引用数据
    for (const pubId in publications) {
      const publication = publications[pubId];
      const numCitations = publication.num_citations;
      const citedbyUrl = publication.citedby_url;

      // 找到页面上的引用元素并更新其内容
      const citationElement = document.querySelector(`.show_paper_citations[data='${pubId}']`);
      if (citationElement) {
        citationElement.innerHTML = `<a href="${citedbyUrl}" target="_blank">${numCitations} citations</a>`;
      } else {
        console.error(`Element with data attribute '${pubId}' not found.`);
      }
    }
  } catch (error) {
    console.error("Error loading citation data:", error);
  }
}

// 页面加载时调用函数
window.onload = loadCitationData;
</script>

<span class='anchor' id='about-me'></span>
# 🙋🏼About Me
Hello! I am Pinglu Zhang (张平路), a master's student at the &nbsp;<img src='./images/uestc.jpg' style='height: 1.5em;'>&nbsp; [Institute of Fundamental and Frontier Sciences (IFFS)](https://www.iffs.uestc.edu.cn/), [University of Electronic Science and Technology of China (UESTC)](https://www.uestc.edu.cn) (电子科技大学，基础与前沿研究院), majoring in Computer Science and Technology. 

I am also part of a joint training program (联合培养) at the &nbsp;<img src='./images/uestc.jpg' style='height: 1.5em;'>&nbsp; [Yangtze Delta Region Institute (Quzhou)](http://ydri.uestc.edu.cn), [University of Electronic Science and Technology of China (UESTC)](https://www.uestc.edu.cn) (电子科技大学，长三角研究院).

I am conducting research on [Sequence Alignment](http://lab.malab.cn/~cjt/MSA/) at the [Malab](http://123.57.240.48/forum.php?mod=viewthread&tid=8672) laboratory under the supervision of [Prof. Quan Zou](http://lab.malab.cn/~zq/) (邹权教授). My work focuses on developing multiple sequence alignment for large-scale data, centromere region alignment, and related topics <a href='https://scholar.google.com/citations?user=T70BtHMAAAAJ&hl'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>. 

Researchers interested in collaboration are welcome to contact me at [pingluzhang@outlook.com](mailto:pingluzhang@outlook.com).


# 🔥 News
- *2024.09.08*: &nbsp;🎉🎉 New Homepage was released! 

# 📝 Publications 
## Selected Publication

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">Bioinformatics 2024</div>
      <img src='images/FMAlign2.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[FMAlign2: a novel fast multiple nucleotide sequence alignment method for ultralong datasets](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btae014/7515251)

**Pinglu Zhang**, Huan Liu, Yanming Wei, Yixiao Zhai, Qinzhong Tian, Quan Zou\*

**Bioinformatics, 2024, CCF-B, IF2023=4.4, Q1.** 

[**Paper**](https://scholar.google.com.hk/citations?view_op=view_citation&hl=zh-CN&user=T70BtHMAAAAJ&citation_for_view=T70BtHMAAAAJ:u-x6o8ySG0sC)&nbsp;&nbsp;[**Code**](https://github.com/malabz/FMAlign2)&nbsp;&nbsp;**Citations:** <strong><span class='show_paper_citations' data='T70BtHMAAAAJ:u-x6o8ySG0sC'></span></strong>

<div>
  <strong>Citations:</strong> <strong><span class='show_paper_citations' data='T70BtHMAAAAJ:u-x6o8ySG0sC'>Loading...</span></strong>
</div>

- FMAlign2 is an improved MSA method that uses a suffix array and vertical division strategy to align ultralong sequences in parallel. 
- FMAlign2 reduces processing time while maintaining accuracy, handling sequences up to billions in length efficiently.

</div>
</div>

## Other Publications

- [PS-mixer: A polar-vector and strength-vector mixer model for multimodal sentiment analysis](https://www.sciencedirect.com/science/article/pii/S0306457322003302), H Lin<sup>†</sup>, **P Zhang**<sup>†</sup>, J Ling, Z Yang\*, LK Lee, W Liu. Information Processing & Management, 2023, CCF-B, IF2022=8.6, Q1.&nbsp;&nbsp;[**Paper**](https://www.sciencedirect.com/science/article/abs/pii/S0306457322003302)&nbsp;&nbsp;[**Code**](https://github.com/metaphysicser/PS-Mixer)&nbsp;&nbsp;**Citations**: <strong><span class='show_paper_citations' data='T70BtHMAAAAJ:u5HHmVD_uO8C'></span></strong>

- [TPMA: A two pointers meta-alignment tool to ensemble different multiple nucleic acid sequence alignments](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011988), Y Zhai, J Chao, Y Wang, **P Zhang**, F Tang\*, Q Zou\*. PLOS Computational Biology, 2024, CCF-B, IF2023=3.8, Q1.&nbsp;&nbsp;[**Paper**](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011988)&nbsp;&nbsp;[**Code**](https://github.com/malabz/TPMA)&nbsp;&nbsp;**Citations**: <strong><span class='show_paper_citations' data='T70BtHMAAAAJ:d1gkVwhDpl0C'></span></strong>

- [Application and Comparison of Machine Learning and Database-Based Methods in Taxonomic Classification of High-Throughput Sequencing Data](https://academic.oup.com/gbe/article-abstract/16/5/evae102/7674165), Q Tian, **P Zhang**, Y Zhai, Y Wang, Q Zou\*. Genome Biology and Evolution, 2024, IF2023=3.2, Q2.&nbsp;&nbsp;[**Paper**](https://academic.oup.com/gbe/article/16/5/evae102/7674165)&nbsp;&nbsp;[**Code**](http://lab.malab.cn/~tqz/project/taxonomic/)&nbsp;&nbsp;**Citations**: <strong><span class='show_paper_citations' data='T70BtHMAAAAJ:9yKSN-GCB0IC'></span></strong>

- [TCM@MPXV: A Resource for Treating Monkeypox Patients in Traditional Chinese Medicine](https://www.eurekaselect.com/article/142054), Xin Zhang, Feiran Zhou, **Pinglu Zhang**, Quan Zou\* and Ying Zhang\*. Current Bioinformatics, 2024, IF2023=2.4, Q2.&nbsp;&nbsp;

# 🎖 Honors and Awards
- *2023.09* The First Prize (Ranked 1st Overall) in the CBC Data Challenge (CBC数据挑战赛全国一等奖).

# 📖 Educations
- *2023.09 - (now)*: Master, [Institute of Fundamental and Frontier Sciences (IFFS)](https://www.iffs.uestc.edu.cn/), [University of Electronic Science and Technology of China (UESTC)](https://www.uestc.edu.cn) (电子科技大学，基础与前沿研究院). &nbsp;<img src='./images/uestc.jpg' style='height: 1.5em;'>&nbsp;

- *2024.06 - (now)*: Master (Joint Program), [Yangtze Delta Region Institute (Quzhou)](http://ydri.uestc.edu.cn), [University of Electronic Science and Technology of China (UESTC)](https://www.uestc.edu.cn) (电子科技大学，长三角研究院). &nbsp;<img src='./images/uestc.jpg' style='height: 1.5em;'>&nbsp; 

- *2019.09 - 2023.06*: Bachelor, [School of Computer Science](http://cs.gdut.edu.cn), [Guangdong University of Technology (GDUT)](http://www.gdut.edu.cn) (广东工业大学，计算机学院). &nbsp;<img src='./images/gdut.png' style='height: 4em;'>&nbsp;


