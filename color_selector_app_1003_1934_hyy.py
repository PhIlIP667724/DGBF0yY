# 代码生成时间: 2025-10-03 19:34:32
import gradio as gr
def color_selector():
    # 定义颜色选择器组件的回调函数
    # 返回用户选择的颜色
    return "Selected color is: " + gr.colors.to_hex(color)

if __name__ == "__main__":
    # 创建一个新的Gradio界面对象
    demo = gr.Interface(
        fn=color_selector,
        inputs=gr.ColorSelector(label="Choose a color"),  # 颜色选择器组件
        outputs="text"  # 输出为文本类型
    )
    # 启动应用
    demo.launch()
