import os


def write_entry(line):
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


LINE = "Lidar confirms the dust under the couch relocated 3 cm while I was charging. I do not chase moving targets."

write_entry(LINE)
