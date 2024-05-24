import streamlit as st
import pandas as pd
import os

# 自定义CSS样式
st.markdown("""
    <style>
    div.row-widget.stRadio > div{flex-direction:column;}
    div.stRadio > label > div[data-baseweb="radio"] > div:first-child {
        background-color: white;
        border: 2px solid gray;
        border-radius: 50%;
    }
    div.stRadio > label > div[data-baseweb="radio"]:hover > div:first-child {
        background-color: lightgray;
    }
    div.stRadio > label > div[data-baseweb="radio"] > div:first-child > div {
        background-color: white;
        border-radius: 50%;
    }
    div.stRadio > label > div[data-baseweb="radio"][aria-checked="true"] > div:first-child {
        background-color: green;
        border: 2px solid green;
    }
    .success-message {
        text-align: center;
        font-size: 24px;
        color: green;
    }
    </style>
    """, unsafe_allow_html=True)

# 定义数据文件路径
data_file = 'survey_data.csv'

# 初始化数据存储
if not os.path.exists(data_file):
    df = pd.DataFrame(columns=[
        "年龄", "性别", "职业", "年收入", "网上购物频率", "购买商品类型", 
        "常用零售平台", "知道数据收集", "数据共享态度", "愿意共享的数据类型", 
        "数据共享担忧", "参与评价频率", "反馈重视程度", "提供更多反馈的激励", 
        "消费者反馈重要性", "倾向购买的新产品类别", "希望新产品具备的特点", 
        "改进信息共享策略", "愿意留下联系方式", "电话号码"
    ])
    df.to_csv(data_file, index=False)

# 初始化页面存储
if 'page' not in st.session_state:
    st.session_state.page = 0

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# 定义下一页和上一页函数
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
            age_options = ["18岁以下", "18-24岁", "25-34岁", "35-44岁", "45-54岁", "55-64岁", "65岁及以上"]
            gender_options = ["男", "女", "不愿透露"]
            occupation_options = ["学生", "在职", "自由职业", "失业", "退休"]
            income_options = ["2万元以下", "2万-4万元", "4万-6万元", "6万-8万元", "8万-10万元", "10万元及以上"]
            
            age_index = st.session_state.get('age_index', 0)
            gender_index = st.session_state.get('gender_index', 0)
            occupation_index = st.session_state.get('occupation_index', 0)
            income_index = st.session_state.get('income_index', 0)
            
            st.session_state.age = st.radio("您的年龄是？", age_options, index=age_index)
            st.session_state.gender = st.radio("您的性别是？", gender_options, index=gender_index)
            st.session_state.occupation = st.radio("您的职业是？", occupation_options, index=occupation_index)
            st.session_state.income = st.radio("您的年收入是？", income_options, index=income_index)
            
            st.session_state.update({
                'age_index': age_options.index(st.session_state.age),
                'gender_index': gender_options.index(st.session_state.gender),
                'occupation_index': occupation_options.index(st.session_state.occupation),
                'income_index': income_options.index(st.session_state.income)
            })
        
        elif st.session_state.page == 1:
            st.subheader(pages[1])
            shopping_freq_options = ["每天", "每周", "每月", "偶尔", "从不"]
            product_type_options = ["电子产品", "服装和配饰", "家用电器", "日用百货", "书籍", "美妆和个人护理", "食品和饮料"]
            platform_options = ["淘宝", "京东", "拼多多", "苏宁易购", "亚马逊"]
            
            shopping_freq_index = st.session_state.get('shopping_freq_index', 0)
            product_type_index = st.session_state.get('product_type_index', 0)
            platform_index = st.session_state.get('platform_index', 0)
            
            st.session_state.shopping_freq = st.radio("您多久进行一次网上购物？", shopping_freq_options, index=shopping_freq_index)
            st.session_state.product_type = st.radio("您通常购买哪些类型的商品？", product_type_options, index=product_type_index)
            st.session_state.platform = st.radio("您经常使用哪些零售平台？", platform_options, index=platform_index)
            
            st.session_state.update({
                'shopping_freq_index': shopping_freq_options.index(st.session_state.shopping_freq),
                'product_type_index': product_type_options.index(st.session_state.product_type),
                'platform_index': platform_options.index(st.session_state.platform)
            })

        elif st.session_state.page == 2:
            st.subheader(pages[2])
            data_collect_options = ["是", "否"]
            sharing_attitude_options = ["非常乐意", "较为乐意", "中立", "不太乐意", "非常不乐意"]
            data_type_options = ["购买记录", "浏览记录", "产品评价和反馈", "个人偏好（如颜色、风格）", "人口统计信息（如年龄、性别）", "以上都不愿意"]
            data_concern_options = ["隐私和安全", "数据滥用", "缺乏透明度", "定向广告", "没有担忧"]
            
            data_collect_index = st.session_state.get('data_collect_index', 0)
            sharing_attitude_index = st.session_state.get('sharing_attitude_index', 0)
            data_type_index = st.session_state.get('data_type_index', 0)
            data_concern_index = st.session_state.get('data_concern_index', 0)
            
            st.session_state.data_collect = st.radio("您是否知道零售平台会收集并利用您的数据进行新产品设计？", data_collect_options, index=data_collect_index)
            st.session_state.sharing_attitude = st.radio("您对共享个人数据给零售平台用于新产品设计的态度如何？", sharing_attitude_options, index=sharing_attitude_index)
            st.session_state.data_type = st.radio("您愿意共享哪些类型的数据给零售平台？", data_type_options, index=data_type_index)
            st.session_state.data_concern = st.radio("您对共享数据给零售平台的主要担忧是什么？", data_concern_options, index=data_concern_index)
            
            st.session_state.update({
                'data_collect_index': data_collect_options.index(st.session_state.data_collect),
                'sharing_attitude_index': sharing_attitude_options.index(st.session_state.sharing_attitude),
                'data_type_index': data_type_options.index(st.session_state.data_type),
                'data_concern_index': data_concern_options.index(st.session_state.data_concern)
            })

        elif st.session_state.page == 3:
            st.subheader(pages[3])
            feedback_freq_options = ["每次都会", "经常", "有时", "很少", "从不"]
            feedback_important_options = ["是", "否", "不确定"]
            feedback_incentive_options = ["激励措施（如折扣、奖励）", "简单快捷的反馈流程", "数据隐私保障", "看到反馈对产品的改进效果"]
            feedback_importance_options = ["非常重要", "重要", "一般", "不太重要", "完全不重要"]
            
            feedback_freq_index = st.session_state.get('feedback_freq_index', 0)
            feedback_important_index = st.session_state.get('feedback_important_index', 0)
            feedback_incentive_index = st.session_state.get('feedback_incentive_index', 0)
            feedback_importance_index = st.session_state.get('feedback_importance_index', 0)
            
            st.session_state.feedback_freq = st.radio("您多常参与产品评价或反馈？", feedback_freq_options, index=feedback_freq_index)
            st.session_state.feedback_important = st.radio("您认为您的反馈在新产品设计中是否被重视？", feedback_important_options, index=feedback_important_index)
            st.session_state.feedback_incentive = st.radio("什么会激励您提供更多的产品反馈？", feedback_incentive_options, index=feedback_incentive_index)
            st.session_state.feedback_importance = st.radio("您认为根据消费者反馈和数据设计的新产品有多重要？", feedback_importance_options, index=feedback_importance_index)
            
            st.session_state.update({
                'feedback_freq_index': feedback_freq_options.index(st.session_state.feedback_freq),
                'feedback_important_index': feedback_important_options.index(st.session_state.feedback_important),
                'feedback_incentive_index': feedback_incentive_options.index(st.session_state.feedback_incentive),
                'feedback_importance_index': feedback_importance_options.index(st.session_state.feedback_importance)
            })

        elif st.session_state.page == 4:
            st.subheader(pages[4])
            product_pref_options = ["创新电子产品", "新款服饰", "升级版家电", "健康食品", "美妆新品", "环保产品"]
            product_feature_options = ["高性价比", "独特设计", "高科技含量", "环保材料", "用户友好", "多功能性"]
            info_sharing_strategy_options = ["提供更透明的数据使用政策", "加强数据安全措施", "提供数据共享的选择权", "增加消费者数据使用的奖励"]
            
            product_pref_index = st.session_state.get('product_pref_index', 0)
            product_feature_index = st.session_state.get('product_feature_index', 0)
            info_sharing_strategy_index = st.session_state.get('info_sharing_strategy_index', 0)
            
            st.session_state.product_pref = st.radio("您更倾向于购买哪些类别的新产品？", product_pref_options, index=product_pref_index)
            st.session_state.product_feature = st.radio("您希望新产品具备哪些特点？", product_feature_options, index=product_feature_index)
            st.session_state.info_sharing_strategy = st.radio("您认为零售平台应如何改进其信息共享策略，以更好地服务消费者？", info_sharing_strategy_options, index=info_sharing_strategy_index)
            
            st.session_state.update({
                'product_pref_index': product_pref_options.index(st.session_state.product_pref),
                'product_feature_index': product_feature_options.index(st.session_state.product_feature),
                'info_sharing_strategy_index': info_sharing_strategy_options.index(st.session_state.info_sharing_strategy)
            })

        elif st.session_state.page == 5:
            st.subheader(pages[5])
            contact_options = ["愿意", "不愿意"]
            contact_index = st.session_state.get('contact_index', 0)
            
            st.session_state.contact = st.radio("您是否愿意留下联系方式以便我们后续与您联系？", contact_options, index=contact_index)
            if st.session_state.contact == "愿意":
                st.session_state.phone = st.text_input("电话号码：", value=st.session_state.get('phone', ''))
            else:
                st.session_state.phone = ""
                
            st.session_state.update({
                'contact_index': contact_options.index(st.session_state.contact),
                'phone': st.session_state.get('phone', '')
            })

            submit = st.form_submit_button("提交")
            if submit:
                if st.session_state.contact == "愿意" and not st.session_state.phone:
                    st.error("请输入电话号码。")
                else:
                    # 读取现有数据
                    df = pd.read_csv(data_file)
                    # 添加新数据
                    new_data = pd.DataFrame({
                        "年龄": [st.session_state.age],
                        "性别": [st.session_state.gender],
                        "职业": [st.session_state.occupation],
                        "年收入": [st.session_state.income],
                        "网上购物频率": [st.session_state.shopping_freq],
                        "购买商品类型": [st.session_state.product_type],
                        "常用零售平台": [st.session_state.platform],
                        "知道数据收集": [st.session_state.data_collect],
                        "数据共享态度": [st.session_state.sharing_attitude],
                        "愿意共享的数据类型": [st.session_state.data_type],
                        "数据共享担忧": [st.session_state.data_concern],
                        "参与评价频率": [st.session_state.feedback_freq],
                        "反馈重视程度": [st.session_state.feedback_important],
                        "提供更多反馈的激励": [st.session_state.feedback_incentive],
                        "消费者反馈重要性": [st.session_state.feedback_importance],
                        "倾向购买的新产品类别": [st.session_state.product_pref],
                        "希望新产品具备的特点": [st.session_state.product_feature],
                        "改进信息共享策略": [st.session_state.info_sharing_strategy],
                        "愿意留下联系方式": [st.session_state.contact],
                        "电话号码": [st.session_state.phone]
                    })
                    df = pd.concat([df, new_data], ignore_index=True)
                    # 保存数据
                    df.to_csv(data_file, index=False)
                    st.session_state.submitted = True
                    st.balloons()
                    st.markdown("<div class='success-message'>感谢您的参与！ 祝你彩票中500万！</div>", unsafe_allow_html=True)
                    st.stop()

        col1, col2 = st.columns(2)
        if st.session_state.page > 0:
            if col1.form_submit_button("上一步"):
                previous_page()

        if st.session_state.page < len(pages) - 1:
            if col2.form_submit_button("下一步"):
                next_page()

# 显示问卷调查表单
if not st.session_state.submitted:
    survey_form()
