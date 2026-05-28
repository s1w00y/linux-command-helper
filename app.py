import streamlit as st
from data import commands

# 页面配置
st.set_page_config(
    page_title="Linux命令速查助手",
    page_icon="🐧",
    layout="wide"
)

# 自定义CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
    }

    .title {
        font-size: 42px;
        font-weight: bold;
        color: #60a5fa;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 18px;
        color: #9ca3af;
        margin-bottom: 30px;
    }

    .card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 18px;
        margin-bottom: 18px;
        border: 1px solid #374151;
        transition: 0.2s;
    }

    .card:hover {
        border: 1px solid #60a5fa;
        transform: scale(1.01);
    }

    .command-name {
        font-size: 24px;
        font-weight: bold;
        color: #60a5fa;
    }

    .command-desc {
        font-size: 16px;
        color: #d1d5db;
        margin-top: 8px;
    }

    .usage {
        background-color: #111827;
        padding: 12px;
        border-radius: 10px;
        color: #34d399;
        font-family: monospace;
        margin-top: 12px;
    }

    .stats {
        background-color: #111827;
        color:white;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #374151;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 标题
st.markdown('<div class="title">🐧 Linux命令速查助手</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">适合Linux / 生信初学者的命令查询工具</div>',
    unsafe_allow_html=True
)

# 侧边栏
st.sidebar.title("⚙️ 功能区")

category = st.sidebar.selectbox(
    "选择分类",
    ["全部", "Linux命令", "生信命令"]
)

search = st.sidebar.text_input("🔍 搜索命令")

# 数据统计
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 数据统计")

st.sidebar.write(f"当前收录命令：{len(commands)}")

linux_count = sum(
    1 for cmd in commands
    if cmd["category"] == "Linux命令"
)

bio_count = sum(
    1 for cmd in commands
    if cmd["category"] == "生信命令"
)

st.sidebar.write(f"Linux命令：{linux_count}")
st.sidebar.write(f"生信命令：{bio_count}")

# 数据过滤
filtered_commands = []

if search:

    for cmd in commands:

        match_category = (
            category == "全部"
            or cmd["category"] == category
        )

        match_search = (
            search.lower() in cmd["name"].lower()
            or search.lower() in cmd["desc"].lower()
        )

        if match_category and match_search:
            filtered_commands.append(cmd)

# 顶部统计栏
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f'''
        <div class="stats">
        <h2>{len(filtered_commands)}</h2>
        <p>当前结果</p>
        </div>
        ''',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '''
        <div class="stats">
        <h2>🐧</h2>
        <p>Linux学习</p>
        </div>
        ''',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '''
        <div class="stats">
        <h2>🧬</h2>
        <p>生信工具</p>
        </div>
        ''',
        unsafe_allow_html=True
    )

st.markdown("---")
if not search:
    st.info("👈 请在左侧搜索框输入命令")

# 命令卡片
for cmd in filtered_commands:

    st.markdown(
        f'''
        <div class="card">

            <div class="command-name">
                {cmd["name"]}
            </div>

            <div class="command-desc">
                {cmd["desc"]}
            </div>

            <div class="usage">
                {cmd["usage"]}
            </div>

        </div>
        ''',
        unsafe_allow_html=True
    )

# 无结果提示
if search and len(filtered_commands) == 0:
    st.warning("没有找到匹配的命令")
