commands = [
    {
        "name": "ls",
        "category": "文件与目录",
        "desc": "列出目录内容",
        "example": "ls -lh",
        "danger": "低",
        "level":"⭐",
        "tags": ["目录","文件","查看","列表"]
    },
    {
        "name": "cd",
        "category": "文件与目录",
        "desc": "切换目录",
        "example": "cd /home",
        "danger": "低",
        "level":"⭐",
        "tags": ["目录","切换","进入","路径"]
    },
    {
        "name": "pwd",
        "category": "文件与目录",
        "desc": "显示当前目录",
        "example": "pwd",
        "danger": "低",
        "level":"⭐"
    },
    {
        "name": "mkdir",
        "category": "文件与目录",
        "desc": "创建目录",
        "example": "mkdir test",
        "danger": "低",
        "level":"⭐"
    },
    {
        "name": "rm",
        "category": "文件与目录",
        "desc": "删除文件或目录",
        "example": "rm -rf test",
        "danger": "高",
        "level":"⭐⭐"
    },
    {
        "name": "cp",
        "category": "文件与目录",
        "desc": "复制文件",
        "example": "cp a.txt b.txt",
        "danger": "中",
        "level":"⭐⭐"
    },
    {
        "name": "mv",
        "category": "文件与目录",
        "desc": "移动或重命名文件",
        "example": "mv old.txt new.txt",
        "danger": "中",
        "level":"⭐⭐"
    },
    {
        "name": "cat",
        "category": "文件查看",
        "desc": "查看文件内容",
        "example": "cat test.txt",
        "danger": "低",
        "level":"⭐"
    },
    {
        "name": "less",
        "category": "文件查看",
        "desc": "分页查看文件",
        "example": "less log.txt",
        "danger": "低",
        "level":"⭐"
    },
    {
        "name": "head",
        "category": "文件查看",
        "desc": "查看文件前几行",
        "example": "head -n 10 file.txt",
        "danger": "低",
        "level":"⭐⭐"
    },
    {
        "name": "tail",
        "category": "文件查看",
        "desc": "查看文件后几行",
        "example": "tail -f log.txt",
        "danger": "低",
        "level":"⭐⭐"
    },
    {
        "name": "grep",
        "category": "文本处理",
        "desc": "搜索文本内容",
        "example": "grep 'error' log.txt",
        "danger": "低",
        "level":"⭐⭐",
        "tags": ["日志", "搜索", "文本", "查找","关键字"]
    },
    {
        "name": "awk",
        "category": "文本处理",
        "desc": "强大的文本处理工具",
        "example": "awk '{print $1}' file.txt",
        "danger": "中",
        "level":"⭐⭐⭐⭐"
    },
    {
        "name": "sed",
        "category": "文本处理",
        "desc": "文本替换与编辑",
        "example": "sed 's/old/new/g' file.txt",
        "danger": "中",
        "level":"⭐⭐⭐⭐"
    },
    {
        "name": "find",
        "category": "搜索查找",
        "desc": "查找文件",
        "example": "find . -name '*.txt'",
        "danger": "低",
        "level":"⭐⭐⭐",
        "tags": ["文件", "搜索","查找","目录","路径"]
    },
    {
        "name": "chmod",
        "category": "权限管理",
        "desc": "修改文件权限",
        "example": "chmod 755 script.sh",
        "danger": "中",
        "level":"⭐⭐⭐"
    },
    {
        "name": "top",
        "category": "系统监控",
        "desc": "查看系统资源",
        "example": "top",
        "danger": "低",
        "level":"⭐"
    },
    {
        "name": "ps",
        "category": "进程管理",
        "desc": "查看进程",
        "example": "ps aux",
        "danger": "低",
        "level":"⭐⭐"
    },
    {
        "name": "kill",
        "category": "进程管理",
        "desc": "结束进程",
        "example": "kill 1234",
        "danger": "高",
        "level":"⭐⭐"
    },
    {
        "name": "ssh",
        "category": "网络命令",
        "desc": "远程连接服务器",
        "example": "ssh user@host",
        "danger": "中",
        "level":"⭐⭐"
    },
    {
        "name": "wget",
        "category": "网络命令",
        "desc": "下载文件",
        "example": "wget https://example.com/file.zip",
        "danger": "低",
        "level":"⭐⭐⭐"
    },
    {
        "name": "curl",
        "category": "网络命令",
        "desc": "发送网络请求",
        "example": "curl https://example.com",
        "danger": "中",
        "level":"⭐⭐⭐"
    },
    {
        "name": "tar",
        "category": "压缩归档",
        "desc": "压缩与解压文件",
        "example": "tar -czvf test.tar.gz test/",
        "danger": "中",
        "level":"⭐⭐⭐"
    },
    {
        "name": "samtools",
        "category": "生信工具",
        "desc": "SAM/BAM 文件处理工具",
        "example": "samtools view file.bam",
        "danger": "中",
        "level":"⭐⭐⭐⭐",
        "tags": ["bam","sam","测序","比对"]
    },
    {
        "name": "bcftools",
        "category": "生信工具",
        "desc": "VCF/BCF 文件处理工具",
        "example": "bcftools view file.vcf.gz",
        "danger": "中",
        "level":"⭐⭐⭐⭐⭐",
        "tags": ["vcf","变异","snp","基因型"]
    },
    {
    "name": "df",
    "category": "系统监控",
    "desc": "查看磁盘空间使用情况",
    "example": "df -h",
    "danger": "低",
    "level": "⭐",
    "tags": ["磁盘","空间","存储","容量"]
    },
    {
    "name": "du",
    "category": "系统监控",
    "desc": "查看目录或文件占用空间",
    "example": "du -sh *",
    "danger": "低",
    "level": "⭐⭐",
    "tags": ["磁盘","目录大小","空间占用","文件大小"]
    },
    {
    "name": "touch",
    "category": "文件与目录",
    "desc": "创建空文件",
    "example": "touch test.txt",
    "danger": "低",
    "level": "⭐"
    },
    {
    "name": "echo",
    "category": "文本处理",
    "desc": "输出文本",
    "example": "echo Hello",
    "danger": "低",
    "level": "⭐"
    },
    {
    "name": "man",
    "category": "帮助命令",
    "desc": "查看命令手册",
    "example": "man grep",
    "danger": "低",
    "level": "⭐"
    },
    {
    "name": "which",
    "category": "帮助命令",
    "desc": "查找命令路径",
    "example": "which python",
    "danger": "低",
    "level": "⭐"
    },
    {
    "name": "whereis",
    "category": "帮助命令",
    "desc": "查找程序相关文件",
    "example": "whereis python",
    "danger": "低",
    "level": "⭐⭐"
    },
    {
    "name": "history",
    "category": "Shell",
    "desc": "查看历史命令",
    "example": "history",
    "danger": "低",
    "level": "⭐"
    },
    {
    "name": "nano",
    "category": "文本编辑",
    "desc": "终端文本编辑器",
    "example": "nano test.txt",
    "danger": "低",
    "level": "⭐⭐"
    },
    {
    "name": "vim",
    "category": "文本编辑",
    "desc": "高级文本编辑器",
    "example": "vim test.txt",
    "danger": "低",
    "level": "⭐⭐⭐⭐"
    },
    {
    "name": "sort",
    "category": "文本处理",
    "desc": "排序文本内容",
    "example": "sort file.txt",
    "danger": "低",
    "level": "⭐⭐"
    },
    {
    "name": "uniq",
    "category": "文本处理",
    "desc": "去除重复行",
    "example": "uniq file.txt",
    "danger": "低",
    "level": "⭐⭐"
    },
    {
    "name": "cut",
    "category": "文本处理",
    "desc": "提取指定列",
    "example": "cut -f1 file.txt",
    "danger": "低",
    "level": "⭐⭐⭐"
    },
    {
    "name": "wc",
    "category": "文本处理",
    "desc": "统计行数、单词数和字符数",
    "example": "wc -l file.txt",
    "danger": "低",
    "level": "⭐"
    },
    {
    "name": "fastqc",
    "category": "生信工具",
    "desc": "测序数据质量控制",
    "example": "fastqc sample.fastq.gz",
    "danger": "低",
    "level": "⭐⭐"
    },
    {
    "name": "bwa",
    "category": "生信工具",
    "desc": "序列比对工具",
    "example": "bwa mem ref.fa reads.fq > aln.sam",
    "danger": "中",
    "level": "⭐⭐⭐⭐"
    },
    {
    "name": "hisat2",
    "category": "生信工具",
    "desc": "RNA-seq比对工具",
    "example": "hisat2 -x genome -U reads.fq",
    "danger": "中",
    "level": "⭐⭐⭐⭐"
    },
    {
    "name": "plink",
    "category": "生信工具",
    "desc": "群体遗传学分析工具",
    "example": "plink --vcf data.vcf",
    "danger": "中",
    "level": "⭐⭐⭐",
    "tags": ["GWAS","群体遗传","PCA","关联分析"]
    },
    {
    "name": "vcftools",
    "category": "生信工具",
    "desc": "VCF文件分析工具",
    "example": "vcftools --vcf test.vcf",
    "danger": "中",
    "level": "⭐⭐⭐"
    },
    {
    "name": "bedtools",
    "category": "生信工具",
    "desc": "基因组区间分析工具",
    "example": "bedtools intersect -a A.bed -b B.bed",
    "danger": "中",
    "level": "⭐⭐⭐⭐"
    },
    {
    "name": "gzip",
    "category": "压缩归档",
    "desc": "压缩文件",
    "example": "gzip file.txt",
    "danger": "低",
    "level": "⭐⭐"
    },
    {
    "name": "gunzip",
    "category": "压缩归档",
    "desc": "解压gz文件",
    "example": "gunzip file.txt.gz",
    "danger": "低",
    "level": "⭐⭐"
    },
    {
    "name": "zip",
    "category": "压缩归档",
    "desc": "创建zip压缩包",
    "example": "zip test.zip file.txt",
    "danger": "低",
    "level": "⭐⭐"
    },
    {
    "name": "unzip",
    "category": "压缩归档",
    "desc": "解压zip文件",
    "example": "unzip test.zip",
    "danger": "低",
    "level": "⭐⭐"
    },
    {
    "name": "sudo",
    "category": "权限管理",
    "desc": "以管理员权限执行命令",
    "example": "sudo apt update",
    "danger": "高",
    "level": "⭐⭐"
    },
    {
    "name": "chown",
    "category": "权限管理",
    "desc": "修改文件所有者",
    "example": "chown user:user file.txt",
    "danger": "中",
    "level": "⭐⭐⭐"
    },
    {
    "name": "uname",
    "category": "系统监控",
    "desc": "查看系统信息",
    "example": "uname -a",
    "danger": "低",
    "level": "⭐"
    },
    {
    "name": "free",
    "category": "系统监控",
    "desc": "查看内存使用情况",
    "example": "free -h",
    "danger": "低",
    "level": "⭐"
    },
    {
    "name": "ping",
    "category": "网络命令",
    "desc": "测试网络连通性",
    "example": "ping google.com",
    "danger": "低",
    "level": "⭐"
    },
    {
    "name": "scp",
    "category": "网络命令",
    "desc": "远程传输文件",
    "example": "scp file.txt user@host:/home",
    "danger": "中",
    "level": "⭐⭐⭐"
    },
    {
    "name": "admixture",
    "category": "生信工具",
    "desc": "群体结构分析",
    "example": "admixture data.bed 3",
    "danger": "中",
    "level": "⭐⭐⭐⭐",
    "bio_level": "进阶"
    },
    {
    "name": "iqtree",
    "category": "生信工具",
    "desc": "系统发育树构建",
    "example": "iqtree -s aln.fa",
    "danger": "中",
    "level": "⭐⭐⭐⭐",
    "bio_level": "进阶"
    },
    {
    "name": "beagle",
    "category": "生信工具",
    "desc": "基因型填充与相位推断",
    "example": "beagle gt=data.vcf",
    "danger": "中",
    "level": "⭐⭐⭐⭐",
    "bio_level": "高级"
    },
    {
    "name": "relate",
    "category": "生信工具",
    "desc": "全基因组家谱推断",
    "example": "Relate --mode All",
    "danger": "中",
    "level": "⭐⭐⭐⭐⭐",
    "bio_level": "高级",
    "tags": ["ARG","家谱","祖先重组","群体遗传","选择信号"]
    },
]