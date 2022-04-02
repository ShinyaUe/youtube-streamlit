import streamlit as st
import time

st.title('Streamlit 超入門')
st.write('Display Image')
st.write('プログレスバーの表示')

latest_itetration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_itetration.text(f'iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

left_column, right_column = st.columns(2)

button = left_column.button('右に文字を表示')
if button:
    right_column.write('ここは右です')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

option = st.selectbox(
    '数字教えて',
    list(range(1,11))
    )
'好きな数字は' ,option

hobby = st.text_input('趣味教えて')
'あなたの趣味は' ,hobby

condition = st.slider('調子どれくらい',0,100,50)
'あなたの調子は' ,condition


# if st.checkbox('show image'):
#     Img = Image.open('IMG_4270.JPG')
#     st.image(Img, caption='spycute', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50, 50]+[35.69, 139.70],
#     columns=['lat', 'lon']
#     #'1列':[1, 2, 3 ,4],
#     #'2列':[10, 20, 30, 40]
# )


# st.table(df.style.highlight_max(axis=0))

#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
# st.map(df)

