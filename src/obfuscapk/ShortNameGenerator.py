import base64
from Crypto.Cipher import AES

class ShortNameGenerator:
    def __init__(self):
        self.identifier_map = {}
        self.used_names = set()

    def e(self, s: str) -> str:
        k = b'0'*16
        c = AES.new(k, AES.MODE_ECB)
        encrypted = c.encrypt(s.encode().ljust(16, b'\0'))
        r = base64.b16encode(encrypted).decode().lower()
        if r[0].isdigit():
            r = 'a' + r
        return r

    def rename_field(self, field_name: str) -> str:
        if field_name in self.identifier_map:
            return self.identifier_map[field_name]

        short_name = self.e(field_name)
        # 处理重复情况
        base_name = short_name
        counter = 0
        while short_name in self.used_names:
            counter += 1
            short_name = f"{base_name}{counter}"

        self.identifier_map[field_name] = short_name
        self.used_names.add(short_name)
        return short_name

# 使用示例
if __name__ == "__main__":
    generator = ShortNameGenerator()
    print(generator.rename_field("user_name"))
    print(generator.rename_field("email_address"))