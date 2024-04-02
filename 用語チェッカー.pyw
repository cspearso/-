import tkinter as tk
import codecs
def process_input():
    #Create Inputs and Outputs
    input_text_1 = entry1.get()
    input_text_2 = entry2.get()
    output_text = ''
    #Create Dictionary
    result_dict = {}
    try:
        with codecs.open(input_text_1,'r','utf-8') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    key, value = parts
                    result_dict[key] = value
    except FileNotFoundError:
        output_text += "用語集のファイルは見つかりませんでした\n"
    #Use Dictionary on File
    line_number = 0
    try:
        with open(input_text_2,'r', encoding='utf-8') as file:
            frequency = 0
            for line in file:
                line_number += 1
                for key in result_dict:
                    if line.strip().find(key) != -1:
                        frequency +=1
                        output_text += '\n「' + key + '」は不適切な言葉です'
                        output_text += '\n説明や言い換え：' + result_dict[key]
                        output_text += '\n' + str(line_number) + '行目' + str(line.strip().find(key)+1)+ '文字目でこの用語が使われました'
                        output_text += '\n' + line + '\n'
            if frequency == 0:
                output_text += '不適切な言葉は見つかりませんでした'
    except FileNotFoundError:
        output_text += "ファイルは見つかりませんでした\n"
        
    #outputting the result
    output_textbox.config(state=tk.NORMAL)
    output_textbox.delete('1.0', tk.END)  # Clear previous content
    output_textbox.insert(tk.END, output_text)  # Insert new content
    output_textbox.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("用語チェッカー")

# Create input prompt label 1
prompt_label1 = tk.Label(root, text="用語集のファイルネームを入力してください")
prompt_label1.pack()

# Create input entry 1
entry1 = tk.Entry(root, width=40)
entry1.pack(pady=5)

# Create input prompt label 2
prompt_label2 = tk.Label(root, text="本文のファイルネームを入力してください")
prompt_label2.pack()

# Create input entry 2
entry2 = tk.Entry(root, width=40)
entry2.pack(pady=5)

# Create process button
process_button = tk.Button(root, text="チェック", command=process_input)
process_button.pack()

# Create output textbox with scrollbar
output_scrollbar = tk.Scrollbar(root)
output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_textbox = tk.Text(root, wrap=tk.WORD, yscrollcommand=output_scrollbar.set)
output_textbox.pack(expand=True, fill=tk.BOTH)
output_scrollbar.config(command=output_textbox.yview)

# Run the Tkinter event loop
root.mainloop()