import streamlit as st

# 页面设置
st.set_page_config(
    page_title="学习方法决策助手",
    page_icon="📚",
    layout="centered"
)

# 标题和介绍
st.title("📚 学习方法决策助手")
st.markdown("""
面对不同的学习任务和状态，选择正确的方法是成功的一半。
请回答以下几个问题，让我为你推荐最适合当前情况的学习方法！
""")

# 初始化会话状态
if 'current_step' not in st.session_state:
    st.session_state.current_step = 1
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

def reset_decision():
    """重置决策过程"""
    st.session_state.current_step = 1
    st.session_state.show_result = False

# 决策逻辑
if not st.session_state.show_result:
    # 步骤1: 时间评估
    if st.session_state.current_step == 1:
        st.subheader("⏰ 第一步：时间评估")
        time_available = st.radio(
            "你有一个大于45分钟的不被打扰的时间段吗？",
            ["是，有一段完整时间", "否，只有碎片化时间"],
            key="step1"
        )
        
        col1, col2 = st.columns([1, 1])
        with col2:
            if st.button("下一步", type="primary"):
                if "碎片化" in time_available:
                    # 直接得出结论1
                    st.session_state.recommendation = {
                        "method": "主动回忆法",
                        "icon": "🔄",
                        "description": "这是利用碎片时间最高效的方法。",
                        "steps": [
                            "合上书本或关闭资料",
                            "在脑中或纸上主动回忆刚才学过的关键知识点",
                            "尝试用自己的话解释概念",
                            "回忆不起来时再查看答案"
                        ],
                        "tips": "适合在等车、排队等场景进行，每次5-15分钟。"
                    }
                    st.session_state.show_result = True
                else:
                    st.session_state.current_step = 2
                st.rerun()

    # 步骤2: 目标评估
    elif st.session_state.current_step == 2:
        st.subheader("🎯 第二步：目标评估")
        learning_goal = st.radio(
            "你这次学习的主要目标是什么？",
            ["理解复杂的理论或概念", "记忆事实、公式或程序性知识"],
            key="step2"
        )
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("上一步"):
                st.session_state.current_step = 1
                st.rerun()
        with col2:
            if st.button("下一步", type="primary"):
                if "记忆事实" in learning_goal:
                    # 得出结论2
                    st.session_state.recommendation = {
                        "method": "间隔重复与练习测试法",
                        "icon": "📅",
                        "description": "这是对抗遗忘曲线、强化长期记忆最科学的方法。",
                        "steps": [
                            "使用Anki等间隔重复软件创建闪卡",
                            "按照系统安排的时间进行复习",
                            "多做自测题和模拟考试",
                            "对错误题目进行重点标记"
                        ],
                        "tips": "坚持每天复习比一次长时间学习效果更好。推荐使用Anki或Quizlet。"
                    }
                    st.session_state.show_result = True
                else:
                    st.session_state.current_step = 3
                st.rerun()

    # 步骤3: 状态评估
    elif st.session_state.current_step == 3:
        st.subheader("💪 第三步：状态评估")
        energy_level = st.radio(
            "你当前的精神状态如何？",
            ["精力充沛，注意力集中", "有些疲惫，注意力容易分散"],
            key="step3"
        )
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("上一步"):
                st.session_state.current_step = 2
                st.rerun()
        with col2:
            if st.button("下一步", type="primary"):
                if "精力充沛" in energy_level:
                    # 得出结论3
                    st.session_state.recommendation = {
                        "method": "费曼技巧或深度研读",
                        "icon": "🌟",
                        "description": "在状态最佳时进行深度加工，建立深刻理解。",
                        "steps": [
                            "选择一个你想要理解的概念",
                            "想象你在向一个完全不懂的人解释这个概念",
                            "遇到解释不清的地方，回到原始材料重新学习",
                            "用更简单、更形象的语言重新组织解释"
                        ],
                        "tips": "费曼技巧能暴露你的知识盲点，是检验真理解的黄金标准。"
                    }
                    st.session_state.show_result = True
                else:
                    st.session_state.current_step = 4
                st.rerun()

    # 步骤4: 阶段评估
    elif st.session_state.current_step == 4:
        st.subheader("📖 第四步：阶段评估")
        learning_stage = st.radio(
            "你目前处于哪个学习阶段？",
            ["初次接触这个材料", "复习已经学过的内容"],
            key="step4"
        )
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("上一步"):
                st.session_state.current_step = 3
                st.rerun()
        with col2:
            if st.button("获取推荐", type="primary"):
                if "初次接触" in learning_stage:
                    st.session_state.recommendation = {
                        "method": "康奈尔笔记法",
                        "icon": "📝",
                        "description": "在状态不佳时，用结构化的方式温和地处理新信息。",
                        "steps": [
                            "将页面分为三部分：主笔记区、线索栏、总结栏",
                            "在主笔记区记录主要内容",
                            "在线索栏写下关键问题或关键词",
                            "在总结栏用1-2句话概括本页核心内容"
                        ],
                        "tips": "这种结构迫使你主动组织信息，比被动划线效果好得多。"
                    }
                else:
                    st.session_state.recommendation = {
                        "method": "思维导图",
                        "icon": "🕸️",
                        "description": "通过可视化方式激活和连接已有知识，建立知识网络。",
                        "steps": [
                            "在中心写下主题名称",
                            "创建主要分支表示核心子主题",
                            "添加次级分支填充细节和例子",
                            "使用颜色、图像来增强记忆"
                        ],
                        "tips": "复习时先尝试凭记忆画图，再对照补充遗漏点。"
                    }
                st.session_state.show_result = True
                st.rerun()

# 显示最终推荐结果
if st.session_state.show_result:
    st.success("### 🎉 为你推荐的学习方法")
    
    rec = st.session_state.recommendation
    st.markdown(f"#### {rec['icon']} {rec['method']}")
    st.markdown(f"**为什么推荐这个方法？** {rec['description']}")
    
    st.markdown("**具体操作步骤：**")
    for i, step in enumerate(rec['steps'], 1):
        st.markdown(f"{i}. {step}")
    
    st.info(f"**💡 小贴士：** {rec['tips']}")
    
    st.divider()
    if st.button("🔄 重新开始决策", use_container_width=True):
        reset_decision()
        st.rerun()

# 侧边栏：学习方法库
with st.sidebar:
    st.header("📋 学习方法库")
    
    st.subheader("🔄 主动回忆法")
    st.caption("适合：碎片时间、强化记忆")
    
    st.subheader("📅 间隔重复")
    st.caption("适合：记忆事实、长期保留")
    
    st.subheader("🌟 费曼技巧")
    st.caption("适合：深度理解、检验真知")
    
    st.subheader("📝 康奈尔笔记")
    st.caption("适合：初次学习、信息整理")
    
    st.subheader("🕸️ 思维导图")
    st.caption("适合：知识整合、建立联系")
    
    st.divider()
    st.markdown("💡 **决策原则**")
    st.markdown("""
    - 因时制宜：根据时间选择方法
    - 目标导向：根据学习目的选择
    - 量力而行：根据状态调整策略
    - 主动为上：主动回忆 > 被动阅读
    """)