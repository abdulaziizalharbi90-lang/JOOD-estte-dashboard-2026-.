import streamlit as st
import pandas as pd
import plotly.express as px

# 1. إعدادات الصفحة والواجهة العربية
st.set_page_config(
    page_title="لوحة تحكم الاستثمار العقاري - الرياض 2026",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تعديل اتجاه الواجهة لتكون من اليمين إلى اليسار (RTL)
st.markdown("""
    <style>
    .reportview-container {
        direction: RTL;
        text-align: right;
    }
    div.stMarkdown {
        text-align: right;
    }
    </style>
""", unsafe_allow_headers=True)

# 2. العنوان الرئيسي
st.title("📊 مرصد الرياض العقاري التفاعلي لعام 2026")
st.subheader("لوحة مؤشرات استثمارية حية مدعومة بالبيانات الرسمية والمصادر الموثوقة")
st.write("---")

# 3. قسم الأرقام الرئيسية (KPI Cards)
st.write("### 📈 المؤشرات العقارية القيادية (الربع الحالي لعام 2026)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="حجم التمويل السكني الجديد (SAMA)",
        value="4.56 مليار ر.س",
        delta="تحت التقييم المالي"
    )

with col2:
    st.metric(
        label="الرقم القياسي لأسعار العقار (GASTAT)",
        value="-1.6%",
        delta="مرحلة تصحيح صحية للمستثمرين",
        delta_color="off"
    )

with col3:
    st.metric(
        label="حصة تمويل الفلل السكنية",
        value="2.76 مليار ر.س",
        delta="الحصة الأكبر"
    )

with col4:
    st.metric(
        label="عقود الإيجار النشطة (إيجار)",
        value="+1.14 مليون عقد",
        delta="طلب إيجاري قوي جداً"
    )

st.write("---")

# 4. الرسوم البيانية التفاعلية وتوزيع التمويل
col_graph, col_dist = st.columns([2, 1])

with col_graph:
    st.write("#### 📊 مقارنة أسعار المتر والعوائد الإيجارية المتوقعة بأحياء الرياض")
    data = {
        'الحي': ['الياسمين', 'النرجس', 'الملقا', 'قرطبة', 'العارض', 'الصحافة'],
        'متوسط سعر المتر (ر.س)': [7500, 6800, 9200, 6200, 5500, 8000],
        'العائد الإيجاري المتوقع (%)': [7.5, 8.0, 7.0, 8.2, 8.5, 7.2]
    }
    df = pd.DataFrame(data)
    
    fig = px.bar(
        df, 
        x='الحي', 
        y='متوسط سعر المتر (ر.س)', 
        color='العائد الإيجاري المتوقع (%)',
        labels={'متوسط سعر المتر (ر.س)': 'سعر المتر', 'العائد الإيجاري المتوقع (%)': 'العائد الاستثماري'},
        color_continuous_scale='Oranges',
        title="توزيع الأسعار والعائد حسب الحي"
    )
    st.plotly_chart(fig, use_container_width=True)

with col_dist:
    st.write("#### 🍕 هيكلة التمويل السكني الجديد للأفراد")
    funding_data = {
        'النوع': ['فلل سكنية', 'شقق سكنية', 'أراضي'],
        'المبلغ بالمليارات (ر.س)': [2.76, 1.27, 0.335]
    }
    df_funding = pd.DataFrame(funding_data)
    fig_pie = px.pie(
        df_funding, 
        values='المبلغ بالمليارات (ر.س)', 
        names='النوع', 
        color_discrete_sequence=px.colors.sequential.Sunsetdark
    )
    st.plotly_chart(fig_pie, use_container_width=True)

st.write("---")

# 5. قسم تحميل مستندات المصادر للتأكد من الأرقام (Verify Sources)
st.write("### ⬇️ تحميل المستندات الرسمية والمصادر الأصلية لعام 2026")
st.write("يمكن للمستثمر تحميل المستند المرجعي الأصلي للتحقق والتدقيق المالي قبل اتخاذ القرار:")

col_dl1, col_dl2, col_dl3 = st.columns(3)

with col_dl1:
    st.info("📄 النشرة الإحصائية للبنك المركزي (SAMA) - مايو 2026")
    try:
        with open("SAMA_May_2026.pdf", "rb") as file:
            st.download_button(
                label="تحميل نشرة SAMA المرجعية (PDF)",
                data=file,
                file_name="SAMA_May_2026.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.caption("⚠️ ملف PDF غير متوفر حالياً على الخادم، سيتاح قريباً.")

with col_dl2:
    st.success("📄 تقرير الرقم القياسي لأسعار العقارات (GASTAT) - الربع الأول 2026")
    try:
        with open("GASTAT_Q1_2026.pdf", "rb") as file:
            st.download_button(
                label="تحميل تقرير أسعار العقارات (PDF)",
                data=file,
                file_name="GASTAT_Q1_2026.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.caption("⚠️ ملف PDF غير متوفر حالياً على الخادم، سيتاح قريباً.")

with col_dl3:
    st.help("📄 تقارير وخرائط الاستثمار بهيئة عقارات الدولة / الهيئة العامة للعقار")
    st.write("[زيارة المنصة الرسمية للهيئة العامة للعقار ↗️](https://rega.gov.sa)")

st.write("---")

# 6. قراءة في السوق العقاري ورؤى استثمارية (Insights & Recommendations)
st.write("### 💡 التحليل الاستراتيجي والتوصيات للمستثمر")

tab1, tab2 = st.tabs(["🎯 فرص الأحياء الواعدة", "🏗️ استراتيجيات التمويل والدخل"])

with tab1:
    st.markdown("""
    * **محور النمو الرأسمالي (شمال الرياض):** تعتبر أحياء **النرجس، العارض، والأمانة** من أفضل الخيارات الاستثمارية بهدف إعادة البيع مستقبلاً، نظراً لقربها المباشر من مشروع **المربع الجديد** وتوسعات مطار الملك سلمان الدولي.
    * **العائد المالي الفوري (الشقق):**
        تعد أحياء مثل **الياسمين، قرطبة، والملقا** هي الحاضنة المثالية للاستثمار السكني المدر للدخل، حيث يقارب العائد الإيجاري للشقق الذكية المؤثثة ما بين **7.5% إلى 8.5%** نتيجة الطلب المرتفع من الموظفين الجدد بالمركز المالي والمغتربين.
    """)

with tab2:
    st.markdown("""
    * **اغتنام حركة التصحيح الحالية (مؤشر أسعار العقارات -1.6%):**
        هذا الانخفاض الطفيف يعكس استقراراً صحياً يعقبه مرحلة تصاعد تدريجي. نوصي باقتناص الصفقات الحالية قبل استئناف عمليات البناء المتسارعة بالبنية التحتية لمشاريع المترو.
    * **إدارة التمويل العقاري:**
        مع تراجع حجم تمويل الشقق نسبياً، يُنصح بتوفير دفعة مقدمة لا تقل عن 30% لتقليل أثر الفوائد المرتفعة وضمان ألا تتجاوز نسبة الاستقطاع الشهري العائد الإيجاري الفعلي للعقار.
    """)
