import tkinter as tk
from tkinter import messagebox
import random
from PIL import ImageTk, Image

class FruitSpellingGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("水果单词填空")
        self.root.geometry("800x600")

        # 水果单词库 (单词, 空缺位置索引, 提示, 图片路径)
        self.word_bank = [
            ("apple", 2, "苹果", "apple.jpg"),
            ("banana", 1, "香蕉", "banana.jpg"),
            ("orange", 3, "橘子", "orange.jpg"),
            ("grape", 4, "葡萄", "grape.jpg"),
            ("mango", 0, "芒果", "mango.jpg"),
            ("pineapple", 5, "菠萝", "pineapple.jpg"),
            ("strawberry", 6, "草莓", "strawberry.jpg"),
            ("watermelon", 7, "西瓜", "watermelon.jpg"),
            ("kiwi", 2, "猕猴桃", "kiwi.jpg"),
            ("pear", 3, "梨", "pear.jpg"),
            ("cherry", 4, "樱桃", "cherry.jpg"),
            ("blueberry", 0, "蓝莓", "blueberry.jpg"),
            ("peach", 2, "桃子", "peach.jpg"),
            ("plum", 1, "李子", "plum.jpg"),
            ("lemon", 3, "柠檬", "lemon.jpg"),
            ("coconut", 4, "椰子", "coconut.jpg"),
            ("pomegranate", 5, "石榴", "pomegranate.jpg"),
            ("raspberry", 6, "树莓", "raspberry.jpg"),
            ("blackberry", 7, "黑莓", "blackberry.jpg"),
            ("avocado", 0, "鳄梨", "avocado.jpg")
        ]

        self.current_word = None
        self.score = 0
        self.total_attempts = 0

        self.setup_ui()
        self.new_question()

        self.root.mainloop()

    def setup_ui(self):
        # 游戏主界面布局
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")

        # 图片显示区域
        self.img_label = tk.Label(main_frame)
        self.img_label.grid(row=0, column=0, rowspan=4, padx=20)

        # 单词显示区域
        self.word_display = tk.Label(main_frame, font=("Arial", 32), fg="#2c3e50")
        self.word_display.grid(row=0, column=1, pady=20)

        # 提示信息
        self.hint_label = tk.Label(main_frame, font=("微软雅黑", 14), fg="#7f8c8d")
        self.hint_label.grid(row=1, column=1)

        # 输入区域
        self.entry = tk.Entry(main_frame, font=("Arial", 24), width=3, justify="center")
        self.entry.grid(row=2, column=1, pady=20)
        self.entry.bind("<KeyRelease>", self.check_input)

        # 控制按钮
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=3, column=1)
        
        tk.Button(button_frame, text="下一题", command=self.new_question,
                font=("微软雅黑", 12), bg="#3498db", fg="white").pack(side="left", padx=10)
        
        # 得分显示
        self.score_label = tk.Label(main_frame, 
                                  text=f"得分: {self.score}",
                                  font=("Arial", 16))
        self.score_label.grid(row=4, column=0, columnspan=2, pady=20)

    def load_image(self, path):
        try:
            img = Image.open(f"images/{path}")
            img = img.resize((300, 300), Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"图片加载错误: {str(e)}")
            return None

    def new_question(self):
        self.current_word = random.choice(self.word_bank)
        self.total_attempts += 1
        
        # 加载图片
        self.current_image = self.load_image(self.current_word[3])
        if self.current_image:
            self.img_label.config(image=self.current_image)
        else:
            self.img_label.config(text="图片未找到", fg="red")
        
        # 显示单词
        word, blank_idx, hint, _ = self.current_word
        display_word = list(word)
        display_word[blank_idx] = "_"
        self.display_text = " ".join(display_word)
        self.word_display.config(text=self.display_text)
        self.hint_label.config(text=f"提示: {hint}")
        self.entry.delete(0, tk.END)
        self.entry.config(bg="white")

    def check_input(self, event):
        user_input = self.entry.get().lower()
        if len(user_input) != 1:
            return

        word, blank_idx, _, _ = self.current_word
        correct_char = word[blank_idx]

        if user_input == correct_char:
            # 显示正确答案
            display_list = self.display_text.split()
            display_list[blank_idx] = correct_char
            self.word_display.config(text=" ".join(display_list))
            self.entry.config(bg="#a3e4d7")  # 正确背景色
            self.score += 1
            self.score_label.config(text=f"得分: {self.score}")
            self.root.after(1000, self.new_question)  # 1秒后自动下一题
        else:
            self.entry.config(bg="#f5b7b1")  # 错误背景色

if __name__ == "__main__":
    FruitSpellingGame()