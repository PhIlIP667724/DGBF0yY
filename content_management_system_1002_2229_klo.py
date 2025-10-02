# 代码生成时间: 2025-10-02 22:29:55
from gradio import gr
import json

# 一个简单的内容管理系统
class ContentManagementSystem:
    def __init__(self):
        # 初始化一个空的存储结构，用来保存内容
        self.storage = {}

    def add_content(self, content_id, content):
        """
        添加新的内容到系统中
        :param content_id: 内容的唯一标识符
        :param content: 要添加的内容
        """
        if content_id in self.storage:
            raise ValueError("Content ID already exists.")
        self.storage[content_id] = content
        return "Content added successfully."

    def get_content(self, content_id):
        """
        根据ID获取内容
        :param content_id: 内容的唯一标识符
        :return: 对应ID的内容
        """
        if content_id not in self.storage:
            raise ValueError("Content not found.")
        return self.storage[content_id]

    def update_content(self, content_id, content):
        """
        更新系统中的内容
        :param content_id: 内容的唯一标识符
        :param content: 新的内容
        """
        if content_id not in self.storage:
            raise ValueError("Content not found.")
        self.storage[content_id] = content
        return "Content updated successfully."

    def delete_content(self, content_id):
        """
        删除系统中的内容
        :param content_id: 内容的唯一标识符
        """
        if content_id not in self.storage:
            raise ValueError("Content not found.")
        del self.storage[content_id]
        return "Content deleted successfully."

# 创建Gradio界面
def create_gradio_interface():
    cms = ContentManagementSystem()

    def handle_add_content(content_id, content):
        try:
            return cms.add_content(content_id, content)
        except ValueError as e:
            return str(e)

    def handle_get_content(content_id):
        try:
            return cms.get_content(content_id)
        except ValueError as e:
            return str(e)

    def handle_update_content(content_id, content):
        try:
            return cms.update_content(content_id, content)
        except ValueError as e:
            return str(e)

    def handle_delete_content(content_id):
        try:
            return cms.delete_content(content_id)
        except ValueError as e:
            return str(e)

    demo = gr.Interface(
        fn=handle_add_content, 
        inputs=["text", "text"], 
        outputs="text",
        title="Add Content"
    )
    demo.add_component(
        fn=handle_get_content, 
        inputs=["text"], 
        outputs="text",
        title="Get Content"
    )
    demo.add_component(
        fn=handle_update_content, 
        inputs=["text", "text"], 
        outputs="text",
        title="Update Content"
    )
    demo.add_component(
        fn=handle_delete_content, 
        inputs=["text"], 
        outputs="text",
        title="Delete Content"
    )
    demo.launch()

if __name__ == "__main__":
    create_gradio_interface()