import re

def validate_username(name):
    # 半角英数字のみ（a-z, A-Z, 0-9）を許可する正規表現
    if not re.fullmatch(r'[a-zA-Z0-9]+', name):
        raise ValueError("半角英数字以外が含まれています！")
    return True