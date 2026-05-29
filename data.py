commands = [
    {
        "name": "ls",
        "category": "文件与目录",
        "desc": "列出目录内容",
        "example": "ls -lh",
        "danger": "低"
    },
    {
        "name": "cd",
        "category": "文件与目录",
        "desc": "切换目录",
        "example": "cd /home",
        "danger": "低"
    },
    {
        "name": "pwd",
        "category": "文件与目录",
        "desc": "显示当前目录",
        "example": "pwd",
        "danger": "低"
    },
    {
        "name": "mkdir",
        "category": "文件与目录",
        "desc": "创建目录",
        "example": "mkdir test",
        "danger": "低"
    },
    {
        "name": "rm",
        "category": "文件与目录",
        "desc": "删除文件或目录",
        "example": "rm -rf test",
        "danger": "高"
    },
    {
        "name": "cp",
        "category": "文件与目录",
        "desc": "复制文件",
        "example": "cp a.txt b.txt",
        "danger": "中"
    },
    {
        "name": "mv",
        "category": "文件与目录",
        "desc": "移动或重命名文件",
        "example": "mv old.txt new.txt",
        "danger": "中"
    },
    {
        "name": "cat",
        "category": "文件查看",
        "desc": "查看文件内容",
        "example": "cat test.txt",
        "danger": "低"
    },
    {
        "name": "less",
        "category": "文件查看",
        "desc": "分页查看文件",
        "example": "less log.txt",
        "danger": "低"
    },
    {
        "name": "head",
        "category": "文件查看",
        "desc": "查看文件前几行",
        "example": "head -n 10 file.txt",
        "danger": "低"
    },
    {
        "name": "tail",
        "category": "文件查看",
        "desc": "查看文件后几行",
        "example": "tail -f log.txt",
        "danger": "低"
    },
    {
        "name": "grep",
        "category": "文本处理",
        "desc": "搜索文本内容",
        "example": "grep 'error' log.txt",
        "danger": "低"
    },
    {
        "name": "awk",
        "category": "文本处理",
        "desc": "强大的文本处理工具",
        "example": "awk '{print $1}' file.txt",
        "danger": "中"
    },
    {
        "name": "sed",
        "category": "文本处理",
        "desc": "文本替换与编辑",
        "example": "sed 's/old/new/g' file.txt",
        "danger": "中"
    },
    {
        "name": "find",
        "category": "搜索查找",
        "desc": "查找文件",
        "example": "find . -name '*.txt'",
        "danger": "低"
    },
    {
        "name": "chmod",
        "category": "权限管理",
        "desc": "修改文件权限",
        "example": "chmod 755 script.sh",
        "danger": "中"
    },
    {
        "name": "top",
        "category": "系统监控",
        "desc": "查看系统资源",
        "example": "top",
        "danger": "低"
    },
    {
        "name": "ps",
        "category": "进程管理",
        "desc": "查看进程",
        "example": "ps aux",
        "danger": "低"
    },
    {
        "name": "kill",
        "category": "进程管理",
        "desc": "结束进程",
        "example": "kill 1234",
        "danger": "高"
    },
    {
        "name": "ssh",
        "category": "网络命令",
        "desc": "远程连接服务器",
        "example": "ssh user@host",
        "danger": "中"
    },
    {
        "name": "wget",
        "category": "网络命令",
        "desc": "下载文件",
        "example": "wget https://example.com/file.zip",
        "danger": "低"
    },
    {
        "name": "curl",
        "category": "网络命令",
        "desc": "发送网络请求",
        "example": "curl https://example.com",
        "danger": "中"
    },
    {
        "name": "tar",
        "category": "压缩归档",
        "desc": "压缩与解压文件",
        "example": "tar -czvf test.tar.gz test/",
        "danger": "中"
    },
    {
        "name": "samtools",
        "category": "生信工具",
        "desc": "SAM/BAM 文件处理工具",
        "example": "samtools view file.bam",
        "danger": "中"
    },
    {
        "name": "bcftools",
        "category": "生信工具",
        "desc": "VCF/BCF 文件处理工具",
        "example": "bcftools view file.vcf.gz",
        "danger": "中"
    },
]