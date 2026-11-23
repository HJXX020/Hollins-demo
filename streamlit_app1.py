import streamlit as st
import pandas as pd

st.set_page_config(page_title="邻里互助平台Demo", layout="wide")

menu = st.sidebar.selectbox("导航菜单", ["项目介绍", "互助广场", "数据看板", "项目规划"])

if menu == "项目介绍":
    st.title("🏘️ 邻里互助平台")
    st.subheader("以社区为单元，搭建本地资源与需求对接平台")
    st.markdown("""
    ### 项目概述
    打造社区内部的需求-资源匹配平台，分为闲置流转、便民求助、邻里帮扶、社区公告四大板块。
    - ✅ 闲置物品交换流转
    - ✅ 临时求助（代取快递、临时照看等）
    - ✅ 社区公益帮扶
    - ✅ 社区通知公告
    """)
    st.divider()
    st.markdown("**定位：** 轻量化社区治理工具，聚焦熟人社区，低成本落地。")

elif menu == "互助广场":
    st.title("🤝 互助广场｜需求与资源")
    data = pd.DataFrame([
        {"类型":"求助","标题":"帮忙代收快递","小区":"阳光小区","状态":"待接单"},
        {"类型":"闲置","标题":"儿童绘本一套","小区":"阳光小区","状态":"可领取"},
        {"类型":"帮扶","标题":"老人上门义诊志愿","小区":"滨河小区","状态":"招募中"},
        {"类型":"闲置","标题":"折叠书桌","小区":"滨河小区","状态":"可领取"},
    ])
    st.dataframe(data, use_container_width=True)
    st.divider()
    st.subheader("发布一条新需求")
    t1, t2, t3 = st.columns(3)
    with t1:
        kind = st.selectbox("类型", ["求助","闲置","帮扶"])
    with t2:
        title = st.text_input("标题")
    with t3:
        community = st.text_input("所在小区")
    if st.button("提交发布"):
        st.success("✅ 发布成功！（演示版本，仅前端展示）")

elif menu == "数据看板":
    st.title("📊 项目数据看板")
    col1,col2,col3 = st.columns(3)
    col1.metric("累计发布需求","42")
    col2.metric("成功对接","28")
    col3.metric("活跃社区","6")

elif menu == "项目规划":
    st.title("📋 后续迭代规划")
    st.markdown("""
    1. 身份核验：仅限本社区居民加入
    2. 评价体系：互助双方信用评价
    3. 地图板块：就近匹配
    4. 管理员后台：社区运营管理
    """)
