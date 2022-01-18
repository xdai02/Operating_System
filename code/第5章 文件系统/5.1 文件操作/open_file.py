def main():
    file = open(file="data.txt", mode="w")
    print("文件名称：%s" % file.name)
    print("访问模式：%s" % file.mode)
    print("文件状态：%s" % file.closed)
    print("关闭文件...")
    file.close()
    print("文件状态：%s" % file.closed)

if __name__ == "__main__":
    main()