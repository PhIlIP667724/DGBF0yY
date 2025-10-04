# 代码生成时间: 2025-10-04 21:16:39
import gradio as gr
def check_in(user_id):
    """
    记录用户打卡信息
    Args:
        user_id (str): 用户ID
    Returns:
        str: 打卡成功与否的消息
    """
    try:
        # 假设有一个数据库或文件存储用户的打卡记录
        with open("attendance_records.txt", "a") as f:
            f.write(f"{user_id} checked in at {datetime.now()}
")
        return "Check-in successful"
    except Exception as e:
        # 错误处理
        return f"Check-in failed: {str(e)}"

def main():
    """
    主函数，设置Graddle界面
    """
    with gr.Blocks() as demo:
        gr.Markdown("This is a simple attendance check-in system")
        user_input = gr.Textbox(label="Enter your user ID")
        check_in_button = gr.Button("Check-in")
        check_in_output = gr.Textbox(label="Check-in result")
        check_in_button.click(check_in, inputs=[user_input], outputs=[check_in_output])
    demo.launch()

if __name__ == "__main__":
    main()