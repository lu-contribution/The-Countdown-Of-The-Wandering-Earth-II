from PIL import Image,ImageFont,ImageDraw
# 作者bilibili@卢祎不念伟
# 导入字体 
tc_font = ImageFont.truetype('字魂创粗黑(商用需授权).ttf',160)
te_font = ImageFont.truetype('字魂创粗黑(商用需授权).ttf',72)
n_font = ImageFont.truetype('DIN 1451 LT W06 Mittelschrift.otf',500)

# 输入文本和倒计时时间
text = ("清明节假期","Qingming Festival is coming".upper())
timetype_cn = "天"
timeleft = 11

# 处理文本和文字间隔
timetype_translate = {'秒':'SECONDS','分钟':'MINUTES','小时':'HOURS',
                            '天':'DAYS','个月':'MONTHS','年':'YEARS'}
if(timeleft == 1):
    timetype_en = timetype_translate[timetype_cn][:-1]
else:
    timetype_en = timetype_translate[timetype_cn]
timetype = (timetype_cn,timetype_en)
text_cn = text[0]
text_en = text[1]
timetype_cn = timetype[0]
timetype_en = timetype[1]
size_e = tc_font.getbbox('空'*(len(text_cn)-1))
size_n = n_font.getbbox(str(timeleft))
size_t = tc_font.getbbox(timetype_cn)
size_1 = tc_font.getbbox('距'+text_cn)
size_2 = tc_font.getbbox('还剩')
size_3 = te_font.getbbox(text_en)
size_4 = te_font.getbbox('IN'+str(timeleft) + timetype_en)


# 处理画布面积并打包size
canvas_width_cn =  size_2[2]-size_1[0]+size_e[2]+size_n[2]+size_t[2]
canvas_width_en =  size_3[2]-size_1[0]+size_e[2]
canvas_height = size_1[3]+size_2[3]+size_3[3]+size_4[3]+size_4[1]
if canvas_width_cn >= canvas_width_en :
    canvas_size = (canvas_width_cn,canvas_height)
else :
    canvas_size = (canvas_width_en,canvas_height)
p_1 = (0,0)
p_2 = (size_e[2],size_1[3]-15)
p_3 = (size_e[2],size_1[3]+size_2[3])
p_4 = (size_e[2],size_1[3]+size_2[3]+size_3[3]+10)


# 开始绘画
im = Image.new('RGBA',size=canvas_size)
pen = ImageDraw.Draw(im)
pen.text(p_1,'距'+text_cn,font=tc_font,fill='white')
pen.text(p_2,'还剩',font=tc_font,fill='white')
pen.text((size_e[2]+size_2[2]+10,-110),str(timeleft),font=n_font,fill='red')
pen.text((size_e[2]+size_2[2]+size_n[2],size_1[3]),timetype_cn,font=tc_font,fill='white')
pen.text(p_3,text_en,font=te_font,fill='white')
pen.text(p_4,'IN ' + str(timeleft) +' '+ timetype_en,font=te_font)
pen.line([size_e[2]-50,size_2[3]+30,size_e[2]-50,size_1[3]+size_2[3]+size_3[3]+size_4[3]+10],fill='red',width=15)
im.show()
im.save('out.png')










