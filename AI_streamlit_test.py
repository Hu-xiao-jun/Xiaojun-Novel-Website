#streamlit 运行需要打开终端输入 streamlit run "./AI_streamlit_test.py"
import streamlit as st

#网页界面设置
st.set_page_config(
    page_title = "晓俊小说网-《别去后山！》",
    page_icon = "🧊",
    layout = "centered",
    menu_items = {}
)

#音频
st.audio("resource/music01.mp3",loop = True)#循环播放
#标题
#定义大标题
st.title("《别去后山！》",text_alignment = "center")
#st.markdown("<h1 style='text-align:center;color:black;font-family:KaiTi;background:none !important;'>《旧楼守夜人》</h1>", unsafe_allow_html=True)
#一级标题
st.header("海大宿管老邱是守夜人",text_alignment = "center")
#二级标题
st.subheader("第一章：我们宿管大爷，多少有点不正常",text_alignment = "center")

#内容
st.write("""
在我们海大，流传着两条绝对不能碰的校园铁律。\n
第一条：晚上十一点后别往后山跑。\n
第二条：十一点前，也别去。\n
后山那栋废弃的旧实验楼，属于学校官方默认的“野生鬼屋”。常年铁门生锈、荒草没过台阶，风一吹，楼道里就传来哗啦哗啦的声响，不像落叶，倒像是有人在深夜不停翻书。\n
学长学姐代代相传：谁要是半夜靠近旧楼，轻则emo一整晚，重则精神恍惚，连着几天做题走神、背书失忆。用我室友的话说，这楼里藏的不是鬼，是专克海大学子的精神BUG。\n
而全镇得住这个BUG的男人，是我们宿舍的宿管，老邱。\n
老邱今年五十出头，头顶发量极具诚实主义，地中海发型常年稳定发挥。平时穿一件洗得发白的深蓝工装外套，趿拉着一双旧布鞋，走路悄无声息，跟贴地滑行似的。\n
在全体海大学生眼里，他就是个再普通不过的老大爷——话少、佛系、管得松，唯一的爱好是半夜巡楼，顺便没收几台偷偷使用的违规小煮锅。\n
我以前也这么想，直到上周我熬大夜赶结课论文，差点把自己熬猝死，才彻底颠覆了三观。\n
那天凌晨一点，整栋宿舍楼死寂沉沉，只有我这间寝室还亮着垂死挣扎的台灯。Word文档空空如也， deadline 近在眼前，我大脑空空，焦虑得浑身难受，索性揣着钥匙下楼，打算去楼下自动贩卖机买瓶可乐续命。\n
刚出楼道门，我就看见月光底下站着个人。\n
是老邱。\n
但又不完全是我认识的那个老邱。\n
平日里瘫在门卫室刷手机、嗑瓜子的他，此刻笔挺地站着，手里拎着一盏黄铜老灯。那灯看着年头久远，满身斑驳锈迹，压根不像是现代物件，灯芯燃着一团微弱的暖光，不刺眼，却格外透亮，把周遭的夜色都压得黯淡几分。\n
最离谱的是风。\n
那晚夜风不小，路边的梧桐树摇得哗哗作响，可老邱手里那簇灯火，纹丝不动，连一丝晃动都没有，仿佛整片晚风都绕着他刻意避开。\n
我心里咯噔一下，下意识躲到柱子后面，不敢出声。\n
只见老邱抬眼，望向黑漆漆的后山方向，慢悠悠吐出一句：“又闹？这帮孩子，压力大到执念都溢出来了。”\n
话音落下，他抬手轻轻一握。\n
我余光瞥见，他指尖好像闪过一丝极淡的微光，快得让人以为是月光错觉。紧接着，后山方向原本沉沉压过来的黑雾，瞬间退了半截，连空气中那股让人胸闷压抑的感觉，都一扫而空。\n
我当场看傻了，脑子里疯狂刷屏：这还是那个只会查寝、收锅的宿管大爷？这怕不是隐世高人下凡蹲守海大、体验退休生活吧？\n
正当我三观重组、脑补出八百字玄幻剧本时，老邱忽然转头，视线精准锁定我藏身的柱子。\n
他语气平淡，带着点看透一切的无奈：“那位熬夜赶论文的同学，看够了没有？”\n
我：“……”\n
当场社死，原地僵住。\n
我硬着头皮走出来，尴尬得脚趾抠出三室一厅，只能假装刚刚啥也没看见，干笑着扯谎：“邱叔，我、我下来买瓶水，睡不着，哈哈。”\n
老邱低头扫了我一眼，目光落在我眼底浓重的青黑上，又瞥了眼我空空如也、连手机都没带的双手，淡淡开口：“睡不着，还是论文一个字没写，焦虑得睡不着？”\n
我瞳孔地震。\n
这大爷不仅会玄学，还会读心？\n
没等我继续编瞎话圆场，老邱拎着那盏古旧铜灯，慢悠悠朝我走近。晚风掠过他的衣角，明明是初秋深夜，我却莫名闻到一丝淡淡的、像旧书卷又像雨后青松的清冽味道。\n
“海大这后山，看着荒，最藏东西。”老邱抬了抬下巴，示意我看向漆黑的后山，语气随意得像在唠家常，“你们这群小孩，天天卷考研、卷绩点、卷保研，心事太重，执念堆多了，就容易撞邪。”\n
我听得头皮发麻，小声嘀咕：“邱叔，您……您还懂这个？我一直以为那些旧楼闹鬼都是谣言。”\n
老邱闻言嗤笑一声，抬手轻轻拂过灯壁的锈迹，灯火轻轻跳动了一下，却依旧稳如磐石。\n
“世上哪有那么多恶鬼妖魔。”\n
“真正缠人的，从来都是你们年轻人放不下的遗憾。”\n
他话说得温和，却带着一种莫名的重量，压得我瞬间没了熬夜的浮躁。\n
就在这时，后山深处，忽然传来一阵清晰的、细碎的翻书声。\n
沙沙，沙沙。\n
深夜空楼，无人自响。\n
我浑身汗毛瞬间竖了起来。\n
而一旁的老邱，只是轻轻叹了口气，拎起铜灯，转身往后山走去。\n
“得，又得加班。”\n
“守宿舍就算了，还得守着你们一屋子的青春执念。”\n
我站在原地，看着他孤瘦的背影融进夜色里，第一次真切意识到：\n
我们海大最神秘的传说，从来不在后山旧楼里。\n
而在这个天天蹲门卫室嗑瓜子的宿管大爷身上......\n
""")
#改换字体
import base64
with open("resource/bg.webp", "rb") as f:
    bg_img = f.read()
bg_base64 = base64.b64encode(bg_img).decode()

st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/jpeg;base64,{bg_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-family: "SimSun", serif;  /* 全局宋体，小说氛围感 */
    color:black !important;
}}
.st-header, .st-subheader {{
    font-family: "SimSun", serif;
    background-color:rgba(0,0,0,0.5);
    padding:8px;
    border-radius:6px;
    color:black !important;
}}
.stMarkdown, .stWrite {{
    font-size:18px;
    line-height:1.6;
    background-color:rgba(0,0,0,0.5);
    padding:8px;
    border-radius:6px;
    color:white !important;
}}
h1 {{
background:none !important
}}
</style>
""", unsafe_allow_html=True)



