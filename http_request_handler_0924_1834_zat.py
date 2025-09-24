# 代码生成时间: 2025-09-24 18:34:13
import gradio as gr
import requests

"""
HTTP请求处理器

这个程序使用GRADIO框架创建一个简单的HTTP请求处理器，
允许用户输入URL并执行HTTP请求。
"""

def handle_http_request(url: str, method: str):
    """
    处理HTTP请求
    
    参数:
    url (str): 请求的URL
    method (str): 请求方法（GET, POST, PUT, DELETE等）
    
    返回:
    str: 响应内容
    
    异常:
    Exception: 如果请求失败
    """
    try:
        if method.upper() == 'GET':
            response = requests.get(url)
        elif method.upper() == 'POST':
            response = requests.post(url)
        elif method.upper() == 'PUT':
            response = requests.put(url)
        elif method.upper() == 'DELETE':
            response = requests.delete(url)
        else:
            raise ValueError('不支持的请求方法')
        
        if response.status_code == 200:
            return response.text
        else:
            return f"请求失败，状态码：{response.status_code}"
    except Exception as e:
        return str(e)

# 创建GRADIO接口
iface = gr.Interface(
    fn=handle_http_request,
    inputs=[gr.Textbox(label='URL'), gr.Radio(['GET', 'POST', 'PUT', 'DELETE'], label='请求方法')],
    outputs='text',
    title='HTTP请求处理器',
    description='输入URL和请求方法，执行HTTP请求'
)

# 启动GRADIO界面
iface.launch()