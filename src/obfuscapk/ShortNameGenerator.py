import random
import string

class SimpleShortNameGenerator:
    def __init__(self):
        self.identifier_map = {}
        self.used_names = set()
        self.first_chars = string.ascii_lowercase + string.ascii_uppercase
        self.all_chars = string.ascii_letters + string.digits

    def _generate_random_name(self, length=2):
        """生成随机短名称"""
        while True:
            # 第一个字符必须是字母
            first_char = random.choice(self.first_chars)

            if length == 1:
                name = first_char
            else:
                # 剩余字符可以是字母或数字
                rest_chars = ''.join(random.choices(self.all_chars, k=length-1))
                name = first_char + rest_chars

            # 检查是否已使用
            if name not in self.used_names:
                self.used_names.add(name)
                return name

    def rename_field(self, field_name: str) -> str:
        if field_name not in self.identifier_map:
            # 优先使用2字符名称，冲突时使用3字符
            short_name = self._generate_random_name(2)
            self.identifier_map[field_name] = short_name

        return self.identifier_map[field_name]