from main import add

def test_add():
    # 1 + 1 は 2 ですが、わざと 3 と比較して失敗させます
    assert add(1, 1) == 2