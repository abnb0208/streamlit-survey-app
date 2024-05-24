import streamlit as st
import pandas as pd

# 初始化数据存储
if 'data' not in st.session_state:
    st.session_state.data = []

if 'page' not in st.session_state:
    st.session_state.page = 0

def next_page():
    st.session_state.page += 1

def previous_page():
    st.session_state.page -= 1

# 定义问卷调查表单
def survey_form():
    pages = [
        "第一部分：基本信息",
        "第二部分：网上购物行为",
        "第三部分：信息共享偏好",
        "第四部分：新产品设计反馈",
        "第五部分：消费者行为与新产品设计",
        "第六部分：联系方式"
    ]

    st.header("零售平台信息共享策略与新产品设计调查")
    st.progress(st.session_state.page / (len(pages) - 1))

    with st.form("survey_form"):
        if st.session_state.page == 0:
            st.subheader(pages[0])
            age = st.selectbox("您的年龄是？", ["18岁以下", "18-24岁", "25-34岁", "35-44岁", "45-54岁", "55-64岁", "65岁及以上"])
            gender = st.selectbox("您的性别是？", ["男", "女", "不愿透露"])
            occupation = st.selectbox("您的职业是？", ["学生", "在职", "自由职业", "失业", "退休"])
            income = st.selectbox("您的年收入是？", ["2万元以下", "2万-4万元", "4万-6万元", "6万-8万元", "8万-10万元", "10万元及以上"])
            st.session_state.update({
                'age': age,
                'gender': gender,
                'occupation': occupation,
                'income': income
            })
        
        elif st.session_state.page == 1:
            st.subheader(pages[1])
            shopping_freq = st.selectbox("您多久进行一次网上购物？", ["每天", "每周", "每月", "偶尔", "从不"])
            product_type = st.selectbox("您通常购买哪些类型的商品？", ["电子产品", "服装和配饰", "家用电器", "日用百货", "书籍", "美妆和个人护理", "食品和饮料"])
            platform = st.selectbox("您经常使用哪些零售平台？", ["淘宝", "京东", "拼多多", "苏宁易购", "亚马逊"])
            st.session_state.update({
                'shopping_freq': shopping_freq,
                'product_type': product_type,
                'platform': platform
            })

        elif st.session_state.page == 2:
            st.subheader(pages[2])
            data_collect = st.selectbox("您是否知道零售平台会收集并利用您的数据进行新产品设计？", ["是", "否"])
            sharing_attitude = st.selectbox("您对共享个人数据给零售平台用于新产品设计的态度如何？", ["非常乐意", "较为乐意", "中立", "不太乐意", "非常不乐意"])
            data_type = st.selectbox("您愿意共享哪些类型的数据给零售平台？", ["购买记录", "浏览记录", "产品评价和反馈", "个人偏好（如颜色、风格）", "人口统计信息（如年龄、性别）", "以上都不愿意"])
            data_concern = st.selectbox("您对共享数据给零售平台的主要担忧是什么？", ["隐私和安全", "数据滥用", "缺乏透明度", "定向广告", "没有担忧"])
            st.session_state.update({
                'data_collect': data_collect,
                'sharing_attitude': sharing_attitude,
                'data_type': data_type,
                'data_concern': data_concern
            })

        elif st.session_state.page == 3:
            st.subheader(pages[3])
            feedback_freq = st.selectbox("您多常参与产品评价或反馈？", ["每次都会", "经常", "有时", "很少", "从不"])
            feedback_important = st.selectbox("您认为您的反馈在新产品设计中是否被重视？", ["是", "否", "不确定"])
            feedback_incentive = st.selectbox("什么会激励您提供更多的产品反馈？", ["激励措施（如折扣、奖励）", "简单快捷的反馈流程", "数据隐私保障", "看到反馈对产品的改进效果"])
            feedback_importance = st.selectbox("您认为根据消费者反馈和数据设计的新产品有多重要？", ["非常重要", "重要", "一般", "不太重要", "完全不重要"])
            st.session_state.update({
                'feedback_freq': feedback_freq,
                'feedback_important': feedback_important,
                'feedback_incentive': feedback_incentive,
                'feedback_importance': feedback_importance
            })

        elif st.session_state.page == 4:
            st.subheader(pages[4])
            product_pref = st.selectbox("您更倾向于购买哪些类别的新产品？", ["创新电子产品", "新款服饰", "升级版家电", "健康食品", "美妆新品", "环保产品"])
            product_feature = st.selectbox("您希望新产品具备哪些特点？", ["高性价比", "独特设计", "高科技含量", "环保材料", "用户友好", "多功能性"])
            info_sharing_strategy = st.selectbox("您认为零售平台应如何改进其信息共享策略，以更好地服务消费者？", ["提供更透明的数据使用政策", "加强数据安全措施", "提供数据共享的选择权", "增加消费者数据使用的奖励"])
            st.session_state.update({
                'product_pref': product_pref,
                'product_feature': product_feature,
                'info_sharing_strategy': info_sharing_strategy
            })

        elif st.session_state.page == 5:
            st.subheader(pages[5])
            contact = st.selectbox("您是否愿意留下联系方式以便我们后续与您联系？", ["愿意", "不愿意"])
            phone = ""
            if contact == "愿意":
                phone = st.text_input("电话号码：")

            submit = st.form_submit_button("提交")
            if submit:
                st.session_state.data.append({
                    "年龄": st.session_state.get('age', ''),
                    "性别": st.session_state.get('gender', ''),
                    "职业": st.session_state.get('occupation', ''),
                    "年收入": st.session_state.get('income', ''),
                    "网上购物频率": st.session_state.get('shopping_freq', ''),
                    "购买商品类型": st.session_state.get('product_type', ''),
                    "常用零售平台": st.session_state.get('platform', ''),
                    "知道数据收集": st.session_state.get('data_collect', ''),
                    "数据共享态度": st.session_state.get('sharing_attitude', ''),
                    "愿意共享的数据类型": st.session_state.get('data_type', ''),
                    "数据共享担忧": st.session_state.get('data_concern', ''),
                    "参与评价频率": st.session_state.get('feedback_freq', ''),
                    "反馈重视程度": st.session_state.get('feedback_important', ''),
                    "提供更多反馈的激励": st.session_state.get('feedback_incentive', ''),
                    "消费者反馈重要性": st.session_state.get('feedback_importance', ''),
                    "倾向购买的新产品类别": st.session_state.get('product_pref', ''),
                    "希望新产品具备的特点": st.session_state.get('product_feature', ''),
                    "改进信息共享策略": st.session_state.get('info_sharing_strategy', ''),
                    "愿意留下联系方式": contact,
                    "电话号码": phone
                })
                st.success("感谢您的参与！")

        col1, col2 = st.columns(2)
        if st.session_state.page > 0:
            if col1.form_submit_button("上一步"):
                previous_page()

        if st.session_state.page < len(pages) - 1:
            if col2.form_submit_button("下一步"):
                next_page()

# 显示问卷调查表单
survey_form()

# 数据保存和可视化
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.write("### 当前已收集的数据")
    st.dataframe(df)

    # 下载数据
    csv = df.to_csv(index=False)
    st.download_button(
        label="下载数据为CSV",
        data=csv,
        file_name='survey_data.csv',
        mime='text/csv',
    )
