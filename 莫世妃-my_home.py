'''我的主页'''
import streamlit as st
import time
from PIL import Image

st.sidebar.write(':blue[小莫的网络根据地]')
page = st.sidebar.radio(':red[我的首页]',[':green[我的兴趣推荐]',':green[我的图片处理工具]',':green[我的智能词典]',':green[我的留言区]',':green[查看世界地图]',':green[对网站的评价]'])

def page_1():
    '''我的兴趣推荐'''
    # 滑块开关 + 进度条
    open_road()
    with open('霞光.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.image('天象奇景.jpg')
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(['电影推荐','游戏推荐','书籍推荐','习题集推荐','音乐推荐','软件推荐'])
    with tab1:
        st.write(':orange[我的电影推荐]')
        st.write(':green[《喜羊羊与灰太狼》系列电影]')
        st.write(':green[《熊出没》系列电影]')
        st.write(':green[《热辣滚烫》]')
    with tab2:
        st.write(':orange[我的游戏推荐]')
        st.write(':green[捉迷藏]')
        st.write(':green[过家家]')
        st.write(':green[《光遇》]')
        st.write(':red[注意：未成年人千万不要沉迷游戏！]')
    with tab3:
        st.write(':orange[我的书籍推荐]')
        st.write(':green[中国古代四大名著]')
        st.write(':green[《哈利·波特》系列]')
        st.write(':green[《海底两万里》]')
        st.write(':red[注意：未成年人千万不要看言情小说！]')
    with tab4:
        st.write(':orange[我的习题集推荐]')
        st.write(':green[《Python3级考前复习题》]')
        st.write(':green[《英语听力》]')
        st.write(':green[《语文阅读理解专练》]')
    with tab5:
        st.write(':orange[我的音乐推荐]')
        st.write(':green[《起风了》]')
        st.write(':green[《星芒》]')
        st.write(':green[《晚夜微雨问海棠》]')
        st.write(':red[注意：听音乐时不要长时间佩戴耳机，否则会对耳朵造成伤害！]')
    with tab6:
        st.write(':orange[我的软件推荐]')
        st.write(':green[百度：这是一个非常实用的应用软件]')
        # 跳转按钮 link_button()
        st.link_button('点击跳转百度首页', 'https://www.baidu.com/')
        st.write(':green[酷狗音乐：这是一个很好用的听歌的软件,喜欢听音乐的朋友们快体验一下]')
        st.link_button('点击跳转酷狗音乐', 'https://www.kugou.com/')

def page_2():
    '''我的图片处理工具'''
    # 滑块开关 + 进度条
    open_road()
    tab_1,tab_2 = st.tabs(['图片换色','图片缩放'])
    with tab_1:
        st.write(':sunglasses:图片换色小程序:sunglasses:')
        uploaded_file_1 = st.file_uploader(':blue[上传图片]',type=['png','jpeg','jpg'])
        if uploaded_file_1:
            # 获取图片文件名称、类型和大小
            file_name = uploaded_file_1.name
            file_type = uploaded_file_1.type
            file_size = uploaded_file_1.size
            img = Image.open(uploaded_file_1)
            tab1,tab2,tab3,tab4 = st.tabs(['原色','改色1','改色2','改色3'])
            with tab1:
                st.image(img)
            with tab2:
                st.image(img_change(img,0,2,1))
            with tab3:
                st.image(img_change(img,1,2,0))
            with tab4:
                st.image(img_change(img,1,0,2))
                
    with tab_2:
        st.write(':sunglasses:图片缩放小程序:sunglasses:')
        uploaded_file_2 = st.file_uploader(':blue[上传图片]',type=['gif','png','jpeg','jpg'])
        if uploaded_file_2:
            img = Image.open(uploaded_file_2)
            w,h = img.size
            st.write('图片原大小(像素)：宽',w,'高',h)
            multiple = st.selectbox('请选择缩放的倍数：', [2.0,1.5,1.25,0.75,0.5])
            w,h = int(w*multiple), int(h*multiple)
            img = img.resize((w,h))
            st.image(img)
            st.write('图片现大小(像素)：宽',w,'高',h)

def page_3():
    '''我的智能词典'''
    # 滑块开关 + 进度条
    open_road()
    st.write(':orange[智能词典]')
    st.write(':blue[这里的单词涵盖了初中和高中的大部分重点单词以及小部分大学单词，应有尽有！]')
    # 从本地文件中将词典信息读取出来，并储存在列表中
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # ① 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    # ② 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    # 两步并为一步
    words_dict = {}
    for i in words_list:
        i = i.split('#')
        words_dict[i[1]] = [int(i[0]),i[2]]
    # 从本地文件中将单词的查询次数读出来，并储存在列表中
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    times_dict = {}
    for i in times_list:
        i = i.split('#')
        times_dict[int(i[0])] = int(i[1])
    # 查找上一个单词
    with open('last_word.txt','r',encoding='utf-8') as f:
        past_words = f.read().split('\n')
    last_word = past_words[-1]
    # 创建输入框
    word = st.text_input('请输入要查询的单词：')
    # 显示查询内容
    if word in words_dict and word != '':
        st.write(words_dict[word][1])
        n = words_dict[word][0]
        if n in times_dict and word != last_word:
            times_dict[n] += 1
        elif n not in times_dict:
            times_dict[n] = 1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message =''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：',times_dict[n])
        with open('last_word.txt','w',encoding='utf-8') as f:
            f.write(last_word + '\n' + word)
        # 触发彩蛋
        if word == 'python':
            st.code('''
                # 恭喜你触发彩蛋，这是一行python代码
                ptint('hello world')''')
        if word == 'snow':
            st.snow()
        if word == 'birthday':
            st.balloons()
    elif word not in words_dict:
        st.write(':green[很抱歉，找不到该单词]')
    # 显示高频查询单词
    words_show = st.toggle('高频查询单词')
    if words_show:
        st.text('显示')
        most = max(times_dict.values())
        for k1,v1 in times_dict.items():
            if v1 == most:
                for k2,v2 in words_dict.items():
                    if v2[0] == k1:
                        st.write(k2,' ',words_dict[k2][1])
                        st.write('查询次数：',times_dict[k1])
    else:
        st.text('隐藏')

def page_4():
    '''我的留言区'''
    # 滑块开关 st.toggle()
    balloons_open = st.toggle('气球上升')
    if not balloons_open:
        st.text('显示')
        st.balloons()
    else:
        st.text('隐藏')
    st.write(':orange[我的留言区]')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    # 滑动条 st.slider()
    messages = ['1 阿短的留言', '2 编程猫的留言', '3 路过的美女的留言', '4 路过的帅哥的留言', '5 老熟人的留言', '6 陌生人的留言', '7 网站主人的留言']
    st.write(':green[请选择要查看的留言：]')
    # 勾选框 st.checkbox()
    col1, col2, col3 = st.columns([2, 2, 3])
    col4, col5, col6 = st.columns([2, 2, 3])
    with col1:
        aduan = st.checkbox(messages[0])
    with col2:
        codemao = st.checkbox(messages[1])
    with col3:
        woman = st.checkbox(messages[2])
    with col4:
        man = st.checkbox(messages[3])
    with col5:
        friend = st.checkbox(messages[4])
    with col6:
        person = st.checkbox(messages[5])
    I = st.checkbox(messages[6])
    name = st.selectbox('我是：',['阿短','编程猫','路过的美女','路过的帅哥','老熟人','陌生人'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] +'\n'
            message = message[:-1]
            f.write(message)
    for i in messages_list:
        if i[1] == '阿短' and aduan:
            with st.chat_message('🌞'):
                st.text(i[1] + '：' + i[2])
        elif i[1] == '编程猫' and codemao:
            with st.chat_message('🍥'):
                st.text(i[1] + '：' + i[2])
        elif i[1] == '网站主人' and I:
            with st.chat_message('🌈'):
                st.write(i[1],'：',i[2])
        elif i[1] == '路过的帅哥' and man:
            with st.chat_message('男'):
                st.text(i[1] + '：' + i[2])
        elif i[1] == '路过的美女' and woman:
            with st.chat_message('女'):
                st.text(i[1] + '：' + i[2])
        elif i[1] == '老熟人' and friend:
            with st.chat_message('🍀'):
                st.text(i[1] + '：' + i[2])
        elif i[1] == '陌生人' and person:
            with st.chat_message('🌸'):
                st.text(i[1] + '：' + i[2])

def page_5():
    # 滑块开关 + 进度条
    open_road()
    st.write(':red[1、请问您对网站的总体评价如何？]')
    # 单项选择框 st.radio()
    choice = st.radio(':green[单项选择题]', ['A.非常好！', 'B.还不错', 'C.一般般', 'D.有待改进(不好)'])
    gekai()
    st.write(':red[2、请问您最喜欢的模块是哪个？]')
    st.write(':green[可多选]')
    # 对齐美观
    col1,col2 = st.columns([2,3])
    col3,col4 = st.columns([2,3])
    col5,col6 = st.columns([2,3])
    # 勾选框 st.checkbox()
    with col1:
        ans_1 = st.checkbox('A.兴趣推荐')
    with col2:
        ans_2 = st.checkbox('B.图片处理工具')
    with col3:
        ans_3 = st.checkbox('C.智能词典')
    with col4:
        ans_4 = st.checkbox('D.留言区')
    with col5:
        ans_5 = st.checkbox('E.对网站的评价')
    answer_2 = (ans_1 or ans_2 or ans_3 or ans_4 or ans_5)
    gekai()
    st.write(':red[3、请问您最喜欢的功能是哪个？]')
    st.write(':green[可多选]')
    # 对齐美观
    col_1,col_2,col_3 = st.columns([2,2,3])
    col_4,col_5,col_6 = st.columns([2,2,3])
    col_7,col_8,col_9 = st.columns([2,2,3])
    # 勾选框 st.checkbox()
    with col_1:
        ans1 = st.checkbox('A.播放音乐')
    with col_2:
        ans2 = st.checkbox('B.处理图片')
    with col_3:
        ans3 = st.checkbox('C.跳转按钮')
    with col_4:
        ans4 = st.checkbox('D.进度条')
    with col_5:
        ans5 = st.checkbox('E.滑块开关')
    with col_6:
        ans6 = st.checkbox('F.单选框')
    with col_7:
        ans7 = st.checkbox('G.勾选框')
    with col_8:
        ans8 = st.checkbox('H.查单词')
    with col_9:
        ans9 = st.checkbox('I.其他')
    answer_3 = (ans1 or ans2 or ans3 or ans4 or ans5 or ans6 or ans7 or ans8 or ans9)
    st.write(':red[4、请您提出对网站的意见和建议：]')
    great_help = st.text_input('意见和建议：')
    if st.button('提交') and choice and answer_2 and answer_3 and great_help:
        st.write(':blue[十分感谢您的宝贵评价！您珍贵的意见和建议将对我有很大的帮助！]')
        with open('评价.txt','r',encoding='utf-8') as f:
            pingjia = f.read().split('\n')
        for i in range(len(pingjia)):
            pingjia[i] = pingjia[i].split(' ')
        pingjia.append([str(int(pingjia[-1][0])+1) , great_help])
        neirong = ''
        with open('评价.txt','w',encoding='utf-8') as f:
            for i in pingjia:
                neirong += i[0] + ' ' + i[1] + '\n'
            f.write(neirong[:-1])

def page_6():
    # 滑块开关 + 进度条
    open_road()
    data = {'latitude':[37.7749,34.0522,40.7128], 'longitude':[-122.4194,-118.2437,-74.0060], 'name':['San Francisco','Los Angeles','New York']}
    st.map(data, zoom = 4, use_container_width = True)

# '''
# data={'latitude':[37.7749,34.0522,40.7128],"longitude':[-122.4194,-118.2437,-74.0060],'name':['San Francisco', 'Los Angeles','New York']
# st .map(data, zoom = 4,use_container_width=True)
# '''

def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img

def words_find(list_words,times_dict,words_dict):
    most = max(list_words)
    for k1,v1 in times_dict.items():
        if v1 == most:
            for k2,v2 in words_dict.items():
                if v2[0] == k1:
                    st.write(k2,words_dict[k2][1])
                    st.write('查询次数：',times_dict[k1])

def open_road():
    # 滑块开关 st.toggle()
    my_open = st.toggle('加载进度条')
    if my_open:
        st.text('隐藏')
    else:
        st.text('显示')
        # 进度条st.progress()
        roading = st.progress(0, '开始加载')
        time.sleep(0.5)
        for i in range(1, 101, 1):
            time.sleep(0.005)
            roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')

def gekai():
    st.write(' ')
    st.write(' ')


if page == ':green[我的兴趣推荐]':
    page_1()
if page == ':green[我的图片处理工具]':
    page_2()
if page == ':green[我的智能词典]':
    page_3()
if page == ':green[我的留言区]':
    page_4()
if page == ':green[对网站的评价]':
    page_5()
if page == ':green[查看世界地图]':
    page_6()
