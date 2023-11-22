ori_file = open("/Users/zhangsan/workspace/dataset/csmsc/000001-010000.txt", "r")
lines = ori_file.readlines()

with open("/Users/zhangsan/workspace/dataset/csmsc/metadata.csv", "w") as log:
    idx = 0
    while idx < len(lines):
        filename_prefix, sentence = lines[idx].strip().split()
        sent = sentence.replace("#1", "").replace("#2", "").replace("#3", "").replace("#4", "")
        rec_line = filename_prefix + "|" + sent + "|" + sent + "\n"
        log.write(rec_line)
        idx = idx + 2

