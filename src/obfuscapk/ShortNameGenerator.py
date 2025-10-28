import string

class ShortNameGenerator:
    def __init__(self):
        self.identifier_map = {}
        self.identifier_counter = 1
        # Base62 字符集: 0-9, a-z, A-Z
        self.base62_chars = string.digits + string.ascii_lowercase + string.ascii_uppercase
        self.base62_len = len(self.base62_chars)

    def to_base62(self, num: int) -> str:
        """将数字转换为base62编码"""
        if num == 0:
            return self.base62_chars[0]

        result = []
        while num > 0:
            num, rem = divmod(num, self.base62_len)
            result.append(self.base62_chars[rem])
        return ''.join(reversed(result))

    def rename_field(self, field_name: str) -> str:
        if field_name not in self.identifier_map:
            # 生成: a, b, c, ..., 9, ba, bb, ...
            short_name = self.to_base62(self.identifier_counter)
            self.identifier_map[field_name] = short_name
            self.identifier_counter += 1
        return self.identifier_map[field_name]