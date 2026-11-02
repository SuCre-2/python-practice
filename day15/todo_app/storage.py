"""存储层：只管读写 JSON 文件，不关心待办的业务逻辑。"""

import json
import os
from pathlib import Path

from models import Task, task_from_dict

FILE = Path(__file__).resolve().parent / 'tasks.json'


def load() -> list[Task]:
    # 返回类型写成 list[Task]。这个标注不只是给人看的：Pylance 会据此检查
    # 调用方的用法，谁把返回值当字典下标访问，编辑器会立刻标红，不用等到运行
    # 文件不存在 = 第一次运行，属于正常情况，静默返回空列表
    if not FILE.exists():
        return []

    try:
        with open(FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        # 文件存在但读不出 = 真出问题了，必须让人知道
        print(f'警告：{FILE.name} 内容损坏，已跳过加载（原文件保持原样）')
        return []

    if not isinstance(data, list):
        print(f'警告：{FILE.name} 结构不对，期望是列表')
        return []

    return [task_from_dict(d) for d in data]


def save(tasks: list[Task]) -> None:
    # 参数标注成 list[Task]：传进来字典列表的话，编辑器当场就报，
    # 不用等 json.dump 那一刻才抛 'dict' object has no attribute 'to_dict'
    # 先写临时文件，成功后再一次性替换，避免写到一半崩溃把原文件截断
    tmp = FILE.with_suffix('.json.tmp')
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump([t.to_dict() for t in tasks], f, ensure_ascii=False, indent=2)
    os.replace(tmp, FILE)
