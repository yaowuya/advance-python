# 500G, 特殊 一行
def my_read_lines(f, newline):
    buffer = ""
    while True:
        # 读出来的值可能包含多个分隔符，需要循环分隔
        while newline in buffer:
            posix = buffer.index(newline)
            yield buffer[:posix]
            buffer = buffer[posix + len(newline):]
        chunk = f.read(4096)
        if not chunk:
            # 说明已经读到了文件结尾
            yield buffer
            break
        buffer += chunk


with open("input.txt", encoding="utf-8") as f:
    for line in my_read_lines(f, "{|}"):
        print(line)
