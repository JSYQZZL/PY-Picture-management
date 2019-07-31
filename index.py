# -*- coding:utf-8 -*-
from PIL import Image as Im
from PIL import ImageTk
import tkinter as tk  # 导入 Tkinter 库
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
import tkinter.ttk
import tkinter.messagebox
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageEnhance
import style_Huminghao  # 调用胡明皓完成文件


# 窗口类（图片对象Tkinter）
class Win(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('图像简易处理及滤镜工具')
        self.geometry('1080x720')
        self.picture = None  # self.picture将作为picture类的实例化对象
        self.img = None  # self.img将作为窗口类中一直变动的PIL对象图片
        self.setupUI()

    def setupUI(self):
        # 左边菜单栏
        left_f = tk.Frame(self, height=720, width=360)
        left_f.pack(side=tk.LEFT)

        # 各种功能按钮名称及位置
        btn1 = tk.Button(left_f, text='打开图像', command=self.openToshow)
        btn1.place(y=25, x=30, width=300, height=40)
        btn2 = tk.Button(left_f, text='截图', command=self.window_cut)
        btn2.place(y=85, x=30, width=144, height=60)
        btn3 = tk.Button(left_f, text='大小', command=self.window_size)
        btn3.place(y=85, x=186, width=144, height=60)
        btn4 = tk.Button(left_f, text='旋转', command=self.window_rotate)
        btn4.place(y=165, x=30, width=144, height=60)
        btn5 = tk.Button(left_f, text='镜像', command=self.window_mirror)
        btn5.place(y=165, x=186, width=144, height=60)
        btn6 = tk.Button(left_f, text='文字', command=self.window_word)
        btn6.place(y=245, x=30, width=144, height=60)
        btn7 = tk.Button(left_f, text='滤镜', command=self.window_style)
        btn7.place(y=245, x=186, width=144, height=60)

        # 各种调整名称及位置
        lb1 = tk.Label(left_f, text='亮 度:')
        lb1.place(y=355, x=55, width=60, height=30)
        self.inp1 = tk.Entry(left_f)
        self.inp1.place(y=355, x=105, width=90, height=30)
        lb2 = tk.Label(left_f, text='%')
        lb2.place(y=355, x=205, width=13, height=30)
        b1 = tk.Button(left_f, text='确定', width=8, command=self.brightnessPic)
        b1.place(y=359, x=240)

        lb3 = tk.Label(left_f, text='色彩度:')
        lb3.place(y=400, x=55, width=60, height=30)
        self.inp2 = tk.Entry(left_f)
        self.inp2.place(y=400, x=105, width=90, height=30)
        lb4 = tk.Label(left_f, text='%')
        lb4.place(y=400, x=205, width=13, height=30)
        b2 = tk.Button(left_f, text='确定', width=8, command=self.coolorPic)
        b2.place(y=404, x=240)

        lb5 = tk.Label(left_f, text='对比度:')
        lb5.place(y=445, x=55, width=60, height=30)
        self.inp3 = tk.Entry(left_f)
        self.inp3.place(y=445, x=105, width=90, height=30)
        lb6 = tk.Label(left_f, text='%')
        lb6.place(y=445, x=205, width=13, height=30)
        b3 = tk.Button(left_f, text='确定', width=8, command=self.contrastPic)
        b3.place(y=449, x=240)

        lb7 = tk.Label(left_f, text='锐 度:')
        lb7.place(y=490, x=55, width=60, height=30)
        self.inp4 = tk.Entry(left_f)
        self.inp4.place(y=490, x=105, width=90, height=30)
        lb8 = tk.Label(left_f, text='%')
        lb8.place(y=490, x=205, width=13, height=30)
        b4 = tk.Button(left_f, text='确定', width=8, command=self.sharpnessPic)
        b4.place(y=494, x=240)

        # 底部恢复、保存、对比
        btn8 = tk.Button(left_f, text='保存图像', command=self.save_pic)
        btn8.place(y=600, x=150, width=180, height=30)
        btn9 = tk.Button(left_f, text='恢复图像', command=self.replay)
        btn9.place(y=550, x=90)
        btn10 = tk.Button(left_f, text='对比图像', command=self.compare)
        btn10.place(y=550, x=170)

        # 右侧图像显示栏
        right_f = tk.Frame(self, height=720, width=720)
        right_f.pack(side=tk.RIGHT)
        self.image_l = tk.Label(right_f, relief='ridge')
        self.image_l.place(x=0, y=0, width=720, height=720)

    # 打开图片时使用，获得地址
    def getAddress(self):
        path = tk.StringVar()
        file_entry = tk.Entry(self, state='readonly', text=path)
        path_ = askopenfilename()
        path.set(path_)
        self.picture = picture()
        return file_entry.get()

    # 打开图片时使用，传值（图）给展示函数
    def openToshow(self):
        address = self.getAddress()
        self.open_picToimg = self.picture.open_pic(address)
        self.firstPic(self.open_picToimg)
        self.show_img(self.open_picToimg)

    # 截图操作页面
    def window_cut(self):
        Cut_win = tk.Toplevel()
        Cut_win.title('截图操作')
        Cut_win.geometry('220x380')
        nowPic = self.img
        if self.img == None:
            lNone = tk.Label(Cut_win, text='请先打开一张图片')
            lNone.place(y=55, x=50)
        else:
            wNow, hNow = nowPic.size
            l1 = tk.Label(Cut_win, text="此时图片尺寸:")
            l1.place(y=30, x=25)
            l2 = tk.Label(Cut_win, text=wNow)
            l2.place(y=55, x=25)
            l3 = tk.Label(Cut_win, text="X")
            l3.place(y=55, x=65)
            l4 = tk.Label(Cut_win, text=hNow)
            l4.place(y=55, x=85)
            l5 = tk.Label(Cut_win, text="截图区域")
            l5.place(y=85, x=25)
            l6 = tk.Label(Cut_win, text="起始点：（左上为（0，0））")
            l6.place(y=115, x=25)
            l7 = tk.Label(Cut_win, text="x：")
            l7.place(y=145, x=25)
            self.e1 = tk.Entry(Cut_win, width=10)
            self.e1.place(y=145, x=55)
            l8 = tk.Label(Cut_win, text="y：")
            l8.place(y=180, x=25)
            self.e2 = tk.Entry(Cut_win, width=10)
            self.e2.place(y=180, x=55)
            l9 = tk.Label(Cut_win, text="终止点：")
            l9.place(y=220, x=25)
            l10 = tk.Label(Cut_win, text="x：")
            l10.place(y=250, x=25)
            self.e3 = tk.Entry(Cut_win, width=10)
            self.e3.place(y=250, x=55)
            l11 = tk.Label(Cut_win, text="y：")
            l11.place(y=285, x=25)
            self.e4 = tk.Entry(Cut_win, width=10)
            self.e4.place(y=285, x=55)
            b1 = tk.Button(Cut_win, text='确定', command=self.getCutpart)
            b1.place(y=320, x=80, width=40)
            b2 = tk.Button(Cut_win, text='完成', command=Cut_win.destroy)
            b2.place(y=350, x=150, width=40)

    # 接收截图区域,传送展示
    def getCutpart(self):
        nCut_pic = self.img
        x = int(self.e1.get())
        y = int(self.e2.get())
        xl = int(self.e3.get())
        yl = int(self.e4.get())
        self.picture = picture()
        showCut_pic = self.picture.Cutpic(nCut_pic, x, y, xl, yl)
        self.show_img(showCut_pic)

    # 大小尺寸操作窗口
    def window_size(self):
        Size_win = tk.Toplevel()
        Size_win.title('尺寸操作')
        Size_win.geometry('200x180')
        l1 = tk.Label(Size_win, text="宽:")
        l1.place(y=30, x=25)
        self.text1 = tk.Entry(Size_win, width=10)
        self.text1.place(y=25, x=50)
        l1_1 = tk.Label(Size_win, text="px")
        l1_1.place(y=28, x=150)
        l2 = tk.Label(Size_win, text="高:")
        l2.place(y=60, x=25)
        self.text2 = tk.Entry(Size_win, width=10)
        self.text2.place(y=55, x=50)
        l2_1 = tk.Label(Size_win, text="px")
        l2_1.place(y=58, x=150)
        b1 = tk.Button(Size_win, text='确定', command=self.getSize_change)
        b1.place(y=100, x=80, width=40)
        b2 = tk.Button(Size_win, text='完成', command=Size_win.destroy)
        b2.place(y=145, x=140, width=40)

    # 获得输入尺寸
    def getSize_change(self):
        sizeNum_w = int(self.text1.get())
        sizeNum_h = int(self.text2.get())
        # print('1')
        self.showSize_change(sizeNum_w, sizeNum_h)
        # print(sizeNum_w, sizeNum_h)

    # 尺寸修改并展示图片
    def showSize_change(self, renewSize_w, renewSize_h):
        # print('2')
        self.picture = picture()
        needResize_pic = self.img
        show_resizePic = self.picture.changeResize(needResize_pic, renewSize_w, renewSize_h)
        self.show_img(show_resizePic)

    # 图像旋转操作窗口
    def window_rotate(self):
        Rot_win = tk.Toplevel()
        Rot_win.title('旋转')
        Rot_win.geometry('225x220')
        l1 = tk.Label(Rot_win, text="角度：")
        l1.place(y=20, x=10)
        self.inpt = tk.Entry(Rot_win, width=13)
        self.inpt.place(y=15, x=50)
        b0 = tk.Button(Rot_win, text='确定', command=lambda: self.getDegree('1'))
        b0.place(y=55, x=160, width=40)
        b1 = tk.Button(Rot_win, text='+90', command=lambda: self.getDegree('2'))
        b1.place(y=85, x=60, width=95)
        b2 = tk.Button(Rot_win, text='-90', command=lambda: self.getDegree('3'))
        b2.place(y=115, x=60, width=95)
        b3 = tk.Button(Rot_win, text='180', command=lambda: self.getDegree('4'))
        b3.place(y=145, x=60, width=95)
        b4 = tk.Button(Rot_win, text='完成', command=Rot_win.destroy)
        b4.place(y=180, x=160, width=40)

    # 旋转角度获取
    def getDegree(self, n):
        self.picture = picture()
        needRotate_pic = self.img
        # print('99')
        # print(n)
        if n == '1':
            shouldDegree = float(self.inpt.get())
            # print('36')
            # print(shouldDegree)
            showRotate_pic = self.picture.rotatePic(needRotate_pic, shouldDegree)
        elif n == '2':
            # print('34')
            showRotate_pic = self.picture.rotatePic(needRotate_pic, +90)
        elif n == '3':
            showRotate_pic = self.picture.rotatePic(needRotate_pic, -90)
        elif n == '4':
            showRotate_pic = self.picture.rotatePic(needRotate_pic, 180)
        else:
            return 0
        self.show_img(showRotate_pic)

    # 镜像操作窗口
    def window_mirror(self):
        Mir_win = tk.Toplevel()
        Mir_win.title('镜像操作')
        Mir_win.geometry('150x150')
        b1 = tk.Button(Mir_win, text='左右', command=self.MirrorImg_lr)
        b1.place(y=30, x=35, width=75)
        b2 = tk.Button(Mir_win, text='上下', command=self.MirrorImg_tb)
        b2.place(y=60, x=35, width=75)
        b3 = tk.Button(Mir_win, text='完成', command=Mir_win.destroy)
        b3.place(y=110, x=80, width=40)

    # 镜像左右调用展示
    def MirrorImg_lr(self):
        self.picture = picture()
        Mirror_img_lr = self.img
        MittotImg_lrFinish = self.picture.MirrorPic_leftOrright(Mirror_img_lr)
        self.show_img(MittotImg_lrFinish)

    # 镜像上下调用展示
    def MirrorImg_tb(self):
        self.picture = picture()
        Mirror_img_tb = self.img
        MittotImg_tbFinish = self.picture.MirrorPic_topOrbuttom(Mirror_img_tb)
        self.show_img(MittotImg_tbFinish)

    # 文字添加功能窗口
    def window_word(self):
        Word_win = tk.Toplevel()
        Word_win.title('镜像操作')
        Word_win.geometry('200x250')
        l1 = tk.Label(Word_win, text='请输入文字：')
        l1.place(y=20, x=25, width=80)
        self.textWord = tk.Entry(Word_win, width=17)
        self.textWord.place(y=45, x=15)
        l2 = tk.Label(Word_win, text='请选择文字颜色：')
        l2.place(y=85, x=25, width=105)
        b1 = tk.Button(Word_win, text='红色', width=8, command=lambda: self.getWord_input('red'))
        b1.place(y=120, x=20)
        b2 = tk.Button(Word_win, text='黑色', width=8, command=lambda: self.getWord_input('black'))
        b2.place(y=120, x=100)
        b3 = tk.Button(Word_win, text='蓝色', width=8, command=lambda: self.getWord_input('blue'))
        b3.place(y=150, x=20)
        b4 = tk.Button(Word_win, text='绿色', width=8, command=lambda: self.getWord_input('green'))
        b4.place(y=150, x=100)
        b5 = tk.Button(Word_win, text='黄色', width=8, command=lambda: self.getWord_input('yellow'))
        b5.place(y=180, x=20)
        b6 = tk.Button(Word_win, text='白色', width=8, command=lambda: self.getWord_input('white'))
        b6.place(y=180, x=100)
        b7 = tk.Button(Word_win, text='完成', command=Word_win.destroy)
        b7.place(y=220, x=150)

    # 获得文字添加的相关对象
    def getWord_input(self, color):
        self.picture = picture()
        needWord_pic = self.img
        showWord = self.textWord.get()
        # print(showWord)
        # print(color)
        showInword_pic = self.picture.wordInput(needWord_pic, showWord, color)
        self.show_img(showInword_pic)

    # 滤镜选择窗口
    def window_style(self):
        Sty_win = tk.Toplevel()
        Sty_win.title('滤镜选择')
        Sty_win.geometry('230x180')
        bt1 = tk.Button(Sty_win, text='图像模糊', command=self.sty_1)
        bt1.place(y=25, x=25, width=80)
        bt2 = tk.Button(Sty_win, text='轮廓滤波', command=self.sty_2)
        bt2.place(y=25, x=115, width=80)
        bt3 = tk.Button(Sty_win, text='高斯模糊', command=self.sty_3)
        bt3.place(y=65, x=25, width=80)
        bt4 = tk.Button(Sty_win, text='浮雕滤镜', command=self.sty_4)
        bt4.place(y=65, x=115, width=80)
        bt5 = tk.Button(Sty_win, text='边界滤镜', command=self.sty_5)
        bt5.place(y=105, x=25, width=80)
        bt6 = tk.Button(Sty_win, text='完成', command=Sty_win.destroy)
        bt6.place(y=140, x=160)

    # 图像模糊获取展示
    def sty_1(self):
        sty_1_pic = self.img
        relSty_1 = style_Huminghao.blurPic(sty_1_pic)
        self.show_img(relSty_1)

    # 边界增强获取展示
    def sty_2(self):
        sty_2_pic = self.img
        reSty_2 = style_Huminghao.edge(sty_2_pic)
        self.show_img(reSty_2)

    # 高斯模糊获取展示
    def sty_3(self):
        sty_3_pic = self.img
        reSty_3 = style_Huminghao.gaussianBlur(sty_3_pic)
        self.show_img(reSty_3)

    # 浮雕滤镜获取展示
    def sty_4(self):
        sty_4_pic = self.img
        reSty_4 = style_Huminghao.emboss(sty_4_pic)
        self.show_img(reSty_4)

    # 边界滤镜获取展示
    def sty_5(self):
        sty_5_pic = self.img
        reSty_5 = style_Huminghao.ffind_edeges(sty_5_pic)
        self.show_img(reSty_5)

    # 亮度调整
    def brightnessPic(self):
        self.picture = picture()
        needBright_pic = self.img
        b_num = float(self.inp1.get())
        briNum = b_num / 100
        showBright_pic = self.picture.brightPic(needBright_pic, briNum)
        self.show_img(showBright_pic)

    # 色彩度调整
    def coolorPic(self):
        self.picture = picture()
        needColor_pic = self.img
        co_num = float(self.inp2.get())
        colNum = co_num / 100
        showColor_pic = self.picture.colornPic(needColor_pic, colNum)
        self.show_img(showColor_pic)

    # 对比度调整
    def contrastPic(self):
        self.picture = picture()
        needCon_pic = self.img
        c_num = float(self.inp3.get())
        ConNum = c_num / 100
        showContrast_pic = self.picture.constractPic(needCon_pic, ConNum)
        self.show_img(showContrast_pic)

    # 锐度调整
    def sharpnessPic(self):
        self.picture = picture()
        needSharp_pic = self.img
        s_num = float(self.inp4.get())
        ShNum = s_num / 100
        showSharp_pic = self.picture.constractPic(needSharp_pic, ShNum)
        self.show_img(showSharp_pic)

    # 原图储存
    def firstPic(self, pic):
        self.Fpic = pic
        return self.Fpic

    # 恢复图像
    def replay(self):
        self.show_img(self.Fpic)

    # 对比图像
    def compare(self):
        Im._show(self.Fpic)

    # 展示函数
    def show_img(self, n_img):
        self.img = n_img  # self.img PIL对象方便传值给picture类以及本类中其他需要使用PIL图像的地方
        img_show = ImageTk.PhotoImage(self.img)
        self.image_l.config(image=img_show)
        self.image_l.image = img_show
        return self.img

    # 保存函数
    def save_pic(self):
        fname = tkinter.filedialog.asksaveasfilename(title='保存文件', filetypes=[("PNG", ".png")])
        self.img.save(str(fname))  # PIL保存


# 图像处理类（图片对象为PIL）
class picture:
    # 打开图像调用
    def open_pic(self, address):
        self.pic_get = Im.open(address).convert('RGBA')
        wid, hei = self.pic_get.size
        if wid > 600 or hei > 400:
            if tk.messagebox.askokcancel('提示', '图片可能过大，是否压缩？'):
                needShow_pic = self.openResize()
                return needShow_pic
            return self.pic_get
        else:
            return self.pic_get

    # 打开图像时的图像压缩展示
    def openResize(self):
        w, h = self.pic_get.size
        w_hope = 500
        h_hope = 300
        f1 = 1.0 * w_hope / w
        f2 = 1.0 * h_hope / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        pic_show = self.pic_get.resize((width, height))
        return pic_show

    # 截图处理
    def Cutpic(self, pic_preCut, p1, p2, p3, p4):
        cropped_pic = pic_preCut.crop((p1, p2, p3, p4))
        return cropped_pic

    # 尺寸大小变化
    def changeResize(self, pic_reshow, newWidth, newHeight):
        reesizeNew_pic = pic_reshow.resize((newWidth, newHeight))
        # print('3')
        return reesizeNew_pic

    # 镜像左右
    def MirrorPic_leftOrright(self, pic_mir_lr):
        Mirror_lrFinish = pic_mir_lr.transpose(Im.FLIP_LEFT_RIGHT)
        return Mirror_lrFinish

    # 镜像上下
    def MirrorPic_topOrbuttom(self, pic_mir_tp):
        Mirror_tbFinish = pic_mir_tp.transpose(Im.FLIP_TOP_BOTTOM)
        return Mirror_tbFinish

    # 文字添加
    def wordInput(self, pic_preWord, textEn, fillColor):
        Wordpic_width, Wordpic_height = pic_preWord.size
        wordFont = ImageFont.truetype('./use.TTF', 30)
        draw = ImageDraw.Draw(pic_preWord)
        draw.text((20, Wordpic_height - 35), text=textEn, font=wordFont, fill=fillColor)
        return pic_preWord

    # 旋转
    def rotatePic(self, pic_prerotate, rodegreee):
        rotateNew_pic = pic_prerotate.rotate(rodegreee, expand=True)
        return rotateNew_pic

    # 亮度
    def brightPic(self, pic_prebright, n):
        pic_brighted = ImageEnhance.Brightness(pic_prebright).enhance(n)
        return pic_brighted

    # 色彩度
    def colornPic(self, pic_preColor, n):
        pic_colored = ImageEnhance.Color(pic_preColor).enhance(n)
        return pic_colored

    # 对比度
    def constractPic(self, pic_preCon, n):
        enh_con = ImageEnhance.Contrast(pic_preCon)
        contrast = n
        pic_contrasted = enh_con.enhance(contrast)
        return pic_contrasted

    # 锐度调整
    def sharpPic(self, pic_preSharp, n):
        pic_sharped = ImageEnhance.Sharpness(pic_preSharp).enhance(n)
        return pic_sharped


if __name__ == '__main__':
    app = Win()
    app.mainloop()
