## 说明
1.all_figure.table.py  检索latex文本中的图表

2.find_duplicate.py 查找bibtex中的重复文献

3.replace_cite_key.py 将重复文件的引用统一

4.replace_de_di.py 不太靠谱的副词形容词检查（不靠谱）

5.test.py ltp包的demo

6.update.py 使用dblp的api更新bibtex文件中的文献条目

## How to use
```
1. update.py
2. manual check --> will automatic
    1 check matches
    2 remove kv--> use vscode rematch
        url  doi  biburl
        -->\n\s+url\s*=\s*([\s\S]*?)
            \n\s+doi\s*=\s*([\s\S]*?)
            \n\s+biburl\s*=\s*([\s\S]*?)
    3 format the booktitle use vscode rematch and match
        re:
        \s+booktitle\s*=\s*\{.*Computer Vision and Pattern([\s\S]*?)\},\n -->\n  booktitle = {{IEEE} Conference on Computer Vision and Pattern Recognition},\n
        \s+booktitle\s*=\s*\{.*International Conference on Computer Vision([\s\S]*?)\},\n -->\n  booktitle = {{IEEE} International Conference on Computer Vision},\n
        \s*publisher\s*=\s* \{.*IEEE.*\},\n -->\n  publisher = {{IEEE}},\n
        \s+booktitle\s*=\s*\{.*Neural Information Processing Systems([\s\S]*?)\},\n -->\n  booktitle = {Advances in Neural Information Processing Systems},\n
        \s+booktitle\s*=\s*\{.*International Conference on Learning Representations([\s\S]*?)\},\n -->\n  booktitle = {International Conference on Learning Representations},\n
        \s+booktitle\s*=\s*\{.*International Conference on Weblogs([\s\S]*?)\},\n
        \s+booktitle\s*=\s*\{.*Conference on Information and Knowledge([\s\S]*?)\},\n
        \s+booktitle\s*=\s*\{.*European Conference([\s\S]*?)\},\n

        match:
        Int. J. Comput. Vis. --> International Journal of Computer Vision
        Trans. Multim. --> Transactions on Multimedia
        Trans. Image Process. --> Transactions on Image Processing
        Trans. Pattern Anal. Mach. Intell. --> Transactions on Pattern Analysis and Machine Intelligence
        Trans. Affect. Comput. --> Transactions on Affective Computing
        Trans. Vis. Comput. Graph. --> Transactions on Visualization and Computer Graphics
        Trans. Inf. Forensics Secur. --> Transactions on Information Forensics and Security
        Trans. Neural Networks --> Transactions on Neural Networks
        Pattern Recognit. --> Pattern Recognition
        Future Gener. Comput. Syst. --> Future Generation Computer Systems
        Expert Syst. Appl. --> Expert Systems with Applications
        Comput. Speech Lang. --> Computer Speech & Language
        Knowl. Based Syst. --> Knowledge-Based Systems
        Comput. Graph. Forum --> Computer Graphics Forum
        Signal Process. --> Signal Processing
        Multim. Tools Appl. --> Multimedia Tools and Applications

3. find_duplicate.py
4. replace_cite_key
