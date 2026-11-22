# pairwise-foliage-phase-lod

## 领域

游戏、图形与多媒体

## 主题

植被风相位

## 说明

实例相位、LOD 无关参数与切换连续。

初始状态下 `render/foliage_phase_lod.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
