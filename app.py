import streamlit as st
from data import commands

# 页面配置
st.set_page_config(
    page_title="Linux命令速查助手",
    page_icon="🐧",
    layout="wide"
)

# 自定义CSS
import random

random_cmd = random.choice(commands)

st.info(
    f"📌 今日推荐命令：{random_cmd['name']} → {random_cmd['desc']}"
)
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
        color: #d1d5db;
        margin-bottom: 30px;
    }

    .card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 18px;
        margin-bottom: 18px;
        border: 1px solid #374151;
        transition: 0.2s;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
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
     background-color: #1f2937;
     color: #f9fafb;
     padding: 15px;
     border-radius: 15px;
     text-align: center;
     border: 1px solid #4b5563;
    }
    
    .stats h2 {
        color: #60a5fa;
        margin-bottom: 8px;
    }

    .stats p {
        color: #e5e7eb;
        font-size: 16px;
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
# 初始化搜索历史
if "history" not in st.session_state:
    st.session_state.history = []
# 侧边栏
st.sidebar.title("⚙️ 功能区")
st.sidebar.markdown("---")
st.sidebar.markdown("### 🤖 AI助手")

question = st.sidebar.text_input(
    "描述你的需求"
)
st.sidebar.markdown("---")
st.sidebar.markdown("### 🕒 最近搜索")

for item in st.session_state.history:
    st.sidebar.write(f"• {item}")
categories = ["全部"] + sorted(
    list(set(cmd["category"] for cmd in commands))
)

category = st.sidebar.selectbox(
    "选择分类",
    categories
)

search = st.sidebar.text_input("🔍 搜索命令")
recommended = None

if question:

    best_score = 0

    for cmd in commands:

        score = 0

        for tag in cmd.get("tags", []):

            if tag in question:
                score += 1

        if score > best_score:
            best_score = score
            recommended = cmd
if search and len(search) >= 2:

    if search not in st.session_state.history:

        st.session_state.history.insert(0, search)

        st.session_state.history = st.session_state.history[:5]
st.sidebar.markdown("---")
st.sidebar.markdown("### 🎯 Linux学习路线")

roadmap = [
    "pwd",
    "ls",
    "cd",
    "mkdir",
    "cp",
    "mv",
    "cat",
    "grep",
    "find"
]

for cmd in roadmap:
    st.sidebar.write(f"✅ {cmd}")
# 数据统计
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 数据统计")

st.sidebar.write(f"当前收录命令：{len(commands)}")

category_counts = {}

for cmd in commands:

    cat = cmd["category"]

    if cat not in category_counts:
        category_counts[cat] = 0

    category_counts[cat] += 1

for cat, count in category_counts.items():
    st.sidebar.write(f"{cat}：{count}")

# 数据过滤
filtered_commands = []

if recommended:
    filtered_commands.append(recommended)

else:

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
st.info("💡 可以使用左侧分类或搜索框快速查找命令")
if recommended:

    st.success(
        f"🤖 AI推荐命令：{recommended['name']}"
    )
if question and not recommended:
    st.warning(
        "🤖 暂时没有找到合适的命令，请尝试换一种描述方式"
    )
# 命令卡片
for cmd in filtered_commands:

    with st.container():

        st.subheader(f"🐧 {cmd['name']}")

        st.write(f"📂 分类：{cmd['category']}")

        st.write(f"📝 说明：{cmd['desc']}")

        st.write(f"📈 难度：{cmd.get('level', '⭐')}")

        st.write(
           "🏷️ 标签：" +
           ", ".join(cmd.get("tags", []))
        )

        st.code(
            cmd.get("example", "暂无示例"),
            language="bash"
        )

        # 风险等级
        if cmd["danger"] == "高":
            st.error("⚠️ 高风险命令")

        elif cmd["danger"] == "中":
            st.warning("⚠️ 中风险命令")

        else:
            st.success("✅ 安全命令")

        st.divider()

# 无结果提示
if search and len(filtered_commands) == 0:
    st.warning("没有找到匹配的命令")
