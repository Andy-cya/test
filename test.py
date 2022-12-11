import streamlit as st
import random
import base64

with st.sidebar:
    st.text("请选择房间类型\n")
    type=st.selectbox(
        "none",
        ('普通房间','机房'),
        label_visibility="collapsed"
        )
    st.text("请输入房间尺寸\n")
    if st.button("随机生成房间尺寸"):
        length=random.uniform(5,20)
        width=length*random.uniform(0.7,1)
        height=random.uniform(2.5,5)
    else:
        length=st.slider("长",5.0,20.0)
        width=st.slider("长宽比",1.0,1.4)*length
        height=st.slider("高",2.5,5.0)


st.markdown("![gif](https://github.com/Andy-cya/test/blob/main/gif.gif) ")
