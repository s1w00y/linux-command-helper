import streamlit as st

st.title("🐧 Linux命令速查助手")
category = st.sidebar.selectbox(
    "选择分类",
    ["全部", "Linux命令", "生信命令"]
)

commands = {
    "删除文件": {
        "cmd": "rm file.txt",
        "desc": "删除指定文件",
        "example": "rm result.txt",
        "category": "Linux命令"
    },

    "复制文件": {
        "cmd": "cp source.txt target.txt",
        "desc": "复制文件到新的位置",
        "example": "cp data.txt backup.txt",
        "category": "Linux命令"
    },
    "移动文件": {
    "cmd": "mv old.txt new.txt",
    "desc": "移动或重命名文件",
    "example": "mv data.txt backup/data.txt",
    "category": "Linux命令"
},
    "查看目录": {
    "cmd": "ls -l",
    "desc": "列出当前目录所有文件和详细信息",
    "example":"ls -lh",
    "category": "Linux命令"
},
    "查看当前路径": {
    "cmd": "pwd",
    "desc": "显示当前所在目录",
    "example": "pwd",
    "category": "Linux命令"
},
    "查找文件": {
    "cmd": "find . -name '*.txt'",
    "desc": "递归搜索txt文件",
    "example": "find . -name '*.vcf.gz'",
    "category": "Linux命令"
},
    "查看目录大小": {
    "cmd": "du -sh *",
    "desc": "查看每个文件夹占用空间",
    "example": "du -sh results/",
    "category": "Linux命令"
},
    "创建目录": {
    "cmd": "mkdir myfolder",
    "desc": "创建新目录",
    "example": "mkdir project_data",
    "category": "Linux命令"
},
    "查看VCF头部": {
    "cmd": "bcftools view file.vcf.gz | head",
    "desc": "查看VCF文件前几行",
    "example": "bcftools view horse.vcf.gz | head",
    "category": "生信命令"
},
    "统计VCF样本数": {
    "cmd": "bcftools query -l file.vcf.gz | wc -l",
    "desc": "统计VCF中的样本数量",
    "example": "bcftools query -l horse.vcf.gz | wc -l",
    "category": "生信命令"
},
    "统计FASTA信息": {
    "cmd": "seqkit stats genome.fa",
    "desc": "统计序列数、长度和GC含量",
    "example": "seqkit stats horse.fa",
    "category": "生信命令"
}
}
st.sidebar.write(
    f"当前收录 {len(commands)} 条命令"
)

question = st.text_input("你想做什么？")

if question != "":

    found = False

    for key in commands:

        if category != "全部":

             if commands[key]["category"] != category:
                 continue

        if question in key:

            found = True

            st.success(key)

            st.code(
                commands[key]["cmd"],
                language="bash"
            )
            st.write("说明：")
            st.write(
                commands[key]["desc"]
            )
            st.write("示例：")
            st.code(
    commands[key]["example"],
    language="bash"
)

    if not found:

        st.warning(
            "暂时没有收录这个命令"
        )
